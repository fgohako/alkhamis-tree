#!/usr/bin/env python3
"""
update_tall_tree.py
Applies the perfected Tall Tree Layout improvements to index.html:
1. Full vertical botanical trunk from base to Adam with bark ridges & gold axon conduit.
2. Symmetrical 4-tier bough radiating outwards (Q, S/H, D, M on left; K34, K01-K15, K16-K33, K35-K46 on right).
3. 0 Overlaps: Prominent family sub-houses placed under portals with exact spacing and smooth cubic Bezier conduits.
4. Clean K34 representation in Master Tree, avoiding overlap with K01-K15.
"""

INDEX_FILE = 'index.html'

with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

m3 = '/* ==========================================================================\n       3. ORGANIC ILLUSTRATED TREE BACKGROUND ART GENERATOR'
m5 = '/* ==========================================================================\n       5. VIEW 2: CHART K34 DIRECT ARCHIVAL TREE'

idx3 = content.find(m3)
idx5 = content.find(m5)

if idx3 == -1 or idx5 == -1:
    print(f"Error: Markers not found. idx3={idx3}, idx5={idx5}")
    exit(1)

new_section_3_4 = """/* ==========================================================================
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
      const isTall = trunkBaseY > 1500;
      const trunkTopY = isTall ? 260 : Math.max(trunkBaseY - 450, 60);

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
      `;

      if (isTall) {
        svg += `
          <!-- Main Solid Botanical Trunk with natural organic tapering up to Adam -->
          <path d="M ${centerX - 105} ${trunkBaseY + 260}
                   C ${centerX - 85} ${trunkBaseY - 400}, ${centerX - 68} 2400, ${centerX - 52} 1600
                   C ${centerX - 40} 1000, ${centerX - 30} 500, ${centerX - 24} 260
                   L ${centerX + 24} 260
                   C ${centerX + 30} 500, ${centerX + 40} 1000, ${centerX + 52} 1600
                   C ${centerX + 68} 2400, ${centerX + 85} ${trunkBaseY - 400}, ${centerX + 105} ${trunkBaseY + 260} Z"
                fill="${trunkCol}" opacity="0.88" />

          <!-- Bark Grain Ridges & Shading -->
          <path d="M ${centerX - 26} ${trunkBaseY + 240} C ${centerX - 20} 2400, ${centerX - 15} 1400, ${centerX - 8} 265"
                stroke="${trunkHighlight}" stroke-width="4" fill="none" opacity="0.65" />
          <path d="M ${centerX + 26} ${trunkBaseY + 240} C ${centerX + 20} 2400, ${centerX + 15} 1400, ${centerX + 8} 265"
                stroke="${trunkHighlight}" stroke-width="4" fill="none" opacity="0.65" />
          
          <!-- Luminous Neural Gold Axon Conduit ascending the center of trunk -->
          <path d="M ${centerX} ${trunkBaseY + 250} L ${centerX} 260"
                stroke="${goldTrim}" stroke-width="2.5" stroke-dasharray="10 5" fill="none" opacity="0.75" />
        `;
      } else {
        svg += `
          <!-- Botanical Trunk for Horizontal / Archival Views -->
          <path d="M ${centerX - 70} ${trunkBaseY + 160}
                   C ${centerX - 50} ${trunkBaseY + 40}, ${centerX - 35} ${trunkBaseY - 150}, ${centerX - 20} ${trunkTopY}
                   L ${centerX + 20} ${trunkTopY}
                   C ${centerX + 35} ${trunkBaseY - 150}, ${centerX + 50} ${trunkBaseY + 40}, ${centerX + 70} ${trunkBaseY + 160} Z"
                fill="${trunkCol}" opacity="0.85" />
          <path d="M ${centerX} ${trunkBaseY + 150} L ${centerX} ${trunkTopY}"
                stroke="${goldTrim}" stroke-width="2" stroke-dasharray="8 4" fill="none" opacity="0.7" />
        `;
      }

      // 5. Sweeping Symmetrical Organic-Neural Boughs
      boughs.forEach(b => {
        const isLeft = b.targetX < centerX;
        const dx = Math.abs(b.targetX - centerX);
        const ctrlX1 = isLeft ? centerX - dx * 0.42 : centerX + dx * 0.42;
        const ctrlY1 = b.sourceY + (b.targetY < b.sourceY ? -50 : 35);
        const ctrlX2 = isLeft ? b.targetX + dx * 0.28 : b.targetX - dx * 0.28;
        const ctrlY2 = b.targetY - 50;

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
        const midY = (b.sourceY + b.targetY) / 2 + 15;
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
        // Left Flank (4 tiers)
        { code: 'Q',       title: 'فرع العراق والقرية (البصرة والنجف)', region: 'العراق', count: '193 فرداً موثقاً', targetX: 1100, targetY: 850, rootId: 'ANC_ROOT_Q' },
        { code: 'S/H',     title: 'فرع السعودية والأحساء والقطيف', region: 'السعودية', count: '162 فرداً موثقاً', targetX: 950, targetY: 1550, rootId: 'ANC_ROOT_S_H' },
        { code: 'D',       title: 'فرع آل داغر وآل عبد النبي', region: 'البحرين والعراق', count: '162 فرداً موثقاً', targetX: 1050, targetY: 2300, rootId: 'ANC_ROOT_D' },
        { code: 'M',       title: 'فرع آل الكايد والمدحوب', region: 'السنابس وسترة', count: '174 فرداً موثقاً', targetX: 1250, targetY: 3050, rootId: 'ANC_ROOT_M' },
        // Right Flank (4 tiers)
        { code: 'k34',     title: 'فرع عيسى وعلي بن خميس (مشجرة K34)', region: 'السنابس', count: '37 فرداً تاريخياً', targetX: 5300, targetY: 850, isK34: true },
        { code: 'K01-K15', title: 'فرع علي بن أحمد آل خميس (الجذع الأكبر)', region: 'السنابس والمنامة', count: '655 فرداً موثقاً', targetX: 5450, targetY: 1550, rootId: 'ANC_ROOT_K01-K15' },
        { code: 'K16-K33', title: 'فرع حسن وعباس آل خميس', region: 'السنابس والبلاد القديم', count: '377 فرداً موثقاً', targetX: 5350, targetY: 2300, rootId: 'ANC_ROOT_K16-K33' },
        { code: 'K35-K46', title: 'فرع عبد الحميد وحسين آل خميس', region: 'السنابس والدراز', count: '404 أفراد موثقين', targetX: 5150, targetY: 3050, rootId: 'ANC_ROOT_K35-K46' }
      ];

      // Symmetrical 4-tier botanical boughs
      const boughs = [
        // Left Flank
        { sourceY: 1100, targetX: 1100, targetY: 850, thickness: 15 },   // Tier 1: Q
        { sourceY: 1600, targetX: 950, targetY: 1550, thickness: 18 },   // Tier 2: S/H
        { sourceY: 2250, targetX: 1050, targetY: 2300, thickness: 20 },  // Tier 3: D
        { sourceY: 2850, targetX: 1250, targetY: 3050, thickness: 24 },  // Tier 4: M
        // Right Flank
        { sourceY: 1100, targetX: 5300, targetY: 850, thickness: 15 },   // Tier 1: K34
        { sourceY: 1600, targetX: 5450, targetY: 1550, thickness: 18 },  // Tier 2: K01-K15
        { sourceY: 2250, targetX: 5350, targetY: 2300, thickness: 20 },  // Tier 3: K16-K33
        { sourceY: 2850, targetX: 5150, targetY: 3050, thickness: 24 }   // Tier 4: K35-K46
      ];

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

      // SECTION C: Render Prominent Family Houses around each Bough in Master Tree (0 Overlaps Guaranteed)
      const allInds = window.FAMILY_DATA.individuals || [];
      const byId = new Map(allInds.map(i => [i.id, i]));
      (window.FAMILY_DATA.k34_nodes || []).forEach(n => byId.set(n.id, n));

      branchDefinitions.forEach(b => {
        let children = [];
        if (b.isK34) {
          const k34Heads = ['k34_isa_ali_1889', 'k34_ali_isa', 'k34_abbas_isa', 'k34_mirza_isa', 'k34_hassan_father', 'k34_mohammed_redha_uncle'];
          children = k34Heads.map(id => byId.get(id)).filter(Boolean);
        } else {
          const root = byId.get(b.rootId);
          if (root && root.child_ids) {
            children = root.child_ids.map(cid => byId.get(cid)).filter(Boolean).slice(0, 6);
          }
        }

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
              <div class="text-[9px] truncate" style="color: var(--text-muted);">${child.relation_type || child.title || child.role || 'رئيس أسرة'}</div>
            </div>
          `;

          card.addEventListener('click', (e) => {
            e.stopPropagation();
            selectPerson(child.id, b.code);
          });
          card.addEventListener('mouseenter', () => traceNeuralKinship(child.id));

          nodesContainer.appendChild(card);

          // Smooth Bezier Conduit line
          svgContent += `
            <path d="M ${b.targetX} ${startY - 25} C ${b.targetX} ${startY - 10}, ${cX + houseW/2} ${startY - 15}, ${cX + houseW/2} ${cY}" 
                  fill="none" stroke="${strokeCol}" stroke-width="1.8" data-from="${b.rootId || b.code}" data-to="${child.id}" />
          `;
        });
      });

      svgConnectors.innerHTML = svgContent;
    }

    """

updated_content = content[:idx3] + new_section_3_4 + content[idx5:]

with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("Successfully injected Section 3 and Section 4 into index.html")
