# Master Prompt: Interactive HTML Explainer — Drawing, Shading, Perspective, Color & Digital Imaging

## Role
Build a single self-contained HTML file for a teacher (Bilal) to present a Digital Arts practical-skills lesson (confident mark-making, construction drawing, shading, one-point perspective, color theory, and digital imaging fundamentals) to students aged 12–17, on a laptop connected to a projector.

## Hard requirements — deliverable format
- ONE `.html` file. All CSS/JS inline. Google Fonts link only external dependency.
- Two logo images provided separately (`bilal-icon.webp`, `bilal-wordmark.webp`, solid `#193cff` background baked in). Convert to base64, embed in header and footer.
  - Header: `<div class="nav-logo"><img src="data:image/webp;base64,..." alt="Logo" width="36" height="36"></div>` — CSS must match exactly: `.nav-logo img { width: 36px; height: 36px; border-radius: 50%; }`
  - Footer: `<img class="footer-logo" src="data:image/webp;base64,..." alt="Logo" width="40" height="40">` — CSS must match exactly: `.footer-logo { width: 40px; height: 40px; border-radius: 50%; margin-bottom: 12px; }`
- Filename: `drawing-color-digital-imaging.html`.

## Visual design system — Dark Animated Theme (reuse exactly)
```css
:root {
  --primary: #193cff; --accent: #00d4aa; --bg: #0a0e27;
  --card: #111638; --card-hover: #1a2050; --text: #fff; --dim: #8892b0;
  --success: #00ff88; --danger: #ff4757; --warn: #ffd700;
}
```
Animated radial-gradient background + ~30 floating particles. Cards rounded (24px/16px), hover lift + glow border, top gradient bar. Fixed nav hidden until scroll, blurred pill-nav, lists all section titles, clickable jump. Font Cairo. Section number badges. Per-section accent variables cycling: cyan `#06B6D4`, amber `#F59E0B`, violet `#8B5CF6`, emerald `#10B981`, pink `#EC4899`, red `#EF4444`, repeat. Every section ends with a `⚠️ أخطاء شائعة` box. Granular scroll-reveal per block via one `IntersectionObserver` (threshold 0.05), `translateY(30px)→0`, `visible` class, `0.6s cubic-bezier(0.4,0,0.2,1)`. Keyboard arrow-nav. Legend boxes next to diagrams. Footer: both logos + encouraging line.

**Color theory sections need real, accurate color swatches** — implement actual HSV manipulation in JS/CSS for the Hue/Saturation/Value and color harmony interactions (not illustrative-only), since color accuracy matters pedagogically here.

## Language rules
`dir="rtl"`, UI in فصحى, explanations in Egyptian Arabic matching the source's warm, direct, teacher-narrating tone. English art terms (Hue, Vanishing Point, Raster, etc.) wrapped `<span dir="ltr">`, "الـ" prefix rule at line/heading/list/table-cell start.

## Mandatory SVG / interactivity rules
No native SVG `<text>` (self-check via grep before finishing each section). Any diagram with 4+ connections built from a JS data lookup, never hand-typed coordinates. All interactive elements must use `data-id` attributes + `id` on the element + `document.getElementById(...).onclick` inside `DOMContentLoaded` (do NOT use querySelector with `data-id` — it fails). Every interactive section must include a "إعادة تشغيل" replay button styled as an outline pill to reset the animation/interaction to its initial state. Checkpoint after each section. Staged build: skeleton → each section → final review.

## Quiz behavior
Hidden by default, revealed by click. Immediate color feedback (green/red) + short explanation. Skip button always available.

## Activity behavior — IMPORTANT
For the two major labeled Activities (Shading Challenge, Mood Palette Challenge): present the full task up front, let students work through it themselves, then a single "اعرض النموذج" button reveals the model answer. The smaller "mini activities" embedded within sections below (Object-into-Forms, One-Point Room practice, File Format Match) are lighter-touch — build them as the section's main hands-on interaction rather than separate quiz-style items, each still ending with a single "اعرض الإجابات" button that reveals all answers at once (NOT click-per-question reveal).

## Logo classes (must match exactly between CSS and HTML)
- Header: `<div class="nav-logo">` wrapping `<img>` — CSS: `.nav-logo { display: inline-block; margin-left: 12px; vertical-align: middle; }` + `.nav-logo img { width: 36px; height: 36px; border-radius: 50%; }`
- Footer: `<img class="footer-logo" ...>` — CSS: `.footer-logo { width: 40px; height: 40px; border-radius: 50%; margin-bottom: 12px; }`

---

## Content

### [Hero] عنوان الدرس
Badge: "Drawing & Design Fundamentals". Gradient-text title. Subtitle inviting the student from "خط واثق واحد" إلى "صورة فيها عمق، ظل، ولون مقصود."

### [Intro] الرسم بثقة: التسخين والملاحظة (accent: cyan)
Based on Slides "Start With Confident Marks" + "Observation + Construction". **Objective:** فهم إن الخط الواثق (حركة هادئة بالدراع كله، مش الرسغ بس) أهم من الدقة من أول مرة، وإن قبل الرسم لازم "نلاحظ" (نقارن الارتفاع والعرض والزوايا والمسافات) قبل ما نحرك القلم، ونسأل نفسنا "الشكل ده عبارة عن إيه في الحقيقة؟" (كوباية = Cylinder، كتاب = Box).
- **Interaction 1 — warm-up practice:** 4 mini canvases (straight lines / curves / circles / ellipses) where the student can draw with mouse/touch, reinforcing the source's exact warm-up sequence.
- **Interaction 2 — whole-arm vs wrist demo:** a toggle showing two line-drawing simulations, one "jittery" (wrist-only) and one "smooth" (whole-arm), illustrating the source's exact point.
- **Quiz:** none (this is a warm-up/mindset section).

### Section 1 — التناسب والمساحة السالبة (accent: amber)
Based on "Proportions & Negative Space". **Objective:** فهم إن Proportions هي العلاقة بين أحجام الأجزاء (مقارنة بالعين مش بالمسطرة — "الكتاب عرضه ضعف عرض الكوباية")، وإن Negative Space (الفراغ حوالين الجسم) أداة لاكتشاف أخطاء الرسم بسرعة.
- **Interaction:** two objects (e.g. a cup and a book) the student can resize relative to each other via sliders, with a live "does this look right?" feedback; a second toggle highlights the negative space (the gap shape between them) to demonstrate the checking technique.
- **Quiz (1 question):** identify a proportion error in a described scenario.

### Section 2 — تبسيط الأجسام: الأشكال الأساسية الأربعة (accent: violet)
Based on "Simplify Objects Into Forms" + Mini Activity "Object Into Forms" + "The Four Basic Forms". **Objective:** فهم إن أي جسم معقد ممكن يتبسط لأشكال أساسية: Sphere (كورة)، Cube (مكعب)، Cylinder (أسطوانة)، Cone (مخروط) — والأمثلة: الكوباية = Cylinder+Ellipse+منحنى، الكتاب = Box، النبتة = Cylinder+أشكال مخروطية.
- **Interaction (this is the section's hands-on mini activity):** a gallery of everyday objects (bottle, cup, pencil case, book, headphones, bag); clicking one reveals it "decomposed" into the basic forms that build it (an animated overlay showing the shapes it's made of), matching the source's exact headphones example (سماعتين=Sphere/Cylinder، الطوق=منحنى، الوسادات=Cylinders صغيرة).
- **Quiz:** none (the decomposition gallery is the reinforcement).

### Section 3 — الإضاءة والظل (accent: emerald)
Based on "Light Direction Controls Value" + "Shadow Vocabulary". **Objective:** فهم القواعد الأساسية: الجهة المواجهة للضوء أفتح، البعيدة أغمق، الظل بيوضح فين الضوء اتمنع، ولازم يكون مصدر ضوء واحد ثابت لكل عناصر الرسمة. المصطلحات الخمسة: Highlight (ألمع نقطة)، Light Side (جانب الضوء)، Core Shadow (الظل الأساسي على الجسم نفسه)، Reflected Light (ضوء منعكس خفيف من الأرض)، Cast Shadow (الظل الساقط على الأرض).
- **Interaction — light direction simulator (central interaction of this section):** a 3D-ish sphere (CSS radial-gradient based) with a draggable "light source" icon around it; as the student moves the light, the highlight/light-side/core-shadow/cast-shadow all update live, with each of the 5 zones labeled via a legend the student can toggle on/off.
- **Quiz (1 question):** identify one of the 5 shadow-vocabulary terms from a description.

### [Activity 1] تحدي تظليل الأشكال الأربعة (Four Forms Shading Challenge) (accent: pink, dashed activity-card style)
Based on "ACTIVITY 1" + "Activity 1 Checklist". Present the task: ارسم الأربع أشكال (Sphere, Cube, Cylinder, Cone)، اختار اتجاه إضاءة واحد وثابت لكل الأشكال، ضيف الخمس أجزاء (Highlight, Core Shadow, Reflected Light, Cast Shadow, Light Side)، واستخدم درجات الرمادي بس. Provide the **checklist as an actual interactive checklist** the student ticks through: ✓ مصدر إضاءة واحد واضح · ✓ 4 درجات رمادي على الأقل (أبيض/رمادي فاتح/رمادي غامق/أسود) · ✓ الظل الساقط لامس الأرض وفي الاتجاه العكسي للضوء · ✓ الشكل حاسس إنه 3D مش مسطح. After working through it, a single "اعرض النموذج" button shows a worked example (a shaded sphere illustration built with the light-direction interaction pattern from Section 3, correctly labeled).

### Section 4 — المنظور: خط الأفق ونقطة التلاشي (accent: red)
Based on "Horizon Line, Eye Level, Vanishing Point" + "One-Point Perspective" + "Three Easy Depth Tools" + Mini Practice "One-Point Room" + "Quick Discussion". **Objective:** فهم الثلاثة مصطلحات: Horizon Line (خط بيمثل مستوى عين المشاهد)، Eye Level (ارتفاع عين الشخص)، Vanishing Point (النقطة اللي الخطوط المتوازية كأنها بتتجمع فيها). ثم بناء غرفة بنقطة تلاشي واحدة: ارسم الحائط الخلفي → حط نقطة التلاشي على خط الأفق → وصّل أركان الغرفة بيها → ضيف عناصر (أثاث) ماشية بنفس اتجاه الخطوط. أدوات إحساس بالعمق بدون منظور: Scale (البعيد أصغر)، Overlap (اللي بيغطي جزء من التاني أقرب)، Placement (اللي تحت أقرب).
- **Interaction (central, this is the section's hands-on mini practice):** an interactive one-point-perspective room builder — student places a vanishing point on a horizon line by clicking, then clicks to add simple furniture blocks (bed/desk/shelf) that automatically orient their guide-lines toward the vanishing point, visually demonstrating why furniture "looks right" only when aligned to it. A toggle can move the vanishing point to show all elements re-orienting live.
- **Quiz (1 question):** match a depth cue (Scale/Overlap/Placement) to its description.

### Section 5 — أساسيات نظرية الألوان (accent: cyan)
Based on "Color Theory Fundamentals" + "Hue, Saturation & Value". **Objective:** Color Wheel (عجلة الألوان)، Primary Colors (أحمر/أزرق/أصفر — أساس نظام RYB اللي بيستخدمه الفنانين، مختلف عن RGB)، Secondary (خلط لونين أساسيين)، Tertiary. ثم HSV: Hue (عائلة اللون نفسها)، Saturation (قوة اللون، من باهت لقوي)، Value (فاتح/غامق).
- **Interaction — live HSV color picker:** three sliders (Hue 0-360, Saturation 0-100%, Value 0-100%) controlling a live color swatch, letting the student directly manipulate each dimension independently and see the result — matches the source's exact "افتح color picker" moment.
- **Quiz (1 question):** given a color change description, identify whether Hue, Saturation, or Value changed.

### Section 6 — تناغم الألوان والإحساس (accent: amber)
Based on "Three Useful Color Harmonies" + "Limited Palettes Make Choices Easier" + "Color Psychology & Mood". **Objective:** 3 أنواع تناغم: Complementary (متقابلين في العجلة، تباين قوي، للفت الانتباه)، Analogous (متجاورين، هادي ومريح)، Monochromatic (لون واحد بدرجات، بسيط وأنيق). نصائح Palette محدودة: 3-6 ألوان أساسية، كرر نفس الألوان، استخدم Accent Color واحد بس (مثال الزرار الأحمر في يوتيوب وسط تصميم أبيض وأسود)، وتجنب شكل "قوس قزح". علم نفس الألوان: Warm (أحمر/برتقالي/أصفر = طاقة وحماس وأحيانًا خطر)، Cool (أزرق/أخضر/بنفسجي = هدوء وغموض)، Neutral (أبيض/رمادي/أسود = بساطة واحترافية).
- **Interaction:** a color-wheel widget where clicking any color highlights its Complementary/Analogous/Monochromatic relationships live (three toggle modes); a separate small "palette builder" lets the student pick up to 6 colors and see them applied to a simple mockup card, with a warning indicator if too many unrelated hues are used (illustrating the "rainbow look" problem).
- **Quiz (2 questions):** one on harmony type identification, one on warm/cool/neutral classification.

### [Activity 2] تحدي لوحة الإحساس (Mood Palette Challenge) (accent: violet, dashed activity-card style)
Based on "ACTIVITY 2". Present the task: كل مجموعة (3-5 طلاب) تختار إحساس واحد (Calm, Energy, Mystery, Cozy, Lonely, Heroic, Futuristic)، تعمل Palette من 5 ألوان تخدم الإحساس ده، تحدد نوع الـ Harmony المستخدم، وتشرح سبب اختيارها. Give students an interactive palette builder (reuse the color-wheel/HSV widgets from Sections 5–6) to actually build their 5-color palette live, tagged with the mood they chose. A single "اعرض نموذج" button reveals the source's example: Calm → Light Blue, Sky Blue, White, Soft Gray, Mint Green.

### Section 7 — أساسيات الصور الرقمية: Raster مقابل Vector (accent: emerald)
Based on "Digital Imaging Fundamentals" + "Raster vs. Vector" + "Pixels, Resolution, Image Size". **Objective:** فهم إن الصور الرقمية مش كلها نفس النوع — Raster (معمولة من Pixels، ممتازة للصور الفوتوغرافية، بتتشوش لو كبرناها زيادة) مقابل Vector (معمولة من Paths/معادلات رياضية، ممتازة للوجوهات والأيقونات، بتفضل واضحة أي حجم). Pixel = أصغر مربع لون؛ Resolution = كمية التفاصيل؛ لازم تحدد حجم الصورة النهائي قبل ما تبدأ.
- **Interaction — the zoom-in comparison (core interaction):** two versions of the same simple logo shape — one built as a pixel grid (Raster), one as a clean scalable shape (Vector) — a shared zoom slider the student drags; the Raster version visibly pixelates/blurs while the Vector version stays crisp at every zoom level.
- **Quiz (1 question):** which format (Raster/Vector) fits a given use case (e.g. a photo vs. a logo that needs a huge banner print).

### Section 8 — صيغ الملفات الشائعة (accent: pink)
Based on "Common File Formats" + Mini Activity "File Format Match". **Objective:** JPG (فوتوغرافي، بدون شفافية)، PNG (بيدعم Transparency، مناسب للأيقونات)، SVG (Vector، للوجوهات، أي حجم بدون فقدان جودة)، PSD (ملف العمل بطبقات Photoshop، مش للمشاركة)، MP4 (فيديو/Animation). التذكير المهم: Working File غير Sharing File.
- **Interaction (this section's hands-on mini activity):** 5 format cards (JPG/PNG/SVG/PSD/MP4) and 4 use-case questions from the source (transparent game icon → PNG · layered editable painting → PSD · short animation export → MP4 · logo that must scale very large, avoid this format → JPG, use SVG instead). Student matches each question to a format card by click; a single "اعرض الإجابات" reveals all 4 with the source's exact reasoning.
- **Quiz:** none (the matching activity is the assessment).

---

### [Closing] من الخط الأول للصورة الكاملة
Visual: a vertical step diagram summarizing the full skill chain: خط واثق → ملاحظة وبناء → تناسب ومساحة سالبة → أشكال أساسية → إضاءة وظل → منظور وعمق → لون وتناغم → صورة رقمية جاهزة للنشر أو الطباعة. Closing line: "كل رسمة احترافية، مهما كانت معقدة، بتبدأ بنفس الأساسيات اللي اتعلمناها النهارده."

---
Build in the staged order above. Run the mandatory checkpoint after every section before moving to the next one.
