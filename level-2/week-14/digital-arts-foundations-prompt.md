# Master Prompt: Interactive HTML Explainer — Digital Arts Foundations

## Role
Build a single self-contained HTML file for a teacher (Bilal) to present a full Digital Arts foundations unit (Digital Art basics, Art vs Design, Design Process, Elements & Principles of Design, Gestalt Principles, Shape Psychology, Visual Symbolism, Composition, plus 2 activities) to students aged 12–17, on a laptop connected to a projector. This is a long, comprehensive unit — build it as one file, let students navigate via the sticky nav.

## Hard requirements — deliverable format
- ONE `.html` file. All CSS/JS inline. Google Fonts link only external dependency.
- Two logo images provided separately (`bilal-icon.webp`, `bilal-wordmark.webp`, solid `#193cff` background baked in). Convert to base64 and embed as `<img>` (do NOT redraw as SVG).
- **Branding markup (use EXACT classes + sizes so the logo is consistent across every site):**
  - Header: `<img class="nav-logo" src="data:image/webp;base64,...">` with CSS `.nav-logo { width:36px; height:36px; border-radius:10px; object-fit:contain; }`
  - Footer: `<img class="footer-logo" src="data:image/webp;base64,...">` with CSS `.footer-logo { height:40px; border-radius:8px; }`
  - The HTML `class` MUST match the CSS exactly (`.nav-logo` NOT `.logo-nav`). A mismatched class renders the image huge. After embedding, verify each `<img>` has a matching CSS rule with an explicit size.
- Filename: `digital-arts-foundations.html`.

## Visual design system — Dark Animated Theme (reuse exactly)
```css
:root {
  --primary: #193cff; --accent: #00d4aa; --bg: #0a0e27;
  --card: #111638; --card-hover: #1a2050; --text: #fff; --dim: #8892b0;
  --success: #00ff88; --danger: #ff4757; --warn: #ffd700;
}
```
Animated radial-gradient background + ~30 floating particles. Cards rounded (24px/16px), hover lift + glow border, top gradient bar. Fixed nav hidden until scroll, blurred pill-nav, lists all section titles, clickable jump. Font Cairo. Section number badges. Per-section accent variables cycling: cyan `#06B6D4`, amber `#F59E0B`, violet `#8B5CF6`, emerald `#10B981`, pink `#EC4899`, red `#EF4444`, repeat. Every section ends with a `⚠️ أخطاء شائعة` box. Granular scroll-reveal per block via one `IntersectionObserver` (threshold 0.05), `translateY(30px)→0`, `visible` class, `0.6s cubic-bezier(0.4,0,0.2,1)`. Keyboard arrow-nav. Legend boxes next to diagrams. Footer: both logos + encouraging line.

**This lesson is visual-heavy, not diagram-heavy** — most interactions are about shapes, color, layout, and image analysis rather than wired diagrams. Where illustrative shapes are needed, build them as clean inline SVG/CSS shapes (circles, squares, triangles, organic blob paths) directly, following the same "no native SVG `<text>`" rule for any labels.

**Global motion + interaction requirements (apply to every section):**
- **Replay button on every interactive animation** — each section's demo/simulation gets a small "↩️ إعادة" reset button to return it to its start state (needed when teaching the same lesson to multiple classes).
- **Section number badges** — each section header uses `<div class="section-number">01</div>` styled 50px circle, `font-weight:900; color:var(--bg)`, background = that section's accent, with the 3s glow loop.
- **Body text is a full self-contained explanation** per section (not slide-style bullets) — a student reading alone should understand the concept, even though the teacher narrates live.
- Every visual demo/fig diagram gets a **legend/key box** explaining what the shapes/colors mean.

## Language rules
`dir="rtl"`, UI in فصحى, explanations in Egyptian Arabic matching the source's warm, direct, teacher-narrating tone. English design terms (Gestalt, Composition, Focal Point, etc.) wrapped `<span dir="ltr">`, "الـ" prefix rule at line/heading/list/table-cell start.

## Mandatory SVG / interactivity rules (non-negotiable)
1. **Never use native SVG `<text>`** — every label/caption/number must be HTML overlaid on the graphic (positioned `<div>`/`<span>`) or `<foreignObject>`. No exceptions, not even single digits.
2. **One fixed, flippable arrow icon** — define one arrow SVG/path once; flip direction with `transform: scaleX(-1)` when a mirrored direction is needed. Never redraw arrows freehand.
3. **Fixed coordinate grid for diagrams** — any diagram built from primitives uses coordinates in multiples of 10, and every connection reuses the exact named coordinate value (fixes disconnected-wire bugs).
4. **Stable wiring** — every interactive element gets a unique `data-id`; ALL click handlers bind inside `DOMContentLoaded` (this is the direct fix for buttons that appear but do nothing).
5. **Checkpoint after each section** — before moving on, verify: no raw SVG `<text>`, all English terms wrapped/prefixed per bidi rule, every connection point matches its defined coordinate, and every button in the section is wired to working JS. Fix before proceeding.
6. **Staged build** — skeleton (nav + base CSS + color/type system, no section content) → one section at a time → final review pass (nav links, keyboard nav, replay buttons, overall bidi/RTL). Do NOT build the whole site in one pass.

## Quiz behavior
Hidden by default, revealed by click. Immediate color feedback (green/red) + short explanation. Skip button always available.

## Activity behavior — IMPORTANT
For both activities: present the full task/scenario up front, let students work through it themselves (in groups, as the source specifies), then a single "اعرض كل الإجابات" / "اعرض النموذج" button reveals the full model answer/solution at once. No per-item locking or immediate feedback for activities.

---

## Content

### [Hero] عنوان الوحدة
Badge: "Digital Arts Foundations". Gradient-text title. Subtitle inviting the student from "إيه هو الـ Digital Art؟" إلى "إزاي تصمم رمز يوصل إحساس من غير كلمة واحدة."

### [Intro] عالم الـ Digital Art (accent: cyan)
Based on Slides 1–4, 7. **Objective:** فهم إن الـ Digital Art هو أي عمل فني بيتعمل بأدوات رقمية (Tablet, Photoshop, Illustrator, Blender, Unity...)، إنه موجود في كل حاجة حوالينا (TikTok, Instagram, ألعاب, تطبيقات البنوك)، وإن فيه وظائف كتير مختلفة (Visual Designer, Illustrator, Animator, Game Artist, UI Designer, Motion Designer, 3D Artist) بس كلهم بيشتركوا في نفس الأساسيات.
- **Traditional vs Digital comparison** (use source's table): ورق وألوان مقابل Tablet وبرامج؛ تعديل صعب مقابل تعديل سهل (Undo/Layers)؛ نسخة واحدة مقابل نسخ لا نهائية.
- **Interaction:** a "before/after color swap" demo — a small illustration where clicking a color swatch instantly recolors it (illustrating the source's "لو العميل قال غير اللون من أزرق لأحمر" example — traditional art can't do this instantly, digital can).
- **Career grid:** 7 small icon cards (one per career from the source), each revealing its one-line description on click/hover.
- **Quiz:** none (this is the on-ramp section).

### Section 1 — الفن مقابل التصميم (Art vs Design) (accent: amber)
Based on Slide 6. **Objective:** الفرق الجوهري — Art هدفه التعبير عن المشاعر (مفتوح للتفسير، الفنان يحدد الهدف)، Design هدفه يحل مشكلة ويوصل رسالة واضحة (العميل يحدد الهدف، النجاح يعتمد على وصول الرسالة).
- **Example:** لوحة منظر طبيعي = Art. لوجو شركة = Design.
- **Interaction:** a two-image comparison slider/toggle — one labeled "Art" (abstract expressive shape) and one labeled "Design" (a clean functional icon like an exit sign), with the source's comparison table revealed alongside.
- **Quiz (1 question):** classify a new example (e.g. a warning sign vs a personal sketch) as Art or Design.

### Section 2 — عملية التصميم الأساسية (accent: violet)
Based on Slide 13. **Objective:** فهم إن أي Designer محترف بيمشي بخطوات: Research (فهم المشكلة وجمع Inspiration) → Explore (تجربة أفكار كتير من غير خوف من الغلط) → Sketch (تخطيط سريع قبل التنفيذ) → Refine (تحسين لحد أفضل نسخة).
- **Example:** تصميم إعلان موبايل جديد يمر بالأربع خطوات بالترتيب.
- **Interaction — reuse step-by-step reveal pattern (Next/Back + step counter):** 4 steps, each with its icon and the source's guiding questions (e.g. Refine step asks: هل العناصر متوازنة؟ هل أهم حاجة واضحة؟).
- **Quiz:** none.

### Section 3 — عناصر الفن: الخط، الشكل، القيمة، الملمس (accent: emerald)
Based on Slides 14–15. **Objective:** فهم إن أي تصميم مبني من عناصر خام: Line (خطوط أفقية=هدوء، رأسية=قوة، مائلة=حركة، منحنية=نعومة، متعرجة=توتر)، Shape (Geometric=نظام مقابل Organic=طبيعي)، Form (بعد ثالث بالظل والإضاءة)، Value (فاتح/غامق يعمل تباين وعمق)، Texture (الإحساس بالسطح)، وإن العناصر دي كلها بتشتغل مع بعض (Relationship).
- **Interaction 1 — line-type demo:** 5 clickable line samples (horizontal/vertical/diagonal/curved/zigzag), each revealing its one-word feeling on click, matching the source exactly.
- **Interaction 2 — shape/form toggle:** a flat square that, on click, gains shading/perspective and becomes a 3D-looking box — illustrating Shape→Form directly (matches the source's exact example).
- **Quiz (1 question):** match a line type to its feeling.

### Section 4 — مبادئ التصميم (accent: pink)
Based on Slides 16–18. **Objective:** فهم القواعد اللي بترتب العناصر: Balance (Symmetrical مقابل Asymmetrical)، Contrast (الاختلاف اللي يلفت النظر)، Emphasis (أهم عنصر تشوفه عينك الأول)، Movement (رحلة العين جوه التصميم)، Unity (كل العناصر تحس إنها من نفس العيلة)، Proportion (العلاقة بين الأحجام). ثم التوضيح المهم: Elements = مكونات، Principles = طريقة الترتيب.
- **Example (use source's exact combined example):** مثلث أسود كبير حواليه دوائر صغيرة فاتحة — العين تروح للمثلث بسبب Contrast + Proportion + Emphasis مع بعض.
- **Interaction:** an interactive canvas with one large dark triangle and several small light circles around it — toggles let the student turn Contrast/Proportion/Emphasis "on/off" individually (e.g. turning off Contrast makes the triangle the same shade as the circles) to see how the focal pull weakens without each principle.
- **Quiz (2 questions):** one on Balance types (Symmetrical vs Asymmetrical), one identifying which principle is at play in a given example.

### Section 5 — مبادئ Gestalt: إزاي المخ بيشوف الصورة (accent: red)
Based on Slide 19 + Proximity/Similarity + Continuation/Closure/Figure-Ground + examples gallery. **Objective:** فهم إن المخ بيحاول ينظم أي معلومات بصرية في مجموعات وأنماط، حتى لو العناصر منفصلة فعليًا. خمس مبادئ: Proximity (القريب من بعضه = مجموعة واحدة)، Similarity (المتشابه = مجموعة واحدة)، Continuation (العين بتكمل مسار الخط)، Closure (المخ بيكمل الأشكال الناقصة)، Figure-Ground (العلاقة بين الشكل والخلفية).
- **This section is the richest opportunity for genuine visual illusions — build these exactly:**
  - **Proximity demo:** a dot grid where dots are grouped in clusters by spacing — student sees them as separate groups despite being identical dots.
  - **Similarity demo:** a grid of dots, all same spacing, but colored in an alternating pattern — student sees color groups emerge.
  - **Closure demo:** a circle or triangle drawn with visible gaps in its outline — the brain still reads it as a complete shape.
  - **Figure-Ground demo:** the classic vase/two-faces illusion, built as clean geometric silhouette shapes (this is a great candidate for an SVG built from the standard fixed-coordinate/data-driven approach given its symmetry).
  - **Continuation demo:** a dotted S-curve path — the eye follows it as one continuous line.
- **Quiz (1 question):** identify which Gestalt principle a given visual example demonstrates.

### Section 6 — لغة الأشكال ومعناها النفسي (accent: cyan)
Based on Geometric vs Organic Shapes + Psychological Meaning of Shapes + Shape Language in Logos/Characters/Environments. **Objective:** فهم إن الأشكال الهندسية (دقيقة، منتظمة، Circles/Squares/Triangles) بتدي إحساس نظام وثبات، والأشكال العضوية (طبيعية، غير منتظمة، Blobs/Curves/Leaves) بتدي إحساس حياة ومرونة. وإن كل شكل أساسي له معنى نفسي: Circle (ناعم، آمن، ودود)، Square (ثابت، موثوق، جاد)، Triangle (طاقة، حدة، خطر/قوة). ونفس المنطق ده بيتكرر في تصميم الشعارات والشخصيات والبيئات.
- **Interaction:** three large shape cards (Circle/Square/Triangle); clicking each reveals its psychological associations (as a word cloud of the source's exact adjectives) and a real-world example (kids' app logo for Circle, bank logo for Square, sports/tech logo for Triangle).
- **Interaction 2 — character mood demo:** a simple character silhouette built from either all-circles or all-triangles, toggled by the student, showing how the same "character" reads as friendly vs dangerous purely from shape choice.
- **Quiz (1 question):** given a brand type (e.g. a children's toy company), pick which shape family fits its logo better.

### Section 7 — الرمزية البصرية والمشاعر (accent: amber)
Based on Visual Symbolism & Emotion. **Objective:** فهم إن الـ Symbol بيختصر فكرة كبيرة في شكل بسيط (زي ❤️ = حب)، وإن نفس الشكل ممكن يوصل مشاعر مختلفة تمامًا حسب السياق الكامل (اللون، الموقع، العناصر المحيطة، الحجم، التباين) مش الشكل لوحده.
- **Example (use exactly):** دائرة صغيرة لوحدها في زاوية الصفحة = وحدة؛ نفس الدائرة وسط دوائر كتير = انتماء.
- **Interaction:** a single circle the student can reposition (isolated in a corner vs. surrounded by other circles) and recolor (light vs dark) — a live caption updates describing the shifting emotional read ("وحدة" → "انتماء", "راحة" → "غموض").
- **Quiz:** none (this section sets up Activity 2 directly).

### Section 8 — التكوين وقيادة عين المشاهد (accent: violet)
Based on Composition/Focal Point/Visual Hierarchy + Rule of Thirds/Leading Lines/Negative Space + Depth/Visual Thinking/Squint Test/Strong Composition. **Objective:** فهم إزاي المصمم بيتحكم في رحلة عين المشاهد: Composition (ترتيب العناصر) يخلق Focal Point (أهم نقطة) ويبني Visual Hierarchy (Primary → Secondary → Supporting). أدوات عملية: Rule of Thirds (شبكة 9 أجزاء، نقاط التقاطع قوية بصريًا)، Leading Lines (خطوط بتوجه العين)، Negative Space (الفراغ عنصر تصميم مش مجرد فراغ). وأخيرًا Depth (Foreground/Midground/Background) والـ Squint Test (تضييق العين لاختبار الـ Hierarchy).
- **Interaction 1 — Rule of Thirds overlay:** an illustrative scene (e.g. a simple landscape) with a toggle-able 3×3 grid overlay; moving the "subject" element to a grid intersection point visibly feels more balanced than centering it.
- **Interaction 2 — Weak vs Strong Hierarchy toggle:** the same poster mockup (title/subtitle/body text) shown two ways — all same size (weak) vs. sized by importance (strong) — student toggles between them and immediately sees the difference.
- **Interaction 3 — Depth layers:** a simple scene with 3 toggle-able layers (Foreground/Midground/Background), each layer's visibility can be switched off to show how depth collapses without it.
- **Note the source's key caveat explicitly:** "Guidelines, not rules" — Rule of Thirds, Leading Lines, and Negative Space are tools, not laws; sometimes breaking them (dead-center composition) is the right call.
- **Quiz (2 questions):** one on Rule of Thirds purpose, one identifying Foreground/Midground/Background in a given description.

---

### [Activity 1] المحقق البصري (Visual Detective Challenge) (accent: emerald, dashed activity-card style)
Based on the source's exact 3 visuals and model solution. Present group roles first (Observer / Writer / Speaker, one line each), then the 3 visual examples as description cards (since actual images aren't available, describe each vividly per the source so students can discuss the same scene): 
- **Visual A:** علبة مشروب طاقة VERDE ENERGY، ألوان خضراء قوية، أوراق نبات، أسهم للأمام، إضاءة قوية حول المنتج.
- **Visual B:** طفل شايل Lantern في غابة ليلية، قمر كبير، قلعة بعيدة، طريق بيقود للقلعة.
- **Visual C:** بوابة ضخمة وسلم طويل، شخصية صغيرة ماشية نحو المدخل، جبال وصخور ضخمة.

For each, students answer 4 fields: Art/Design/Both — 2 Visual Elements — 1 Design Principle — Message/Emotion. A single "اعرض النموذج الكامل" button reveals the source's exact model answers for all 3 (Visual A: Design, Color+Shape, Emphasis, "طاقة طبيعية ونضارة"; Visual B: Art, Value+Color, Contrast, "مغامرة وغموض"; Visual C: Art, Space+Shape, Scale, "عظمة واستكشاف").

### [Activity 2] تحدي رموز المشاعر الثلاثة (Three Emotion Symbols Challenge) (accent: pink, dashed activity-card style)
Based on the source's exact activity. Present the task: كل مجموعة (4-5 طلاب) تختار 3 مشاعر مختلفة (مثال: Calm, Energy, Fear) وتصمم رمز بسيط تجريدي (Abstract) لكل واحد، باستخدام أشكال وخطوط ومسافات بس — من غير أي كلمات جوه الرمز. Include the source's **Shape Bank + Emotion Guide** as a reference panel: Circle→Calm/Joy, Square→Stability/Confidence, Triangle/Zigzag→Energy/Tension/Fear; Straight lines→نظام وقوة, Curved lines→راحة وهدوء, Zigzag lines→توتر وخطر. Include the **suggested time plan** as a small timeline (5 min اختيار المشاعر → 10–15 min بناء الرموز → 5 min تحسين → 3 min تجهيز الشرح).

Give students an interactive mini-canvas: a palette of basic shapes/lines (draggable or click-to-place) they can arrange to build their own symbol live on screen, matching the "use only shapes/lines/size/spacing/negative space, no words" constraint.

A single "اعرض نموذج كامل" button reveals the source's exact model solution: Calm → دائرة كبيرة في المنتصف مع دوائر صغيرة حولها. Energy → مثلثات وخطوط Zigzag خارجة للخارج. Fear → شكل صغير محاصر بين مثلثات حادة متجهة نحوه — each with its "why" reasoning from the source.

---

### [Closing] كل حاجة اتعلمناها في جملة واحدة
Use a summary visual connecting the full chain: Elements (Line, Shape, Form, Value, Texture) → Principles (Balance, Contrast, Emphasis, Movement, Unity, Proportion) → Gestalt (إزاي المخ بيجمعهم) → Shape Psychology & Symbolism (المعنى) → Composition (الترتيب النهائي اللي يوجه عين المشاهد). Closing line: "التصميم الناجح مش مجرد عناصر جميلة — هو عناصر مرتبة صح، بتوصل إحساس، من غير ما تحتاج كلمة واحدة."

---
Build in the staged order above. Run the mandatory checkpoint after every section before moving to the next one.
