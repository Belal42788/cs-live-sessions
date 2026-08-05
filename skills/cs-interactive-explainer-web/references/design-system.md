# Design System — CS Interactive Explainer

Embed all of this into the master prompt as strict requirements, not suggestions.

## Audience & purpose
Students aged 12–17. The site is built **for the teacher (Bilal) to present from**, standing in front of a class with a laptop + projector. It is NOT a student self-study tool. One single experience — do not build a student/teacher mode toggle. Quiz answers and any "detail" content are hidden by default and revealed on click by the teacher during the lesson.

## Layout & platform
- Single self-contained HTML file: all CSS, JS, SVG, and the logo (base64) live inside the one file. No external files, no CDN dependencies for anything critical (Google Fonts link is fine).
- Desktop-first (laptop screen size and up). Mobile is not a priority — don't spend effort on a mobile layout, but don't break outright either.
- Sticky top navigation bar listing all section titles, clickable to jump directly to a section. Not a sidebar.
- Structure: intro section ("هنتعلم ايه النهارده" — what we'll learn today) → one block per confirmed section → closing summary section.
- Section-internal layout (text vs. SVG placement — side by side or stacked) is left to the AI agent's judgment per section, whichever fits that section's content best.

## Color & type — Dark Animated Theme
This is a **dark theme** with animated backgrounds. Do NOT use light/white backgrounds.

### CSS Variables (mandatory)
```css
:root {
  --primary: #193cff;
  --accent: #00d4aa;
  --bg: #0a0e27;
  --card: #111638;
  --card-hover: #1a2050;
  --text: #fff;
  --dim: #8892b0;
  --success: #00ff88;
  --danger: #ff4757;
  --warn: #ffd700;
}
```

### Per-section accent colors
Each section gets its own accent color from this palette, used on that section's number badge, top border, and icon:
- Cyan `#06B6D4`, Amber `#F59E0B`, Violet `#8B5CF6`, Emerald `#10B981`, Pink `#EC4899`, Red `#EF4444`, Blue `#193cff`

### Background
- Body background: `var(--bg)` (`#0a0e27` — dark navy).
- Animated radial gradient overlay: two soft radial gradients (primary at 30% 50%, accent at 70% 80%) with a slow 20s ease-in-out loop that gently shifts position. applied via `position: fixed` behind everything.
- Floating particles: 30 small dots (`4px`, `var(--primary)`, `opacity: 0.3`) floating upward on a 15s linear loop, staggered delays. Purely decorative, `pointer-events: none`.

### Cards & containers
- `background: var(--card)` (`#111638`)
- `border: 1px solid rgba(255,255,255,0.05)`
- `border-radius: 24px` on large containers, `16px` on smaller cards.
- Hover: `background: var(--card-hover)` + `translateY(-5px)` + `border-color: rgba(25,60,255,0.3)`.
- Diagram containers get a top gradient bar: `height: 3px; background: linear-gradient(90deg, var(--primary), var(--accent))`.

### Navigation
- Fixed top bar, `background: rgba(10,14,39,0.95)` with `backdrop-filter: blur(20px)`.
- `border-bottom: 1px solid rgba(25,60,255,0.3)`.
- Starts hidden (`translateY(-100%)`), appears after scrolling 100px.
- Nav links: pill-shaped (`border-radius: 25px`), `color: var(--dim)`, hover/active: `color: var(--text); background: rgba(25,60,255,0.2); border-color: var(--primary)`.

### Typography
- Arabic font: Cairo (from Google Fonts), weights 400/600/700/900.
- Body text: `color: var(--dim)` (`#8892b0`).
- Headings: `color: var(--text)`, `font-weight: 900`.
- Hero title: `clamp(36px, 8vw, 80px)` with gradient text span (`linear-gradient(135deg, var(--primary), var(--accent))`).

## Motion — mandatory, this is the part earlier attempts got too static
The site must feel alive, not like a static printed page. Two concrete mechanisms, both required:

**1. Landing hero section (first viewport, before any lesson content)**
A full first-screen hero: small pill badge, big title with the key term highlighted via a gradient-text span, a one-line subtitle, and a "start" button that scrolls down to the first section. Every hero element enters with a staggered fade-up on page load (opacity 0→1 + translateY(40px→0), ~0.8s ease-out, each element delayed ~0.2s after the previous — badge, then title, then subtitle, then button). Add 2–3 large soft blurred circles floating gently in the hero background (slow up/down loop, ~6s, different delays per circle) purely for visual life — low opacity, decorative only, never on top of text.

**2. Scroll-triggered reveal on every content block — not just once per section**
Wrap *each individual piece* of content (section header, each concept card, each example box, each recap box, each diagram) in its own reveal element — not one reveal wrapper around a whole giant section. This is what makes content feel like it's being "read line by line with you" instead of dumped as one wall of text.
- Base state: `opacity: 0; transform: translateY(30px);` with `transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1)`
- Revealed state (class `visible` added by JS): `opacity: 1; transform: translateY(0)`
- Trigger mechanism: a single `IntersectionObserver` (threshold ~0.05) observing all `.section-inner` elements; when an element intersects, add its `visible` class. Also a fallback `checkVisibility()` on scroll for elements already in view.
- Keep body text broken into these small revealing chunks (a short paragraph, then a diagram, then the next short paragraph) rather than one long paragraph followed by one diagram.

**3. Small looping decorative animations, used purposefully (not everywhere)**
- Wires/current flow in circuit-style diagrams: animate `stroke-dashoffset` on a dashed stroke (`stroke-dasharray`) to suggest current flowing along a wire — great fit for circuit/gate diagrams.
- A pulsing scale (`transform: scale(1) → scale(1.05) → scale(1)`, ~2s loop) on an element to indicate "this is currently active/on".
- A glow animation on section number badges: `box-shadow: 0 0 20px rgba(25,60,255,0.3) → 0 0 40px rgba(25,60,255,0.6)`, 3s infinite loop.
- A blink (opacity 1↔0.25 loop) for something like a status LED.
- Use these for things that are genuinely "live" or "on" in a diagram — not as generic decoration everywhere.
- Corner radius: soft/rounded on large elements — cards, buttons, containers, section frames. Sharper/more geometric only inside technical diagram details.
- Illustration style: clean geometric primitives (rect/line/arrow) for technical content, with glow effects (`filter: drop-shadow`) on active elements.

## Language rules
- Page-level: `dir="rtl"` on `<html>`.
- UI microcopy (buttons, nav labels, e.g. "التالي", "جرّب", "إجابة") — Modern Standard Arabic (فصحى).
- Explanation body text — Egyptian Arabic dialect (مصري), with English CS terms preserved in English, not translated/transliterated.
- Body text per section is a full, detailed, self-contained explanation (not slide-style minimal bullets) — a student reading it alone should be able to understand the concept, even though it's primarily used by the teacher narrating live.
- **Bidi rule (mandatory)**: prepend "الـ" before any English term that starts a line, a heading, a list item, or a table cell.
- Wrap every embedded English term in a `<span dir="ltr">` for correct bidi isolation. Do not rely on plain text bidi resolution.
- No hover/click tooltips for technical terms — the body explanation must be sufficient on its own.

## Interaction
- Two trigger types combine: elements animate/reveal as they scroll into view, AND clicking reveals further detail (used by the teacher live).
- Interaction complexity target: medium — small step-by-step simulations per concept, not single toggle-only effects and not full multi-screen simulations.
- Every section's interactive animation has a **replay button** to reset it back to the start (needed when teaching the same lesson to multiple classes in one day).
- **Keyboard navigation**: left/right arrow keys move between steps/sections, for hands-free presenting.
- Legend/key box next to any technical diagram (array, tree, circuit, etc.) explaining what each color/shape represents.

## Quiz (optional per section — decided during the Q&A, not by default)
- Number of questions per section depends on that section's complexity — can be more than one if warranted.
- Immediate feedback on selection: color (green/red) plus a short sentence explaining *why* a wrong answer is wrong.
- A skip button is always available.

## Code snippets
- When the lesson includes code examples, render them with syntax highlighting (e.g. highlight.js via CDN, or an inline minimal highlighter — agent's choice as long as it doesn't break the single-file requirement if CDN is unavailable offline; prefer bundling a minimal highlighter inline over a hard CDN dependency).
- **Code panels MUST be LTR**: the whole page is `dir="rtl"`, so code panels inherit RTL and look broken. Every code panel wrapper must have `dir="ltr"`, and the CSS must include:
  ```css
  .code-panel, .code-panel .code-body, .code-panel .code-header {
    direction: ltr;
    text-align: left;
    unicode-bidi: isolate;
  }
  ```

## Activity grid layout
- Used when a section has a simulation/demo alongside code or explanation. CSS:
  ```css
  .activity-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
  }
  .activity-grid .demo-panel {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 20px;
    background: rgba(255,255,255,.03);
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,.06);
  }
  ```
- On mobile (`max-width: 860px`), stack to single column: demo-panel first (order: 1), code-panel second (order: 2).
- When there's no code panel (animation only), use `grid-template-columns: 1fr` instead.

## Section accent color variables
- For multi-section sites, define per-section colors as CSS variables: `--s1` through `--s5` (or more if needed).
- Use these on section number badges, top borders, card borders, and tab buttons.
- Example: `--s1: #06B6D4; --s2: #F59E0B; --s3: #8B5CF6; --s4: #10B981; --s5: #EC4899;`

## Section number badges
- Each section header gets a numbered badge: `<div class="section-number">01</div>`.
- Styled with `width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 18px; color: var(--bg);` and a gradient background using that section's accent color.

## Tabbed sections
- When a section has multiple sub-topics (e.g. cashier + AI + data analysis under one chapter), use a tab bar.
- Tab bar: horizontal row of pill-shaped buttons, active tab gets the section's accent color.
- Only one `.tab-panel` visible at a time, toggled by JS.

## Interactive simulation patterns

### Cart with product selection (cashier pattern)
- Product grid: clickable buttons with emoji + name + price, "إضافة" badge.
- Cart display: items with qty controls (+ / -), remove button (🗑️), subtotal, discount row (hidden until triggered), final total.
- Discount logic: auto-apply when subtotal > threshold (e.g. 10% off over 500 EGP).
- Reset button: clears cart, hides totals, hides receipt.
- Print receipt button: generates a monospace receipt card (dashed border, `direction: ltr`) showing items as `Name Price × Qty`, original total, discount (if any), final total, "Thank you!".

### Teachable Machine simulator
- Training view: 3 class cards side by side, each with a grid of ~8 emoji thumbnails and a label.
- "Train Model" button → progress bar animation → switches to test view after completion.
- Test view: test image + name on left, probability bars (horizontal, per class) on right that animate filling in.
- Results table: 3 rows (Image | Prediction | Confidence), one deliberately wrong prediction included.

### Parking simulation
- LED bulbs: 4 colored bulbs (green, red, yellow, blue) with `.bulb` base class and `.on-green` / `.on-red` etc. for lit state.
- Counter display: large number showing current count.
- Entry/Exit buttons: trigger LED blink animation (yellow for entry, blue for exit) via setTimeout.
- IO diagram: 3 boxes (Inputs → Processing → Outputs) that light up in sequence on each action.

### Step-by-step reveal (Next/Back)
- Steps stacked vertically, only the current step is visible (`.step-card.active`).
- "التالي" / "السابق" buttons with a step counter (`1 / 4`).
- JS: `stepIdx` tracks current, buttons call `stepDir(+1)` or `stepDir(-1)`.

### Bar chart with reveal
- Bars built dynamically from data array, height proportional to max value.
- Initially dimmed (opacity 0.7), values hidden.
- "اكشف التحليل" button reveals all bars, highlights max (green) and min (red), shows conclusion text.
- "إعادة" button resets to initial state.

## Common mistakes box
- Every section ends with an error box: `<div class="error-box">`.
- Contains `⚠️ أخطاء شائعة` heading + bullet list of common student mistakes.
- Styled with `border: 1px solid rgba(255,71,87,.2); background: rgba(255,71,87,.05); border-radius: 12px; padding: 16px;`.

## Branding
- Logo files are provided in `assets/` (`bilal-icon.webp` = icon-only mark, `bilal-wordmark.webp` = full "Bilal" wordmark). Convert to base64 and embed as `<img>` — do not attempt to redraw the logo as SVG.
- The logo files have a solid `#193cff` background baked into the image (not transparent). Display them inside a small rounded container/badge sized to fit the logo closely, rather than placing the raw square directly on the page background — this reads as intentional rather than a stray colored box.
- Header and footer both carry the brand: header can use the icon or wordmark; footer must include the logo plus a short, simple encouraging sentence for students (in Egyptian Arabic).
- Standard logo markup and sizing (use these exact classes and values so the logo is identical across every site):
  - Header: `<img class="nav-logo" src="data:image/webp;base64,...">` with CSS `.nav-logo { width: 36px; height: 36px; border-radius: 10px; object-fit: contain; }`
  - Footer: `<img class="footer-logo" src="data:image/webp;base64,...">` with CSS `.footer-logo { height: 40px; border-radius: 8px; }`
  - The HTML `class` MUST match the CSS class exactly (`.nav-logo`, NOT `.logo-nav`). If a mismatched class is used, the browser renders the image at its full natural size (huge). After embedding the logo, verify the `<img>` has a matching CSS rule with an explicit size.

## Misc
- If given content is very long (spans more than one lesson), the site should still be built as one file covering the full scope — this is a warning-only case, not a refusal case, and is handled upstream in the Q&A (Bilal is warned before generation, not by the site build itself).
- HTML filename: auto-generate an English slug from the lesson title (lowercase, hyphen-separated, no spaces) — e.g. "loops-and-iteration.html".
