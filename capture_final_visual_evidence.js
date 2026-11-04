const path = require('path');
const puppeteer = require('/home/gohako/.gemini/antigravity/scratch/family-tree-app/node_modules/puppeteer-core');

(async () => {
  console.log('Capturing Final Visual Evidence Suite...');
  const browser = await puppeteer.launch({
    executablePath: '/home/gohako/.local/bin/chromium',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu'],
    defaultViewport: { width: 1440, height: 900 }
  });

  const page = await browser.newPage();
  const htmlUrl = 'file://' + path.resolve('index.html');
  await page.goto(htmlUrl, { waitUntil: 'networkidle0' });

  // 1. K34 in Dark Mode (High-contrast bright gold lines)
  console.log('1. Capturing K34 in Dark Mode...');
  await page.evaluate(() => {
    applyTheme('dark');
    switchView('k34');
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'test_evidence/evidence_k34_dark.png' });

  // 2. K34 in Light / Parchment Mode (Deep bronze lines)
  console.log('2. Capturing K34 in Light Mode...');
  await page.evaluate(() => {
    applyTheme('parchment');
    switchView('k34');
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'test_evidence/evidence_k34_light.png' });

  // 3. Branch D (Tall vertical cascade, NOT flat ribbon!)
  console.log('3. Capturing Branch D (Tall Architecture)...');
  await page.evaluate(() => {
    applyTheme('dark');
    switchView('D');
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'test_evidence/evidence_branch_d_tall.png' });

  // 4. Branch M (Tall vertical cascade, NOT flat ribbon!)
  console.log('4. Capturing Branch M (Tall Architecture)...');
  await page.evaluate(() => {
    switchView('M');
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'test_evidence/evidence_branch_m_tall.png' });

  // 5. Branch K01-K15 (Tall vertical cascade, Zero overlap, Clean lines)
  console.log('5. Capturing Branch K01-K15 (Tall Architecture)...');
  await page.evaluate(() => {
    switchView('K01-K15');
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'test_evidence/evidence_branch_k01_k15_tall.png' });

  // 6. Master Grand Tall Tree to Adam
  console.log('6. Capturing Master Grand Tall Tree...');
  await page.evaluate(() => {
    switchView('master');
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'test_evidence/evidence_master_tall.png' });

  // 7. Mobile Phone Viewport (iPhone 14: 390 x 844, touch mode)
  console.log('7. Capturing Mobile Phone Viewport (iPhone 14)...');
  await page.setViewport({ width: 390, height: 844, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
  await page.evaluate(() => {
    switchView('k34');
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'test_evidence/evidence_mobile_iphone14_k34.png' });

  await page.evaluate(() => {
    switchView('D');
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'test_evidence/evidence_mobile_iphone14_branch_d.png' });

  console.log('All visual evidence captured successfully!');
  await browser.close();
})();
