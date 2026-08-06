# Master Prompt: Interactive HTML Explainer — Session 2: Lists, Links, Media, Tables & Forms

## Role
Build a single self-contained HTML file for a teacher (Bilal) presenting the second web development session — Lists, Links, Buttons, Images, Video, Tables, and Forms — to students aged 12–17 who completed Session 1 (How the Web Works + basic text tags), on a laptop connected to a projector.

## Hard requirements — deliverable format
- ONE `.html` file. All CSS/JS inline. Google Fonts link only external dependency.
- Two logo images provided separately (`bilal-icon.webp`, `bilal-wordmark.webp`, solid `#193cff` background baked in). Convert to base64, embed as `<img>` inside a small rounded badge, using the exact classes `.nav-logo` (36px) and `.footer-logo` (40px) from the design system — verify the CSS rule exists and matches, or the logo renders huge.
- Filename: `session2-lists-media-tables-forms.html`.

## Visual design system — Dark Animated Theme (reuse exactly)
```css
:root {
  --primary: #193cff; --accent: #00d4aa; --bg: #0a0e27;
  --card: #111638; --card-hover: #1a2050; --text: #fff; --dim: #8892b0;
  --success: #00ff88; --danger: #ff4757; --warn: #ffd700;
}
```
Animated radial-gradient background + ~30 floating particles. Cards rounded (24px/16px), hover lift + glow border, top gradient bar. Fixed nav hidden until scroll, blurred pill-nav, lists all section titles, clickable jump. Font Cairo. Section number badges. Per-section accent variables cycling: cyan `#06B6D4`, amber `#F59E0B`, violet `#8B5CF6`, emerald `#10B981`, pink `#EC4899`, red `#EF4444`, repeat. Every section ends with a `⚠️ أخطاء شائعة` box. Emoji policy: keep emojis out of the written content entirely — no emojis in headings, paragraphs, buttons, card text, status messages, or quiz text (reads like plain professional teaching material). Use emojis ONLY inside interactive activity/simulation elements as image-like visual props (e.g. 🚶 a person walking, 🖱️ a cursor clicking a button, 🖼️ an image being dropped into a site), styled with the CSS keyframe classes `.emoji-pulse` / `.emoji-shake` / `.emoji-walk` / `.emoji-float` / `.emoji-glow` so they read as deliberate visual objects, never as floating decoration. Keep the small functional-feedback set: ✅ correct, ❌ wrong, ⚠️ warning/error box, directional arrows (← →) on step buttons, 💡 hint in a fix suggestion, 🔒 status in the login activity. SVG illustrations that ARE used must be vibrant/gradient/premium per the standard SVG quality rule — never flat or dull. Granular scroll-reveal per block via one `IntersectionObserver` (threshold 0.05), `translateY(30px)→0`, `visible` class.

## Live Code Preview pattern — mandatory, and always show the FULL document
Every code example in this lesson must show the **complete HTML document** (`<!DOCTYPE html>` through `</html>`, including `<head>`), never a body-only fragment. Pair every code panel (`dir="ltr"`, monospace, tag/attribute/string color-tinted via `<span>`) with a live `<iframe>` (`srcdoc` set from the panel content via JS) that renders it for real.

## Language rules
`dir="rtl"` for the page shell and Arabic text. UI in فصحى, explanations in Egyptian Arabic, simple and encouraging (students are still early beginners). Code, tag names, and attribute names stay in English `dir="ltr"`. "الـ" prefix rule for English terms starting a line/heading/list/table cell.

## Mandatory SVG / interactivity rules
No native SVG `<text>` (self-check via grep before finishing each section — this includes checking for "textarea" false positives). Any diagram with 4+ connections built from a JS data lookup, never hand-typed coordinates. Stable `data-id` + `DOMContentLoaded` binding. Checkpoint after each section. Staged build: skeleton → each section → final review.

## Quiz behavior
Hidden by default, revealed by click. Immediate color feedback (green/red) + short explanation. Skip button always available.

---

## Content

### [Hero] عنوان الجلسة
Badge: "الجلسة الثانية: عناصر الويب". Gradient-text title. Subtitle: "من نص بسيط لصفحة فيها قوائم، صور، جداول، وفورم بيشتغل فعليًا."

### [Intro] العب مع الـ Attributes (accent: cyan)
**الشرح النظري (embedded in the intro cards):** في الجلسة دي هنبدأ نشرح عناصر زي القوائم والصور والجداول والفورم. لكن قبل ما نبدأ، لازم نفهم الـ Attributes — هي "إعدادات" بتتكتب جوه الوسم نفسه وبتغيّر سلوكه أو شكله. في نوعين من الـ attributes: **واحدة ليها خيارات محددة** (زي `type` بتاعة الـ `<ul>`: `disc` أو `circle` أو `square` — بتختار شكل النقطة)، و**واحدة نص حر** (زي `href` بتاعة الـ `<a>`: بتكتب أي عنوان تحب تروح له). النوع الأول بنعرضه كـ Dropdown والنوع التاني كخانة كتابة. وكل مثال في الجلسة هنعرضه كـ صفحة HTML كاملة (`<!DOCTYPE html>` لحد `</html>` مع الـ `<head>`) — عشان الطالب يعتاد الشكل الحقيقي لأي صفحة ويب.

**This is the dedicated opening playground, built exactly as discussed:**
- A live code panel + iframe preview, starting with a simple `<ul>` list.
- A **dropdown control** for `type` with options `disc / circle / square` — changing it live-updates the `<ul type="...">` attribute in the code panel and the rendered list style in the iframe.
- A second live example: an `<a>` tag. A **dropdown control** for `target` (`_self / _blank`), AND a **text input control** for `href` (free text, e.g. student can type any URL) — both update the same live code panel + iframe.
- A short explanatory line establishing the pattern for the whole lesson: "بعض الـ attributes ليها اختيارات محددة (زي type) فهتلاقيها Dropdown، وبعضها نص حر (زي href) فهتلاقيها خانة تكتب فيها."
- **Quiz:** none — this is a hands-on warm-up.

### Section 1 — القوائم: مرتبة، غير مرتبة، ومتداخلة (accent: amber)
Based on UL/OL/Nested List. **Objective:** `<ul>` لقائمة غير مرتبة (بنقط، `type="disc|circle|square"`)، `<ol>` لقائمة مرتبة بالأرقام، والقوائم ممكن تتداخل جوه بعضها (List جوه List).
- **الشرح النظري (embedded as explanation text):** القوائم من أكتر الحاجات استخدامًا في أي صفحة ويب — كل مينو (Navigation Menu) بتلاقيه على أي موقع هو في الأصل `<ul>`. الـ `<ul>` بنستخدمه لما الترتيب مش مهم (مكونات أكلة، مزايا منتج، روابط مينو) والمتصفح بيحط نقطة • قدام كل عنصر. الـ `<ol>` بنستخدمه لما الترتيب مهم جدًا (خطوات تثبيت، وصفة طبخ، ترتيب المنافسة) والمتصفح بيرقّم لوحده 1, 2, 3 — لو زودت عنصر أو شلت عنصر، الترقيم بيتظبط لوحده، عمرك ما بتكتب الأرقام بإيدك. كل عنصر جوه أي قائمة لازم يكون داخل `<li>` (List Item) — الـ `<li>` ممكن يحط جواه نص، أو لينك، أو صورة، أو حتى قائمة تانية كاملة. والقوائم المتداخلة (List جوه List) بنكتب قائمة جديدة **جوه الـ `<li>`** نفسه — المتصفح بيرجّعها لليمين وبيغيّر شكل النقطة من • لنقطة مجوّفة ○، فتبان كأنها "قسم جوه قسم". كمان: القوائم بتتحكي للسكرين ريدر (Screen Reader) كمجموعة مترابطة ("list, 5 items") — فالاستخدام الصحيح ليها بيخلي الصفحة متاحة أكتر (Accessible).
- **Live examples exactly from source:**
  - `unordered-list.html` — قائمة باللغات: HTML / CSS / JavaScript (ثبت إن تبديل الترتيب مش بيغيّر المعنى → `<ul>`).
  - `ordered-list.html` — خطوات: Open your code editor → Create a new file called index.html → Write your HTML structure → Save and open in the browser (لازم الترتيب → `<ol>`).
  - `nested-list.html` — متداخلة: Frontend (تحتها HTML/CSS/JavaScript) + Backend (تحتها Node.js/Express) — قائمة جوه الـ `<li>`.
- **Common mistake (embed exactly):** كتابة نص جوه `<ul>`/`<ol>` مباشرة من غير `<li>` — غلط. لازم كل عنصر يتلف في `<li>`. (اعرض قبل/بعد: النص من غير `<li>` بيتلصق في سطر واحد من غير نقط من غير أي هيكل.)
- **Quiz (1 question):** أي Tag يستخدم لقائمة بالأرقام، `<ul>` ولا `<ol>`؟

### Section 2 — الروابط والأزرار (accent: violet)
Based on `<a>` tag + `<button>`. **Objective:** `<a href="...">` للانتقال بين صفحات أو مواقع (`target="_blank"` يفتح تاب جديد)، وممكن كمان تنتقل لجزء معين في نفس الصفحة باستخدام `href="#id"`. `<button>` بينفذ Action (زي إرسال فورم)، وله `type="submit|button|reset"`.
- **الشرح النظري (embedded as explanation text):** بدون اللينك، كل صفحة ويب هتكون "جزيرة" منعزلة — اللينك هو اللي بيربط كل حاجة ببعضها. الـ `<a>` بيعمل اللينك، وأهم attribute فيه هو `href`. في تلات أنواع روابط: (1) **رابط تنقّل بين صفحات نفس الموقع** بيستخدم Relative Path (زي `about.html` أو `pages/contact.html`) — مسار نسبي محسوب من مكان الملف الحالي، و`../` معناها "اطلع فولدر ورا". (2) **رابط خارجي لموقع تاني** بيبدأ دايماً بـ `https://` (Absolute Path)، وبنضيف `target="_blank"` عشان يفتح في تاب جديد، ومعاه `rel="noopener noreferrer"` للأمان. (3) **رابط قفزة جوه نفس الصفحة** (`href="#id"`) بياخدك لجزء معين من الصفحة، و`id` لازم يطابق الـ href بالظبط. ولما نحط `<img>` أو `<button>` جوه `<a>`, بيبقوا روابط قابلة للنقر. **الفرق بين `<a>` و`<button>`:** الـ `<a>` للتنقل، والـ `<button>` لإجراء Action على نفس الصفحة (إرسال فورم). لو عايز زرار شكل جميل بينقّل، اتفّف الـ `<button>` جوه `<a>`. أنواع الـ `<button>`: `submit` (بيسجّل الفورم)، `reset` (بيرجّع القيم الافتراضية)، `button` (معندوش فعل على الفاضي — للـ JavaScript). تنبيه: أي `<button>` جوه `<form>` من غير `type` بيتحول لـ `submit` من نفسه — حدد `type` دايمًا.
- **Live examples (exactly from source):**
  - **رابط خارجي بـ `target="_blank"`:** `https://github.com` مع `rel="noopener noreferrer"` — لاحظ إن الصفحة بتفتح في تاب جديد والأصل فاضل فاتح. (لو حذفت `https://`, المتصفح بيدور على ملف محلي اسمه `www.google.com` ويديك 404.)
  - **المسارات النسبية:** من جوّه `pages/about.html`، الرابط `index.html` غلط (بيطّلع فولدر `pages` ويقلب 404) والصح `../index.html`.
  - **رابط قفزة جوه الصفحة:** صفحة تجريبية فيها قسمين بـ `id` (زي `#skills` و `#hi`) وروابط بيقفزوا بينهم فعلًا — الـ `id` لازم يطابق الـ `href` بالظبط (حروف صغيرة و hyphens).
  - **Wrap non-text:** صورة جوه `<a>` (كليبل للـ home) + `<button>` جوه `<a>`.
- **Interaction:** أزرار الـ `<button>` بأنواعها التلاتة (submit/button/reset) جوه فورم بسيط تجريبي، الطالب يشوف الفرق العملي بينهم.
- **Quiz (1 question):** لو عايز الرابط يفتح في تاب جديد، تستخدم إيه؟

### Section 3 — الصور والفيديو (accent: emerald)
Based on `<img>` + `<video>` + Mini Example. **Objective:** `<img src="" alt="" width="" height="">` لعرض الصور — الـ `alt` مهم جدًا للـ accessibility (وبيظهر بدل الصورة لو ما اتحملتش)، ويفضل تغيير `width` بس وسيب `height` يتحسب لوحده عشان الصورة ما تتشوهش. `<video controls autoplay muted loop>` لتشغيل الفيديو — `autoplay` غالبًا مش هيشتغل غير مع `muted`.
- **الشرح النظري (embedded as explanation text):** الويب تنصمّ طبيعته عن الصور والفيديو. الـ `<img>` هو Void Element (ما لهوش وسم قفل) وبياخد الصورة من `src`، والـ `alt` إجباري — بيتحكا بسكرين ريدر، وبيظهر بدل الصورة لو ما اتحملتش، وبيفيد الـ SEO. لو الصورة "ديكور" بس، اكتب `alt=""` فارغة (عشان السكرين ريدر يتجاهلها) — لكن متسيبها من غير `alt` خالص. مقياس: حدد `width` بس وسيب `height` يتحسب لوحده عشان يحافظ على Aspect Ratio — لو حددت الاتنين بنسب مختلفة الصورة بتتسوّه. الـ `<video>` (عكس `<img>`) له وسم فتح وقفل، وبدون `controls` بيبقى صندوق أسود مش قادر تتحكم فيه؛ `autoplay` مش بيشتغل غير مع `muted`؛ وبتقدر تحط `poster` كصورة قبل التشغيل. العناصر دي بتشتغل مع بعض في صفحات حية (Hero، معرض منتجات، زر Call-to-Action جنب صورة).
- **Common mistake (embed exactly, with a visible before/after):** تحديد `width` و`height` مختلفين بيشوه الصورة؛ الأفضل تحديد `width` بس.
- **Interaction — reuse this section's Mini Example as a combined live playground (FocusFlow landing from source):** صفحة حية فيها: زرّين بادئين (`Start Free Trial` و`Watch Demo ▶` اللي بينقّل لـ `#demo-video`) + صورة Hero بصيغة حقيقية (استخدم `https://picsum.photos/...` زي ما السورس نفسه فاعل في الـ Activity) مع `alt` حقيقي + فيديو بـ `controls width="720"` و`poster` — كل ده في صفحة واحدة حية. (الفيديو هيظهر fallback text عن عدم الدعم — ده طبيعي لأن الـ src بيبقى مسار نسبي مش موجود.)
- **Quiz (1 question):** ليه مهم نحط `alt` للصورة؟

### Section 4 — الجداول: الأساسيات (accent: pink)
Based on `<table>`/`<tr>`/`<th>`/`<td>` + Mini Project "Students Marks". **Objective:** الجدول بيتكون من `<table>` (الجدول كله)، `<tr>` (صف)، `<th>` (عنوان عمود، بيبقى Bold تلقائي)، `<td>` (بيانات الخلية).
- **الشرح النظري (embedded as explanation text):** في بيانات بطبيعتها "ثنائية الأبعاد" — ليها صفوف وأعمدة والعلاقة بينهم ليها معنى (جدول حصص، درجات طلبة، مقارنة أسعار). الـ `<table>` هو الحاوية الكاملة، جواه بنحط صفوف `<tr>`، وجوه كل صف خلايا `<td>`. رؤوس الأعمدة بنكتبها بـ `<th>` — مش `<td>` — لأن `<th>` بيعطي معنى سيمانتي للسكرين ريدر وبيبقى Bold من نفسه. كل الصفوف لازم يكون فيها نفس عدد الخلايا، وإلا الجدول باين مكسور. وللوصولية، نقدر نضيف `scope="col"` أو `scope="row"` للـ `<th>`. ملحوظة تاريخية: في التسعينيات الناس كانوا بيستخدموا الجداول لبناء صفحات كاملة (Layout) — دلوقتي ده غلط تمامًا؛ الجداول للبيانات، والتخطيط بـ CSS.
- **Live example (exactly from source):** `table-headers.html` — جدول Student Name / Math / Science / Average، صف واحد: Ahmed → 85 / 90 / 87.5 (رؤوس بـ `<th scope="col">` واسم الطالب بـ `<th scope="row">`).
- **[Mini Project] جدول درجات الطلبة (Students Marks — from source complete-table):** جدول حقيقي (Name / Math / Science / English) بالبيانات الأصلية من السورس: Ahmed → 88/92/79، Sara → 95/87/93، Omar → 72/80/85، والطالب يقدر يضيف صف جديد بنفسه من خلال حقول نص + زرار "ضيف طالب" تحدّث الجدول الحي.
- **Common mistake (embed exactly):** حط `<td>` مباشرة جوه `<table>` من غير `<tr>` — غلط، لازم يتلف جوه `<tr>` الأول.
- **Quiz:** none (the mini project is the reinforcement).

### Section 5 — الجدول الكامل: thead، tbody، tfoot (accent: red)
Based on "Complete Table". **Objective:** الشكل الاحترافي للجدول: `<thead>` (رؤوس الأعمدة)، `<tbody>` (البيانات الأساسية)، `<tfoot>` (إجماليات أو ملاحظات، غالبًا بـ `colspan` عشان يمتد عبر كل الأعمدة).
- **الشرح النظري (embedded as explanation text):** الجدول الاحترافي بيتقسم لتلات أجزاء سيمانتيين: `<thead>` فيه صف الرؤوس (اللي بنكتبه بـ `<th>`)، و`<tbody>` فيه صفوف البيانات، و`<tfoot>` في الآخر فيه صف الإجماليات أو الملاحظات (ممكن نستخدم `colspan` عشان يمدد على كل الأعمدة). القسمة دي بتخلي المتصفح والسكرين ريدر يقرؤوا الجدول صح، وبيسهل تنسيق كل جزء لوحده بـ CSS. كمان نقدر نحط `<caption>` كعنوان للجدول (بيبان فوقه وبيتقري للسكرين ريدر).
- **Live example (exactly from source — complete-table.html):** الجدول الكامل "Student Grades — Term 1": `<thead>` فيه Name / Math / Science / English، و`<tbody>` فيه Ahmed → 88/92/79 و Sara → 95/87/93 و Omar → 72/80/85، و`<tfoot>` فيه صف "Class Average" → 85 / 86.3 / 85.7. (في السورس التفوّت مش بستخدم `colspan` — اتبع السورس؛ ولو عملته بعرض مختلف أوضح إن `colspan` بيخلّي الملاحظة تمدد عبر الأعمدة.)
- **Interaction:** toggle بيورّي/يخبي كل جزء (thead/tbody/tfoot) لوحده بألوان مختلفة عشان الطالب يميز الحدود بينهم بصريًا.
- **Quiz:** none.

### Section 6 — الفورمات ومدخلات المستخدم (accent: cyan)
Based on `<form>` + `<input type="...">` + label/id + name + placeholder. **Objective:** `<form>` حاوية بتجمع عناصر الإدخال مع بعض. `<input>` أنواعه المهمة: `text, password, email, number, date, radio, checkbox`. `<label for="id">` بيوصف الـ input ولازم `for` يساوي `id` بتاعه (عشان الضغط على الـ label يحدد الـ input تلقائي — مهم للـ accessibility). `name` هو الاسم اللي بيتبعت للـ backend (مش بيظهر للمستخدم). `placeholder` مجرد رسالة مساعدة، مش بتتبعت.
- **الشرح النظري (embedded as explanation text):** الفورم هو الوسيلة الأساسية اللي المستخدم بيتواصل بيها مع الموقع. الـ `<form>` حاوية ليها `action` (فين تتبعت البيانات — نستخدم `#` كمساحة لسه مفيش server) و`method` (`GET` بيضيف البيانات في الـ URL — مناسب للبحث؛ `POST` بيبعت البيانات في جسم الطلب — مناسب للباسوورد). الـ `<input>` هو العنصر الأكثر تنوعًا — وسم وحيد (void) بيتغير شكله وسلوكه كليًا حسب `type`: `text`, `email` (بتتحقق من صيغة الإيميل), `password` (الحروف مختفية), `number`, `date` (تقويم), `checkbox`, `radio`, `file`. **الـ `<label>` إجباري:** اربط `for` بتاع الـ label بـ `id` بتاع الـ input بالظبط — الضغط على نص الـ label بيفعّل (focus) الـ input تلقائيًا، والسكرين ريدر بيقرا الـ label. **`name` هو المفتاح اللي بيتبعت للـ server** (من غيره البيانات مش بتتبعت أصلاً)، و**`placeholder` مجرد نص مساعد بيفضى أول ما تكتب** (مش بديل عن الـ label). `required` يخلي المتصفح يمنع الإرسال لو الحقل فاضي. النصوص الطويلة بـ `<textarea>`، والقوائم بـ `<select>`+`<option>`، والتجميع بـ `<fieldset>`+`<legend>` — وكل أزرار الـ radio في مجموعة واحدة لازم تشترك في نفس `name` عشان تبقى "اختر واحد بس".
- **Live example — reuse the Intro's guided-control pattern here too:** `<input>` مع **Dropdown لـ type** (text/password/email/number/date/radio/checkbox) يورّي إزاي شكل الـ input بيتغير فعليًا لكل نوع، بجانب **حقول نص لـ placeholder وname** الطالب يجربهم بنفسه.
- **label + id demo:** زوج `<label for="username">` و`<input id="username">` حي، الطالب يدوس على الكلام (label) ويشوف الـ input بيتفعل (focus) تلقائي — يوضح أهمية الربط.
- **Common mistake (embed exactly):** نسيان ربط `label` بالـ `id` بتاع الـ input بالضغط عليه، مش بيحصل حاجة.
- **Quiz (1 question):** إيه الفرق بين `name` و`placeholder`؟

### [Activity] فورم تسجيل دخول كامل (accent: amber, dashed activity-card style)
Based on "Complete Login Form" — `login-form.html` from source, verbatim: `<form action="/login" method="POST">` with Email field (`label for="email"`, `input type="email" id="email" name="email" placeholder="you@example.com" required`), Password field (`label for="password"`, `input type="password" id="password" name="password" required`), a "Remember me on this device" checkbox (`label` wrapping `input type="checkbox" name="remember" value="1"`), and a `button type="submit"` "Log In". Present it as a fully live, working playground — students can type in it and see the values (not actually submitted anywhere, just demonstrating real interactive form behavior). A single "اعرض الكود كامل" button reveals the full annotated source.

---

### [Closing] كل التاجات اللي اتعلمناها النهارده
Visual: an icon grid recapping every tag from this session (`<ul>`, `<ol>`, `<a>`, `<button>`, `<img>`, `<video>`, `<table>`, `<form>`, `<input>`, `<label>`), each with its one-line purpose. Closing line: "دلوقتي عندك كل الأدوات الأساسية لصفحة ويب حقيقية — قوائم، روابط، وسائط، جداول، وفورم شغال."

---
Build in the staged order above. Run the mandatory checkpoint after every section before moving to the next one.
