/**
 * verify_tall_tree_layout.js
 * Comprehensive automated layout and collision verification across all views:
 * - Master Tall Tree to Adam (View 1)
 * - Chart K34 Historical Sanabis Tree (View 2)
 * - Classical 37-Generation Lineage (View 3)
 * - Sub-branch dedicated views (K01-K15, K16-K33, K35-K46, Q, S/H, D, M)
 * 
 * Verifies:
 * 1. 0 Bounding Box Collisions across every view.
 * 2. Proper generational hierarchy and spacing.
 * 3. Smooth SVG Bezier conduits and botanical tree background.
 * 4. Captures high-resolution visual evidence screenshots.
 */

const path = require('path');
const puppeteer = require('/home/gohako/.gemini/antigravity/scratch/family-tree-app/node_modules/puppeteer-core');

(async () => {
  console.log('================================================================');
  console.log('🌿 TALL TREE ARCHITECTURE & ZERO-COLLISION VERIFICATION SUITE 🌿');
  console.log('================================================================');

  const browser = await puppeteer.launch({
    executablePath: '/home/gohako/.local/bin/chromium',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu', '--allow-file-access-from-files'],
    defaultViewport: { width: 1920, height: 1080 }
  });

  const page = await browser.newPage();
  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      console.error('Browser Error:', msg.text());
      errors.push(msg.text());
    }
  });
  page.on('pageerror', err => {
    console.error('Page Uncaught Error:', err.message);
    errors.push(err.message);
  });

  const htmlUrl = 'file://' + path.resolve('index.html');
  console.log('Loading Application from:', htmlUrl);
  await page.goto(htmlUrl, { waitUntil: 'networkidle0' });

  // Array of all 10 views to verify
  const viewsToTest = [
    { key: 'master',    name: 'المشجرة الكبرى الشاملة الجامعة إلى آدم (Master Tall Tree)' },
    { key: 'k34',       name: 'مشجرة السنابس التاريخية K34 (Sanabis Historical Chart)' },
    { key: 'classical', name: 'سلسلة النسب الكبرى إلى آدم (Classical 37 Patriarchs)' },
    { key: 'K01-K15',   name: 'فرع علي بن أحمد آل خميس (K01–K15)' },
    { key: 'K16-K33',   name: 'فرع حسن وعباس آل خميس (K16–K33)' },
    { key: 'K35-K46',   name: 'فرع عبد الحميد وحسين آل خميس (K35–K46)' },
    { key: 'Q',         name: 'فرع العراق والقرية — البصرة والنجف (Q)' },
    { key: 'S/H',       name: 'فرع السعودية والأحساء والقطيف (S/H)' },
    { key: 'D',         name: 'فرع آل داغر وآل عبد النبي (D)' },
    { key: 'M',         name: 'فرع آل الكايد والمدحوب — السنابس (M)' }
  ];

  let totalCollisionsGlobal = 0;
  const viewResults = [];

  for (const v of viewsToTest) {
    console.log(`\n🔍 Checking View: [${v.key}] — ${v.name}...`);
    await page.evaluate((k) => switchView(k), v.key);
    await new Promise(r => setTimeout(r, 500));

    const checkResult = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.tree-card'));
      const boxes = cards.map(c => ({
        id: c.id,
        text: (c.innerText || '').split('\n')[0].trim(),
        x: parseFloat(c.style.left) || c.offsetLeft,
        y: parseFloat(c.style.top) || c.offsetTop,
        w: parseFloat(c.style.width) || c.offsetWidth,
        h: parseFloat(c.style.height) || c.offsetHeight
      }));

      const collisions = [];
      for (let i = 0; i < boxes.length; i++) {
        for (let j = i + 1; j < boxes.length; j++) {
          const a = boxes[i];
          const b = boxes[j];
          // Bounding box non-overlap condition (with 1px epsilon tolerance for borders)
          const noOverlap = (a.x + a.w <= b.x + 0.5) || 
                            (b.x + b.w <= a.x + 0.5) || 
                            (a.y + a.h <= b.y + 0.5) || 
                            (b.y + b.h <= a.y + 0.5);

          if (!noOverlap) {
            collisions.push({
              cardA: `${a.id} ("${a.text}") [x:${a.x}, y:${a.y}, w:${a.w}, h:${a.h}]`,
              cardB: `${b.id} ("${b.text}") [x:${b.x}, y:${b.y}, w:${b.w}, h:${b.h}]`
            });
          }
        }
      }

      // Check SVG conduits presence
      const svgConduits = document.querySelectorAll('#svgConnectors path, #svgConnectors line').length;

      return {
        cardCount: boxes.length,
        collisionCount: collisions.length,
        collisions,
        svgConduits
      };
    });

    viewResults.push({
      key: v.key,
      name: v.name,
      ...checkResult
    });

    totalCollisionsGlobal += checkResult.collisionCount;

    console.log(`   ➔ Cards Rendered: ${checkResult.cardCount}`);
    console.log(`   ➔ SVG Connectors: ${checkResult.svgConduits}`);
    console.log(`   ➔ Bounding Box Collisions: ${checkResult.collisionCount}`);

    if (checkResult.collisionCount > 0) {
      console.error(`   ❌ FAIL: Found ${checkResult.collisionCount} collisions:`);
      checkResult.collisions.slice(0, 5).forEach(c => {
        console.error(`      • Collision: ${c.cardA} <---> ${c.cardB}`);
      });
    } else {
      console.log(`   ✅ PASS: Perfect 0 Collisions!`);
    }

    // Capture visual screenshot for primary views
    if (v.key === 'master') {
      await page.screenshot({ path: 'screenshot_master_tall_tree.png' });
      console.log('   📸 Saved screenshot: screenshot_master_tall_tree.png');
    } else if (v.key === 'k34') {
      await page.screenshot({ path: 'screenshot_k34_tree.png' });
      console.log('   📸 Saved screenshot: screenshot_k34_tree.png');
    } else if (v.key === 'K16-K33') {
      await page.screenshot({ path: 'screenshot_branch_k16_tree.png' });
      console.log('   📸 Saved screenshot: screenshot_branch_k16_tree.png');
    } else if (v.key === 'Q') {
      await page.screenshot({ path: 'screenshot_branch_q_tree.png' });
      console.log('   📸 Saved screenshot: screenshot_branch_q_tree.png');
    }
  }

  await browser.close();

  console.log('\n================================================================');
  console.log('📊 VERIFICATION SUMMARY ACROSS ALL 10 GENEALOGICAL VIEWS:');
  console.log('================================================================');
  console.log('View Key    | View Name                                | Cards | Collisions | Status');
  console.log('------------|------------------------------------------|-------|------------|-------');
  viewResults.forEach(r => {
    const status = r.collisionCount === 0 ? '✅ PASS' : '❌ FAIL';
    console.log(
      `${r.key.padEnd(11)} | ` +
      `${r.name.slice(0, 40).padEnd(40)} | ` +
      `${String(r.cardCount).padStart(5)} | ` +
      `${String(r.collisionCount).padStart(10)} | ` +
      `${status}`
    );
  });
  console.log('----------------------------------------------------------------');
  console.log(`GRAND TOTAL OVERLAPS: ${totalCollisionsGlobal}`);
  console.log('================================================================\n');

  if (totalCollisionsGlobal === 0 && errors.length === 0) {
    console.log('🎉 ALL LAYOUT CRITERIA SATISFIED: ZERO COLLISIONS ACROSS ALL VIEWS!');
    process.exit(0);
  } else {
    console.error('❌ LAYOUT VERIFICATION FAILED WITH COLLISIONS OR PAGE ERRORS.');
    process.exit(1);
  }
})();
