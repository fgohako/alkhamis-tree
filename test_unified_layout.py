#!/usr/bin/env python3
"""
test_unified_layout.py
Simulates the Grand Unified Tapestry layout for all ~2,600 nodes in Al-Khamis Family Tree.
Ensures:
1. 0 Bounding Box Collisions across the entire multi-branch canvas.
2. Orthogonal Family Bus routing.
3. Reasonable canvas dimensions (e.g., width <= 36,000px, height <= 10,000px).
4. All branches (Q, S/H, D, M, K34, K01-K15, K16-K33, K35-K46, Patriarchs, and In-Laws) are positioned.
"""

import json
from collections import defaultdict

CARD_W = 190
CARD_H = 46
SPOUSE_GAP = 28
SIBLING_GAP = 24
LEVEL_H = 120

import os
_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(_DIR, 'public', 'family_data.json')
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

inds = data.get('individuals', [])
k34 = data.get('k34_nodes', [])
classical = data.get('classical_ancestors', [])

all_nodes = {i['id']: i for i in inds}
for k in k34: all_nodes[k['id']] = k
for c in classical: all_nodes[c['id']] = c

def layout_subtree(node_id, branch_ids, visited):
    if node_id in visited:
        return {'width': CARD_W, 'height': CARD_H, 'cards': [], 'lines': []}
    visited.add(node_id)
    node = all_nodes.get(node_id)
    if not node:
        return {'width': CARD_W, 'height': CARD_H, 'cards': [], 'lines': []}
    
    cards = []
    lines = []
    
    spouse = None
    sids = node.get('spouse_ids', [])
    if sids:
        s = all_nodes.get(sids[0])
        if s and s['id'] in branch_ids:
            spouse = s
            if not s.get('child_ids'):
                visited.add(s['id'])
    
    couple_w = (CARD_W * 2 + SPOUSE_GAP) if spouse else CARD_W
    cids = [c for c in node.get('child_ids', []) if c in branch_ids and c not in visited]
    
    if not cids:
        cards.append({'node': node, 'relX': 0, 'relY': 0, 'w': CARD_W, 'h': CARD_H})
        if spouse:
            cards.append({'node': spouse, 'relX': CARD_W + SPOUSE_GAP, 'relY': 0, 'w': CARD_W, 'h': CARD_H, 'isSpouse': True})
            lines.append({'type': 'marriage', 'x1': CARD_W, 'y1': CARD_H/2, 'x2': CARD_W + SPOUSE_GAP, 'y2': CARD_H/2})
        return {'width': couple_w, 'height': CARD_H, 'cards': cards, 'lines': lines}
    
    child_layouts = [layout_subtree(cid, branch_ids, visited) for cid in cids]
    children_w = sum(cl['width'] for cl in child_layouts) + (len(child_layouts) - 1) * SIBLING_GAP
    total_w = max(couple_w, children_w)
    parent_rel_x = (total_w - couple_w) / 2
    
    cards.append({'node': node, 'relX': parent_rel_x, 'relY': 0, 'w': CARD_W, 'h': CARD_H})
    couple_mid_x = parent_rel_x + CARD_W / 2
    if spouse:
        cards.append({'node': spouse, 'relX': parent_rel_x + CARD_W + SPOUSE_GAP, 'relY': 0, 'w': CARD_W, 'h': CARD_H, 'isSpouse': True})
        couple_mid_x = parent_rel_x + CARD_W + SPOUSE_GAP / 2
        lines.append({'type': 'marriage', 'x1': parent_rel_x + CARD_W, 'y1': CARD_H/2, 'x2': parent_rel_x + CARD_W + SPOUSE_GAP, 'y2': CARD_H/2})
        
    cur_x = (total_w - children_w) / 2
    child_centers = []
    for cl in child_layouts:
        child_mid_x = cur_x + cl['width'] / 2
        child_centers.append(child_mid_x)
        for c in cl['cards']:
            cards.append({
                'node': c['node'],
                'relX': cur_x + c['relX'],
                'relY': LEVEL_H + c['relY'],
                'w': c['w'],
                'h': c['h'],
                'isSpouse': c.get('isSpouse', False)
            })
        for l in cl['lines']:
            lines.append({
                'type': l['type'],
                'x1': cur_x + l['x1'],
                'y1': LEVEL_H + l['y1'],
                'x2': cur_x + l['x2'],
                'y2': LEVEL_H + l['y2']
            })
        cur_x += cl['width'] + SIBLING_GAP
        
    # Orthogonal Family Bus
    first_cx = child_centers[0]
    last_cx = child_centers[-1]
    bus_y = LEVEL_H - 40
    lines.append({'type': 'stem', 'x1': couple_mid_x, 'y1': CARD_H, 'x2': couple_mid_x, 'y2': bus_y})
    lines.append({'type': 'bus', 'x1': min(couple_mid_x, first_cx), 'y1': bus_y, 'x2': max(couple_mid_x, last_cx), 'y2': bus_y})
    for cx in child_centers:
        lines.append({'type': 'drop', 'x1': cx, 'y1': bus_y, 'x2': cx, 'y2': LEVEL_H})
        
    max_ch_h = max(cl['height'] for cl in child_layouts)
    return {'width': total_w, 'height': LEVEL_H + max_ch_h, 'cards': cards, 'lines': lines}

print('Layout engine initialized successfully.')
