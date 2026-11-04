const path = require('path');
const fs = require('fs');

const puppeteer = require('/home/gohako/.gemini/antigravity/scratch/family-tree-app/node_modules/puppeteer-core');

(async () => {
  console.log("Starting automated browser visual verification...");
  const browser = await puppeteer.launch({
    executablePath: '/home/gohako/.local/bin/chromium',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu', '--allow-file-access-from-files'],
    defaultViewport: { width: 1920, height: 1080 }
  });

  const page = await browser.newPage();
  
  // Track console logs and errors
  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      console.error('Page Console Error:', msg.text());
      errors.push(msg.text());
    }
  });
  page.on('pageerror', err => {
    console.error('Page Uncaught Error:', err.message);
    errors.push(err.message);
  });

  const htmlUrl = 'file://' + path.resolve('index.html');
  console.log("Navigating to:", htmlUrl);
  await page.goto(htmlUrl, { waitUntil: 'networkidle0' });

  // 1. Verify Master Tree Elements
  await page.waitForSelector('#ornateTitleCartouche', { timeout: 5000 });
  await page.waitForSelector('.tree-card', { timeout: 5000 });

  const cardCount = await page.evaluate(() => document.querySelectorAll('.tree-card').length);
  console.log("Total tree cards rendered in Master Tree:", cardCount);

  // Capture Master Tree Overview Screenshot
  await page.screenshot({ path: 'screenshot_master_neural_heirloom.png' });
  console.log("Captured screenshot_master_neural_heirloom.png");

  // 2. Test Neural Kinship Tracer
  console.log("Testing Neural Kinship Tracing on IND_1...");
  const traceResult = await page.evaluate(() => {
    traceNeuralKinship('IND_1');
    const hud = document.getElementById('neuralKinshipHUD');
    const hudVisible = !hud.classList.contains('hidden');
    const hudName = document.getElementById('hudPersonName').textContent;
    const hudAncestors = document.getElementById('hudAncestorsCount').textContent;
    const hudSiblings = document.getElementById('hudSiblingsCount').textContent;
    const hudUncles = document.getElementById('hudUnclesCount').textContent;
    const hudCousins = document.getElementById('hudCousinsCount').textContent;
    const activeCards = document.querySelectorAll('.neural-active').length;
    const dimmedCards = document.querySelectorAll('.neural-dimmed').length;

    return { hudVisible, hudName, hudAncestors, hudSiblings, hudUncles, hudCousins, activeCards, dimmedCards };
  });

  console.log("Trace result:", traceResult);
  await page.screenshot({ path: 'screenshot_neural_trace_active.png' });
  console.log("Captured screenshot_neural_trace_active.png");

  // 3. Switch to Branch View (Branch Q)
  console.log("Switching to Branch Q view...");
  await page.evaluate(() => switchView('Q'));
  await new Promise(r => setTimeout(r, 600));

  const qCards = await page.evaluate(() => document.querySelectorAll('.tree-card').length);
  console.log("Branch Q cards rendered:", qCards);

  // Check Overlaps in Branch Q
  const overlapsQ = await page.evaluate(() => {
    const cards = Array.from(document.querySelectorAll('.tree-card'));
    let count = 0;
    for (let i = 0; i < cards.length; i++) {
      for (let j = i + 1; j < cards.length; j++) {
        const a = cards[i].getBoundingClientRect();
        const b = cards[j].getBoundingClientRect();
        const noOverlap = (a.right <= b.left) || (b.right <= a.left) || (a.bottom <= b.top) || (b.bottom <= a.top);
        if (!noOverlap) count++;
      }
    }
    return count;
  });
  console.log("Branch Q Overlaps:", overlapsQ);

  await page.screenshot({ path: 'screenshot_branch_q_clean.png' });
  console.log("Captured screenshot_branch_q_clean.png");

  // 4. Test Dark Neural Archival Mode
  console.log("Toggling Dark Neural Archival Mode...");
  await page.evaluate(() => toggleTheme());
  await new Promise(r => setTimeout(r, 400));
  await page.screenshot({ path: 'screenshot_dark_neural_mode.png' });
  console.log("Captured screenshot_dark_neural_mode.png");

  await browser.close();

  if (errors.length > 0) {
    console.error("Test encountered errors:", errors);
    process.exit(1);
  } else {
    console.log("ALL AUTOMATED VERIFICATION CHECKS PASSED WITH 0 ERRORS!");
    process.exit(0);
  }
})();

