# Master Prompt: Interactive HTML Explainer — Cybersecurity Foundations

## Role
Build a single self-contained HTML file for a CS teacher (Bilal) to present a full Cybersecurity foundations unit (7 topics + 2 activities) to students aged 12–17, on a laptop connected to a projector. This is a long, comprehensive unit — build it as one file, warn nobody, just build it well and let students navigate via the sticky nav.

## Hard requirements — deliverable format
- ONE `.html` file. All CSS/JS inline. Google Fonts link only external dependency.
- Two logo images provided separately (`bilal-icon.webp`, `bilal-wordmark.webp`, solid `#193cff` background baked in). Convert to base64, embed as `<img>` inside a small rounded badge.
- Filename: `cybersecurity-foundations.html`.

## Visual design system — Dark Animated Theme (reuse exactly)
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
- Animated radial gradient background + ~30 floating particles (slow upward loop, primary color, low opacity).
- Cards: `background: var(--card)`, rounded (`24px`/`16px`), hover lift + glow border, top gradient bar.
- Fixed nav (hidden until scroll, `backdrop-filter: blur(20px)`), pill-shaped links, lists every section title, clickable jump.
- Font: Cairo. Section number badges (circular, gradient fill from section's accent color).
- Code panels (if any) forced `dir="ltr"` + `unicode-bidi: isolate`.
- Every section ends with a `⚠️ أخطاء شائعة` common-mistakes box (`border: 1px solid rgba(255,71,87,.2); background: rgba(255,71,87,.05)`).
- Granular scroll-reveal on every individual block via one `IntersectionObserver` (threshold 0.05), `opacity:0; translateY(30px)` → class `visible` → `opacity:1; translateY(0)`, `0.6s cubic-bezier(0.4,0,0.2,1)`.
- Keyboard arrow-key navigation. Legend/key box next to any diagram. Footer: both logos + encouraging sentence.

## Per-section accent colors — stable variables, assign once (the following --s vars replaced exactly)
```css
--s1: #06B6D4;  /* cyan   — Section 1 */
--s2: #F59E0B;  /* amber  — Section 2 */
--s3: #8B5CF6;  /* violet — Section 3 */
--s4: #10B981;  /* emerald— Section 4 */
--s5: #EC4899;  /* pink   — Section 5 */
--s6: #EF4444;  /* red    — Section 6 */
--s7: #00d4aa;  /* accent — Activity 1 */
--s8: #06B6D4;  /* cyan   — Section 7 */
--s9: #8B5CF6;  /* violet — Activity 2 */
```
Apply each section's variable to its number badge (gradient `--sX → var(--accent)`), its top gradient bar, and its interactive elements. Do not re-declare hex per section inline.

## Activity cards — dashed outline spec (mandatory for both activities)
```css
.activity-card {
  background: var(--card);
  border: 2px dashed rgba(255,255,255,.25);
  border-radius: 24px;
  overflow: hidden;
}
.activity-card .activity-header {
  background: rgba(255,255,255,.04);
  padding: 14px 20px;
  font-weight: 900;
  color: var(--text);
}
```
Use `.activity-card` (not plain `.card`) for `[Activity 1]` and `[Activity 2]` so they read as worksheet-style vs regular lesson sections.

## Language rules
`dir="rtl"`, UI in فصحى, explanations in Egyptian Arabic (translate/adapt the source English content into Egyptian Arabic with the same warm, direct, example-driven tone used in Bilal's other lessons), English technical terms (Cybersecurity, Confidentiality, Authentication, etc.) in English wrapped in `<span dir="ltr">`, with "الـ" prefix when starting a line/heading/list item/table cell. Full detailed explanation per section, broken into scroll-reveal chunks, not slide bullets.

## Mandatory SVG / interactivity rules
1. Never use native SVG `<text>` — all writing via HTML/`foreignObject`, no exceptions even for short English labels. Mandatory self-check: grep the finished file for literal `<text` before considering any section done.
2. One fixed, flippable arrow icon (`transform:scaleX(-1)`), never redrawn per instance.
3. Any diagram with more than ~4 connections: build wires from a JS data lookup (signal name → `{x,y}`), never hand-typed coordinates. Verify programmatically that every wire's endpoints resolve to real defined ports.
4. Every interactive element has a stable `data-id`; JS binds after `DOMContentLoaded`. Do not use inline `onclick=` — all handlers attach via `.addEventListener` after DOM ready.
5. **Every interactive animation/simulation/toggle/flip has a replay/reset button** that returns that element to its start state (Bilal presents the same lesson to multiple classes per day). This is mandatory on all interactions below.
6. Checkpoint after each section: bidi correctness, wiring correctness, working buttons + reset, — before moving on.
7. Staged build: skeleton+CSS → each section individually with checkpoint → final review pass.

## Quiz behavior
Hidden by default, revealed by click. Immediate color feedback (green/red) + short sentence explaining why wrong. Always a skip button.

---

## Content

### [Hero] عنوان الوحدة
Badge: "Cybersecurity Foundations". Title with gradient text. Subtitle inviting the student into the world of digital protection — from understanding the digital world we live in, to choosing a career track in the field.

### Section 1 — العالم الرقمي وأصوله الرقمية (accent: --s1 cyan)
Based on Topic 1. **Objective:** الطالب يفهم إن العالم بيتحول رقميًا بسرعة (Digital Transformation)، وإن الأجهزة بقت متصلة ببعض (Connected Systems)، وإن ليه كل واحد فينا "أصول رقمية" (Digital Assets) لازم تتحمي، وإن فيه فرق بين البيانات الشخصية والبيانات المؤسسية.
- **Examples:** المدارس (من السبورة الطباشير لـ Google Classroom)، البنوك (من الشباك لتطبيق الموبايل)، التسوق (من المحل لأمازون)، الرعاية الصحية (من الورق للسجلات الرقمية).
- **Interaction — flip toggle cards:** grid of 4 cards (school/bank/shopping/healthcare). Click a card to flip between its front (old manual way) and back (new digital way); card flips via `scaleX(-1)` around the Y axis — click again flips back. Reuse the single flip arrow/mechanism, do not re-embed/ redraw per card.
- **Asset-sorting interaction:** grid of example items (photos, social media account, game items, cryptocurrency, documents) the student clicks to drop into one of three drop-zones: Personal / Business / Gaming. Correct drop highlights green, wrong red, with a one-line explanation.
- **Quiz (1 question):** identify whether a given example is Personal Data or Organizational Data.

### Section 2 — إيه هو الـ Cybersecurity (accent: --s2 amber)
Based on Topic 2. **Objective:** تعريف الـ Cybersecurity، وفهم الأهداف الثلاثة الأساسية (Confidentiality/Integrity/Availability — مقدمة سريعة هنا، التفصيل الكامل في section 4)، وإن الحماية محتاجة ناس + Processes + Technology مع بعض، والفرق بين Cybersecurity وInformation Security.
- **Example:** حد بيحاول يسرق حساب ألعابك — الـ cybersecurity بتحميك بكلمة سر قوية، Two-Factor Authentication، مراقبة محاولات الدخول الغريبة.
- **Interaction: "three-legged stool" — People / Process / Technology** as three legs; click "remove" next to any one leg and the stool (security) collapses with an animation, along with the source's bank example (missing training → phishing victim; missing process → anyone can access data; missing technology → firewall behind). Has a reset button to restore all three legs.
- **Quiz (1 question):** Cybersecurity vs Information Security — which is broader?

### Section 3 — ليه الـ Cybersecurity مهم جدًا (accent: --s3 violet)
Based on Topic 3. **Objective:** فهم التأثير الحقيقي: مادي (Financial)، خصوصية (Privacy)، استمرارية الأعمال (Business Continuity)، أمن قومي (National Security).
- **Real incident case-study flip cards** (exact real incidents from the source): **Colonial Pipeline (2021)** — هجوم Ransomware أوقف خط أنابيب وقود رئيسي، الشركة دفعت 4.4 مليون دولار، محطات بنزين فضلت من غير وقود. **Yahoo (2013-2014)** — 3 مليار حساب اتسرق، ثاني أكبر اختراق في التاريخ. **WannaCry (2017)** — انتشر في أكتر من 200 دولة، عطّل مستشفيات وأوقف عمليات جراحية، خسائر بأكتر من 10 مليار دولار.
- **Interaction — flip cards:** front = name + year + icon; back = what happened + real-world cost/impact. Flip with `scaleX(-1)` (same flip transform as Section 1). Reset button clears all flips to front.
- **Quiz (1 question):** match an incident to its type of impact (financial/privacy/business continuity/national security).

### Section 4 — مثلث الـ CIA بالتفصيل (accent: --s4 emerald)
Based on Topic 4 (deepens CIA intro from Section 2). **Objective:** فهم عميق للثلاثة مبادئ: Confidentiality (السرية)، Integrity (الدقة)، Availability (التوافر) — وإزاي فشل أي واحد فيهم بيأثر بشكل مختلف.
- **Examples (exact real scenarios from the source):** التزام الـ Confidentiality — ثغرة في سرقة سجلات طبية وكشوف حالة صحية نفسية، الجهة تميز ضده. Failure الـ Integrity — ثغرة بتغيير جرعة الثورة من 50mg لـ 500mg في نظام مستشفى، المريض بياخد جرعة زايدة. Failure الـ Availability — هجوم DDoS بيوقف موقع، العملاء مايقدروش يتوصلوا للدروس.
- **Interaction — "What if this principle fails?" — tabbed simulator (reuse the tab pattern):** three tabs (Confidentiality / Integrity / Availability); clicking one shows the corresponding failure scenario animated (e.g. Integrity tab shows 50mg→500mg change animating on a prescription card with a "⚠️ خطر" flash). Include the "three-legged stool" baseline (bank example: lose any one and customers leave). Reset restores the default tab.
- **Quiz (3 questions):** one per principle, matching a scenario to Confidentiality/Integrity/Availability.

### Section 5 — من أنت؟ وإيه مسموع لك؟ (Authentication, Authorization, Accountability, Non-Repudiation) (accent: --s5 pink)
Based on Topic 5. **Objective:** فهم 4 مبادئ إضافية بيشتغلوا مع الـ CIA Triad: Authentication ("أنت مين؟")، Authorization ("مسموعلك تعمل إيه؟")، Accountability ("عملت إيه؟")، Non-Repudiation ("تقدر تنكر عملتها؟").
- **Central interaction — step-by-step bank transfer walkthrough** (reuse the step-by-step reveal pattern, Next/Back with a step counter): Step 1 Authentication (expand idari + بصر, النظام يتأكد "أنت Sarah Johnson") → Step 2 Authorization (النظام يتأكد اللي مسموع — تحويل لغاية 10,000 جنيه، قد ما به توصل لحسابات تانية) → Step 3 Accountability (النظام يسجل من حوّل، كام، وإمتى) → Step 4 Non-Repudiation (التحويل موقّع رقميًا، مايقدرش يقول "أنا ماعملتش كده"). Reset/Back to step 1.
- **Password strength mini-interaction:** input-style comparison --- weak examples ("password123", "12345678") vs strong ("BlueMountain$Guitar42"), with a live strength bar (low/ok/strong) that re-colors as the teacher shows different inputs.
- **Quiz (1 question):** given a scenario, identify which of the 4 concepts it represents.

### Section 6 — الأصول وسطح الهجوم (accent: --s6 red)
Based on Topic 6. **Objective:** فهم إن الـ Asset هو أي حاجة قيمة متحاجة protection (5 أنواع: Information, Technology, People, Reputation, Physical)، وإن الـ Attack Surface هي كل نقاط الدخول المحتملة، وإن الـ Digital Footprint هو أثرك الرقمي كله.
- **Example:** تشبيه البيت بأبواب وشبابيك كتير (attack surface كبير) مقابل بيت بباب واحد بس (attack surface صغير).
- **Interaction — house diagram:** multiple "entry points" (door, windows, garage) the student clicks to toggle open/closed — each closed entry point visually shrinks a highlighted "attack surface", reinforcing that fewer entry points = smaller surface. Reset reopens default.
- **Quiz (1 question):** classify an example asset into one of the 5 types.

### [Activity 1] خريطة أمانك الرقمي (My Digital Security Map) (accent: --s7, dashed activity-card)
Based on Topic 6's activity. **Interactive personal tool** (the standout feature): a live-editable 5-column table (Digital Asset / Asset Type dropdown / Personal Data Yes-No / Attack Surface text / Digital Footprint text) where the student adds their own rows (button: "+ ضيف أصل رقمي"), pre-seeded with 2 example rows from the source (Phone photos, Social media account). After at least 3 rows are added, reveal a follow-up mini-section: pick your top asset and take it to a CIA principle dropdown, then write one protection action. Mirrors the source's 7-step worksheet.
- **Quiz:** none (the activity is the assessment).

### Section 7 — مسارات المهن في الأمن السيبراني (accent: --s8 cyan)
Based on Topic 7. **Objective:** فهم إن الـ Cybersecurity مش وظيفة واحدة — فيه 8 مسارات مختلفة (SOC Analyst, Incident Response, Threat Intelligence, Penetration Testing, Digital Forensics, AppSec, Cloud Security, GRC), كل واحد بشخصية شغل مختلفة.
- **Interaction — tabbed pattern (reuse proven tab bar):** 8 pill tabs, one per career track; each panel shows what they do (one line), a condensed "day in the life" timeline (3–4 key moments from the source's daily schedules), and a compact "مناسب لو بتحب... / مش مناسب لو..." two-column mini-list.
- **Quiz (1 question):** match a short "what they do" description to the correct career track (from the source's comparison table).

### [Activity 2] دور على مسارك المهني (Find Your Cyber Career Track) (accent: --s9, dashed)
Based on Topic 7's activity. **Interaction:** present the 8 source scenarios one at a time; student clicks which of the 8 tracks matches each scenario; immediate feedback per match (green/red + the source's key word explanation, e.g. "الكلمة المفتاحية: Monitors — ده شغل SOC Analyst"). After all 8 matched, reveal a short reflective prompt: "نهي مسارين عجبتك أكتر، وليه؟" (open text, no grading) — matching the source's second part.
- **Quiz:** the matching game itself is the test.

---

### [Closing] رحلة الأمن السيبراني الكاملة
Visual: a vertical step diagram summarizing the full journey: العالم الرقمي → إيه هو الـ Cybersecurity → ليه مهم → CIA Triad → Authentication/Authorization/Accountability/Non-Repudiation → الأصول وسطح الهجوم → خريطتك الشخصية → مسارات المهن → مسارك انت. Each step lights up in order on scroll/commit.

---
Build in the staged order specified above. Run the mandatory checkpoint after every section before moving to the next.