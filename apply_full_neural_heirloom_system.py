#!/usr/bin/env python3
"""
apply_full_neural_heirloom_system.py
Complete injection of the Neural-Botanical Heirloom Engine matching Image 2 into index.html.
"""

import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Marker 1: Section 3 start
m3 = '/* ==========================================================================\n       3. ORGANIC ILLUSTRATED TREE BACKGROUND ART GENERATOR'
# Marker 2: Section 5 start (View 2 K34)
m5 = '/* ==========================================================================\n       5. VIEW 2: CHART K34 DIRECT ARCHIVAL TREE'
# Marker 3: Section 7 start (Sub-branch view)
m7 = '/* ==========================================================================\n       7. VIEW 4: SUB-BRANCH FAMILY UNIT VIEW'
# Marker 4: Section 8 start (Registry table)
m8 = '/* ==========================================================================\n       8. VIEW 5: MASTER REGISTRY TABLE'

idx3 = content.find(m3)
idx5 = content.find(m5)
idx7 = content.find(m7)
idx8 = content.find(m8)

print(f"Indices: m3={idx3}, m5={idx5}, m7={idx7}, m8={idx8}")
assert idx3 != -1 and idx5 != -1 and idx7 != -1 and idx8 != -1

# Replacement for Section 3 & 4 (generateOrganicTreeBackground + renderMasterTreeToAdam)
section_3_and_4 = """/* ==========================================================================
       3. ORGANIC ILLUSTRATED TREE BACKGROUND ART GENERATOR (IMAGE 2 REPLICA)
       ========================================================================== */
    function generateOrganicTreeBackground(theme, w, h, centerX, trunkBaseY, boughs, showCartouche = false) {
      const isDark = theme === 'dark';
      const goldTrim = isDark ? '#f59e0b' : '#c5a059';
      const goldDim = isDark ? '#b45309' : '#dfc187';
      const trunkCol = isDark ? '#854d0e' : '#452b17';
      const trunkHighlight = isDark ? '#f59e0b' : '#784620';
      const barkDark = isDark ? '#451a03' : '#2b180a';
      const leaf1 = isDark ? '#059669' : '#2e5b3f';
      const leaf2 = isDark ? '#10b981' : '#3b7a57';
      const leaf3 = isDark ? '#f59e0b' : '#d4af37';
      const textCol = isDark ? '#f8fafc' : '#1f140c';
      const subCol = isDark ? '#f59e0b' : '#8c531d';

      let svg = '<g id="illustratedOrganicTreeLayer">';

      // 1. Antique Double Fillet Border around the Canvas (Matching Image 2 Heirloom Poster)
      svg += `
        <rect x="40" y="40" width="${w - 80}" height="${h - 80}" fill="none" stroke="${goldTrim}" stroke-width="2.5" opacity="0.45" />
        <rect x="52" y="52" width="${w - 104}" height="${h - 104}" fill="none" stroke="${goldTrim}" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.35" />
      `;

      // 2. Corner Rosettes & Filigree (Image 2 style)
      const corners = [
        { x: 46, y: 46 },
        { x: w - 46, y: 46 },
        { x: 46, y: h - 46 },
        { x: w - 46, y: h - 46 }
      ];
      corners.forEach(c => {
        svg += `
          <circle cx="${c.x}" cy="${c.y}" r="8" fill="${goldTrim}" opacity="0.75" />
          <circle cx="${c.x}" cy="${c.y}" r="18" fill="none" stroke="${goldTrim}" stroke-width="1.5" opacity="0.5" />
          <circle cx="${c.x}" cy="${c.y}" r="26" fill="none" stroke="${goldTrim}" stroke-width="0.8" stroke-dasharray="4 2" opacity="0.3" />
        `;
      });

      // 3. Symmetrical Generational Rulers along Left & Right Margins (Matching Image 2 "9 GENERATIONS")
      const genLabels = [
        { label: "الجيل ١: الأجداد المؤسسون والأسلاف الكبار (1819م وما قبل)", y: 350 },
        { label: "الجيل ٢: الأجداد المباشرون وتفرع البطون التاريخية", y: 750 },
        { label: "الجيل ٣: الآباء المؤسسون والأعمام الكبار", y: 1250 },
        { label: "الجيل ٤: جيل الأجداد المعاصرين", y: 1750 },
        { label: "الجيل ٥: جيل الآباء والأعمام", y: 2250 },
        { label: "الجيل ٦: جيل الأبناء والإخوة وأبناء العمومة", y: 2750 },
        { label: "الجيل ٧: جيل الأحفاد والشباب المعاصر", y: 3250 },
        { label: "الجيل ٨: جيل البراعم والأجيال الصاعدة", y: 3650 }
      ];

      genLabels.forEach(g => {
        svg += `
          <g opacity="0.4" transform="translate(75, ${g.y})">
            <circle cx="0" cy="0" r="5" fill="${goldTrim}" />
            <line x1="12" y1="0" x2="160" y2="0" stroke="${goldTrim}" stroke-width="1" stroke-dasharray="4 2" />
            <text x="170" y="4" font-family="Amiri, serif" font-size="13" font-weight="bold" fill="${subCol}">${g.label}</text>
          </g>
          <g opacity="0.4" transform="translate(${w - 75}, ${g.y})">
            <circle cx="0" cy="0" r="5" fill="${goldTrim}" />
            <line x1="-12" y1="0" x2="-160" y2="0" stroke="${goldTrim}" stroke-width="1" stroke-dasharray="4 2" />
            <text x="-170" y="4" text-anchor="end" font-family="Amiri, serif" font-size="13" font-weight="bold" fill="${subCol}">${g.label}</text>
          </g>
        `;
      });

      // 4. Central Majestic Tree Trunk & Root System (Image 2 Replica)
      svg += `
        <!-- Majestic Root System spreading outward across base -->
        <path d="M ${centerX - 90} ${trunkBaseY + 220} 
                 C ${centerX - 240} ${trunkBaseY + 290}, ${centerX - 520} ${trunkBaseY + 380}, ${centerX - 780} ${trunkBaseY + 460}
                 C ${centerX - 620} ${trunkBaseY + 480}, ${centerX - 350} ${trunkBaseY + 380}, ${centerX - 40} ${trunkBaseY + 260} Z"
              fill="${trunkCol}" opacity="0.82" />
        <path d="M ${centerX + 90} ${trunkBaseY + 220} 
                 C ${centerX + 240} ${trunkBaseY + 290}, ${centerX + 520} ${trunkBaseY + 380}, ${centerX + 780} ${trunkBaseY + 460}
                 C ${centerX + 620} ${trunkBaseY + 480}, ${centerX + 350} ${trunkBaseY + 380}, ${centerX + 40} ${trunkBaseY + 260} Z"
              fill="${trunkCol}" opacity="0.82" />
        <path d="M ${centerX - 20} ${trunkBaseY + 240} 
                 C ${centerX - 60} ${trunkBaseY + 380}, ${centerX - 120} ${trunkBaseY + 540}, ${centerX - 160} ${trunkBaseY + 680}
                 C ${centerX - 80} ${trunkBaseY + 670}, ${centerX - 10} ${trunkBaseY + 480}, ${centerX + 20} ${trunkBaseY + 260} Z"
              fill="${barkDark}" opacity="0.75" />

        <!-- Main Solid Botanical Trunk with natural tapering -->
        <path d="M ${centerX - 95} ${trunkBaseY + 260}
                 C ${centerX - 75} ${trunkBaseY + 80}, ${centerX - 55} ${trunkBaseY - 400}, ${centerX - 42} ${trunkBaseY - 1800}
                 L ${centerX + 42} ${trunkBaseY - 1800}
                 C ${centerX + 55} ${trunkBaseY - 400}, ${centerX + 75} ${trunkBaseY + 80}, ${centerX + 95} ${trunkBaseY + 260} Z"
              fill="${trunkCol}" opacity="0.88" />

        <!-- Bark Grain Ridges & Shading -->
        <path d="M ${centerX - 24} ${trunkBaseY + 240} C ${centerX - 18} ${trunkBaseY}, ${centerX - 14} ${trunkBaseY - 600}, ${centerX - 10} ${trunkBaseY - 1700}"
              stroke="${trunkHighlight}" stroke-width="4" fill="none" opacity="0.65" />
        <path d="M ${centerX + 24} ${trunkBaseY + 240} C ${centerX + 18} ${trunkBaseY}, ${centerX + 14} ${trunkBaseY - 600}, ${centerX + 10} ${trunkBaseY - 1700}"
              stroke="${trunkHighlight}" stroke-width="4" fill="none" opacity="0.65" />
        
        <!-- Luminous Neural Gold Axon Conduit ascending the center of trunk -->
        <path d="M ${centerX} ${trunkBaseY + 250} L ${centerX} ${trunkBaseY - 1800}"
              stroke="${goldTrim}" stroke-width="2.5" stroke-dasharray="10 5" fill="none" opacity="0.7" />
      `;

      // 5. Sweeping Symmetrical Organic-Neural Boughs
      boughs.forEach(b => {
        const isLeft = b.targetX < centerX;
        const ctrlX1 = isLeft ? centerX - 320 : centerX + 320;
        const ctrlY1 = b.sourceY + 90;
        const ctrlX2 = isLeft ? b.targetX + 260 : b.targetX - 260;
        const ctrlY2 = b.targetY - 100;

        svg += `
          <!-- Main Bough Limb -->
          <path d="M ${centerX} ${b.sourceY} C ${ctrlX1} ${ctrlY1}, ${ctrlX2} ${ctrlY2}, ${b.targetX} ${b.targetY}"
                fill="none" stroke="${trunkCol}" stroke-width="${b.thickness || 16}" stroke-linecap="round" opacity="0.75" />
          <!-- Bark Highlight -->
          <path d="M ${centerX} ${b.sourceY} C ${ctrlX1} ${ctrlY1}, ${ctrlX2} ${ctrlY2}, ${b.targetX} ${b.targetY}"
                fill="none" stroke="${trunkHighlight}" stroke-width="${Math.max((b.thickness || 16) - 6, 3)}" stroke-linecap="round" opacity="0.55" />
          <!-- Embedded Neural Synaptic Conduit -->
          <path d="M ${centerX} ${b.sourceY} C ${ctrlX1} ${ctrlY1}, ${ctrlX2} ${ctrlY2}, ${b.targetX} ${b.targetY}"
                fill="none" stroke="${goldTrim}" stroke-width="1.8" stroke-dasharray="8 6" opacity="0.6" />
        `;

        // Botanical Leaf Clusters along the bough curve
        const midX = (centerX + b.targetX) / 2;
        const midY = (b.sourceY + b.targetY) / 2 + 25;
        const angle = isLeft ? -22 : 22;

        svg += `
          <g transform="translate(${midX}, ${midY}) rotate(${angle})">
            <ellipse cx="0" cy="0" rx="22" ry="11" fill="${leaf1}" opacity="0.85" />
            <ellipse cx="${isLeft ? -18 : 18}" cy="-10" rx="18" ry="9" fill="${leaf2}" opacity="0.9" />
            <ellipse cx="${isLeft ? -30 : 30}" cy="-18" rx="14" ry="7" fill="${leaf3}" opacity="0.95" />
          </g>
          <g transform="translate(${b.targetX}, ${b.targetY - 45}) rotate(${isLeft ? -15 : 15})">
            <ellipse cx="0" cy="0" rx="20" ry="10" fill="${leaf2}" opacity="0.85" />
            <ellipse cx="${isLeft ? 15 : -15}" cy="-8" rx="16" ry="8" fill="${leaf1}" opacity="0.9" />
            <ellipse cx="${isLeft ? 26 : -26}" cy="-14" rx="12" ry="6" fill="${leaf3}" opacity="0.95" />
          </g>
          <!-- Neural Synapse Junction Node -->
          <circle cx="${b.targetX}" cy="${b.targetY}" r="7" fill="${goldTrim}" opacity="0.8" />
          <circle cx="${b.targetX}" cy="${b.targetY}" r="15" fill="none" stroke="${goldTrim}" stroke-width="1.5" stroke-dasharray="3 2" opacity="0.5" />
        `;
      });

      // 6. Grand Baroque Title Cartouche (Image 2 style)
      if (showCartouche) {
        const cartW = 1000;
        const cartH = 220;
        const cartX = centerX - cartW / 2;
        const cartY = 65;
        const cartBg = isDark ? '#141824' : '#fffdf8';

        svg += `
          <g id="ornateTitleCartouche">
            <rect x="${cartX}" y="${cartY}" width="${cartW}" height="${cartH}" rx="32" 
                  fill="${cartBg}" stroke="${goldTrim}" stroke-width="3" 
                  filter="drop-shadow(0 10px 35px rgba(0,0,0,0.20))" />
            <rect x="${cartX + 8}" y="${cartY + 8}" width="${cartW - 16}" height="${cartH - 16}" rx="24" 
                  fill="none" stroke="${goldTrim}" stroke-width="1.2" stroke-dasharray="6 3" opacity="0.65" />

            <path d="M ${centerX - 70} ${cartY} Q ${centerX} ${cartY - 36} ${centerX + 70} ${cartY} Q ${centerX} ${cartY - 16} ${centerX - 70} ${cartY} Z" 
                  fill="${goldTrim}" opacity="0.85" />

            <text x="${centerX}" y="${cartY + 54}" text-anchor="middle" font-family="Amiri, serif" font-size="34" font-weight="700" fill="${textCol}" letter-spacing="1">
              مشجرة عائلة آل خميس الكبرى الجامعة
            </text>
            <text x="${centerX}" y="${cartY + 90}" text-anchor="middle" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="${subCol}" letter-spacing="4">
              THE AL-KHAMIS HISTORICAL FAMILY TREE
            </text>
            <text x="${centerX}" y="${cartY + 135}" text-anchor="middle" font-family="Cairo, sans-serif" font-size="15" font-weight="600" fill="${textCol}" opacity="0.92">
              سلسلة الأنساب التاريخية الشاملة المعتمدة من آدم عليه السلام إلى اليوم
            </text>
            <text x="${centerX}" y="${cartY + 175}" text-anchor="middle" font-family="Amiri, serif" font-size="14" font-weight="bold" fill="${subCol}">
              أوال التاريخية • السنابس وسترة والبلاد القديم • مملكة البحرين • ١٨١٩م
            </text>
          </g>
        `;
      }

      svg += '</g>';
      return svg;
    }

    /* ==========================================================================
       4. VIEW 1: MASTER GRAND TREE TO ADAM (ORGANIC NEURAL HEIRLOOM MASTER)
       ========================================================================== */
    function renderMasterTreeToAdam() {
      if (!window.FAMILY_DATA || !window.FAMILY_DATA.individuals) {
        setTimeout(renderMasterTreeToAdam, 100);
        return;
      }

      document.getElementById('registryViewOverlay').classList.add('hidden');
      document.getElementById('chartHeaderTitle').textContent = 'المشجرة الكبرى الشاملة الجامعة إلى آدم عليه السلام (تحفة الأنساب الملكية)';
      document.getElementById('chartHeaderSubtitle').textContent = 'الهيكل الشجري العضوي الجامع: تفرع الأنساب والأعمام وأبناء العمومة والأحفاد بنظام الشبكة العصبية 🌿';

      nodesContainer.innerHTML = '';
      svgConnectors.innerHTML = '';

      const isDark = currentTheme === 'dark';
      const strokeCol = isDark ? '#d97706' : '#6d4b30';
      const spouseCol = isDark ? '#fbbf24' : '#b8860b';

      const totalCanvasWidth = 6400;
      const totalCanvasHeight = 4000;
      const centerX = 3200;
      setCanvasDimensions(totalCanvasWidth, totalCanvasHeight);

      // 8 Grand Boughs definitions radiating symmetrically (4 left, 4 right)
      const branchDefinitions = [
        // Left Flank
        { code: 'Q',       title: 'فرع العراق والقرية (البصرة والنجف)', region: 'العراق', count: '193 فرداً موثقاً', targetX: 1100, targetY: 850, rootId: 'ANC_ROOT_Q' },
        { code: 'S/H',     title: 'فرع السعودية والأحساء والقطيف', region: 'السعودية', count: '162 فرداً موثقاً', targetX: 950, targetY: 1550, rootId: 'ANC_ROOT_S_H' },
        { code: 'D',       title: 'فرع آل داغر وآل عبد النبي', region: 'البحرين والعراق', count: '162 فرداً موثقاً', targetX: 1050, targetY: 2300, rootId: 'ANC_ROOT_D' },
        { code: 'M',       title: 'فرع آل الكايد والمدحوب', region: 'السنابس وسترة', count: '174 فرداً موثقاً', targetX: 1250, targetY: 3050, rootId: 'ANC_ROOT_M' },
        // Right Flank
        { code: 'k34',     title: 'فرع عيسى وعلي بن خميس (مشجرة K34)', region: 'السنابس', count: '37 فرداً تاريخياً', targetX: 5300, targetY: 850, isK34: true },
        { code: 'K01-K15', title: 'فرع علي بن أحمد آل خميس (الجذع الأكبر)', region: 'السنابس والمنامة', count: '655 فرداً موثقاً', targetX: 5450, targetY: 1550, rootId: 'ANC_ROOT_K01-K15' },
        { code: 'K16-K33', title: 'فرع حسن وعباس آل خميس', region: 'السنابس والبلاد القديم', count: '377 فرداً موثقاً', targetX: 5350, targetY: 2300, rootId: 'ANC_ROOT_K16-K33' },
        { code: 'K35-K46', title: 'فرع عبد الحميد وحسين آل خميس', region: 'السنابس والدراز', count: '404 أفراد موثقين', targetX: 5150, targetY: 3050, rootId: 'ANC_ROOT_K35-K46' }
      ];

      const boughs = branchDefinitions.map(b => ({
        sourceY: 1600,
        targetX: b.targetX,
        targetY: b.targetY,
        thickness: 18
      }));

      // Render Illustrated Botanical Tree Background
      let svgContent = generateOrganicTreeBackground(currentTheme, totalCanvasWidth, totalCanvasHeight, centerX, 3400, boughs, true);

      // SECTION A: 14 Epoch Patriarchs along the Central Trunk
      const patriarchs = [
        { id: "ANC_ADAM", name: "آدم عليه السلام", title: "أبو البشر وخليفة الله في الأرض", era: "بداية الخلق", y: 300 },
        { id: "ANC_SHEETH", name: "شيث عليه السلام", title: "هبة الله ووصي آدم الأول", era: "العصر الأول", y: 395 },
        { id: "ANC_IDRIS", name: "إدريس عليه السلام", title: "أخنوخ — أول من خط بالقلم", era: "العصر الأول", y: 490 },
        { id: "ANC_NUH", name: "نوح عليه السلام", title: "شيخ المرسلين والآدم الثاني", era: "عصر الطوفان", y: 585 },
        { id: "ANC_SAM", name: "سام بن نوح", title: "أبو الشعوب والقبائل السامية", era: "ما بعد الطوفان", y: 680 },
        { id: "ANC_HUD", name: "عابر (هود عليه السلام)", title: "فاتح عهد وقبائل العرب العاربة", era: "العصر القديم", y: 775 },
        { id: "ANC_IBRAHIM", name: "إبراهيم الخليل عليه السلام", title: "خليل الرحمن وإمام الحنفاء", era: "~1900 ق.م", y: 870 },
        { id: "ANC_ISMAIL", name: "إسماعيل الذبيح عليه السلام", title: "نبي الله وباني البيت الحرام", era: "~1800 ق.م", y: 965 },
        { id: "ANC_ADNAN", name: "عَدْنَان", title: "جد العرب العدنانية المستعربة", era: "~600 ق.م", y: 1060 },
        { id: "ANC_MAADD", name: "معدّ بن عدنان", title: "جد قبائل نزار ومضر وربيعة", era: "العصر القديم", y: 1155 },
        { id: "ANC_NIZAR", name: "نزار بن معدّ", title: "أبو ربيعة ومضر وإياد وأنمار", era: "العصر القديم", y: 1250 },
        { id: "ANC_RABIAH", name: "رَبِيعَة بن نزار", title: "ربيعة الفرس — الجذم العدناني بالبحرين التاريخية", era: "العصر القديم", y: 1345 },
        { id: "ANC_TAGHLIB", name: "بنو تغلب وعبد القيس", title: "قبائل ربيعة العريقة بإقليم البحرين (أوال)", era: "صدر الإسلام", y: 1440 },
        { id: "ANC_KHAMIS_ROOT", name: "علي بن خميس بن أحمد آل خميس (1819-1896م)", title: "الجد الجامع ومؤسس الأسرة بالسنابس وسترة", era: "1819 - 1896م", y: 1545 }
      ];

      patriarchs.forEach((anc, idx) => {
        const card = document.createElement('div');
        card.id = `card_${anc.id}`;
        card.className = 'absolute tree-card rounded-2xl px-4 py-2.5 shadow-xl text-center cursor-pointer transition-all flex flex-col justify-center';
        card.style.left = `${centerX - 140}px`;
        card.style.top = `${anc.y}px`;
        card.style.width = '280px';
        card.style.height = '60px';
        card.style.borderColor = isDark ? '#d97706' : '#b8860b';
        card.style.borderWidth = '2px';

        card.innerHTML = `
          <div class="font-bold text-sm font-amiri" style="color: ${isDark ? '#fef3c7' : '#8c531d'};" dir="rtl">${anc.name}</div>
          <div class="text-[10px] font-sans truncate" style="color: var(--text-muted);" dir="rtl">${anc.title}</div>
        `;

        card.addEventListener('click', (e) => {
          e.stopPropagation();
          showClassicalModal(anc);
        });
        nodesContainer.appendChild(card);

        if (idx > 0) {
          const prev = patriarchs[idx - 1];
          svgContent += `
            <line x1="${centerX}" y1="${prev.y + 60}" x2="${centerX}" y2="${anc.y}" 
                  stroke="${strokeCol}" stroke-width="3" marker-end="url(#arrow-gold-down)" data-from="${prev.id}" data-to="${anc.id}" />
          `;
        }
      });

      // SECTION B: The 8 Grand Branch Portals
      branchDefinitions.forEach(b => {
        const bCard = document.createElement('div');
        bCard.id = `branch_portal_${b.code}`;
        bCard.className = 'absolute tree-card rounded-2xl p-3 shadow-2xl text-center cursor-pointer transition-all flex flex-col justify-center';
        bCard.style.left = `${b.targetX - 160}px`;
        bCard.style.top = `${b.targetY}px`;
        bCard.style.width = '320px';
        bCard.style.height = '86px';
        bCard.style.borderColor = isDark ? '#38bdf8' : '#3b7a57';
        bCard.style.borderWidth = '2px';

        bCard.innerHTML = `
          <div class="font-bold text-sm font-amiri" style="color: ${isDark ? '#38bdf8' : '#2e5b3f'};" dir="rtl">${b.title}</div>
          <div class="text-[11px] font-mono mt-0.5" style="color: var(--gold-accent);">${b.count} • ${b.region}</div>
          <div class="text-[10px] mt-1 text-sky-600 dark:text-sky-400 font-semibold flex items-center justify-center gap-1">
            <span>🔍 انقر للاستعراض والتكبير الكامل</span>
          </div>
        `;

        bCard.addEventListener('click', (e) => {
          e.stopPropagation();
          switchView(b.code);
        });

        nodesContainer.appendChild(bCard);
      });

      // SECTION C: Render Prominent Family Houses around each Bough in Master Tree
      const allInds = window.FAMILY_DATA.individuals || [];
      const byId = new Map(allInds.map(i => [i.id, i]));
      (window.FAMILY_DATA.k34_nodes || []).forEach(n => byId.set(n.id, n));

      // 1. K34 Archival Tree under K34 Portal
      const k34Nodes = window.FAMILY_DATA.k34_nodes || [];
      const k34StartX = 5300 - 800;
      const k34StartY = 970;

      k34Nodes.forEach(node => {
        const card = document.createElement('div');
        card.id = `card_${node.id}`;
        card.className = 'absolute tree-card rounded-xl px-2.5 py-1.5 flex items-center justify-between text-xs shadow-md cursor-pointer transition-all';
        card.style.left = `${node.x + k34StartX}px`;
        card.style.top = `${node.y + k34StartY}px`;
        card.style.width = `${node.width || 190}px`;
        card.style.height = `${node.height || 46}px`;

        const isLiving = node.status_type === 'living';
        card.innerHTML = `
          <div class="truncate w-full text-right" dir="rtl">
            <div class="flex items-center gap-1.5 justify-between">
              <span class="font-bold text-[12px] font-arabic truncate" style="color: var(--text-main);">${node.short_name || node.name}</span>
              <span class="text-[10px] shrink-0">${isLiving ? '🟢' : '⚪'}</span>
            </div>
            <div class="text-[9px] truncate" style="color: var(--text-muted);">${node.role || ''}</div>
          </div>
        `;

        card.addEventListener('click', (e) => {
          e.stopPropagation();
          selectPerson(node.id, 'k34');
        });
        card.addEventListener('mouseenter', () => traceNeuralKinship(node.id));

        nodesContainer.appendChild(card);
      });

      // 2. Prominent Sub-House Patriarchs under K01-K15, Q, S/H, D, M
      branchDefinitions.filter(b => !b.isK34).forEach(b => {
        const root = byId.get(b.rootId);
        if (!root || !root.child_ids) return;

        const children = root.child_ids.map(cid => byId.get(cid)).filter(Boolean).slice(0, 6);
        const count = children.length;
        if (count === 0) return;

        const houseW = 190;
        const houseH = 46;
        const gap = 20;
        const totalW = count * houseW + (count - 1) * gap;
        const startX = b.targetX - totalW / 2;
        const startY = b.targetY + 115;

        // Stem from Portal to house bar
        svgContent += `
          <line x1="${b.targetX}" y1="${b.targetY + 86}" x2="${b.targetX}" y2="${startY - 25}" 
                stroke="${strokeCol}" stroke-width="2" marker-end="url(#arrow-gold-down)" />
        `;

        children.forEach((child, idx) => {
          const cX = startX + idx * (houseW + gap);
          const cY = startY;

          const card = document.createElement('div');
          card.id = `card_${child.id}`;
          card.className = 'absolute tree-card rounded-xl px-2.5 py-1.5 flex items-center justify-between text-xs shadow-md cursor-pointer transition-all';
          card.style.left = `${cX}px`;
          card.style.top = `${cY}px`;
          card.style.width = `${houseW}px`;
          card.style.height = `${houseH}px`;

          const isLiving = child.status_type === 'living';
          card.innerHTML = `
            <div class="truncate w-full text-right" dir="rtl">
              <div class="flex items-center gap-1.5 justify-between">
                <span class="font-bold text-[11px] font-arabic truncate" style="color: var(--text-main);">${child.short_name || child.name}</span>
                <span class="text-[9px] shrink-0">${isLiving ? '🟢' : '⚪'}</span>
              </div>
              <div class="text-[9px] truncate" style="color: var(--text-muted);">${child.relation_type || 'رئيس أسرة'}</div>
            </div>
          `;

          card.addEventListener('click', (e) => {
            e.stopPropagation();
            selectPerson(child.id, b.code);
          });
          card.addEventListener('mouseenter', () => traceNeuralKinship(child.id));

          nodesContainer.appendChild(card);

          // Conduit line
          svgContent += `
            <path d="M ${b.targetX} ${startY - 25} C ${b.targetX} ${startY - 10}, ${cX + houseW/2} ${startY - 15}, ${cX + houseW/2} ${cY}" 
                  fill="none" stroke="${strokeCol}" stroke-width="1.8" data-from="${b.rootId}" data-to="${child.id}" />
          `;
        });
      });

      svgConnectors.innerHTML = svgContent;
    }
"""

# Replacement for Section 7 (Universal Balanced Hierarchical Sub-branch view + Neural Kinship Engine)
section_7_and_neural = """/* ==========================================================================
       7. VIEW 4: SUB-BRANCH FAMILY UNIT VIEW (BALANCED SYMMETRICAL TREE ENGINE)
       ========================================================================== */
    function renderSubBranchView(branchCode) {
      if (!window.FAMILY_DATA || !window.FAMILY_DATA.individuals) {
        setTimeout(() => renderSubBranchView(branchCode), 100);
        return;
      }
      document.getElementById('registryViewOverlay').classList.add('hidden');
      
      const branchTitles = {
        'k34': 'مشجرة السنابس التاريخية — أسرة عيسى وعلي بن خميس (K34)',
        'K01-K15': 'مشجرة فرع علي بن أحمد آل خميس (K01–K15)',
        'K16-K33': 'مشجرة فرع حسن وعباس آل خميس (K16–K33)',
        'K35-K46': 'مشجرة فرع عبد الحميد وحسين آل خميس (K35–K46)',
        'Q': 'مشجرة فرع العراق والقرية — البصرة والنجف (Q)',
        'S/H': 'مشجرة فرع السعودية والأحساء والقطيف (S/H)',
        'D': 'مشجرة فرع آل داغر وآل عبد النبي (D)',
        'M': 'مشجرة فرع آل الكايد والمدحوب — السنابس (M)'
      };
      
      document.getElementById('chartHeaderTitle').textContent = branchTitles[branchCode] || `مشجرة فرع ${branchCode}`;
      document.getElementById('chartHeaderSubtitle').textContent = 'هيكلية الأنساب الشجرية المتناظرة: الأجداد والآباء والأعمام والأبناء بخطوط عصبية انسيابية 🌿';

      nodesContainer.innerHTML = '';
      svgConnectors.innerHTML = '';

      const isDark = currentTheme === 'dark';
      const strokeCol = isDark ? '#d97706' : '#6d4b30';
      const spouseCol = isDark ? '#fbbf24' : '#b8860b';

      const allInds = window.FAMILY_DATA.individuals || [];
      const k34Nodes = window.FAMILY_DATA.k34_nodes || [];
      const byId = new Map(allInds.map(i => [i.id, i]));
      k34Nodes.forEach(n => byId.set(n.id, n));

      const branchNodes = allInds.filter(i => {
        const b = i.sub_branch || i.chart || i.branch || '';
        return b.includes(branchCode) && !i.isUnlinked;
      });

      if (branchNodes.length === 0) {
        nodesContainer.innerHTML = `
          <div class="p-16 text-center text-slate-400 font-arabic text-sm" dir="rtl">
            <div class="text-2xl mb-2">📜</div>
            لا توجد شجرة أسرية متصلة مسجلة تحت هذا الرمز مباشرة.<br>
            <button onclick="switchView('master')" class="mt-4 px-5 py-2.5 bg-amber-600 text-white rounded-xl text-xs font-bold hover:bg-amber-700 shadow-md transition-all">
              العودة إلى المشجرة الكبرى الجامعة
            </button>
          </div>
        `;
        return;
      }

      const branchIds = new Set(branchNodes.map(i => i.id));
      const roots = branchNodes.filter(node => {
        const pids = node.parent_ids || [];
        return !pids.some(pid => branchIds.has(pid));
      });

      roots.sort((a, b) => {
        if (a.id.startsWith('ANC_ROOT_')) return -1;
        if (b.id.startsWith('ANC_ROOT_')) return 1;
        return 0;
      });

      const CARD_W = 190;
      const CARD_H = 46;
      const SPOUSE_GAP = 28;
      const SIBLING_GAP = 24;
      const LEVEL_H = 120;

      // Symmetrical Hierarchical Layout Algorithm (0 Overlaps, 0 Staircases)
      function layoutBalancedSubtree(nodeId, visited = new Set()) {
        if (visited.has(nodeId)) return { width: CARD_W, height: CARD_H, cards: [], lines: [] };
        visited.add(nodeId);

        const node = byId.get(nodeId);
        if (!node) return { width: CARD_W, height: CARD_H, cards: [], lines: [] };

        const cards = [];
        const lines = [];

        let spouse = null;
        if (node.spouse_ids && node.spouse_ids.length > 0) {
          const s = byId.get(node.spouse_ids[0]);
          if (s && branchIds.has(s.id)) {
            spouse = s;
            if ((spouse.child_ids || []).length === 0) visited.add(spouse.id);
          }
        }
        const coupleW = spouse ? (CARD_W * 2 + SPOUSE_GAP) : CARD_W;

        const children = (node.child_ids || [])
          .filter(cid => branchIds.has(cid) && !visited.has(cid))
          .map(cid => byId.get(cid))
          .filter(Boolean);

        if (children.length === 0) {
          cards.push({ node, relX: 0, relY: 0, width: CARD_W, height: CARD_H });
          if (spouse) {
            cards.push({ node: spouse, relX: CARD_W + SPOUSE_GAP, relY: 0, width: CARD_W, height: CARD_H, isSpouse: true });
            lines.push({ type: 'marriage', from: node.id, to: spouse.id, x1: CARD_W, y1: CARD_H/2, x2: CARD_W + SPOUSE_GAP, y2: CARD_H/2 });
          }
          return { width: coupleW, height: CARD_H, cards, lines };
        }

        const childLayouts = children.map(c => layoutBalancedSubtree(c.id, visited));
        let childrenW = 0;
        childLayouts.forEach((cl, i) => {
          childrenW += cl.width;
          if (i > 0) childrenW += SIBLING_GAP;
        });

        const totalW = Math.max(coupleW, childrenW);
        const parentRelX = (totalW - coupleW) / 2;

        cards.push({ node, relX: parentRelX, relY: 0, width: CARD_W, height: CARD_H });
        let coupleMidX = parentRelX + CARD_W / 2;

        if (spouse) {
          cards.push({ node: spouse, relX: parentRelX + CARD_W + SPOUSE_GAP, relY: 0, width: CARD_W, height: CARD_H, isSpouse: true });
          coupleMidX = parentRelX + CARD_W + SPOUSE_GAP / 2;
          lines.push({ 
            type: 'marriage', 
            from: node.id, 
            to: spouse.id, 
            x1: parentRelX + CARD_W, 
            y1: CARD_H / 2, 
            x2: parentRelX + CARD_W + SPOUSE_GAP, 
            y2: CARD_H / 2 
          });
        }

        let curChildX = (totalW - childrenW) / 2;
        childLayouts.forEach((cl, i) => {
          const ch = children[i];
          const childMidX = curChildX + cl.width / 2;

          cl.cards.forEach(c => {
            cards.push({
              node: c.node,
              relX: curChildX + c.relX,
              relY: LEVEL_H + c.relY,
              width: c.width,
              height: c.height,
              isSpouse: c.isSpouse
            });
          });

          cl.lines.forEach(l => {
            lines.push({
              ...l,
              x1: curChildX + l.x1,
              y1: LEVEL_H + l.y1,
              x2: curChildX + l.x2,
              y2: LEVEL_H + l.y2
            });
          });

          // Smooth Bezier conduit from parent to child
          lines.push({
            type: 'conduit',
            fromId: node.id,
            toId: ch.id,
            x1: coupleMidX,
            y1: CARD_H,
            x2: childMidX,
            y2: LEVEL_H
          });

          curChildX += cl.width + SIBLING_GAP;
        });

        const maxChildH = Math.max(...childLayouts.map(cl => cl.height));
        return { width: totalW, height: LEVEL_H + maxChildH, cards, lines };
      }

      // Layout all roots
      let currentX = 160;
      const allCards = [];
      const allLines = [];
      const visited = new Set();

      roots.forEach(root => {
        if (visited.has(root.id)) return;
        const res = layoutBalancedSubtree(root.id, visited);
        res.cards.forEach(c => {
          allCards.push({
            ...c,
            x: currentX + c.relX,
            y: 180 + c.relY
          });
        });
        res.lines.forEach(l => {
          allLines.push({
            ...l,
            x1: currentX + l.x1,
            y1: 180 + l.y1,
            x2: currentX + l.x2,
            y2: 180 + l.y2
          });
        });
        currentX += res.width + 120;
      });

      const maxX = Math.max(currentX + 160, 3200);
      let maxY = 1800;
      allCards.forEach(c => {
        if (c.y + c.height + 250 > maxY) maxY = c.y + c.height + 250;
      });

      setCanvasDimensions(maxX, maxY);

      // Organic Tree Background
      let svg = generateOrganicTreeBackground(currentTheme, maxX, maxY, maxX / 2, 160, [], false);

      // Render Connectors
      allLines.forEach(l => {
        if (l.type === 'marriage') {
          svg += `
            <line x1="${l.x1}" y1="${l.y1}" x2="${l.x2}" y2="${l.y2}" stroke="${spouseCol}" stroke-width="2" stroke-dasharray="4 3" data-from="${l.from}" data-to="${l.to}" />
            <text x="${(l.x1 + l.x2)/2}" y="${l.y1 + 4}" text-anchor="middle" font-size="12">💍</text>
          `;
        } else if (l.type === 'conduit') {
          const midY = (l.y1 + l.y2) / 2;
          svg += `
            <path d="M ${l.x1} ${l.y1} C ${l.x1} ${midY}, ${l.x2} ${midY}, ${l.x2} ${l.y2}" 
                  fill="none" stroke="${strokeCol}" stroke-width="2" marker-end="url(#arrow-gold-down)" data-from="${l.fromId}" data-to="${l.toId}" />
          `;
        }
      });

      svgConnectors.innerHTML = svg;

      // Render HTML Cards
      allCards.forEach(c => {
        const card = document.createElement('div');
        card.id = `card_${c.node.id}`;
        card.className = 'absolute tree-card rounded-xl px-2.5 py-1.5 flex items-center justify-between text-xs shadow-md cursor-pointer transition-all';
        card.style.left = `${c.x}px`;
        card.style.top = `${c.y}px`;
        card.style.width = `${c.width}px`;
        card.style.height = `${c.height}px`;

        if (c.node.id.startsWith('ANC_ROOT_')) {
          card.style.borderColor = isDark ? '#38bdf8' : '#3b7a57';
          card.style.borderWidth = '2px';
        }

        const isLiving = c.node.status_type === 'living';
        card.innerHTML = `
          <div class="truncate w-full text-right" dir="rtl">
            <div class="flex items-center gap-1.5 justify-between">
              <span class="font-bold text-[11px] font-arabic truncate" style="color: var(--text-main);">${c.node.short_name || c.node.name}</span>
              <span class="text-[9px] shrink-0">${isLiving ? '🟢' : '⚪'}</span>
            </div>
            <div class="text-[9px] truncate" style="color: var(--text-muted);">${c.node.relation_type || c.node.title || ''}</div>
          </div>
        `;

        card.addEventListener('click', (e) => {
          e.stopPropagation();
          selectPerson(c.node.id, branchCode);
        });
        card.addEventListener('mouseenter', () => traceNeuralKinship(c.node.id));

        nodesContainer.appendChild(card);
      });

      fitToScreen();
    }

    /* ==========================================================================
       NEURAL KINSHIP PROPAGATION & INTERACTIVE HUD ENGINE
       ========================================================================== */
    function getAncestors(id, byId, visited = new Set()) {
      const node = byId.get(id);
      if (!node || visited.has(id)) return [];
      visited.add(id);
      const pids = node.parent_ids || [];
      const ancestors = [];
      pids.forEach(pid => {
        const p = byId.get(pid);
        if (p) {
          ancestors.push(p);
          ancestors.push(...getAncestors(pid, byId, visited));
        }
      });
      return ancestors;
    }

    function getDescendants(id, byId, visited = new Set()) {
      const node = byId.get(id);
      if (!node || visited.has(id)) return [];
      visited.add(id);
      const cids = node.child_ids || [];
      const descendants = [];
      cids.forEach(cid => {
        const c = byId.get(cid);
        if (c) {
          descendants.push(c);
          descendants.push(...getDescendants(cid, byId, visited));
        }
      });
      return descendants;
    }

    function getSiblings(id, byId) {
      const node = byId.get(id);
      if (!node) return [];
      const pids = node.parent_ids || [];
      if (pids.length === 0) return [];
      const sibSet = new Set();
      pids.forEach(pid => {
        const par = byId.get(pid);
        if (par) {
          (par.child_ids || []).forEach(cid => {
            if (cid !== id && byId.has(cid)) sibSet.add(cid);
          });
        }
      });
      return Array.from(sibSet).map(sid => byId.get(sid)).filter(Boolean);
    }

    function getUncles(id, byId) {
      const node = byId.get(id);
      if (!node) return [];
      const pids = node.parent_ids || [];
      const uncleSet = new Set();
      pids.forEach(pid => {
        const parSibs = getSiblings(pid, byId);
        parSibs.forEach(s => uncleSet.add(s.id));
      });
      return Array.from(uncleSet).map(uid => byId.get(uid)).filter(Boolean);
    }

    function getCousins(id, byId) {
      const uncles = getUncles(id, byId);
      const cousinSet = new Set();
      uncles.forEach(u => {
        (u.child_ids || []).forEach(cid => {
          if (cid !== id && byId.has(cid)) cousinSet.add(cid);
        });
      });
      return Array.from(cousinSet).map(cid => byId.get(cid)).filter(Boolean);
    }

    function traceNeuralKinship(personId) {
      if (!personId || !window.FAMILY_DATA) return;
      const allInds = window.FAMILY_DATA.individuals || [];
      const byId = new Map(allInds.map(i => [i.id, i]));
      (window.FAMILY_DATA.k34_nodes || []).forEach(n => byId.set(n.id, n));
      (window.FAMILY_DATA.classical_ancestors || []).forEach(a => byId.set(a.id, a));

      const person = byId.get(personId);
      if (!person) return;

      const ancestors = getAncestors(personId, byId);
      const descendants = getDescendants(personId, byId);
      const siblings = getSiblings(personId, byId);
      const uncles = getUncles(personId, byId);
      const cousins = getCousins(personId, byId);

      const ancestorIds = new Set(ancestors.map(a => a.id));
      const descendantIds = new Set(descendants.map(d => d.id));
      const siblingIds = new Set(siblings.map(s => s.id));
      const uncleIds = new Set(uncles.map(u => u.id));
      const cousinIds = new Set(cousins.map(c => c.id));
      const spouseIds = new Set(person.spouse_ids || []);

      const connectedIds = new Set([
        personId,
        ...ancestorIds,
        ...descendantIds,
        ...siblingIds,
        ...uncleIds,
        ...cousinIds,
        ...spouseIds
      ]);

      const allCards = document.querySelectorAll('.tree-card');
      allCards.forEach(card => {
        const rawId = card.id.replace('master_card_', '').replace('card_', '');
        card.classList.remove('neural-active', 'neural-ancestor', 'neural-sibling', 'neural-uncle', 'neural-cousin', 'neural-descendant', 'neural-dimmed');

        if (rawId === personId) {
          card.classList.add('neural-active');
        } else if (ancestorIds.has(rawId)) {
          card.classList.add('neural-ancestor');
        } else if (siblingIds.has(rawId)) {
          card.classList.add('neural-sibling');
        } else if (uncleIds.has(rawId)) {
          card.classList.add('neural-uncle');
        } else if (cousinIds.has(rawId)) {
          card.classList.add('neural-cousin');
        } else if (descendantIds.has(rawId)) {
          card.classList.add('neural-descendant');
        } else {
          card.classList.add('neural-dimmed');
        }
      });

      const lines = svgConnectors.querySelectorAll('line, path');
      lines.forEach(l => {
        const from = l.getAttribute('data-from');
        const to = l.getAttribute('data-to');
        if ((from && connectedIds.has(from)) || (to && connectedIds.has(to))) {
          l.classList.add('neural-pulse-line');
        } else {
          l.classList.remove('neural-pulse-line');
        }
      });

      // Update HUD
      const hud = document.getElementById('neuralKinshipHUD');
      if (hud) {
        document.getElementById('hudPersonName').textContent = person.short_name || person.name;
        document.getElementById('hudPersonBranch').textContent = `${person.branch || person.sub_branch || ''} • ${person.generation || ''}`;
        document.getElementById('hudAncestorsCount').textContent = ancestors.length;
        document.getElementById('hudSiblingsCount').textContent = siblings.length;
        document.getElementById('hudUnclesCount').textContent = uncles.length;
        document.getElementById('hudCousinsCount').textContent = cousins.length;
        document.getElementById('hudDescendantsCount').textContent = descendants.length;

        document.getElementById('hudOpenDrawerBtn').onclick = () => {
          populatePersonDrawer(person);
          document.getElementById('personDrawer').classList.remove('translate-x-full');
          document.getElementById('drawerBackdrop').classList.remove('hidden');
        };

        hud.classList.remove('hidden');
      }
    }

    function clearNeuralKinship() {
      const allCards = document.querySelectorAll('.tree-card');
      allCards.forEach(card => {
        card.classList.remove('neural-active', 'neural-ancestor', 'neural-sibling', 'neural-uncle', 'neural-cousin', 'neural-descendant', 'neural-dimmed');
      });
      const lines = svgConnectors.querySelectorAll('.neural-pulse-line');
      lines.forEach(l => l.classList.remove('neural-pulse-line'));
      const hud = document.getElementById('neuralKinshipHUD');
      if (hud) hud.classList.add('hidden');
    }

    // Dismiss neural highlight on background click
    viewport.addEventListener('click', (e) => {
      if (!e.target.closest('.tree-card') && !e.target.closest('#neuralKinshipHUD') && !e.target.closest('button')) {
        clearNeuralKinship();
      }
    });
"""

# Reconstruct the file:
# Part 1: From start to idx3
# Part 2: section_3_and_4
# Part 3: From idx5 to idx7 (preserves K34 and Classical views)
# Part 4: section_7_and_neural
# Part 5: From idx8 to end (preserves Registry table, Drawer, etc.)

new_content = (
    content[:idx3] +
    section_3_and_4 + "\n" +
    content[idx5:idx7] +
    section_7_and_neural + "\n" +
    content[idx8:]
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully injected Neural-Botanical Heirloom Engine into index.html!")

