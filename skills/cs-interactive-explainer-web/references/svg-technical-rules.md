# SVG & Interactivity Technical Rules — Non-Negotiable

These rules exist because of real, repeated failures Bilal hit in earlier attempts (broken Arabic/English text rendering inside SVG, disconnected wires in circuit diagrams, buttons that silently didn't work). Embed all six of these into the master prompt as strict requirements the AI agent must follow, not as suggestions it can weigh against other priorities.

### 1. Never use native SVG `<text>` elements
SVG `<text>` renders bidi (mixed Arabic/English) content incorrectly and mishandles RTL direction. All writing — labels, captions, numbers, anything — must be HTML overlaid on the graphic (positioned `<div>`/`<span>` elements) or placed inside a `<foreignObject>`. No exceptions, even for single characters or numbers.

### 2. One fixed, flippable arrow/direction icon
Don't let the agent redraw an arrow or directional icon freehand each time it's needed. Define one icon (SVG path or icon font) once, and flip its direction with CSS `transform: scaleX(-1)` where a mirrored direction is needed. This guarantees every arrow in the document points the same, correct way relative to the page's RTL direction.

### 3. Fixed coordinate grid for technical diagrams
Diagrams like arrays, trees, linked lists, or circuits must be built from simple primitives (`rect`, `circle`, `line`) placed on a fixed coordinate grid using multiples of 10 (e.g. x/y values like 10, 20, 30…). Every connection or node point must be defined **once** as a named coordinate, and every line/wire that connects to it must reuse that exact coordinate value — never an approximate nearby number. This is the direct fix for the "disconnected wire" bug seen in circuit diagrams.

### 4. Stable, wired-up interactive elements
Every interactive element (button, clickable node, etc.) needs a unique, stable `data-id` attribute. All JavaScript that binds click handlers must wait for `DOMContentLoaded` before running. This is the direct fix for buttons that appeared in the HTML but silently did nothing.

### 5. Mandatory checkpoint after each section
After building each section (not at the very end), the AI agent must explicitly verify, before moving on:
- Bidi correctness (no raw SVG `<text>`, all English terms wrapped and prefixed correctly per the bidi rule)
- Every connection point in that section's diagram(s) actually matches its defined coordinate (no visually disconnected lines)
- Every button/interactive element in that section is actually wired to working JS (not just present in the markup)

If any of these checks fail, fix them before proceeding to the next section — don't defer fixes to a final pass.

### 6. Staged build process
The AI agent must not attempt the entire site in one pass — this caused timeouts/failures on long tasks previously. Required stages:
1. **Skeleton stage**: HTML structure + base CSS (nav, layout shell, color/type system) — no section content yet.
2. **Per-section stage**: build one section at a time — its explanation text, its SVG/interaction, its quiz if applicable — running the checkpoint in rule 5 before moving to the next section.
3. **Final review stage**: pass over the whole assembled file checking cross-section consistency (nav links all work, keyboard navigation works across all sections, replay buttons all reset correctly, overall bidi/RTL correctness).

This staging must be written into the master prompt explicitly as the required build order, not left implicit.
