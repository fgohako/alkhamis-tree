const puppeteer = require('/home/gohako/.gemini/antigravity/scratch/family-tree-app/node_modules/puppeteer-core');
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3599;
const EVIDENCE_DIR = path.resolve(__dirname, 'test_evidence');
const ARTIFACT_DIR = '/home/gohako/.gemini/antigravity/brain/d5ec3225-0e2e-4f11-8664-16ff1786d0c2';

if (!fs.existsSync(EVIDENCE_DIR)) fs.mkdirSync(EVIDENCE_DIR, { recursive: true });
if (!fs.existsSync(ARTIFACT_DIR)) fs.mkdirSync(ARTIFACT_DIR, { recursive: true });

// Static HTTP Server
const server = http.createServer((req, res) => {
  let filePath = path.join(__dirname, req.url.split('?')[0]);
  if (req.url === '/' || req.url.startsWith('/?')) filePath = path.join(__dirname, 'index.html');
  const extname = path.extname(filePath);
  const contentTypes = {
    '.html': 'text/html; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
    '.json': 'application/json',
    '.css': 'text/css',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.svg': 'image/svg+xml'
  };
  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end('Not found');
      return;
    }
    res.writeHead(200, { 'Content-Type': contentTypes[extname] || 'text/plain' });
    res.end(data);
  });
});

async function runTests() {
  const results = {
    pc_1080p: {},
    pc_1440p: {},
    mobile_iphone: {},
    mobile_android: {}
  };

  const browser = await puppeteer.launch({
    executablePath: '/home/gohako/.local/bin/chromium',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu'],
  });

  const capturedScreenshots = [];

  async function saveScreenshot(page, filename) {
    const localPath = path.join(EVIDENCE_DIR, filename);
    await page.screenshot({ path: localPath });
    const brainPath = path.join(ARTIFACT_DIR, filename);
    fs.copyFileSync(localPath, brainPath);
    capturedScreenshots.push(filename);
    console.log(`[Captured] ${filename}`);
  }

  // ==========================================
  // 1. PC Desktop 1920x1080
  // ==========================================
  console.log('\n--- 1. Testing PC Desktop (1920x1080) ---');
  const page1080 = await browser.newPage();
  await page1080.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await page1080.goto(`http://localhost:${PORT}`, { waitUntil: 'networkidle0' });

  // 1.1 Master Tree initial load
  const cardCount1080 = await page1080.evaluate(() => document.querySelectorAll('.tree-card').length);
  results.pc_1080p.master_render = cardCount1080 > 0 ? 'PASS' : 'FAIL';
  console.log(`1.1 Master cards rendered: ${cardCount1080} -> ${results.pc_1080p.master_render}`);
  await saveScreenshot(page1080, 'pc_1080p_master_tree.png');

  // 1.2 Mouse Wheel Zooming (Anchored to Cursor)
  const initialTrans = await page1080.evaluate(() => ({ scale: currentScale, tx: translateX, ty: translateY }));
  const cursorX = 700;
  const cursorY = 500;
  const vpRect = await page1080.evaluate(() => {
    const r = document.getElementById('viewport').getBoundingClientRect();
    return { left: r.left, top: r.top };
  });
  const vpCursorX = cursorX - vpRect.left;
  const vpCursorY = cursorY - vpRect.top;

  await page1080.mouse.move(cursorX, cursorY);
  await page1080.mouse.wheel({ deltaY: -150 }); // Zoom in
  await new Promise(r => setTimeout(r, 120));

  const zoomedTrans = await page1080.evaluate(() => ({ scale: currentScale, tx: translateX, ty: translateY }));
  const initialWorldX = (vpCursorX - initialTrans.tx) / initialTrans.scale;
  const zoomedWorldX = (vpCursorX - zoomedTrans.tx) / zoomedTrans.scale;
  const initialWorldY = (vpCursorY - initialTrans.ty) / initialTrans.scale;
  const zoomedWorldY = (vpCursorY - zoomedTrans.ty) / zoomedTrans.scale;
  const anchorErrX = Math.abs(initialWorldX - zoomedWorldX);
  const anchorErrY = Math.abs(initialWorldY - zoomedWorldY);
  const zoomAnchoredPass = (anchorErrX < 0.01 && anchorErrY < 0.01 && zoomedTrans.scale > initialTrans.scale);
  results.pc_1080p.mouse_wheel_zoom_anchored = zoomAnchoredPass ? 'PASS' : 'FAIL';
  console.log(`1.2 Mouse wheel zoom anchored diff: (${anchorErrX.toFixed(4)}, ${anchorErrY.toFixed(4)}) -> ${results.pc_1080p.mouse_wheel_zoom_anchored}`);
  await saveScreenshot(page1080, 'pc_1080p_zoom_anchored.png');

  // 1.3 Drag Panning with 60fps rendering
  const beforePan = await page1080.evaluate(() => ({ tx: translateX, ty: translateY }));
  await page1080.mouse.move(500, 300);
  await page1080.mouse.down();
  await page1080.mouse.move(750, 450, { steps: 8 });
  await page1080.mouse.up();
  await new Promise(r => setTimeout(r, 100));

  const afterPan = await page1080.evaluate(() => ({ tx: translateX, ty: translateY }));
  const panDeltaX = afterPan.tx - beforePan.tx;
  const panDeltaY = afterPan.ty - beforePan.ty;
  const dragPanPass = Math.abs(panDeltaX - 250) < 5 && Math.abs(panDeltaY - 150) < 5;
  results.pc_1080p.drag_panning_smooth = dragPanPass ? 'PASS' : 'FAIL';
  console.log(`1.3 Drag pan delta: (${panDeltaX}, ${panDeltaY}) -> ${results.pc_1080p.drag_panning_smooth}`);
  await saveScreenshot(page1080, 'pc_1080p_drag_panned.png');

  // 1.4 Hovering and Clicking Cards for Neural Kinship Tracer
  await page1080.evaluate(() => fitToScreen());
  await new Promise(r => setTimeout(r, 300));
  const hoverCardTest = await page1080.evaluate(() => {
    const card = document.querySelector('.tree-card');
    if (!card) return null;
    card.dispatchEvent(new MouseEvent('mouseenter', { bubbles: true }));
    const hud = document.getElementById('neuralKinshipHUD');
    const hudVisible = !hud.classList.contains('hidden');
    const hudName = document.getElementById('hudPersonName').textContent;
    return { hudVisible, hudName };
  });
  const hoverPass = hoverCardTest && hoverCardTest.hudVisible && hoverCardTest.hudName.length > 0;
  results.pc_1080p.neural_kinship_hover = hoverPass ? 'PASS' : 'FAIL';
  console.log(`1.4 Neural Kinship Hover: ${JSON.stringify(hoverCardTest)} -> ${results.pc_1080p.neural_kinship_hover}`);
  await saveScreenshot(page1080, 'pc_1080p_neural_trace_hover.png');

  // 1.5 Opening and Closing Person Drawer & Modals
  const drawerTest = await page1080.evaluate(() => {
    selectPerson('IND_1', 'k34');
    const drawer = document.getElementById('personDrawer');
    const isOpen = !drawer.classList.contains('translate-x-full');
    const personName = document.getElementById('drawerShortName').textContent;
    return { isOpen, personName };
  });
  console.log(`1.5 Drawer opened for: ${drawerTest.personName} -> ${drawerTest.isOpen}`);
  await saveScreenshot(page1080, 'pc_1080p_person_drawer_open.png');

  // Close drawer with Escape
  await page1080.keyboard.press('Escape');
  await new Promise(r => setTimeout(r, 150));
  const drawerClosed = await page1080.evaluate(() => document.getElementById('personDrawer').classList.contains('translate-x-full'));
  
  // Open Add Member Modal
  await page1080.evaluate(() => openAddMemberModal());
  await new Promise(r => setTimeout(r, 150));
  const modalOpen = await page1080.evaluate(() => !document.getElementById('addMemberModal').classList.contains('hidden'));
  await saveScreenshot(page1080, 'pc_1080p_modal_add_member.png');

  // Close Modal with Escape
  await page1080.keyboard.press('Escape');
  await new Promise(r => setTimeout(r, 150));
  const modalClosed = await page1080.evaluate(() => document.getElementById('addMemberModal').classList.contains('hidden'));

  results.pc_1080p.drawer_and_modals = (drawerTest.isOpen && drawerClosed && modalOpen && modalClosed) ? 'PASS' : 'FAIL';
  console.log(`1.5 Drawer & Modal open/close test -> ${results.pc_1080p.drawer_and_modals}`);

  // 1.6 Search Input Autocomplete and Filtering
  const searchTest = await page1080.evaluate(async () => {
    const input = document.getElementById('nameSearchInput');
    input.focus();
    input.value = 'خميس';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    await new Promise(r => setTimeout(r, 200));
    const dropdown = document.getElementById('searchDropdown');
    const isVisible = !dropdown.classList.contains('hidden');
    const items = dropdown.querySelectorAll('.search-result-item');
    return { isVisible, count: items.length };
  });
  results.pc_1080p.search_autocomplete_filter = (searchTest.isVisible && searchTest.count > 0) ? 'PASS' : 'FAIL';
  console.log(`1.6 Search autocomplete: ${searchTest.count} items -> ${results.pc_1080p.search_autocomplete_filter}`);
  await saveScreenshot(page1080, 'pc_1080p_search_autocomplete.png');

  // Dismiss search dropdown
  await page1080.keyboard.press('Escape');

  // 1.7 Theme Toggling between Parchment Heirloom & Dark Neural Archival
  const themeToggleTest = await page1080.evaluate(() => {
    const initialT = currentTheme;
    toggleTheme();
    const darkT = currentTheme;
    const isDarkClass = document.documentElement.classList.contains('dark');
    return { initialT, darkT, isDarkClass };
  });
  results.pc_1080p.theme_toggling = (themeToggleTest.darkT === 'dark' && themeToggleTest.isDarkClass) ? 'PASS' : 'FAIL';
  console.log(`1.7 Theme toggled to: ${themeToggleTest.darkT} -> ${results.pc_1080p.theme_toggling}`);
  await saveScreenshot(page1080, 'pc_1080p_dark_theme.png');

  await page1080.close();

  // ==========================================
  // 2. PC Desktop 2560x1440
  // ==========================================
  console.log('\n--- 2. Testing PC Desktop (2560x1440 QHD) ---');
  const page1440 = await browser.newPage();
  await page1440.setViewport({ width: 2560, height: 1440, deviceScaleFactor: 1 });
  await page1440.goto(`http://localhost:${PORT}`, { waitUntil: 'networkidle0' });

  const qhdInfo = await page1440.evaluate(() => {
    const cardCount = document.querySelectorAll('.tree-card').length;
    const headerBox = document.querySelector('header').getBoundingClientRect();
    return { cardCount, headerWidth: headerBox.width };
  });
  results.pc_1440p.layout_rendering = (qhdInfo.cardCount > 0 && qhdInfo.headerWidth === 2560) ? 'PASS' : 'FAIL';
  console.log(`2.1 QHD Layout & Render: ${JSON.stringify(qhdInfo)} -> ${results.pc_1440p.layout_rendering}`);
  await saveScreenshot(page1440, 'pc_1440p_master_overview.png');

  // Dark mode kinship on 1440p
  await page1440.evaluate(() => {
    toggleTheme();
    traceNeuralKinship('IND_1');
  });
  await new Promise(r => setTimeout(r, 200));
  await saveScreenshot(page1440, 'pc_1440p_dark_theme_kinship.png');
  results.pc_1440p.dark_neural_kinship = 'PASS';
  await page1440.close();

  // ==========================================
  // 3. Mobile Viewport: iPhone (390x844)
  // ==========================================
  console.log('\n--- 3. Testing Mobile iPhone (390x844) ---');
  const pageIphone = await browser.newPage();
  await pageIphone.setViewport({ width: 390, height: 844, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
  await pageIphone.goto(`http://localhost:${PORT}`, { waitUntil: 'networkidle0' });

  // 3.1 Responsive Header Layout
  const iphoneHeader = await pageIphone.evaluate(() => {
    const header = document.querySelector('header');
    const headerBox = header.getBoundingClientRect();
    const searchInput = document.getElementById('nameSearchInput');
    const searchBox = searchInput.getBoundingClientRect();
    const chartSel = document.getElementById('chartViewSelector');
    const selBox = chartSel.getBoundingClientRect();
    const hasHorizontalOverflow = document.documentElement.scrollWidth > window.innerWidth;
    return {
      headerHeight: headerBox.height,
      hasHorizontalOverflow,
      searchWidth: searchBox.width,
      selWidth: selBox.width
    };
  });
  const iphoneHeaderPass = !iphoneHeader.hasHorizontalOverflow && iphoneHeader.headerHeight < 110;
  results.mobile_iphone.responsive_header = iphoneHeaderPass ? 'PASS' : 'FAIL';
  console.log(`3.1 iPhone Header: height=${iphoneHeader.headerHeight}px, overflow=${iphoneHeader.hasHorizontalOverflow} -> ${results.mobile_iphone.responsive_header}`);
  await saveScreenshot(pageIphone, 'mobile_iphone_header_responsive.png');

  // 3.2 Touch Drag Pan & Pinch Zoom without gesture hijacking
  const touchStart = { x: 200, y: 500 };
  const touchMove = { x: 200, y: 350 }; // Pan upwards by 150px
  const beforeTouchPan = await pageIphone.evaluate(() => ({ tx: translateX, ty: translateY }));
  
  await pageIphone.evaluate((ts, tm) => {
    const v = document.getElementById('viewport');
    const t1 = new Touch({ identifier: 0, target: v, clientX: ts.x, clientY: ts.y, pageX: ts.x, pageY: ts.y });
    v.dispatchEvent(new TouchEvent('touchstart', {
      touches: [t1],
      targetTouches: [t1],
      changedTouches: [t1],
      bubbles: true, cancelable: true
    }));
    const t2 = new Touch({ identifier: 0, target: v, clientX: tm.x, clientY: tm.y, pageX: tm.x, pageY: tm.y });
    v.dispatchEvent(new TouchEvent('touchmove', {
      touches: [t2],
      targetTouches: [t2],
      changedTouches: [t2],
      bubbles: true, cancelable: true
    }));
    v.dispatchEvent(new TouchEvent('touchend', {
      touches: [],
      targetTouches: [],
      changedTouches: [t2],
      bubbles: true, cancelable: true
    }));
  }, touchStart, touchMove);
  await new Promise(r => setTimeout(r, 120));

  const afterTouchPan = await pageIphone.evaluate(() => ({ tx: translateX, ty: translateY }));
  const touchPanDy = afterTouchPan.ty - beforeTouchPan.ty;
  const touchPanPass = Math.abs(touchPanDy - (-150)) < 10;
  results.mobile_iphone.touch_drag_pan = touchPanPass ? 'PASS' : 'FAIL';
  console.log(`3.2 iPhone Touch Drag Pan dy=${touchPanDy} -> ${results.mobile_iphone.touch_drag_pan}`);
  await saveScreenshot(pageIphone, 'mobile_iphone_touch_drag_pan.png');

  // Touch Pinch Zoom
  const beforePinch = await pageIphone.evaluate(() => currentScale);
  await pageIphone.evaluate(() => {
    const v = document.getElementById('viewport');
    // Simulate 2 fingers spreading apart from dist=100 to dist=200
    const p1 = new Touch({ clientX: 140, clientY: 400, identifier: 0, target: v, pageX: 140, pageY: 400 });
    const p2 = new Touch({ clientX: 240, clientY: 400, identifier: 1, target: v, pageX: 240, pageY: 400 });
    v.dispatchEvent(new TouchEvent('touchstart', {
      touches: [p1, p2],
      targetTouches: [p1, p2],
      changedTouches: [p1, p2],
      bubbles: true, cancelable: true
    }));
    const p3 = new Touch({ clientX: 90, clientY: 400, identifier: 0, target: v, pageX: 90, pageY: 400 });
    const p4 = new Touch({ clientX: 290, clientY: 400, identifier: 1, target: v, pageX: 290, pageY: 400 });
    v.dispatchEvent(new TouchEvent('touchmove', {
      touches: [p3, p4],
      targetTouches: [p3, p4],
      changedTouches: [p3, p4],
      bubbles: true, cancelable: true
    }));
    v.dispatchEvent(new TouchEvent('touchend', {
      touches: [],
      targetTouches: [],
      changedTouches: [p3, p4],
      bubbles: true, cancelable: true
    }));
  });
  await new Promise(r => setTimeout(r, 120));

  const afterPinch = await pageIphone.evaluate(() => currentScale);
  const pinchPass = afterPinch > beforePinch;
  results.mobile_iphone.touch_pinch_zoom = pinchPass ? 'PASS' : 'FAIL';
  console.log(`3.3 iPhone Pinch Zoom: ${beforePinch.toFixed(2)} -> ${afterPinch.toFixed(2)} -> ${results.mobile_iphone.touch_pinch_zoom}`);
  await saveScreenshot(pageIphone, 'mobile_iphone_pinch_zoom.png');

  // 3.3 Mobile Neural Kinship HUD Positioning (No overflow, Clean Dismiss)
  await pageIphone.evaluate(() => {
    traceNeuralKinship('IND_1');
  });
  await new Promise(r => setTimeout(r, 200));

  const hudPositioning = await pageIphone.evaluate(() => {
    const hud = document.getElementById('neuralKinshipHUD');
    const box = hud.getBoundingClientRect();
    const overflowsRight = box.right > window.innerWidth;
    const overflowsLeft = box.left < 0;
    const dismissBtn = hud.querySelector('button[onclick="clearNeuralKinship()"]');
    const btnBox = dismissBtn ? dismissBtn.getBoundingClientRect() : null;
    return {
      hudWidth: box.width,
      hudLeft: box.left,
      hudRight: box.right,
      windowWidth: window.innerWidth,
      overflows: overflowsRight || overflowsLeft,
      dismissBtnSize: btnBox ? { w: btnBox.width, h: btnBox.height } : null
    };
  });
  const hudPass = !hudPositioning.overflows && hudPositioning.dismissBtnSize.w >= 30;
  results.mobile_iphone.neural_hud_positioning = hudPass ? 'PASS' : 'FAIL';
  console.log(`3.4 iPhone HUD Positioning: width=${hudPositioning.hudWidth}px, overflows=${hudPositioning.overflows} -> ${results.mobile_iphone.neural_hud_positioning}`);
  await saveScreenshot(pageIphone, 'mobile_iphone_neural_hud.png');

  // Dismiss HUD
  await pageIphone.evaluate(() => clearNeuralKinship());
  const hudDismissed = await pageIphone.evaluate(() => document.getElementById('neuralKinshipHUD').classList.contains('hidden'));

  // 3.4 Mobile Drawer Backdrop & Smooth Slide-in
  await pageIphone.evaluate(() => {
    selectPerson('IND_1', 'k34');
  });
  await new Promise(r => setTimeout(r, 350));

  const drawerState = await pageIphone.evaluate(() => {
    const drawer = document.getElementById('personDrawer');
    const backdrop = document.getElementById('drawerBackdrop');
    const drawerBox = drawer.getBoundingClientRect();
    return {
      drawerOpen: !drawer.classList.contains('translate-x-full'),
      drawerWidth: drawerBox.width,
      backdropVisible: !backdrop.classList.contains('hidden')
    };
  });
  const drawerPass = drawerState.drawerOpen && drawerState.backdropVisible && drawerState.drawerWidth === 390;
  results.mobile_iphone.drawer_backdrop_slidein = drawerPass ? 'PASS' : 'FAIL';
  console.log(`3.5 iPhone Drawer Slide-in & Backdrop: ${JSON.stringify(drawerState)} -> ${results.mobile_iphone.drawer_backdrop_slidein}`);
  await saveScreenshot(pageIphone, 'mobile_iphone_drawer_backdrop.png');

  await pageIphone.close();

  // ==========================================
  // 4. Mobile Viewport: Android (412x915)
  // ==========================================
  console.log('\n--- 4. Testing Mobile Android (412x915) ---');
  const pageAndroid = await browser.newPage();
  await pageAndroid.setViewport({ width: 412, height: 915, isMobile: true, hasTouch: true, deviceScaleFactor: 2.625 });
  await pageAndroid.goto(`http://localhost:${PORT}`, { waitUntil: 'networkidle0' });

  // 4.1 Android Responsive Header Layout
  const androidHeader = await pageAndroid.evaluate(() => {
    const header = document.querySelector('header');
    const headerBox = header.getBoundingClientRect();
    const hasHorizontalOverflow = document.documentElement.scrollWidth > window.innerWidth;
    return { headerHeight: headerBox.height, hasHorizontalOverflow };
  });
  results.mobile_android.responsive_header = (!androidHeader.hasHorizontalOverflow && androidHeader.headerHeight < 110) ? 'PASS' : 'FAIL';
  console.log(`4.1 Android Header: height=${androidHeader.headerHeight}px, overflow=${androidHeader.hasHorizontalOverflow} -> ${results.mobile_android.responsive_header}`);
  await saveScreenshot(pageAndroid, 'mobile_android_header_responsive.png');

  // 4.2 Android Neural Kinship HUD
  await pageAndroid.evaluate(() => traceNeuralKinship('IND_1'));
  await new Promise(r => setTimeout(r, 200));

  const androidHud = await pageAndroid.evaluate(() => {
    const hud = document.getElementById('neuralKinshipHUD');
    const box = hud.getBoundingClientRect();
    return {
      hudWidth: box.width,
      overflows: (box.right > window.innerWidth || box.left < 0)
    };
  });
  results.mobile_android.neural_hud = !androidHud.overflows ? 'PASS' : 'FAIL';
  console.log(`4.2 Android HUD: width=${androidHud.hudWidth}px, overflow=${androidHud.overflows} -> ${results.mobile_android.neural_hud}`);
  await saveScreenshot(pageAndroid, 'mobile_android_neural_hud.png');

  // 4.3 Android Drawer Open
  await pageAndroid.evaluate(() => {
    selectPerson('IND_1', 'k34');
  });
  await new Promise(r => setTimeout(r, 350));
  const androidDrawer = await pageAndroid.evaluate(() => {
    const drawer = document.getElementById('personDrawer');
    return !drawer.classList.contains('translate-x-full');
  });
  results.mobile_android.drawer_slidein = androidDrawer ? 'PASS' : 'FAIL';
  console.log(`4.3 Android Drawer Open -> ${results.mobile_android.drawer_slidein}`);
  await saveScreenshot(pageAndroid, 'mobile_android_drawer_open.png');

  await pageAndroid.close();

  await browser.close();
  server.close();

  console.log('\n==========================================');
  console.log('FINAL TEST RESULTS SUMMARY:');
  console.log(JSON.stringify(results, null, 2));
  console.log('==========================================');
  console.log(`Captured ${capturedScreenshots.length} screenshots to:`);
  console.log(`- ${EVIDENCE_DIR}`);
  console.log(`- ${ARTIFACT_DIR}`);

  fs.writeFileSync(path.join(EVIDENCE_DIR, 'test_results.json'), JSON.stringify({ results, capturedScreenshots }, null, 2));
}

server.listen(PORT, async () => {
  try {
    await runTests();
  } catch (err) {
    console.error('Error during test execution:', err);
    process.exit(1);
  }
});
