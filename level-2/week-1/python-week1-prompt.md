# Master Prompt: Interactive HTML Explainer — Python Week 1: Intro to Programming + Python Basics

## Role
Build a single self-contained HTML file for a teacher (Bilal) presenting the **first Python programming session** — what programming is, setting up the environment, why Python, syntax, input/output, and basic data types — to students aged 12–17 who have never coded before, on a laptop connected to a projector. Students are complete beginners; keep the tone simple, warm, and encouraging.

## Deliverable format — hard requirements
- ONE `.html` file. All CSS, JS, SVG, and logos inline (base64). Only external dependency allowed: Google Fonts link (Cairo).
- Embed the two logos as base64 `<img>` with the EXACT classes and sizes below (do not redraw as SVG):
  - Header: `<img class="nav-logo" src="data:image/webp;base64,...">` → CSS `.nav-logo { width: 36px; height: 36px; border-radius: 10px; object-fit: contain; }`
  - Footer: `<img class="footer-logo" src="data:image/webp;base64,...">` → CSS `.footer-logo { height: 40px; border-radius: 8px; }`
  - The logo images have a solid `#193cff` background baked in; display them inside a small rounded container/badge sized to fit the logo closely.
- Footer also carries a short encouraging Egyptian-Arabic sentence for students.
- Filename (auto slug from the lesson title): `python-week1-intro-to-programming.html`.

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
- Fixed top nav: `rgba(10,14,39,0.95)` + `backdrop-filter: blur(20px)`, bottom border `rgba(25,60,255,0.3)`, hidden until 100px scroll, pill links.
- Typography: Cairo (400/600/700/900), body `var(--dim)`, headings white 900. Hero title `clamp(36px,8vw,80px)` with gradient-text span. `dir="rtl"` on `<html>`.
- Per-section accent colors cycling through: cyan `#06B6D4`, amber `#F59E0B`, violet `#8B5CF6`, emerald `#10B981`, pink `#EC4899`, red `#EF4444` — applied to that section's number badge (50px circle, accent gradient, `color: var(--bg)`, font-weight 900), top border, card borders, tab buttons. Define as `--s1`…`--s7`.

## Motion — mandatory, the site must feel alive (NOT a static page)
1. **Landing hero (first viewport)**: pill badge, big gradient-text title, one-line subtitle, "start" button scrolling to section 1. Elements enter with staggered fade-up on load (opacity 0→1 + translateY(40px→0), ~0.8s, each delayed ~0.2s). Add 2–3 large soft blurred circles floating gently in the hero background (slow up/down loop ~6s, different delays).
2. **Scroll-triggered reveal on EVERY content piece** — wrap each section header, each concept card, each example box, each recap box, each diagram in its OWN reveal element (`.section-inner` with `opacity:0; translateY(30px)` → `.visible`). One `IntersectionObserver` (threshold ~0.05) + a `checkVisibility()` scroll fallback. Body text must be broken into small reveal chunks, not one giant block.
3. **Purposeful small loops**: pulsing scale (~2s) on "currently active" elements, glow animation on section badges (3s), blink for a status LED, `stroke-dashoffset` flow on wires where relevant.

## Emoji policy — minimal, activity-only, never in text
- NO emojis in headings, body text, buttons, cards, labels, or quiz text. Site reads like plain professional teaching material.
- Emojis allowed ONLY as image-props inside interactive simulations (e.g. 🍞 the bread in the robot-chef steps, ⌨️ typing, ☁️ Colab, 💻 Jupyter). Style them as deliberate animated objects with keyframe classes: `.emoji-pulse`, `.emoji-shake`, `.emoji-walk`, `.emoji-float`, `.emoji-glow` — smooth, lightweight, educational.
- Allowed functional marks only: ✅ ❌ ⚠️ (error box heading) ← → (nav/step buttons) 💡 (in a fix suggestion). Nothing else.

## Teaching philosophy
Projected live by the teacher. Every visual should attract attention immediately, explain the concept visually BEFORE the text, and **show an action instead of describing it** (e.g. 🍞 steps assembling the sandwich, ⌨️ typing into the notebook, the "Run" button firing). Sections feel interactive, colorful, expressive, memorable — without being childish.

## Language rules
- UI microcopy (buttons, nav, e.g. "التالي", "السابق", "جرّب", "إجابة", "اعرض", "ابدأ") — Modern Standard Arabic (فصحى).
- Explanation body text — Egyptian Arabic dialect (مصري), English CS terms preserved in English.
- **Bidi rule (mandatory)**: prepend "الـ" before any English term that starts a line, heading, list item, or table cell; wrap EVERY embedded English term in `<span dir="ltr">` for correct bidi isolation. Never rely on plain-text bidi resolution.
- Body text is a full, self-contained explanation (not slide-style bullets) — a student reading alone should understand the concept.
- No hover/click tooltips for terms.

## Code display pattern (Python — NOT a live iframe)
Python code cannot be genuinely rendered in a browser like HTML/CSS, so use a **simulated terminal**:
- Code panel `dir="ltr"`, monospace, with the mandatory CSS:
  ```css
  .code-panel, .code-panel .code-body, .code-panel .code-header {
    direction: ltr; text-align: left; unicode-bidi: isolate;
  }
  ```
- Escape the code first, then tint keywords/strings/comments with `<span>` classes (minimal inline highlighter — no hard CDN dependency; a tiny built-in highlighter is preferred over external JS).
- A terminal-style output panel (dark, monospace, output text in `--accent`) with a "▶ Run" button. On click, the EXACT expected output from the source appears via a short line-by-line typewriter/fade-in animation — clearly labeled as a simulated run.
- **Exception — build these 3 GENUINELY interactive** (real JS computation, not canned animation): the **Personal Greeter**, **Simple Calculator**, and **Grade Checker** (Section 5). Real input fields matching each program's `input()` calls, computing actual output in JS with the exact source logic (grade thresholds: ≥90 → A ⭐, ≥75 → B 👍, ≥60 → C 🟡, else → F 😢).

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
- **Step-by-step reveal (Next/Back)** for the Robot Chef (4 steps), the Colab guide (6 steps), and the Python timeline: steps stacked, only current visible (`.step-card.active`), "التالي"/"السابق" buttons + counter (`1 / 4`). Every interactive animation has a **replay button**.
- **Keyboard navigation**: left/right arrows move between steps/sections, for hands-free presenting.
- **Legend/key box** next to any technical diagram.
- **Activity grid layout** where a demo sits beside code/explanation:
  ```css
  .activity-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
  .activity-grid .demo-panel { display:flex; flex-direction:column; gap:16px; padding:20px;
    background:rgba(255,255,255,.03); border-radius:16px; border:1px solid rgba(255,255,255,.06); }
  ```
  Mobile (≤860px): single column, demo first (order 1), code second (order 2). Animation-only: `grid-template-columns: 1fr`.

## Quiz behavior
- Hidden by default, revealed by teacher click. Immediate green/red feedback + a short sentence explaining WHY a wrong answer is wrong. Skip button always available. Replay/reset available.
- The lesson's source already ships 4 ready-made MCQs with correct answers — use them EXACTLY as given (embedded below per section), do not invent replacements.

## Common mistakes box
Every section ends with `<div class="error-box">` containing `⚠️ أخطاء شائعة` heading + a bullet list of the specific common mistakes for that section (each given below). Style: `border:1px solid rgba(255,71,87,.2); background:rgba(255,71,87,.05); border-radius:12px; padding:16px;`.

---

## Content

### [Hero] عنوان الأسبوع
Badge: "Python — أول خطوة". Gradient-text title. Subtitle: "من مجرد فكرة في دماغك، لحد تعليمات الكمبيوتر بينفذها بالظبط زي ما إنت عايز."

### [Intro] إيه هي البرمجة؟ (accent: cyan)
**Objective:** Programming = إديت الكمبيوتر تعليمات خطوة بخطوة. Programmer = الشخص اللي بيكتب التعليمات. Program = مجموعة التعليمات النهائية اللي الكمبيوتر بينفذها. Code = اللغة الخاصة اللي بنكتب بيها التعليمات. الكمبيوتر بيفهم الكهرباء بس (تشغيل/إطفاء = Binary 0/1) — عشان كده لغات زي Python بتبقى جسر بين الإنسان والآلة.
- **Analogy (use exactly):** الكمبيوتر زي طالب سريع جدًا وبيمشي بالتعليمات بالظبط، بس مفيهوش خيال — لو ما قلتلوش كل خطوة، مش هيعرف يعمل حاجة.
- **Block-based vs Text-based (use exactly):** Block-Based (زي Scratch — سحب وإفلات، ألوان، بيمنع أخطاء النحو عشان تركز على المنطق) مقابل Text-Based (زي Python — أسطر كود حقيقية بكلمات ورموز، اللي بيستخدمه مهندسو الـ AI كل يوم).
- **Glossary terms (use exactly):** Algorithm (خطة أو وصفة خطوة بخطوة لحل مشكلة — بتعملها قبل ما تكتب الكود)، Syntax (قواعد اللغة النحوية — زي علامات الترقيم في الجملة)، Logic (جزء التفكير — بيحدد ترتيب الخطوات وبيحسم قرارات الكمبيوتر).
- **Central interaction — the Robot Chef Analogy, 4-step reveal (reuse step-by-step pattern):** "اعمل ساندوتش" لوحدها مش كفاية — الروبوت مش هيعمل حاجة لأن التعليمات عامة جدًا. الخطوات بالظبط: **01** هات شريحة عيش (كل خطوة لازم تكون دقيقة وواضحة) → **02** افتح برطمان الزبدة (الكمبيوتر معندوش حس سليم — محتاج كل تفصيلة) → **03** افرد الزبدة على العيش (الدقة هي كل حاجة) → **04** حط شريحة العيش التانية (تقسيم المهمة الكبيرة لخطوات صغيرة = البرمجة). Each step with its 🍞 icon prop.
- **Quiz (embed the source's exact question):** إيه هو الـ Algorithm؟ → A: لغة برمجة زي Python. B: خطة أو وصفة خطوة بخطوة لحل مشكلة. C: الـ 0s والـ 1s اللي الكمبيوتر بيفهمها. D: نوع من أجهزة الكمبيوتر. (Correct: **B**.)
- **Common mistakes box:** الفرق بين الـ Algorithm ولغة البرمجة · إنك تقول "اعمل كده" من غير تفاصيل وتتوقع الكمبيوتر يفهمك · إنك تحسب إن الكمبيوتر عنده "حس سليم".

### Section 1 — تجهيز بيئة العمل: Google Colab و Jupyter (accent: amber)
**Objective:** عشان نكتب Python محتاجين مكان نكتب فيه الكود ونشغله. في خيارين: **Google Colab** (في المتصفح بس — مفيش تثبيت، بيشتغل على أي جهاز، وبيحفظ في Google Drive تلقائيًا) و**Jupyter محلي** (تثبيت على جهازك — شغل Offline ومشاريع متقدمة).
- **Recommendation (use exactly):** ابدأ بـ Colab — هو الأنسب للمبتدئين. تقدر تنقل لـ Jupyter المحلي في أي وقت بعدين لو احتجت قوة أكبر.
- **Interaction — step-by-step reveal for the Colab guide (6 steps exactly):** 01 افتح المتصفح وروح لـ colab.research.google.com → 02 سجل دخول بحساب جوجل → 03 دوس "New Notebook" → 04 غيّر الاسم → 05 اكتب أول كود في أول خلية → 06 دوس Shift+Enter وشوف الناتج تحت.
- **Live-feel first run (simulated terminal):** خلية كود `print("Hello, Python!")` مع زرار "▶ Run" — أول تشغيل كود للطالب، الناتج يظهر بنمط الـ terminal.
- **Note (brief, secondary):** Jupyter المحلي موجود لو حابب تشتغل Offline — تفاصيله التقنية (متطلبات النظام، خطوات التثبيت) في مرجع إضافي لمين عايز يجرب على جهازه.
- **Common mistakes box:** تثبيت Jupyter وتجهيزات معقدة قبل ما تجرب Colab الأول · قلق من "التثبيت" وهو مش محتاج فعلًا للمبتدئ · إنك تنسى تحفظ شغلك في Jupyter المحلي.

### Section 2 — إيه هي لغة Python وليه هي الأفضل؟ (accent: violet)
**Objective:** Python لغة برمجة **عالية المستوى** (High-level — مصممة للبشر، بتستخدم كلمات إنجليزية زي print و if و input)، **عامة الغرض** (General-purpose — مواقع وألعاب وأدوات بيانات وذكاء اصطناعي)، و**مُفسَّرة** (Interpreted — بتشتغل سطر بسطر فورًا، تكتب وتشغل وتشوف). ابتكرها Guido van Rossum سنة 1989.
- **Guido's goal (use exactly):** "عايز لغة تكون ممتعة في الاستخدام وسهلة في القراءة."
- **Timeline (step reveal, use exactly):** 1989 جويدو بدأ يكتبها في إجازة الكريسماس → 1991 إصدار Python 1.0 → 2008 إصدار Python 3.0 → النهارده هي اللغة #1 في الـ AI وعلم البيانات والتعليم.
- **3 reasons Python wins (use exactly):** (1) **بتتقرأ زي لغة البشر** — مثال `print("Hello, World!")` حتى لو مبرمجتش قبل كده تقدّر تخمن بيقول إيه. (2) **مكتبات جاهزة = صندوق عُدّة ضخم** — بدل ما تبني المحرك من الحديد والمسامير، بتركّبه جاهز (NumPy للعمليات الحسابية السريعة، Pandas لتنظيم وتحليل الجداول، Matplotlib للرسوم البيانية، Scikit-learn للـ machine learning، TensorFlow للشبكات العصبية، OpenCV لتعليم الكمبيوتر يشوف). (3) **مش هتكون لوحدك أبدًا** — لو علقت، حد سأل سؤالك قبل كده، وفيه آلاف الشروح المجانية ومجتمع ضخم.
- **Real-world grid (use exactly):** Spotify (تحليل ذوقك الموسيقي) · Instagram (معالجة صورك) · Netflix (تحديد التوصيات) · Google (البحث وأنظمة الـ AI) · Tesla (معالجة بيانات الحساسات للقيادة الذاتية).
- **Comparison table (use exactly):** Python vs Java vs C++ (سهولة التعلم: سهلة جدًا / متوسطة / صعبة؛ بتتقرأ زي الإنجليزي: أيوة / نوعًا ما / لأ؛ الأفضل للـ AI والبيانات: المعيار الصناعي / نادر / نادر؛ السرعة: متوسطة / سريعة / سريعة جدًا).
- **Glossary terms (use exactly):** Syntax (قواعد كتابة الكود) · Interpreter (الأداة اللي بتقرأ وتشغّل كود Python سطر بسطر) · Open Source (مجاني 100% وأي حد يقدر يحسنه) · Library (كود جاهز بيعطي برنامجك قدرات) · Variable (صندوق باسم بيخزن قيمة) · Bug (خطأ في الكود بيسبب سلوك غير متوقع) · Debugging (إيجاد الأخطاء وإصلاحها) · Script (ملف Python فيه تعليماتك) · IDE (التطبيق اللي بتكتب وتشغّل فيه) · Algorithm (خطة خطوة بخطوة لحل مشكلة).
- **Common mistakes box:** الظن إن "Python بطيئة فهي سيئة" — التكلفة مقبولة مقابل سهولتها وقوتها في الـ AI والبيانات · الخلط بين الـ interpreter والـ compiler (الاتنين بيترجموا الكود العالي للغة الآلة، بس بطريقة مختلفة) · الظن إن اللغات المحترمة هي الصعبة فقط.

### Section 3 — قواعد كتابة الكود (Syntax) (accent: emerald)
**Objective:** كل سطر في Python تعليمة واحدة اسمها **statement**، وPython بيقرا الكود من فوق لتحت سطر بسطر. **كل statement في سطر لوحده — مفيش semicolons زي Java أو C++.** الكومنتات اللي بتبدأ بـ `#` Python بيتجاهلها تمامًا — هي ملاحظات للقارئ بس.
- **Simulated terminal examples (use exactly):**
  1. Three prints in a row: `print("Hello!")` / `print("I am learning Python.")` / `print("This is fun!")` → output shows each on its own line.
  2. Line continuation with `\`: `num = 1 + 2 + 3 + \` … `7 + 8 + 9 + 10` → `print(num)` → 55.
  3. Multiple statements on one line with semicolons: `b = 201; a = 101; c = 301` then print a/b/c → 101 201 301.
  4. The `print()` basics: `print("My name is Alex")  # prints text` / `print(100)` / `print(10 + 5)` → My name is Alex 100 15.
  5. Comments: `# This line prints a welcome message` / `print("Welcome to Python!")  # comment at end` — emphasize Python ignores `#` and anything after it.
- **Key rules (use exactly):** النصوص لازم تكون جوه علامات اقتباس `" "` أو `' '` — الأرقام لأ. الكومنت بيديك شرح لنفسك/غيرك — عادة حلوة تكتبها دايمًا.
- **Common mistakes box:** كتابة semicolons زي Java/C++ · توقع إن الكومنت هيطلع في الناتج · نسيان علامات الاقتباس حوالين النص (الأرقام بس من غير اقتباس).

### Section 4 — الحوار بين المستخدم والبرنامج: print() و input() (accent: pink)
**Objective:** كل برنامج في العالم بيعمل حاجتين: بياخد معلومات وبيرجع معلومات. في Python دول الاتنين في دالتين: **`print()`** (البرنامج بيتكلم معك — بيظهر الرسايل والنتايج على الشاشة) و**`input()`** (إنت بتتكلم مع البرنامج — بيكتب ويستني إنت تكتب وتدوس Enter). **القاعدة الأهم: أي حاجة بتدخل من `input()` بتتخزن كـ String دايمًا حتى لو كتبت رقم — مش تقدر تعمل عليها عمليات حسابية قبل ما تحولها بـ `int()` أو `float()`.**
- **3 ways to format output (use exactly):** (1) Concatenation بـ `+` (`"Welcome, " + name + "!"`) (2) Comma separation — الأسهل، من غير تحويل (`print("Name:", name, "Age:", age)`) (3) **f-Strings** ⭐ — المعيار الاحترافي الحديث: `f` قبل الاقتباس و `{ }` لدمج المتغيرات (`print(f"Student {name} is {age} years old and scored {score}.")`).
- **Special print() options (use exactly):** `sep` بيغيّر الفاصل بين القيم (`print("Python","is","awesome",sep="-")`) و`end` بيحدد إيه يحصل بعد الطباعة بدل السطر الجديد (`print("Loading", end="...")` + `print("Done!")` → Loading...Done!).
- **The 3 flagship LIVE programs (build with REAL JS computation per the code display pattern):**
  1. **Personal Greeter** — inputs: name, city → real output `Hello, {name}! Great to meet someone from {city}.`
  2. **Simple Calculator** — inputs: two numbers → real output `{num1} + {num2} = {result}`.
  3. **Grade Checker** — inputs: student name, score (0–100) → real output using the exact if/elif thresholds: `score >= 90 → "A ⭐"`, `>= 75 → "B 👍"`, `>= 60 → "C 🟡"`, else `"F 😢"`. Show the if/elif chain in the code panel beside the live form.
- **Quiz (embed the source's exact question):** المستخدم كتب عمره (16) في `input()`. Python بيخزنها إزاي؟ → A: int — Python بيكشف إنه رقم. B: float — ممكن يكون decimal. C: str — لأن `input()` دايمًا بترجع string. D: bool — قيمة صح/غلط. (Correct: **C**.)
- **Common mistakes box:** إجراء عمليات حسابية على ناتج `input()` من غير `int()`/`float()` · خلط نص ورقم بـ `+` · نسيان أن كل مدخلات المستخدم نصوص (حتى الأرقام).

### Section 5 — أنواع البيانات الأساسية: int, float, str, bool (accent: red)
**Objective:** 4 حاويات بتخزن فيها المعلومات: **int** (أرقام صحيحة — إيجابي/سلبي/صفر من غير نقطة عشرية)، **float** (أرقام فيها نقطة عشرية — للدقة)، **str** (أي تسلسل حروف في علامات اقتباس — نص)، **bool** (قيمتين بس True/False — محرك كل قرار). **Python ديناميكية الأنواع** — بيحدد النوع لوحده من القيمة، من غير ما تعلن عنه يدويًا.
- **Analogy (use exactly):** حاويات المطبخ — كل نوع بيانات له الحاوية المناسبة. مش هتحط شوربة في كيس ورقي، ولا تحمل مية في مصفاية — كل نوع له "العبوة" الصح.
- **int live demo (use exactly):** `a = 20; b = 6` → `+` (26) `-` (14) `*` (120) `//` floor division (3) `%` modulo (2) `**` exponent (64000000). **Key difference:** `print(10 / 2)` → `5.0` (float — دايمًا!) مقابل `print(10 // 2)` → `5` (int — floor division).
- **float live demo (use exactly):** scientific notation `1.5e8` = 150,000,000 (بعد الشمس!) و`2.5e-4`؛ دمج int + float بيرجع float دايمًا (`5 + 2.0` → `7.0`)؛ `round(pi, 2)` / `round(pi, 4)`. Real-world floats: الأسعار (9.99 EGP)، إحداثيات GPS، درجات دقة الـ ML.
- **str live demo (use exactly):** concatenation (`"Data" + " " + "Science"` → Data Science)، repetition (`"-" * 20`)، `len("Alexandria")` → 10، **indexing يبدأ من 0** (`name[0]` → P، `name[-1]` → n)، **slicing** `[start:end]` والـ end غير مضموّن (`name[0:3]` → Pyt، `name[2:]` → thon). **Interactive methods table**: `.upper() .lower() .strip() .replace() .split() .count()` — student types any text and applies each method live.
- **bool live demo (use exactly):** مقارنات (`10 > 5` True، `3 == 7` False، `"a" == "b"` False)؛ عمليات `and` (الاثنين) `or` (واحد على الأقل) `not` (عكس)؛ `if` بيتحكم بكل قرار (`score >= 60` → passed). **تنبيه مهم (استخدم بالظبط):** `True` و `False` لازم يتكتبوا بحرف كبير بالظبط — `true` أو `TRUE` خطأ. Python حساسة لحالة الأحرف. Truthy/Falsy table: `0` / `""` / `None` → False؛ أي رقم غير صفر أو أي نص مش فاضي → True.
- **Combined program (use exactly):** Student Profile — name (str)، age (int)، gpa (float)، is_honor_roll (bool) + شرط المنحة `if is_honor_roll and gpa >= 3.5` → "Congratulations … you qualify for the scholarship!".
- **Type conversion (use exactly):** `int("15")` → 15، `float("3.14")` → 3.14، `str(100)` → "100"، `bool(0)` → False. Real use: `age = int(input(...))` ثم `age + 5`.
- **Common mistakes table (use exactly):** `"10" + 5` → لازم `int("10") + 5` · `true` بدل `True` (حساسية الحروف) · `10 / 2` تتوقع 5 بس الناتج `5.0` → استخدم `10 // 2` · `print(name + age)` بيمنع خلط str و int → `print(name + str(age))`.
- **Quiz (embed the source's exact 2 questions):**
  1. ناتج `print(17 % 5)`؟ → A: 1. B: 2 — الباقي (17 ÷ 5 = 3 والباقي 2). C: 17.5. D: 85. (Correct: **B**.)
  2. ناتج `print("5" * 3)`؟ → A: 15 — ضرب 5 في 3. B: "555" — تكرار النص! C: Error — مينفعش تضرب string. D: "5 5 5" بمسافات. (Correct: **B**.)

### [Closing] ملخص الأسبوع الأول
Use the source's own summary card structure: 4 mini-cards recapping the data types — **int** (أرقام صحيحة بس، من غير نقطة عشرية، عملياته `+ - * // % **`، مثال `age = 16`) · **float** (عليه نقطة عشرية، خلطه مع int بيدي float، `round()` بيضبط الدقة، مثال `gpa = 3.75`) · **str** (نص في اقتباسات، indexing يبدأ من 0، methods زي `.upper()`، وكل ما ييجي من `input()` بتبقى str) · **bool** (True/False بس، بحرف كبير، بيقوّي كل if).
Closing line (use exactly): "من فكرة الروبوت اللي محتاج تعليمات دقيقة، لحد أول برنامج بتاعك بيتكلم مع المستخدم — دلوقتي بقى عندك الأساس اللي أي مبرمج Python بدأ بيه." Every expert was once a beginner — الفرق الوحيد بينك وبين المحترف هو الوقت والممارسة.

---

## Build order (mandatory, from the SVG technical rules)
1. **Skeleton stage**: HTML structure + base CSS (nav, layout shell, color/type system, hero) — no section content yet.
2. **Per-section stage**: build one section at a time (explanation + SVG/interaction + quiz if any), running the per-section checkpoint (bidi, connected coordinates, wired buttons) before moving on.
3. **Final review stage**: full-file pass — all nav links work, keyboard navigation works across all sections, every replay button resets correctly, overall RTL/bidi correctness, `<text` self-check, logo classes match CSS exactly.

Pay special attention to Section 4 — the 3 example programs need genuinely working JS computation, not simulated output. And to the motion rules — a static build is a failed build.
