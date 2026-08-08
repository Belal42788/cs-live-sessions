# Master Prompt: Interactive HTML Explainer — Python Week 2: Operators, Strings, Types, Logic & Conditionals

## Role
Build a single self-contained HTML file for a teacher (Bilal) presenting the **second Python session** — arithmetic, string operations, type conversion, comparisons/booleans, and if/elif/else — to students aged 12–17 who completed Week 1, on a laptop connected to a projector.

## Hard requirements — deliverable format
- ONE `.html` file. All CSS/JS inline. Google Fonts link only external dependency.
- Two logo images provided separately (`bilal-icon.webp`, `bilal-wordmark.webp`). Embed as base64 using the exact `.nav-logo` (36px) / `.footer-logo` (40px) classes, in a rounded `.logo-badge` container (the logo has a solid `#193cff` background baked in).
- Filename: `python-week2-operators-types-conditionals.html`.

## Visual design system — Dark Animated Theme (reuse exactly, non-negotiable)
```css
:root {
  --primary: #193cff; --accent: #00d4aa; --bg: #0a0e27;
  --card: #111638; --card-hover: #1a2050; --text: #fff; --dim: #8892b0;
  --success: #00ff88; --danger: #ff4757; --warn: #ffd700;
}
```
- Animated radial-gradient background (two soft gradients at 30% 50% and 70% 80%, slow 20s ease-in-out loop) + ~30 floating 4px particles (primary, opacity .3, 15s linear, staggered). Purely decorative, `pointer-events: none`.
- Cards: `background: var(--card)`, `border: 1px solid rgba(255,255,255,0.05)`, radius 24px large / 16px small, hover lift `translateY(-5px)` + accent border. Diagram containers get a top gradient bar (3px, `linear-gradient(90deg, var(--primary), var(--accent))`).
- Fixed top nav: `rgba(10,14,39,0.95)` + `backdrop-filter: blur(20px)`, bottom border `rgba(25,60,255,0.3)`, hidden until 100px scroll, pill links. **Nav links scroll horizontally** (`overflow-x:auto`, hidden scrollbars, `flex-shrink:0` links) instead of wrapping.
- Typography: Cairo (400/600/700/900), body `var(--dim)`, headings white 900. Hero title `clamp(36px,8vw,80px)` with gradient-text span. `dir="rtl"` on `<html>`.
- Per-section accent colors cycling through: cyan `#06B6D4`, amber `#F59E0B`, violet `#8B5CF6`, emerald `#10B981`, pink `#EC4899`, red `#EF4444` — applied to that section's number badge (50px circle, accent gradient, `color: var(--bg)`, font-weight 900), top border, card borders. Define as `--s1`…`--s5`.

## Motion — mandatory, the site must feel alive (NOT a static page)
1. **Landing hero (first viewport)**: pill badge, big gradient-text title, one-line subtitle, "start" button scrolling to section 1. Elements enter with staggered fade-up on load (opacity 0→1 + translateY(40px→0), ~0.8s, each delayed ~0.2s). Add 2–3 large soft blurred circles floating gently in the hero background (slow up/down loop ~6s, different delays).
2. **Scroll-triggered reveal on EVERY content piece** — wrap each section header, each concept card, each example box, each recap box, each diagram in its OWN reveal element (`.rv` with `opacity:0; translateY(30px)` → `.visible`). One `IntersectionObserver` (threshold ~0.05) + a `checkVisibility()` scroll fallback. Body text must be broken into small reveal chunks, not one giant block.
3. **Purposeful small loops**: pulsing scale (~2s) on "currently active" elements, glow animation on section badges (3s), blink for a status LED, `stroke-dashoffset` flow on wires where relevant.

## Emoji policy — minimal, activity-only, never in text
- NO emojis in headings, body text, buttons, cards, labels, or quiz text. Site reads like plain professional teaching material.
- Emojis allowed ONLY as image-props inside interactive simulations (e.g. 🍭 the candy division example, 🧩 the concatenation puzzle, 🏗️ the factory, 🚪 the gate). Style them as deliberate animated objects with keyframe classes: `.emoji-pulse`, `.emoji-shake`, `.emoji-walk`, `.emoji-float`, `.emoji-glow` — smooth, lightweight, educational.
- Allowed functional marks only: ✅ ❌ ⚠️ (error box heading) ← → (nav/step buttons) 💡 (in a fix suggestion). Nothing else.

## Teaching philosophy
Projected live by the teacher. Every visual should attract attention immediately, explain the concept visually BEFORE the text, and **show an action instead of describing it** (e.g. 🍭 candies split between friends, 🧩 puzzle pieces snapping together, the if-gate swinging open). Sections feel interactive, colorful, expressive, memorable — without being childish.

## Language rules
- UI microcopy (buttons, nav, e.g. "التالي", "السابق", "جرّب", "إجابة", "اعرض", "ابدأ") — Modern Standard Arabic (فصحى).
- Explanation body text — Egyptian Arabic dialect (مصري), English CS terms preserved in English.
- **Bidi rule (mandatory)**: prepend "الـ" before any English term that starts a line, heading, list item, or table cell; wrap EVERY embedded English term in `<span dir="ltr">` for correct bidi isolation. Never rely on plain-text bidi resolution.
- Body text is a full, self-contained explanation (not slide-style bullets) — a student reading alone should understand the concept.
- No hover/click tooltips for terms.

## Code display pattern — RUNNABLE CODE PLAYGROUND (mandatory, replaces the old "simulated terminal")
Every code example in this lesson is real runnable Python. Do NOT ship a static highlighted snippet and do NOT simulate output. Apply the code-playground pattern from `references/code-playground.md` verbatim:
- Every code panel becomes an **auto-growing editable `<textarea class="py-edit">`** that always shows ALL of its lines — no internal scrollbars, no manual resizing, no "expand the box to see the rest".
- A control bar (`▶ Run` + `↺ إعادة` + hint "✏️ عدّل الكود وشغّله — شوف الناتج أو الأخطاء") and a hidden output terminal (`.term`).
- Output appears ONLY after pressing **▶ Run** — never an always-on live preview beside the code.
- **Friendly error panel** (`.py-err`): error-type badge + Arabic-only plain-language explanation + `المكان: السطر N` + the offending source line. Raw tracebacks are FORBIDDEN; English detail strings are dropped.
- Embed the **Mini-Python interpreter** and the **editor wiring JS** (`wireEditors()` + `friendlyErr` + hint mapping) from `references/code-playground.md` verbatim. The interpreter already supports `print`, `input()`, `int()/float()/str()/bool()/len()/round()/type()`, f-strings, indexing/slicing, string methods, comparison & logical operators, and `if/elif/else` blocks.
- **Inputs feed Run**: fields wired via `data-inputs="id1,id2"` on the `.code-panel` feed the program's `input()` queue; `data-seed` pre-seeds variables from field values. Put labeled input fields in a `.demo-panel` beside the code panel (use the `.activity-grid` two-column layout: demo-panel + code-panel).
- **5 flagship examples** below are genuine playgrounds (editable code + real inputs + Run), not widgets.

## Mandatory SVG / interactivity rules (from the SVG technical rules — non-negotiable)
1. **Never use native SVG `<text>`.** All writing inside/over diagrams must be HTML overlays (`<div>`/`<span>`) or `<foreignObject>`. No exceptions, even for short English labels. Self-check: grep for `<text` — any real match (not "textarea") is a violation; do this per section.
2. **One fixed, flippable arrow icon** defined once; mirror with CSS `transform: scaleX(-1)`.
3. **Fixed coordinate grid** for technical diagrams: primitives on multiples of 10; named coordinates; wires built from a single JS data source (define signal→{x,y} map + component inputs as names, generate wires programmatically), with an assertion loop verifying endpoints resolve.
4. **Stable interactive elements**: unique `data-id` on every button/clickable; all JS binding waits for `DOMContentLoaded`.
5. **Checkpoint after EACH section** (bidi correctness, connected coordinates, buttons actually wired) before moving on — never defer to the end.
6. **Staged build process (required order)**: (1) skeleton — HTML shell + nav + full CSS system, no content; (2) each section individually, running the checkpoint per section; (3) final review pass — nav links, keyboard nav, replay buttons, overall bidi/RTL.
7. **SVG visual quality**: rich saturated colors, gradients, highlights, soft shadows, one top-left light source, no dull/flat shapes, polished premium look, consistent per-section palette.
8. **Flow/journey connectors must be inline SVG arrows** (rounded stroke + arrowhead polygon with gradient fill), never emoji arrows.

## Interaction patterns to reuse (from the design system)
- **Step-by-step reveal (Next/Back)** where a sequence fits (e.g. PEMDAS precedence ladder, the "Standard Workflow" 3 steps of type conversion, the if-gate decision flow). Steps stacked, only current visible (`.step-card.active`), "التالي"/"السابق" buttons + counter (`1 / 3`). Every interactive animation has a **replay button**.
- **Keyboard navigation**: left/right arrows move between sections, for hands-free presenting.
- **Legend/key box** next to any technical diagram.
- **Activity grid layout** where a demo sits beside code:
  ```css
  .activity-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
  .activity-grid .demo-panel { display:flex; flex-direction:column; gap:16px; padding:20px;
    background:rgba(255,255,255,.03); border-radius:16px; border:1px solid rgba(255,255,255,.06); }
  ```
  Mobile (≤860px): single column, demo first (order 1), code second (order 2). Animation-only: `grid-template-columns: 1fr`.

## Quiz behavior
- Hidden by default, revealed by teacher click (`.quiz-reveal-trigger` + `.qz-hidden` body). Immediate green/red feedback + a short sentence explaining WHY a wrong answer is wrong. Skip button always available.
- Quiz options use the flexbox layout with a letter badge: `<button class="q-opt"><span class="optlet">A</span> …</button>` (`.optlet` is a small rounded letter badge — keeps Arabic/English text clean, never mixed into one string).
- The lesson's source ships 5 ready-made MCQs with correct answers — use them EXACTLY as given (embedded below per section), do not invent replacements.

## Common mistakes box
Every section ends with `<div class="error-box">` containing `⚠️ أخطاء شائعة` heading + a bullet list of the specific common mistakes for that section (each given below). Style: `border:1px solid rgba(255,71,87,.2); background:rgba(255,71,87,.05); border-radius:12px; padding:16px;`.

---

## Content

### [Hero] عنوان الأسبوع
Badge: "Python — الأسبوع الثاني". Gradient-text title. Subtitle: "من رقمين بسيطين لبرنامج بياخد قرارات لوحده."

### Section 1 — العمليات الحسابية والتعبيرات (accent: cyan)
**Objective:** الأربعة عمليات الأساسية (`+ - * **`) + التلاتة عمليات القسمة المختلفة: `/` (قسمة عادية، دايمًا بترجع float — `10 / 2` = `5.0`)، `//` (Floor Division، بتقرّب لتحت وتشيل الباقي — `17 // 5` = 3)، `%` (Modulo، بيرجع الباقي بس — `17 % 5` = 2). ثم ترتيب الأولويات PEMDAS: أقواس → أسس → ضرب/قسمة (من الشمال لليمين، بتشمل `* / // %`) → جمع/طرح (من الشمال لليمين). قوة الـ Exponent: `10 ** 6` = مليون في أقل من ميكروثانية.
- **Analogy (use exactly):** 10 حلاوة على 3 أصحاب — `10/3` = 3.33 (فوضى! كل صاحب بياخد جزء مكسور)، `10//3` = 3 حلاوات كاملة لكل واحد، `10%3` = حلاوة واحدة فاضلة في الطبق.
- **Precedence examples (use exactly):** `(10 + 2) * 5` = 60 · `2 + 3 ** 2` = 11 · `10 * 2 // 5` = 4 · `10 - 2 + 5` = 13.
- **Tip (use exactly):** Explicit is Better — `total = (price * quantity) + shipping` أوضح بكتير من `total = price * quantity + shipping`.
- **Flagship playground — Talabat bill splitter (real inputs → Run):** input fields `burger_price` (150), `quantity` (3), `delivery_fee` (45), `voucher` (20) feed the code's `input()` calls via `data-inputs`. The code computes `subtotal = (burger_price * quantity) + delivery_fee`, `final_total = subtotal - voucher`, `each_pays = final_total / 3`, prints `The final total is: 475` and `Each person pays: 158.33333333333334` with the default inputs.
- **Quiz (embed exactly):** ناتج `print(10 + 10 // 3)`؟ → A: 6. B: 13.333333333333334. C: 13 — أقسم الأول (`10//3 = 3`) ثم اجمع (صح). D: 20. (Correct: **C**.)
- **Common mistakes box:** ترتيب الأولويات من غير أقواس بيديك نتيجة غلط · الخلط بين `/` و `//` و `%` · إنك تستنى القسمة العادية ترجع int وهي دايمًا float.

### Section 2 — التعامل مع النصوص: Concatenation و Repetition (accent: amber)
**Objective:** الـ String سلسلة حروف بين علامتي اقتباس (`" "` أو `' '`) — "قاعدة الاقتباسات": من غيرها Python بيفسّر الكلمة كاسم متغير أو أمر. `+` بيلزّق نصوص جنب بعض (Concatenation، من غير ما يضيف مسافة تلقائي). `*` بيكرر النص (Repetition، أسرع طريقة لعمل خطوط فاصلة — `"*" * 20`). Escape Sequences: `\n` (سطر جديد)، `\t` (مسافة Tab واسعة، بتظبط الأعمدة). "Code vs Reality": بتكتب `\n` في الكود لكن المخرج بينطقها كقفزة لسطر جديد.
- **Analogy (use exactly):** الـ Concatenation زي قطع بازل بتتلزق ببعض — الغراء (`+`) رفيع، مش بيضيف مسافة لوحده، لازم تحط `" "` بنفسك.
- **Example (use exactly):** `border = "*" * 20` ثم print حولين `"Welcome, " + first + "!"` → تلاتة أسطر: `********************` / `Welcome, Mazin!` / `********************`.
- **Tab example (use exactly):** `print("Item:\tBurger\nPrice:\t150 EGP")` → سطرين بأعمدة متظبطة.
- **Flagship playground — Event ticket builder (real inputs → Run):** input fields `guest` (Mazin) and `seat` (B-25) feed `input()`; code builds `border = "=" * 30` and `ticket_body = "GUEST NAME:\t" + guest + "\nSEAT NUMBER:\t" + seat`, prints the bordered ticket exactly matching the source format.
- **Common mistake box (use exactly):** فخ الـ Price Tag — `"Price: " + 100` بيعمل TypeError، مينفعش تلزق نص مع رقم من غير تحويل (هنتعلم الحل في الدرس الجاي).
- **Quiz (embed exactly):** إيه وظيفة الرمز `\t`؟ → A: ينقل النص لسطر جديد. B: يضيف مسافة أفقية واسعة (Tab). C: يكرر النص كذا مرة. D: ينهي البرنامج. (Correct: **B**.)
- **Common mistakes box:** نسيان علامات الاقتباس حوالين النص · الخلط بين النص والرقم في `+` · إنك تتوقع `+` يضيف مسافة تلقائي.

### Section 3 — التحويل بين أنواع البيانات (accent: violet)
**Objective:** Type Conversion (Casting) — تغيير "شكل" البيانات لبناء كائن جديد. 3 دوال أساسية: `int()` (يبني رقم صحيح)، `float()` (يبني رقم عشري)، `str()` (يبني نص). السبب الأهم: `input()` بترجع String دايمًا حتى لو المستخدم كتب رقم — ده سر لغز "10 + 20 = 1020". The Standard Workflow بخطواته التلاتة، و type() للمرة بتدعم الـ Debugging. **Truncation vs Up-casting:** `int(9.9)` = 9 (قص للأسفل، مش تقريب!) مقابل `float(10)` = 10.0 (إضافة دقة).
- **Analogy (use exactly):** دوال التحويل زي مصنع (Factory) — بياخد المادة الخام (نص) ويبني منها حاجة جديدة (رقم)، والنسخة القديمة (النص) بتفضل موجودة زي ما هي.
- **The Standard Workflow (3 steps, step-by-step reveal, use exactly):** 01 اجمع الإدخال (`weight = input("Enter weight: ")`) → 02 حوّل الشكل (`weight_num = float(weight)`) → 03 اعمل العمليات الحسابية بأمان (`print(weight_num / 2)`).
- **Truncation example (use exactly):** `raw_score = 98.7`, `clean_score = int(raw_score)` → `Original: 98.7` / `Truncated: 98`.
- **type() example (use exactly):** `a = 10`, `b = "10"` → `print(type(a))` يطبع `<class 'int'>` و `print(type(b))` يطبع `<class 'str'>`.
- **Flagship playground — Type inspector (real input → Run):** a text input feeds `input()`; the code shows `type(data)`, then attempts `int(data)` and `float(data)`. With a numeric value all three print successfully; typing "apple" triggers the friendly `ValueError` panel in Arabic (القيمة مش قابلة للتحويل للنوع المطلوب) — the teacher can demonstrate the crash live.
- **Common mistake box:** `int("apple")` بيعمل ValueError — المصنع مش سحر، محتاج مادة خام شكلها رقم فعلاً.
- **Quiz (embed exactly):** ناتج `print(int(15.9))`؟ → A: 16. B: 15 — القص للأسفل مش تقريب (صح). C: 15.0. D: ValueError. (Correct: **B**.)
- **Common mistakes box:** شغل عمليات حسابية على ناتج `input()` من غير `int()`/`float()` · الخلط بين الـ Truncation والتقريب · إنك تنسى أن القيمة الأصلية بتفضل زي ما هي.

### Section 4 — طرح الأسئلة على البيانات: المقارنات والـ Booleans (accent: emerald)
**Objective:** الـ Boolean له حالتين بس: `True`/`False` (بحرف كبير إجباري — `true` أو `TRUE` غلط). عمليات المقارنة: `== != > < >= <=`. **القاعدة الأخطر:** `=` (Telling — تكليف/تخزين قيمة، فعل بيغيّر الذاكرة) مختلف تمامًا عن `==` (Asking — سؤال بيرجع Boolean). Logical Operators: `and` (البوابة الشرهة، الكل لازم يكون True)، `or` (البوابة السهلة، واحد بس كفاية)، `not` (بيعكس القيمة). المقارنة بين النصوص حساسة لحالة الأحرف.
- **Analogy (use exactly):** بوابة أمان الموبايل — `(fingerprint_ok and passcode_ok)` محتاج الاتنين، قايمة VIP `(is_on_list or has_invite)` أي واحد كفاية.
- **Example (use exactly):** `is_admin = True`, `has_permission = False` → `print("Access Both:", is_admin and has_permission)` = False · `print("Access Either:", is_admin or has_permission)` = True.
- **Note (important, use exactly):** المقارنة بين النصوص حساسة لحالة الأحرف — `"Admin" == "admin"` نتيجتها False.
- **Dangerous bug (use exactly):** لو استخدمت `=` وأنت قاصد `==`، Python هيحسب إنك بتخزن قيمة مش بتسأل — أخطاء منطقية صعبة تلاقيها.
- **Flagship playground — Comparison & logic playground (real inputs → Run):** two number inputs + an operator dropdown (`== != > < >= <=`) generate a comparison line that runs for real; separately, two boolean selects (True/False) + a logical-operator dropdown (`and or not`) generate a logic line that runs for real.
- **Quiz (embed exactly):** نتيجة `(10 == 10) and (5 > 10)`؟ → A: True. B: False — الشرط الأول صح والتاني غلط، و`and` محتاج الاتنين (صح). C: 1. D: SyntaxError. (Correct: **B**.)
- **Common mistakes box:** الخلط بين `=` و `==` · كتابة `true`/`TRUE` بدل `True` · نسيان أن مقارنة النصوص حساسة لحالة الأحرف.

### Section 5 — اتخاذ القرارات: if / elif / else (accent: pink)
**Objective:** الكود عادة بيمشي من فوق لتحت زي قطر على سكة واحدة، لكن الـ Conditionals بتعمل "مفترق طرق". `if` (فحص شرط، لازم نقطتين `:` في الآخر) + Indentation إجبارية (4 مسافات) بتحدد إيه اللي "ملك" الشرط. `elif` (خطة ب، ممكن تتكرر كذا مرة) و`else` (شبكة أمان نهائية لو مفيش شرط اتحقق). **القاعدة: أول شرط True بس هو اللي بيشتغل** — Python بيوقف عند أول شرط True وبيتجاهل الباقي.
- **Analogy (use exactly):** الـ if زي بوابة مقفولة — لو الشرط True البوابة بتفتح، لو False Python بيكمل في الطريق العادي من غير ما يدخل.
- **Indentation demo (use exactly):** `if True:` → `print("I am INSIDE the if.")` (4 مسافات) مقابل `print("I am OUTSIDE the if.")` (0 مسافة) — الطالب يشوف بصريًا الفرق بين اللي "ملك" الشرط واللي مستقل عنه.
- **Flagship playground — Shipping calculator (real input → Run):** order-total input feeds `input()`; the code runs the exact `if/elif/else` from the source: `total >= 500` → "Free Shipping!"، `total >= 300` → "Shipping cost: 20 EGP"، غير كده → "Shipping cost: 50 EGP". Default input 450 → "Shipping cost: 20 EGP".
- **Nesting example (use exactly):** `if age >= 12:` وجواه `if has_id:` (8 مسافات) → "Access Granted!" / "You need an ID card." / "Too young to enter." — استخدم رسمة "سلم" بصرية توضح مستويات الإزاحة (4 مسافات لكل مستوى).
- **First-match rule (use exactly):** Python بيفحص السلسلة من فوق لتحت؛ أول شرط True بيدخل بلوكه وبيخرج من الشجرة كلها — حتى لو شرط تاني وراه True برضه، بيتم تجاهله.
- **Quiz (embed exactly):** إيه وظيفة الإزاحة (Indentation) في جملة الـ if؟ → A: شكل جميل بس اختياري. B: بتحدد الكود اللي بينتمي للجملة (صح). C: بتخلي البرنامج أسرع. D: بتقلب الكود تعليق. (Correct: **B**.)
- **Common mistakes box:** نسيان النقطتين `:` بعد الشرط · إزاحة مش متساوية (3 مسافات هنا و4 هناك) → IndentationError · توقع أن `elif` تانية هتتفحص حتى لو شرط قبلها True.

### [Closing] من الحساب للقرار
Visual: step recap connecting the whole week with SVG arrows: عمليات حسابية → نصوص → تحويل الأنواع → مقارنات ومنطق → قرارات بـ if/elif/else. Closing line: "دلوقتي برنامجك مش بس بيحسب وبيتكلم — بقى يقدر ياخد قرارات لوحده." Footer carries the wordmark logo + a short encouraging Egyptian-Arabic sentence.

---

## Build order (mandatory, from the SVG technical rules)
1. **Skeleton stage**: HTML structure + base CSS (nav, layout shell, color/type system, hero) — no section content yet.
2. **Per-section stage**: build one section at a time (explanation + SVG/interaction + code playground + quiz if any), running the per-section checkpoint (bidi, connected coordinates, wired buttons, playground Run works) before moving on.
3. **Final review stage**: full-file pass — all nav links work, keyboard navigation works across all sections, every replay button resets correctly, every code playground's ▶ Run produces real output and the friendly error panel works on bad input, overall RTL/bidi correctness, `<text` self-check, logo classes match CSS exactly.

Pay special attention to the code playgrounds — these need the Mini-Python interpreter embedded verbatim and genuinely working Run output, not simulated output. And to the motion rules — a static build is a failed build.
