# Master Prompt: Interactive HTML Explainer — The Creative Process: From References to Final Presentation

## Role
Build a single self-contained HTML file for a teacher (Bilal) to present a full Digital Arts creative-process unit — from gathering references, through ideation, feedback, and iteration, to final production and presenting an Artist Statement — to students aged 12–17, on a laptop connected to a projector. This is a long, narrative, project-based unit: build it as one continuous journey, not disconnected topics.

## Hard requirements — deliverable format
- ONE `.html` file. All CSS/JS inline. Google Fonts link only external dependency.
- Two logo images provided separately (`bilal-icon.webp`, `bilal-wordmark.webp`, solid `#193cff` background baked in). Convert to base64, embed as `<img>` inside a small rounded badge.
- Filename: `creative-process-references-to-presentation.html`.

## Visual design system — Dark Animated Theme (reuse exactly)
```css
:root {
  --primary: #193cff; --accent: #00d4aa; --bg: #0a0e27;
  --card: #111638; --card-hover: #1a2050; --text: #fff; --dim: #8892b0;
  --success: #00ff88; --danger: #ff4757; --warn: #ffd700;
}
```
Animated radial-gradient background + ~30 floating particles. Cards rounded (24px/16px), hover lift + glow border, top gradient bar. Fixed nav hidden until scroll, blurred pill-nav, lists all section titles, clickable jump. Font Cairo. Section number badges. Per-section accent variables cycling: cyan `#06B6D4`, amber `#F59E0B`, violet `#8B5CF6`, emerald `#10B981`, pink `#EC4899`, red `#EF4444`, repeat. Every section ends with a `⚠️ أخطاء شائعة` box. Granular scroll-reveal per block via one `IntersectionObserver` (threshold 0.05), `translateY(30px)→0`, `visible` class, `0.6s cubic-bezier(0.4,0,0.2,1)`. Keyboard arrow-nav. Legend boxes next to diagrams. Footer: both logos + encouraging line.

## A unifying feature — the "My Project" tracker (build this once, reuse everywhere)
This lesson's source material reuses the SAME project fields repeatedly at every stage (Theme, Main Character, Environment/Place, Mood, Colors, Important Objects, Story). Implement ONE persistent, small collapsible "مشروعي" panel (fixed corner or top-accessible) where the student fills these fields once early on (Section 2/3) and the panel stays accessible throughout the whole page — later sections (Inspiration Map, Three Concepts, Peer Critique, Final Production, Artist Statement) reference back to it, reinforcing that this is one continuous project, not separate exercises. Use `localStorage` so it persists across a session (this file will be hosted standalone, not as a Claude artifact, so localStorage is fine).

## Language rules
`dir="rtl"`, UI in فصحى, explanations in Egyptian Arabic matching the source's warm, direct, teacher-narrating tone. English terms (Mood Board, Thumbnail, Iteration, etc.) wrapped `<span dir="ltr">`, "الـ" prefix rule at line/heading/list/table-cell start.

## Mandatory SVG / interactivity rules
No native SVG `<text>` (self-check via grep before finishing each section). Any diagram with 4+ connections built from a JS data lookup, never hand-typed coordinates. Stable `data-id` + `DOMContentLoaded` binding. Checkpoint after each section. Staged build: skeleton → each section → final review.

## Quiz behavior
Hidden by default, revealed by click. Immediate color feedback (green/red) + short explanation. Skip button always available.

## Activity behavior — IMPORTANT
For the 3 major labeled Activities (Inspiration Map Challenge, Peer Critique & Improve, Final Presentation Prep): present the full task/template up front, let students work through it (filling their own "My Project" fields where relevant), then a single "اعرض النموذج" button reveals the source's model example. No per-item locking or immediate feedback for activities.

---

## Content

### [Hero] عنوان الرحلة
Badge: "The Creative Process". Gradient-text title. Subtitle: "من أول صورة Reference لحد ما تقف تشرح مشروعك — رحلة كل مصمم محترف."

### [Intro] ليه بنستخدم References، وإزاي نجمعها أخلاقيًا (accent: cyan)
Based on "Why Artists Use References" + "Reference Gathering Techniques" + "Ethical Use of References". **Objective:** الـ Reference مش غش — هو أداة تعلم أساسية بيستخدمها كل الفنانين المحترفين، بتخليهم يفهموا قبل ما يرسموا ويزودوا الدقة. بندرس بيها 5 حاجات: Light, Color, Shapes, Texture, Composition. نوعين رئيسيين: Subject References (الحاجة نفسها من زوايا مختلفة) وStyle References (طريقة الرسم/الإحساس). الاستخدام الأخلاقي: **Safe** = Study, Combine, Transform, Credit Sources, Create Your Own. **Risky** = Tracing, Copying, Removing Credit, Claiming Another Artist's Idea.
- **Interaction:** a "Safe vs Risky" sorting card game — 5 behaviors the student drags/clicks into the correct column, with the source's exact examples.
- **Quiz (1 question):** distinguish Subject Reference from Style Reference in a given scenario.

### Section 1 — الـ Mood Board: تجميع كل حاجة في مكان واحد (accent: amber)
Based on "Mood Boards" + Mini Activity "Reference Board Builder". **Objective:** الـ Mood Board لوحة بنجمع فيها كل مراجع المشروع (صور، ألوان، ملاحظات) في مكان واحد بدل ما تكون متفرقة، عشان ناخد قرارات أسرع.
- **This is where the "My Project" tracker panel gets introduced and first filled in** (fields from the source's exact template: Project Title, Project Theme, Main Character, Environment/Place, Mood, Color Palette (3-5 colors), Important Objects, Story Idea).
- **Interaction — reuse the mini-activity structure:** student picks one Theme (from the source's list: Calm Forest, Futuristic City, Cozy Room, Mystery Cave, Heroic Journey — or types their own), then builds a 5-reference board by choosing one example each for Subject, Place, Mood, Colors, Texture, writing one sentence explaining each choice (matching the source's exact "اخترنا الصورة دي علشان..." pattern).
- **Quiz:** none (the board-building activity is the reinforcement).

### Section 2 — مصادر الإلهام وتحليل المراجع بعين مصمم (accent: violet)
Based on "Finding Inspiration" + "Analyze Visual References". **Objective:** 4 مصادر إلهام: Everyday Life (المدرسة، الشارع، الحيوانات)، Digital Culture (ألعاب، تطبيقات، سوشيال ميديا)، Professional Art (تعلم مش تقليد)، Personal Interests. ثم إزاي نحلل صورة بعين مصمم: Focal Point (أول حاجة العين تروحلها)، Colors Create the Mood، Light Source، Repeated Shapes، Composition.
- **Interaction:** a "read this image like a designer" exercise — an illustrative scene the student clicks through 5 guided questions (matching the source's exact classroom exercise: أول حاجة شوفتها؟ اللون الأساسي إيه؟ النور جاي منين؟ فيه أشكال متكررة؟ عينك مشت إزاي؟), each revealing the designer's-eye answer.
- **Quiz (1 question):** identify which inspiration source a given example belongs to.

### Section 3 — الموضوع، الإحساس، والرسالة (Theme, Mood & Message) (accent: emerald)
Based on "Themes & Moods". **Objective:** أي تصميم ناجح بيجاوب على 4 أسئلة: Theme (بيتكلم عن إيه؟)، Mood (عايز المشاهد يحس بإيه؟)، Message (إيه الرسالة؟)، Audience (مين الجمهور؟). الإحساس بيطلع من Visual Clues مجتمعة: الألوان، الإضاءة، الأشكال، الخامات، التكوين.
- **Interaction:** student picks a Theme (from their own "My Project" panel) and a Mood, then sees a live-adjusting mockup card whose colors/lighting-tone shift to match the chosen mood, reinforcing that the same theme can carry different moods.
- **Quiz (1 question):** given an audience (e.g. "طفل صغير"), pick the design choices that fit.

### [Activity 1] تحدي خريطة الإلهام (Inspiration Map Challenge) (accent: pink, dashed activity-card style)
Based on "Activity 1: Inspiration Map Challenge" + "Activity 1 Checklist". Teams of 3 (roles: Idea Leader, Reference Thinker, Presenter), 20-25 minutes. Present the exact mind-map structure: a center circle with the Theme, and 6 branches — Character, Place, Mood, Colors, Objects, Story. Student fills these branches (auto-populated from their "My Project" panel where possible, editable). Then: **Generate Three Concepts** — 3 different directions for the same theme (source's example: Space Adventure → Astronaut on Mars / Robot City / Alien Jungle). Provide the **checklist as an interactive checklist**: ✓ Clear Theme · ✓ Mood Clues (كل العناصر بتدي نفس الإحساس) · ✓ Three Concepts (جربت أكتر من فكرة فعلاً) · ✓ Original Mix (مزيج جديد، مش نسخ). A single "اعرض النموذج" button reveals the source's Space Adventure example in full.

### Section 4 — توليد الأفكار: عصف ذهني وخرائط ذهنية (accent: red)
Based on "Brainstorming Methods" + "Mind Mapping" + "Generate Multiple Ideas". **Objective:** Brainstorming: Quantity First (اكتب أي فكرة الأول)، Combine Ideas (Robot+Jungle)، Ask "What If?" (What if the city was underwater?). Mind Mapping: فكرة في النص، فروع حواليها (Setting/Mood/Character/Color/Objects/Story)، رموز سريعة بدل جمل. توليد أفكار متعددة بمنطق **Safe / Creative / Bold**: Idea 1 (سهلة وواضحة) → Idea 2 (غيّر حاجة كبيرة زي Mood أو Setting) → Idea 3 (فكرة جريئة، زاوية كاميرا مختلفة أو حجم غير متوقع).
- **Interaction:** a "What If?" generator — student picks two random elements from two lists (the source's exact combos: Robot/Jungle/Pirate/Space/Castle/Cyberpunk...) and the site combines them into a new prompt live; separately, a Safe/Creative/Bold 3-card ladder using the source's Robot Cafe example (روبوت بيقدم قهوة → كافيه في الفضاء → مدينة كاملة كلها روبوتات بتخدم البشر).
- **Quiz:** none (generative, not fact-recall).

### Section 5 — من الفكرة للـ Thumbnail: التجربة والتكرار (accent: cyan)
Based on Mini Practice "Three Concepts" + "Quick Discussion" + "Thumbnail Sketches" + "Iteration Improves the Work". **Objective:** Thumbnail Sketches = رسمات صغيرة سريعة (مش جميلة، الهدف التفكير مش الإنتاج)، نجرب فيها أماكن مختلفة لـ Focal Point وFore/Mid/Background قبل ما نختار. قبل ما نلتزم بفكرة، 3 أسئلة: Clear Message؟ Strong Mood؟ Possible to Finish (وقت/أدوات/مهارات متاحة)؟ ثم Iteration بـ 3 مراحل: **Step 1 Rough Idea** (أشكال كبيرة بس) → **Step 2 Better Design** (ترتيب، إضاءة، ألوان) → **Step 3 Final Polish** (حواف وتفاصيل وجودة العرض).
- **Interaction — reuse step-by-step reveal pattern:** the 3 Iteration steps shown as an evolving single illustration that gets progressively more refined at each step (rough blocks → arranged composition → polished details), Next/Back navigation.
- **Quiz (1 question):** given a described sketch, judge whether it passes the "Possible to Finish" check.

### Section 6 — إعطاء واستقبال الـ Feedback (accent: amber)
Based on "Giving Constructive Feedback" + "Receiving Feedback" + "Explain Artistic Decisions". **Objective — Giving:** Start Positive (ابدأ بحاجة كويسة) → Be Specific ("العنوان صغير ومش باين" مش "مش حلو") → Suggest Next Step (اقترح حل، مش بس مشكلة). **Objective — Receiving:** Feedback مش هجوم شخصي؛ Listen First (متقاطعش)؛ Ask Questions لو مش واضح؛ Write Down Repeated Comments (لو أكتر من واحد قال نفس الحاجة، دي إشارة مهمة)؛ Choose Useful Feedback (مش كل اقتراح لازم يتنفذ — إنت صاحب القرار). **Explaining decisions:** لما تعرض شغلك، اشرح Theme (ليه اخترت الموضوع)، Process (References/Mood Board/Thumbnails/Iterations)، Decision (ليه الألوان دي، ليه المكان ده).
- **Interaction:** a "write feedback" mini-tool — student picks from example weak feedback ("مش حلو") vs sees it transformed into the Start Positive → Be Specific → Suggest Next Step structure live, using the source's exact examples.
- **Quiz (1 question):** identify which of the 3 giving-feedback steps is missing from a given (weak) feedback example.

### [Activity 2] تحدي المراجعة الجماعية (Peer Critique & Improve) (accent: violet, dashed activity-card style)
Based on "Activity 2: Peer Critique & Improve". Groups of 4 with roles: Artist, Feedback Speaker, Note Taker, Time Keeper. Structure: **One Strength** → **One Question** (not criticism — opens thinking, e.g. "ليه اخترت تخلي الشخصية صغيرة جدًا؟") → **One Suggestion** (single, actionable) → **Artist Writes One Improvement**. Build this as a 4-step guided form the student fills in for their own work (or a partner's), reusing the "My Project" panel for context. A single "اعرض نموذج" button shows the source's exact example flow (Strength: "اختيار الألوان ممتاز" → Question → Suggestion: "جرّب تزود التباين حوالين العنصر الرئيسي").

### Section 7 — من الخطة للتنفيذ النهائي (accent: emerald)
Based on "Final Project Production" + "Refine Your Artwork" + "Apply Feedback Wisely". **Objective:** حوّل الخطة لشغل كامل، ابني على المواد اللي جهزتها (متبدأش من الصفر)، ابدأ بالأشكال الكبيرة قبل التفاصيل، طبّق كل حاجة اتعلمتها (Perspective, Light, Shadow, Color, Focal Point, Hierarchy)، واحفظ نسخ مختلفة (v1, v2, v3). **Refinement** مش معناه تفاصيل أكتر — معناه: **Fix First** (المشاكل الأساسية زي وضوح العنصر الرئيسي والتباين) قبل **Polish Last** (الحواف والتفاصيل الصغيرة). **تطبيق الفيدباك بذكاء:** قارن كل تعليق بهدفك، ابدأ بالمشاكل المتكررة، جرّب تعديل واحد في المرة، واحتفظ بنسخة قبل أي تعديل كبير.
- **Interaction:** a "Fix First vs Polish Last" before/after — two versions of a mockup card (one with a clear/high-contrast focal point but no fine details, one with lots of fine details but a weak focal point) — student picks which one is closer to "done right", reinforcing the Fix-First-Polish-Last order regardless of detail level.
- **Quiz:** none.

### [Activity 3] بيان الفنان والتحضير للعرض النهائي (Artist Statement & Presentation Prep) (accent: red, dashed activity-card style)
Based on "Artist Statement" + Mini Activity "Final Presentation Prep". Present the Artist Statement's 5-part framework: **Theme** (بيتكلم عن إيه؟) → **Process** (References، Thumbnails، إزاي الفيدباك ساعد) → **Decisions** (ليه اللون/الإضاءة/المكان ده) → **Challenge** (أصعب حاجة قابلتك وإزاي تعاملت معاها) → **Reflection** (لو عندك وقت أكتر كنت هتعمل إيه). Build this as a guided writing tool: 5 short text fields, each pre-filled with a hint pulled from the "My Project" panel plus the source's example phrasing style. Then the Presentation Prep checklist: اختار عنوان واضح وسهل التذكر → اكتب Artist Statement في 3 جمل بس → جهّز موادك (Mood Board, أفضل Thumbnail, الشغل النهائي, تعديل بسبب Feedback) → اتدرب تشرح أهم قرار تصميم. A single "اعرض المثال" button reveals the source's example artist statement line ("استخدمت ألوان باردة وإضاءة هادئة علشان أوصل إحساس بالوحدة والغموض").

---

### [Closing] الرحلة الكاملة: من صورة واحدة لعرض متكامل
Visual: vertical step diagram summarizing the full journey: References → Mood Board → Inspiration & Analysis → Theme & Mood → Inspiration Map (3 Concepts) → Brainstorming & Iteration → Thumbnails → Feedback (Give & Receive) → Peer Critique → Final Production → Refinement → Artist Statement → العرض النهائي. If the "My Project" panel has been filled in, show a final summary card pulling together everything the student entered across the whole lesson as their finished project brief.

---
Build in the staged order above. Run the mandatory checkpoint after every section before moving to the next one.
