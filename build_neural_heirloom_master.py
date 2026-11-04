#!/usr/bin/env python3
"""
build_neural_heirloom_master.py
Applies the complete neural-botanical heirloom overhaul to index.html
matching Image 2 (The Roettgers Family Tree) and the neural network specification.
"""

import sys
import re

INDEX_PATH = 'index.html'

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Dual Theme CSS for canvas background and Neural Network styling
css_addition = """
    /* ================= NEURAL NETWORK & HEIRLOOM ARTISTRY STYLING ================= */
    #viewport {
      background: radial-gradient(circle at 50% 35%, #fffdfa 0%, #f4eee2 60%, #ebe1cf 100%) !important;
    }
    .dark #viewport, .theme-dark #viewport {
      background: radial-gradient(circle at 50% 30%, #0d1527 0%, #070a14 70%, #04060b 100%) !important;
    }

    /* Neural Kinship Interactive Classes */
    .neural-active {
      transform: scale(1.08) !important;
      z-index: 50 !important;
      border-color: #f59e0b !important;
      box-shadow: 0 0 25px rgba(245, 158, 11, 0.75), 0 0 50px rgba(245, 158, 11, 0.45) !important;
      border-width: 2.5px !important;
    }

    .neural-ancestor {
      transform: scale(1.04) !important;
      z-index: 45 !important;
      border-color: #d97706 !important;
      box-shadow: 0 0 18px rgba(217, 119, 6, 0.55) !important;
      background: linear-gradient(180deg, #fef3c7 0%, #fde68a 100%) !important;
      color: #78350f !important;
    }
    .dark .neural-ancestor {
      background: linear-gradient(180deg, #2e2210 0%, #1c1409 100%) !important;
      color: #fef3c7 !important;
      border-color: #f59e0b !important;
    }

    .neural-sibling {
      transform: scale(1.04) !important;
      z-index: 45 !important;
      border-color: #0284c7 !important;
      box-shadow: 0 0 18px rgba(2, 132, 199, 0.55) !important;
      background: linear-gradient(180deg, #e0f2fe 0%, #bae6fd 100%) !important;
      color: #0369a1 !important;
    }
    .dark .neural-sibling {
      background: linear-gradient(180deg, #0c273e 0%, #061624 100%) !important;
      color: #7dd3fc !important;
      border-color: #38bdf8 !important;
    }

    .neural-uncle {
      transform: scale(1.04) !important;
      z-index: 45 !important;
      border-color: #7c3aed !important;
      box-shadow: 0 0 18px rgba(124, 58, 237, 0.55) !important;
      background: linear-gradient(180deg, #f3e8ff 0%, #e9d5ff 100%) !important;
      color: #6d28d9 !important;
    }
    .dark .neural-uncle {
      background: linear-gradient(180deg, #24143d 0%, #130a22 100%) !important;
      color: #c4b5fd !important;
      border-color: #a78bfa !important;
    }

    .neural-cousin {
      transform: scale(1.04) !important;
      z-index: 45 !important;
      border-color: #059669 !important;
      box-shadow: 0 0 18px rgba(5, 150, 105, 0.55) !important;
      background: linear-gradient(180deg, #d1fae5 0%, #a7f3d0 100%) !important;
      color: #047857 !important;
    }
    .dark .neural-cousin {
      background: linear-gradient(180deg, #092c1f 0%, #051811 100%) !important;
      color: #6ee7b7 !important;
      border-color: #34d399 !important;
    }

    .neural-descendant {
      transform: scale(1.04) !important;
      z-index: 45 !important;
      border-color: #ea580c !important;
      box-shadow: 0 0 18px rgba(234, 88, 12, 0.55) !important;
      background: linear-gradient(180deg, #ffedd5 0%, #fed7aa 100%) !important;
      color: #c2410c !important;
    }
    .dark .neural-descendant {
      background: linear-gradient(180deg, #351a0c 0%, #1d0e06 100%) !important;
      color: #fdba74 !important;
      border-color: #fb923c !important;
    }

    .neural-dimmed {
      opacity: 0.20 !important;
      filter: grayscale(45%) !important;
      transition: opacity 0.25s ease, filter 0.25s ease !important;
    }

    .neural-pulse-line {
      stroke: #f59e0b !important;
      stroke-width: 4px !important;
      stroke-dasharray: 10 5 !important;
      animation: neuralPulseFlow 1.2s linear infinite !important;
      filter: drop-shadow(0 0 8px rgba(245, 158, 11, 0.8)) !important;
    }

    @keyframes neuralPulseFlow {
      to { stroke-dashoffset: -30; }
    }
"""

# Check if css already added
if '/* ================= NEURAL NETWORK & HEIRLOOM ARTISTRY STYLING ================= */' not in html:
    html = html.replace('/* Tree Node Card Styling (Zero Overlap Guaranteed) */', css_addition + '\n    /* Tree Node Card Styling (Zero Overlap Guaranteed) */')

# 2. Add Floating Neural HUD before </main> or at end of body
hud_html = """
  <!-- Floating Neural Kinship HUD (Interactive Relationship Explorer) -->
  <div id="neuralKinshipHUD" class="hidden fixed bottom-6 left-6 z-40 p-4 rounded-2xl shadow-2xl backdrop-blur-md border transition-all duration-300" style="background: var(--header-bg); border-color: var(--gold-accent); min-width: 330px; max-width: 380px;" dir="rtl">
    <div class="flex items-center justify-between gap-3 mb-2 pb-2 border-b border-amber-500/20">
      <div class="flex items-center gap-2.5">
        <div class="w-8 h-8 rounded-xl bg-gradient-to-tr from-amber-600 to-amber-400 flex items-center justify-center text-white text-base shadow">
          🧠
        </div>
        <div>
          <h4 id="hudPersonName" class="font-bold text-xs sm:text-sm font-arabic" style="color: var(--text-main);">الاسم</h4>
          <p id="hudPersonBranch" class="text-[10px]" style="color: var(--text-muted);">الفرع والجيل</p>
        </div>
      </div>
      <button onclick="clearNeuralKinship()" class="w-6 h-6 flex items-center justify-center text-slate-400 hover:text-red-500 rounded-lg text-sm font-bold transition-colors" title="إلغاء التحديد">✕</button>
    </div>
    
    <div class="grid grid-cols-2 gap-1.5 text-[11px] font-arabic mt-2">
      <div class="p-1.5 rounded-lg bg-amber-500/10 border border-amber-500/30 flex items-center justify-between">
        <span class="flex items-center gap-1"><span>👑</span><span>الأسلاف:</span></span>
        <span id="hudAncestorsCount" class="font-mono font-bold text-amber-600 dark:text-amber-400">0</span>
      </div>
      <div class="p-1.5 rounded-lg bg-sky-500/10 border border-sky-500/30 flex items-center justify-between">
        <span class="flex items-center gap-1"><span>👬</span><span>الإخوة:</span></span>
        <span id="hudSiblingsCount" class="font-mono font-bold text-sky-600 dark:text-sky-400">0</span>
      </div>
      <div class="p-1.5 rounded-lg bg-purple-500/10 border border-purple-500/30 flex items-center justify-between">
        <span class="flex items-center gap-1"><span>🧔</span><span>الأعمام:</span></span>
        <span id="hudUnclesCount" class="font-mono font-bold text-purple-600 dark:text-purple-400">0</span>
      </div>
      <div class="p-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-between">
        <span class="flex items-center gap-1"><span>🌿</span><span>أبناء العم:</span></span>
        <span id="hudCousinsCount" class="font-mono font-bold text-emerald-600 dark:text-emerald-400">0</span>
      </div>
    </div>
    
    <div class="mt-2 p-1.5 rounded-lg bg-orange-500/10 border border-orange-500/30 flex items-center justify-between text-[11px] font-arabic">
      <span class="flex items-center gap-1"><span>👶</span><span>الأبناء والأحفاد المتفرعون:</span></span>
      <span id="hudDescendantsCount" class="font-mono font-bold text-orange-600 dark:text-orange-400">0</span>
    </div>

    <div class="mt-3 flex gap-2">
      <button id="hudOpenDrawerBtn" class="flex-1 py-1.5 rounded-xl bg-gradient-to-r from-amber-600 to-amber-700 hover:from-amber-700 hover:to-amber-800 text-white font-bold text-xs shadow transition-all flex items-center justify-center gap-1.5">
        <span>📋</span>
        <span>سجل الفرد والوثائق</span>
      </button>
      <button onclick="clearNeuralKinship()" class="px-3 py-1.5 rounded-xl border border-slate-300 dark:border-slate-700 text-xs font-semibold hover:bg-slate-100 dark:hover:bg-slate-800 transition-all text-slate-600 dark:text-slate-300">
        إعادة العرض
      </button>
    </div>
  </div>
"""

if 'id="neuralKinshipHUD"' not in html:
    html = html.replace('</body>', hud_html + '\n</body>')

print("Step 1 complete: CSS and HUD injected.")
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

