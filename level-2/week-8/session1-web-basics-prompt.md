# Master Prompt: Interactive HTML Explainer — Session 1: How the Web Works + Your First HTML Tags

## Role
Build a single self-contained HTML file for a teacher (Bilal) presenting the **very first web development session** to students aged 12–17 who have never touched web development before. This session covers two theory topics (What is the Web, What is a Website Made Of) and a hands-on practical part (first HTML tags), on a laptop connected to a projector.

## Hard requirements — deliverable format
- ONE `.html` file. All CSS/JS inline. Google Fonts link only external dependency.
- Two logo images provided separately (`bilal-icon.webp`, `bilal-wordmark.webp`, solid `#193cff` background baked in). Convert to base64, embed as `<img>` inside a small rounded badge.
- Filename: `session1-how-the-web-works.html`.

## Visual design system — Dark Animated Theme (reuse exactly)
```css
:root {
  --primary: #193cff; --accent: #00d4aa; --bg: #0a0e27;
  --card: #111638; --card-hover: #1a2050; --text: #fff; --dim: #8892b0;
  --success: #00ff88; --danger: #ff4757; --warn: #ffd700;
}
```
Animated radial-gradient background + ~30 floating particles. Cards rounded (24px/16px), hover lift + glow border, top gradient bar. Fixed nav hidden until scroll, blurred pill-nav, lists all section titles, clickable jump. Font Cairo. Section number badges. Per-section accent variables cycling: cyan `#06B6D4`, amber `#F59E0B`, violet `#8B5CF6`, emerald `#10B981`, pink `#EC4899`, red `#EF4444`, repeat. Code panels forced `dir="ltr"` + `unicode-bidi: isolate`. Every section ends with a `⚠️ أخطاء شائعة` box. Granular scroll-reveal per block via one `IntersectionObserver` (threshold 0.05), `translateY(30px)→0`, `visible` class. Keyboard arrow-nav. Footer: both logos + encouraging line.

## NEW interaction pattern for this lesson — Live Code Preview
This is a first-time pattern for this project (previous lessons used SVG diagrams; this one is web development, so the most powerful "interaction" is the real thing: actual rendered HTML/CSS in the browser). Use this pattern anywhere the content shows code + "Browser Output":
- A code panel (`dir="ltr"`, monospace, syntax-tinted by keyword vs string vs tag using simple `<span>` color classes — not a heavy syntax-highlighting library) showing the HTML/CSS.
- A live preview panel next to or below it: an `<iframe>` whose `srcdoc` attribute is set (via JS) to the code panel's current content, so it renders for real in the browser — this is genuine rendering, not a simulated image.
- Where the source calls for a step comparison (e.g. "same HTML, now with CSS applied"), show two live iframes side by side, or one iframe with a toggle switching its `srcdoc` between the two versions.
- Where the source shows a **network/log-style "Simulation"** (packet journey, browser render steps, HTTP request/response, DNS lookup timeline) — these are NOT real code, they're conceptual walkthroughs. Build these as an animated terminal/log-style card: lines appear one at a time (typewriter or fade-in-sequence on scroll/click), styled like a console (monospace, `--accent` for success lines, `--dim` for in-progress).
- For the hands-on practical section (see below), give students a **real live playground**: an editable code panel (starts pre-filled with the lesson's example) + live iframe preview that updates as they type or as they click "uncomment" toggles — this replaces Bilal's own classroom technique of progressively uncommenting sections in a real `.html` file, but lets each student control the reveal themselves.

## Language rules
`dir="rtl"` for the page shell and all Arabic explanation text. UI in فصحى, explanations in Egyptian Arabic — this is students' **first contact with web dev**, so keep explanations extra simple, concrete, and encouraging, avoiding jargon-on-jargon. All code, URLs, and file names stay in English with `dir="ltr"`. "الـ" prefix rule at line/heading/list/table-cell start for English terms.

## Mandatory SVG / interactivity rules
No native SVG `<text>` (self-check via grep before finishing each section). Any diagram with 4+ connections built from a JS data lookup, never hand-typed coordinates. Stable `data-id` + `DOMContentLoaded` binding. Checkpoint after each section. Staged build: skeleton → each section → final review.

## Quiz behavior
Hidden by default, revealed by click. Immediate color feedback (green/red) + short explanation. Skip button always available.

---

## Content — Part A: Theory (Topic 1 — What is the Web?)

### [Hero] عنوان الجلسة
Badge: "أول جلسة في عالم الويب". Gradient-text title. Subtitle: "كل مرة بتفتح موقع، بيحصل ورا الكواليس رحلة كاملة في أقل من ثانية — تعالى نكتشفها."

### Section 1 — الإنترنت: الشبكة اللي بتوصل العالم كله (accent: cyan)
**Objective:** فهم إن الإنترنت شبكة عملاقة بتوصل بلايين الأجهزة، وإن أي معلومة بتتبعت بتتقسم لقطع صغيرة اسمها Packets وترجع تتجمع تاني عند الوصول.
- **Analogy:** كل بيت في العالم = جهاز كمبيوتر، والطرق اللي بتوصل البيوت = الإنترنت.
- **Interaction — animated log simulation** (reuse the console-log pattern): "Hello from Cairo!" يتقسم لـ 3 Packets، كل واحد يعدي على Router مصر → Router أوروبا → لندن، ويتجمعوا تاني في الآخر (استخدم نص السورس بالظبط).
- **Key Facts table** (Global Network, Physical Infrastructure, Data Transfer, Always On, Decentralized) كـ 5 كروت صغيرة.
- **Quiz:** none.

### Section 2 — الويب مقابل الإنترنت (accent: amber)
**Objective:** الإنترنت = البنية التحتية (الطرق)، الويب = خدمة بتشتغل فوقها (المحلات والأماكن اللي بتزورها). مش كل استخدام للإنترنت بيبقى ويب (واتساب بيستخدم إنترنت مش ويب، يوتيوب في المتصفح بيستخدم الاتنين).
- **Side-by-side comparison table** (use source exactly: What it is / Created / Examples / Accessed by / Required?).
- **Interaction:** a simple "is this the Web?" sorting game — 5 activities (WhatsApp call, YouTube in browser, online game server, checking Gmail in a browser tab, a video call app) student classifies as "Internet only" or "Internet + Web".
- **Quiz (1 question):** WhatsApp استخدام — إنترنت بس ولا إنترنت وويب؟

### Section 3 — الموقع مقابل الصفحة (Website vs Web Page) (accent: violet)
**Objective:** Website = مجموعة صفحات تحت نفس العنوان، Web Page = صفحة واحدة بس.
- **Analogy:** الموقع = كتاب، الصفحة = صفحة واحدة جواه (ويكيبيديا = الكتاب، مقال مصر = صفحة واحدة فيه).
- **Interaction:** an expandable youtube.com tree (matches source exactly: youtube.com/ → Home Page, /watch?v=abc → Video Page, /results?q=cat → Search Page, /channel/xyz → Channel Page) student clicks each branch to see it highlighted as "ONE web page inside the website."
- **Quiz (1 question):** given "bbc.com" and "a single news article on it", identify which is Website and which is Web Page.

### Section 4 — المتصفح: المترجم اللي بيحول الكود لصفحة (accent: emerald)
**Objective:** المتصفح برنامج بيقرا كود الصفحة ويحولها لشكل ملون قابل للضغط عليه (Rendering).
- **Popular browsers grid:** Chrome/Edge/Firefox/Safari/Opera icons.
- **Interaction — step-by-step reveal (7 steps, exact source sequence):** URL في شريط العنوان → طلب للسيرفر → السيرفر يرد بالملفات → قراءة HTML → قراءة CSS → قراءة JS → عرض الصفحة، مع الـ simulation الزمنية بالظبط (Step 1→7 بالمللي ثانية).
- **Quiz:** none.

### Section 5 — علاقة الـ Client بالـ Server (accent: pink)
**Objective:** كل زيارة موقع فيها طرفين: Client (المتصفح بتاعك، بيطلب) وServer (كمبيوتر قوي بيرد بالملفات).
- **Analogy:** مطعم — إنت الزبون (Client) بتطلب، المطبخ هو الـ Server بيجهز ويرجعلك، الشبكة هي الجرسون.
- **Interaction — animated request/response flow:** رسمة بسيطة CLIENT ←→ SERVER بسهمين متحركين (REQUEST رايح، RESPONSE جاي)، مع الـ Network Log simulation بالظبط من السورس (`GET https://google.com` → `200 OK`).
- **Quiz (1 question):** مين اللي "بيطلب" في العلاقة، المتصفح ولا السيرفر؟

### Section 6 — الرحلة الكاملة: من كتابة العنوان لظهور الصفحة (accent: red)
**Objective:** تجميع كل حاجة في تسلسل واحد: كتابة العنوان → DNS يترجم الاسم لـ IP → الطلب يعدي على الإنترنت → السيرفر يستقبل → يرد بالملفات → المتصفح يعرضها.
- **Interaction — the full timeline simulation** (use source's exact 9-line log: DNS lookup → resolved → TCP connection → GET request → 200 OK → HTML parsing → CSS applied → JS executed → page displayed, with the millisecond timestamps).
- **DNS explained briefly** (phone book analogy) as a small note card, flagged as "هنتعمق فيها في درس متقدم لاحقًا."
- **Quiz:** none.

### [Recap 1] كل حاجة اتعلمناها عن الإنترنت والويب
Use the source's own 6-card recap grid exactly: Internet & Web / Website vs Page / Browser / Client / Server / Web Flow — each a compact bullet-point card, styled as a visual "cheat sheet" moment before moving to Topic 2.

---

## Content — Part B: Theory (Topic 2 — What is a Website Made Of?)

### Section 7 — تشريح الـ URL (accent: cyan)
**Objective:** أي صفحة على الويب ليها عنوان فريد اسمه URL، ومكوّن من أجزاء ثابتة.
- **Analogy:** URL = عنوان بريدي كامل — Protocol = نوع البريد، Domain = اسم الشارع والمبنى، Path = رقم الشقة.
- **Interaction — labeled URL breakdown:** `https://www.wikipedia.org/wiki/Internet?lang=en` مقسّم لأجزاء ملونة قابلة للضغط (Protocol/Subdomain/Domain/TLD/Path/Query)، كل جزء يديله تعريفه بالظبط من جدول السورس. كمان مثال يوتيوب وجوجل من السورس.
- **Quiz (1 question):** في `docs.github.com/en/get-started`، إيه الـ subdomain؟

### Section 8 — طلب وإجابة: HTTP Request & Response (accent: amber)
**Objective:** كل تحميل صفحة فيه رسالة طلب (Request) من المتصفح ورسالة رد (Response) من السيرفر، وده اسمه HTTP.
- **Request contains:** Method (GET/POST) + URL + Headers. **Response contains:** Status Code + Headers + Body.
- **Interaction:** two live-log cards side by side — "Browser → Server" (Method/URL/Protocol/Host/Browser) و"Server → Browser" (Status/Content-Type/Size/Body) — using the exact source examples.
- **Status codes table** (200/301/404/500) with the source's "you've seen 404 before" callout as a highlighted note.
- **Quiz (1 question):** إيه معنى status code 404؟

### Section 9 — تسلسل تحميل الموقع بالتفصيل (accent: violet)
**Objective:** نسخة أعمق من Section 6 — 9 خطوات دقيقة (Type URL → DNS Lookup → DNS Reply → TCP Connection → HTTP Request → HTTP Response → Parse HTML → Load Resources → Render Page).
- **Interaction — the detailed network timeline** (use source's exact simulated log with real millisecond values, ending with "⚡ 50 to 100 separate requests" callout).
- **Quiz:** none (this section reinforces Section 6, not new fact-recall).

### Section 10 — HTML وCSS وJavaScript: التلاتة اللي بيبنوا أي موقع (accent: emerald)
**Objective:** HTML = الهيكل، CSS = الشكل، JavaScript = السلوك والتفاعل.
- **Analogy:** بيت — HTML = الحيطان والأوض، CSS = الدهان والأثاث، JavaScript = الكهرباء اللي بتشغل حاجات.
- **THIS IS WHERE THE LIVE PREVIEW PATTERN IS ESSENTIAL — build 3 real live demos exactly matching the source's code:**
  1. Plain HTML (h1 + p + a) → live iframe showing it unstyled.
  2. Same HTML + the source's exact CSS (colored h1, styled p, bold blue link) → live iframe showing it styled, toggle-able against version 1.
  3. The button + JavaScript example (`getElementById`, `addEventListener`) → a REAL working live button the student can click, showing the message appear — this must actually execute, not be a static mockup.
- **File comparison table** (HTML/.html/Structure, CSS/.css/Design, JS/.js/Interactivity, each with "Without It" consequence).
- **Quiz (1 question):** لو شلنا الـ CSS بس، هيحصل إيه للصفحة؟

### Section 11 — مواقع ثابتة مقابل مواقع ديناميكية (accent: pink)
**Objective:** Static = نفس المحتوى لكل الزوار (بورتفوليو، منيو مطعم). Dynamic = محتوى مخصص لكل زائر حسب بياناته (يوتيوب، أمازون، إنستجرام).
- **Two-column comparison card** (Static features list vs Dynamic features list, exactly from source) + the real-world examples table.
- **Interaction:** 5 example sites (personal portfolio, restaurant menu, YouTube, Amazon, Instagram) student classifies Static/Dynamic with the source's exact reasoning revealed after.
- **Note:** highlight the source's reassurance — "كمبتدئين، هتبدأ بمواقع Static، ده أساس كل مطور ويب."
- **Quiz:** none (the classification interaction is the check).

### Section 12 — أدوات المطوّر: DevTools (accent: red)
**Objective:** كل متصفح فيه أدوات مدمجة (F12 أو Inspect) بتوريك الكود الحقيقي وراء أي موقع.
- **Interaction:** a mock DevTools panel (Elements/Console/Network/Sources/Application tabs) showing the source's exact HTML snippet in the Elements view, each tab revealing its one-line purpose on click.
- **Reassurance callout (important for first-timers, use exactly):** أي تعديل في DevTools بيأثر على المتصفح بتاعك بس، مش على الموقع الحقيقي — رجّع الصفحة (Refresh) وهترجع زي ما كانت.
- **Quiz:** none — end with the source's "Try It Now" invitation as a direct instruction, not a quiz.

### [Recap 2] كل حاجة اتعلمناها عن بنية الموقع
Use the source's own second recap grid exactly: URL / HTTP Request / HTTP Response / Website Loading / HTML-CSS-JS / Static vs Dynamic / DevTools.

---

## Content — Part C: Practical (Hands-On HTML Tags)

### [Practical Intro] دلوقتي هنكتب كود حقيقي (accent: cyan, distinct visual treatment marking the shift from theory to practice)
Short framing: لحد دلوقتي فهمنا إزاي الويب شغال، دلوقتي هنكتب أول أسطر HTML بإيدينا. كل مثال هنا شغال فعليًا — جرب، غيّر، بلاش تخاف تكسر حاجة.

### Section 13 — العناوين والفقرات (Headings & Paragraphs) (accent: amber)
Based on the practical file's first example (h1, h2, h3, h4, p tags). **Live playground:** pre-loaded with the exact source example (Welcome to My Website / About Me / My Name / first name / My name is Ahmed / My Age / I am 15 years old), editable code panel + live iframe. A short note explaining the heading hierarchy (h1 biggest/most important down to h4).
- **Quiz:** none (practice-first section).

### Section 14 — تنسيق النص: Bold, Italic, Underline (accent: violet)
Based on the second commented example (`<b>`, `<i>`, `<u>`). **Live playground:** the exact source paragraph ("I am learning HTML, CSS, and JavaScript") pre-loaded, editable — student can toggle which words get which tag and see the result live.

### Section 15 — النص المهم: strong, em, mark (accent: emerald)
Based on the third commented example. **Live playground:** the exact source examples (Warning! / Practice every day. / HTML is easy. highlighted) — note the semantic difference from Section 14 (strong/em carry meaning, b/i are purely visual) as a short "⚠️ أخطاء شائعة" callout, since this distinction is easy to miss.

### Section 16 — حذف، إضافة، وتنسيقات إضافية: del, ins, small, br (accent: pink)
Based on the fourth commented example. **Live playground:** the exact source price-comparison example (Old Price 200 EGP struck through, New Price 150 EGP inserted, offer note in small text).

### Section 17 — التطبيق العملي: أربع مشاريع صغيرة (accent: red)
Based on the four "Example" blocks in the file (My Profile, School News, Computer Store, Daily Routine). Present as 4 tabs (reuse the proven tabbed pattern) — each tab is a full live playground pre-loaded with that example's exact source code, letting students see how all the tags combine in a realistic mini-page. Include a short prompt after each: "جرب تغيّر النص أو تضيف تاج جديد."

### [Closing] من الفهم للتنفيذ
Visual: a simple step recap connecting Part A (كيف يشتغل الويب) → Part B (من إيه المواقع مبنية) → Part C (أول أسطر كود حقيقية كتبتها بنفسك). Closing line: "دلوقتي بقى عندك الأساس اللي أي مطور ويب بدأ بيه — من هنا هنبني كل حاجة."

---
Build in the staged order above. Run the mandatory checkpoint after every section before moving to the next one. Pay special attention to Section 10 and Part C — these need genuinely working live iframes, not static mockups, since the whole pedagogical point is that students see real rendering happen.
