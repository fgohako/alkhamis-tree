const puppeteer = require('/home/gohako/.gemini/antigravity/scratch/family-tree-app/node_modules/puppeteer-core');

(async () => {
  console.log('================================================================');
  console.log('⚡ TESTING REGISTRY PERFORMANCE & MOBILE LOCATE (تحديد الموقع) ⚡');
  console.log('================================================================');

  const browser = await puppeteer.launch({
    executablePath: '/home/gohako/.local/bin/chromium',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu'],
    defaultViewport: { width: 390, height: 844 } // iPhone 14
  });

  const page = await browser.newPage();
  
  const pageErrors = [];
  page.on('pageerror', err => {
    pageErrors.push(err.message);
    console.error('❌ PAGE ERROR:', err.message);
  });

  await page.goto('file:///home/gohako/Documents/antigravity/dazzling-mendel/al-khamis-family-tree/index.html', { waitUntil: 'networkidle2' });

  // 1. Check helper functions
  const fnChecks = await page.evaluate(() => {
    return {
      traceNeuralKinship: typeof traceNeuralKinship,
      clearNeuralKinship: typeof clearNeuralKinship,
      getAncestors: typeof getAncestors,
      getTargetViewForPerson: typeof getTargetViewForPerson,
      flyToPerson: typeof flyToPerson,
      centerOnCardElement: typeof centerOnCardElement
    };
  });
  console.log('Function type checks:', fnChecks);
  for (const [k, v] of Object.entries(fnChecks)) {
    if (v !== 'function') throw new Error(`Function ${k} is not defined (type: ${v})`);
  }

  // 2. Open Registry Overlay
  console.log('\n--- Test 1: Opening Registry Table ---');
  await page.evaluate(() => {
    switchView('registry');
  });
  await new Promise(r => setTimeout(r, 200));

  const countText = await page.$eval('#registryCountBadge', el => el.textContent);
  console.log('Registry count badge:', countText);

  // 3. Performance Test: Simulate rapid typing in Registry Search Box
  console.log('\n--- Test 2: Rapid Typing in Registry Search Box (Lag Benchmark) ---');
  const t0 = Date.now();
  await page.type('#registryFilterInput', 'حسن علي عيسى علي خميس', { delay: 10 });
  await new Promise(r => setTimeout(r, 250)); // Wait for debounce
  const t1 = Date.now();
  console.log(`Typing 22 characters + debounced search took: ${t1 - t0}ms`);

  const filteredCount = await page.$eval('#registryCountBadge', el => el.textContent);
  console.log('Filtered count:', filteredCount);

  const rowCount = await page.$$eval('#registryTableBody tr', rows => rows.length);
  console.log('Rows rendered in DOM:', rowCount);

  // Capture screenshot of filtered registry table
  await page.screenshot({ path: 'test_evidence/evidence_registry_fast_search.png' });
  console.log('Saved test_evidence/evidence_registry_fast_search.png');

  // 4. Test "عرض في المشجرة" on Mobile
  console.log('\n--- Test 3: Locate on Mobile (تحديد الموقع من السجل) ---');
  // Click first row's "عرض في المشجرة" button
  const clickedName = await page.evaluate(() => {
    const btn = document.querySelector('#registryTableBody tr button');
    if (!btn) return null;
    const name = btn.closest('tr').children[1].textContent;
    btn.click();
    return name;
  });
  console.log('Clicked "عرض في المشجرة" for:', clickedName);

  await new Promise(r => setTimeout(r, 400)); // Wait for flyToPerson animation

  // Check state after locating on mobile:
  const locateState = await page.evaluate(() => {
    const isRegistryHidden = document.getElementById('registryViewOverlay').classList.contains('hidden');
    const isDrawerClosed = document.getElementById('personDrawer').classList.contains('translate-x-full');
    const activeSelectedCard = document.querySelector('.tree-card.active-selected');
    const currentView = activeView;
    const toast = document.getElementById('toastMsg')?.textContent;
    return {
      isRegistryHidden,
      isDrawerClosed,
      currentView,
      activeSelectedId: activeSelectedCard ? activeSelectedCard.id : null,
      toast
    };
  });
  console.log('Locate on Mobile State:', locateState);

  if (!locateState.isRegistryHidden) throw new Error('Registry overlay should be hidden after locating');
  if (!locateState.isDrawerClosed) throw new Error('Person drawer should be closed on mobile to prevent blocking');
  if (!locateState.activeSelectedId) throw new Error('Card should have .active-selected class');

  await page.screenshot({ path: 'test_evidence/evidence_mobile_locate_success.png' });
  console.log('Saved test_evidence/evidence_mobile_locate_success.png');

  // 5. Test "تحديد الموقع على المشجرة" from Drawer on Mobile
  console.log('\n--- Test 4: "تحديد الموقع على المشجرة" from Drawer ---');
  await page.evaluate(() => {
    // Open drawer for a person from Branch M
    const p = findPersonById('IND_5'); // Branch M
    populatePersonDrawer(p);
    document.getElementById('personDrawer').classList.remove('translate-x-full');
    document.getElementById('drawerBackdrop').classList.remove('hidden');
  });
  await new Promise(r => setTimeout(r, 200));

  // Now click drawerCenterBtn
  await page.evaluate(() => {
    document.getElementById('drawerCenterBtn').click();
  });
  await new Promise(r => setTimeout(r, 400));

  const drawerLocateState = await page.evaluate(() => {
    const isDrawerClosed = document.getElementById('personDrawer').classList.contains('translate-x-full');
    const activeSelectedCard = document.querySelector('.tree-card.active-selected');
    const currentView = activeView;
    const toast = document.getElementById('toastMsg')?.textContent;
    return {
      isDrawerClosed,
      currentView,
      activeSelectedId: activeSelectedCard ? activeSelectedCard.id : null,
      toast
    };
  });
  console.log('Drawer Center Button State:', drawerLocateState);
  if (!drawerLocateState.isDrawerClosed) throw new Error('Drawer should close when drawerCenterBtn is clicked');
  if (drawerLocateState.currentView !== 'M') throw new Error(`IND_5 should route to Branch M (got ${drawerLocateState.currentView})`);

  await page.screenshot({ path: 'test_evidence/evidence_drawer_locate_branch_m.png' });
  console.log('Saved test_evidence/evidence_drawer_locate_branch_m.png');

  // 6. Test Header Search live autocomplete
  console.log('\n--- Test 5: Header Search Live Autocomplete ---');
  await page.type('#nameSearchInput', 'عيسى علي', { delay: 15 });
  await new Promise(r => setTimeout(r, 250));

  const dropdownCount = await page.$$eval('.search-result-item', items => items.length);
  console.log('Autocomplete items returned:', dropdownCount);
  if (dropdownCount === 0) throw new Error('Search autocomplete should return results');

  await page.screenshot({ path: 'test_evidence/evidence_header_search_fast.png' });
  console.log('Saved test_evidence/evidence_header_search_fast.png');

  console.log('\nTotal page errors encountered:', pageErrors.length);
  if (pageErrors.length > 0) throw new Error(`Encountered ${pageErrors.length} page errors: ${pageErrors.join(', ')}`);

  console.log('\n🎉 ALL TESTS PASSED WITH 0 ERRORS! 🎉');
  await browser.close();
})();
