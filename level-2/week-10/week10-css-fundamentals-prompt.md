# Master Prompt: Interactive HTML Explainer — Week 10: CSS Fundamentals

## Role
Build a single self-contained HTML file for a teacher (Bilal) presenting CSS fundamentals — what CSS is, how to link it, colors, text styling, and classes/IDs — to students aged 12–17 who completed the HTML weeks (Sessions 1–3 / Weeks 8–9), on a laptop connected to a projector.

## Hard requirements — deliverable format
- ONE `.html` file. All CSS/JS inline. Google Fonts link only external dependency.
- Two logo images provided separately (`bilal-icon.webp`, `bilal-wordmark.webp`). Embed as base64 using the exact `.nav-logo` (36px) / `.footer-logo` (40px) classes.
- Filename: `week10-css-fundamentals.html`.

## Visual design system — Dark Animated Theme (reuse exactly)
```css
:root {
  --primary: #193cff; --accent: #00d4aa; --bg: #0a0e27;
  --card: #111638; --card-hover: #1a2050; --text: #fff; --dim: #8892b0;
  --success: #00ff88; --danger: #ff4757; --warn: #ffd700;
}
```
Animated radial-gradient background + ~30 floating particles. Cards rounded (24px/16px), hover lift + glow border, top gradient bar. Fixed nav hidden until scroll, blurred pill-nav. Font Cairo. Section number badges. Per-section accent variables cycling: cyan `#06B6D4`, amber `#F59E0B`, violet `#8B5CF6`, emerald `#10B981`, pink `#EC4899`, red `#EF4444`. Every section ends with a `⚠️ أخطاء شائعة` box. Prefer animated emojis over static SVGs. SVG quality rule applies where SVGs are used (vibrant, gradients, top-left light).

## Live Code Preview pattern — mandatory
Every code example shows the **full HTML document** (`<!DOCTYPE html>` through `</html>`), code panel `dir="ltr"` monospace with proper escaping (escape first, then color-tint — do not let markup leak as visible text), paired with a live `<iframe srcdoc="...">`. CSS examples show both the HTML and the linked/internal CSS together, with the rendered result live.

## Language rules
`dir="rtl"` for page shell and Arabic text. UI in فصحى, explanations in Egyptian Arabic, simple and encouraging. Code/CSS stays English `dir="ltr"`. "الـ" prefix rule for English terms starting a line/heading/list/table cell.

## Mandatory SVG / interactivity rules
No native SVG `<text>` (grep self-check). Diagrams with 4+ connections built from a JS data lookup. Stable `data-id` + `DOMContentLoaded` binding. Checkpoint after each section. Staged build: skeleton → each section → final review.

## Quiz behavior
Hidden by default, revealed by click. Immediate color feedback (green/red) + short explanation. Skip button always available.

## Activity behavior
For the closing Profile Page activity: present the full task/requirements up front, let students work through it themselves, then a single "اعرض الحل الكامل" button reveals the full walkthrough solution.

---

## Content

### [Hero] عنوان الأسبوع
Badge: "CSS Fundamentals". Gradient-text title. Subtitle: "الأسبوع اللي هنخلي فيه الصفحة تبقى شكلها زي ما إنت عايز، مش زي ما المتصفح قرر."

### [Intro] إيه هو الـ CSS (accent: cyan)
**Objective:** الفرق بين Content (HTML، إيه اللي في الصفحة) و Presentation (CSS، شكلها إزاي). CSS بيستهدف عناصر HTML موجودة أصلاً، مش بيضيف محتوى جديد — "HTML بيبني الأوضة، CSS بيدهنها ويرتبها."
- **Live before/after demo:** نفس الـ `<h1>` و`<p>` — قبل أي CSS (نص أسود عادي) وبعد (`h1{color:blue;font-size:32px;}` و`p{color:green;}`) جنب بعض.
- **Quiz (1 question):** CSS بتضيف محتوى جديد للصفحة ولا بس تغيّر شكل الموجود؟

### Section 1 — صياغة قاعدة الـ CSS (accent: amber)
**Objective:** أي قاعدة CSS مبنية من 3 أجزاء: Selector (العنصر المستهدف) + Property (الخاصية) + Value (القيمة)، جوه `{ }` وبعد كل قيمة `;`.
- **Live example:** `h1 { color: blue; }` مع شرح تفاعلي لكل جزء (يقدر الطالب يدوس على كل كلمة في القاعدة فيتلون ويطلعله شرحها).
- **Quiz (1 question):** في `p { font-size: 18px; }`، إيه الـ Property وإيه الـ Value؟

### Section 2 — إزاي نوصل الـ CSS بالـ HTML (accent: violet)
**Objective:** 3 طرق: **Inline** (`style=""` على العنصر نفسه، أقوى أولوية بس أسوأ ممارسة)، **Internal** (`<style>` جوه `<head>`، لصفحة واحدة بس)، **External** (ملف `.css` منفصل موصول بـ `<link rel="stylesheet" href="style.css">`، الطريقة الاحترافية والمعيار في كل مشروع حقيقي).
- **Comparison table** (استخدم جدول المصدر بالظبط: أين يعيش/يحتاج ملف/بيطبق على/قابل لإعادة الاستخدام/الأفضل لـ).
- **Interaction:** toggle بين الثلاث طرق يوري نفس الـ `<h1>` بنفس الستايل، بس الكود يتغير حسب الطريقة المختارة (live iframe لكل واحدة).
- **Common mistake box (استخدم أمثلة المصدر بالظبط):** خطأ في اسم الملف (`styles.css` بدل `style.css`)، أو نسيان الـ `rel="stylesheet"`، أو الملف في مجلد فرعي من غير تحديد المسار.
- **Quiz (1 question):** أي طريقة هي المعيار الاحترافي لمشروع حقيقي؟

### Section 3 — الألوان: color و background-color (accent: emerald)
**Objective:** خاصية `color` بتلوّن نص العنصر، و`background-color` بتلوّن خلفيته. طرق كتابة اللون (4 طرق — من `style s3.css` بالظبط): **اسم اللون** (`red`,`blue`,`green`,`black`,`white`,`orange`)، **Hex** (`#ff0000` — كل زوج بيمثل لونًا: `ff` أحمر، `00` أخضر، `00` أزرق)، **RGB** (`rgb(255,0,0)` — كل قيمة من 0 لـ 255)، **RGBA** (`rgba(255,0,0,0.5)` — الأخيرة `A` هي الـ alpha والشفافية، من 0 شفاف تمامًا لـ 1 ظاهر تمامًا، وأمثلة بينهم: 0.1, 0.2, 0.3, 0.5, 0.75, 0.9).
- **Live interactive color picker:** الطالب يختار عنصر (h1/p/span) ويجرب الطرق الأربع: قايمة أسماء، حقل hex، و3 sliders لـ RGB، وسلايدر منفصل لـ Alpha بيتعامل مع RGBA، ويشوف اللون/الشفافية يتغيّر لحظيًا على نفس النص.
- **Live from source (مهم):** `#main-title` الجوه `style s3.css` متلوّن بـ `rgba(0,0,255,0.5)` — اعرض نفس اللون بدون شفافية للمقارنة.
- **Common mistake box:** الخلط بين `color` (لون النص) و`background-color` (لون الخلفية)، وكتابة قيمة الـ Alpha غلط (من 0 لـ 1 مش من 0 لـ 255).
- **Quiz (1 question):** `color: rgba(255,0,0,0.5);` — الـ `0.5` معناها إيه؟

### Section 4 — التحكم في النص (accent: pink)
**Objective:** خصائص تنسيق النص (من `style s3.css` بالظبط): `text-align` (left/center/right — بتتحكم في مكان النص جوه العنصر، مش بتزيّح العنصر نفسه)، `font-family` (Arial, Verdana واضح, Tahoma ممتاز للعربي, Georgia, Times New Roman, sans-serif, serif)، `font-size` (بـ px — النقطة الدقيقة على الشاشة؛ 12 صغير / 16 عادي / 24 عنوان صغير / 40 عنوان رئيسي)، `font-weight` (100–900 أو neutral/bold مع 900 سميك جدًا)، `text-decoration` (none/underline/overline/line-through)، `line-height` (رقم بدون وحدة — من 1 لـ 2، الأفضل 1.6–1.7). وأبعاد: `width` (`100px` قيمة ثابتة، `50%`/`100%` نسبة من عرض الأب، ومش بتتحكم في height).
- **Live interactive demo:** فقرة نص واحدة مع قوائم اختيار (dropdown لكل خاصية) — الطالب يختار كل خاص ويشوف تأثيرها فورًا على نفس النص، مع شريط **width** slider يحوّل صورة بين `100px` / `50%` / `100%`.
- **Note the exact recommendation:** `line-height: 1.6` أو `1.7` المعيار الاحترافي لراحة القراءة؛ `font-size` لازمها وحدة.
- **Quiz (1 question):** `font-size:20;` من غير وحدة بيعمل إيه؟
- **Quiz (1 question):** `text-decoration: none` بيستخدمن لإيه غالبًا (إزالة خط الروابط)؟
- **Common mistake box (أوجه من `style s3.css`):** نسيان `;` بعد القيمة، نسيان `:` الخاصية والقيمة، نسيان الوحدة (`font-size:20` بدل `20px`)، كتابة اسم الخاصية غلط (`text-weight` بدل `font-weight`)، ونسيان إغلاق `} `.

### [Live Practice] معمل الـ CSS Playground (accent: red — this is the central hands-on section, give it real weight)
This is the core interactive feature, built from the **exact provided practical file `session3.html`** (and it's the CSS source it links, `style s3.css`). Reproduce the page structure precisely, with its elements: `h1#main-title`, `h2.section-title` (About Me / My Skills / Profile Image / Buttons / Links / Product Cards / Contact Info / Mini Profile / CSS Selectors Practice), `.description` paragraphs, `p` normal paragraphs, `img` profile image, `ul` My Skills list, `a` YouTube/Facebook/Instagram links, `.card` product cards, and `.primary-btn` / `.secondary-btn` Contact buttons. Present the unstyled HTML exactly (code panel with the full document), with a live `<iframe>` preview starting completely unstyled.

**Playground controls:**
- Element selector (dropdown or clickable tabs): Heading (`#main-title`) / Section Titles (`h2.section-title`) / Paragraphs (`.description` vs normal) / Buttons (.primary-btn/.secondary-btn) / Links (`a`) / Image (`img`) / List (`ul`).
- Per-element control panel: dropdowns for fixed-choice properties (`text-align`, `font-weight`, `text-decoration`, `font-family`, `color` named) و free controls for open-ended ones (`color`/`background-color` picker, `font-size`/`line-height`/`width` sliders).
- Every change updates the live CSS panel (building up a real `style s3.css` content shown alongside) AND the live `<iframe>` preview of the **whole playground page** — so students see their choices compound into a fully styled page, exactly mirroring the real VS Code + Live Server workflow Bilal uses in class.
- Include a "نسخ الـ CSS" button so students can copy what they built.
- **Quiz:** none — this whole section is hands-on practice, not a fact-check.

### Section 5 — الكلاسات (Classes) والـ IDs (accent: cyan)
**Objective:** الفرق الجوهري — عناصر الوسم (`h2`) بتستهدف كل العناصر من نفس النوع مرة واحدة، وده بيبقى محدود. الحل: **Class** (`.name`, بنقطة) — قابل للتكرار على أكتر من عنصر، للأنماط المشتركة (كروت، أزرار). **ID** (`#name`, بهاش) — لازم يكون فريد، مرة واحدة بس في الصفحة، للعناصر الهيكلية الفريدة (header, footer).
- **Live example — the exact "3 headings, 1 rule" problem then the fix:** أول `h2 { color: orange; }` بيلوّن كل العناوين بنفس اللون (غير مرغوب)، بعدين نفس المثال بـ class مختلف لكل عنوان يديله لون مستقل.
- **Decision guide (استخدم قواعد المصدر بالظبط):** هيتكرر العنصر؟ → Class. قسم هيكلي فريد؟ → ID.
- **Common mistake box (من `style s3.css` بالظبط):** استخدام `#` مع class (`#description` غلط — الصح `.description`)، واستخدام `.` مع id (`.main-title` غلط — الصح `#main-title`).
- **Quiz (1 question):** لعنصر هيتكرر في الصفحة عدة مرات بنفس الشكل، تستخدم Class ولا ID؟

---

### [Activity] صفحة البروفايل الشخصية (accent: amber, dashed activity-card style)
Present the full task exactly as in the source: صفحة بروفايل شخصي فيها `<h1>` بالاسم (بـ ID)، `<img>` صورة شخصية، `<p>` بايو (بـ Class)، `<button>` "Contact Me"، `<a>` لينك موقع مفضل — كل ده جوه ملف `style.css` خارجي منفصل. المطلوب: خلفية صفحة غير بيضاء، لونين نص مختلفين على الأقل، خط مختلف عن الافتراضي، محاذاة في النص، Class واحد على الأقل، ID واحد على الأقل.

Give students a live playground pre-loaded with the unstyled HTML skeleton (matching the source's exact starting structure) to build their own version.

A single "اعرض الحل الكامل" button reveals the source's exact model solution (`body` gray background + Arial + center; `#main-title` blue + 40px; `.description` green + 18px + line-height 1.6; `img` width 200px; `button` orange background + white text; `a` red + no underline), shown as the full annotated final code + live rendered result.

---

### [Closing] من HTML بس لصفحة مصممة
Visual: step recap — Content (HTML) → Selector/Property/Value → طريقة الربط (External) → لون ونص → Class/ID للتحكم الدقيق → صفحة كاملة مصممة بإيدك. Closing line: "الأسبوع اللي فات كتبت المحتوى، النهارده لبسته شكل. الأسبوع الجاي هنتعلم إزاي نرتب العناصر في المكان الصح (Layout)."

---
Build in the staged order above. Run the mandatory checkpoint after every section before moving to the next one. Pay special attention to the Live Practice section — this needs genuinely working live iframes reflecting real accumulated CSS, not a static mockup.
