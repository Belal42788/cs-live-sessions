# Master Prompt: Interactive HTML Explainer — Threats, Attacks & Threat Actors

## Role
Build a single self-contained HTML file for a CS teacher (Bilal) to present a Cybersecurity lesson on Threats/Vulnerabilities/Risks/Attacks, Threat Actors, the Attack Lifecycle, Social Engineering, Malware, and Network Attacks, to students aged 12–17, on a laptop connected to a projector.

## Hard requirements — deliverable format
- ONE `.html` file. All CSS/JS inline. Google Fonts link only external dependency.
- Two logo images provided separately (`bilal-icon.webp`, `bilal-wordmark.webp`, solid `#193cff` background baked in). Convert to base64, embed as `<img>` inside a small rounded badge.
- Filename: `cybersecurity-threats-and-attacks.html`.

## Visual design system — Dark Animated Theme (reuse exactly)
```css
:root {
  --primary: #193cff; --accent: #00d4aa; --bg: #0a0e27;
  --card: #111638; --card-hover: #1a2050; --text: #fff; --dim: #8892b0;
  --success: #00ff88; --danger: #ff4757; --warn: #ffd700;
}
```
Animated radial-gradient background + ~30 floating particles. Cards rounded (24px/16px), hover lift + glow border, top gradient bar. Fixed nav hidden until scroll, blurred pill-nav, lists all section titles, clickable jump. Font Cairo. Section number badges. Per-section accent variables cycling: cyan `#06B6D4`, amber `#F59E0B`, violet `#8B5CF6`, emerald `#10B981`, pink `#EC4899`, red `#EF4444`, repeat. Code/English-heavy panels forced `dir="ltr"` + `unicode-bidi:isolate`. Every section ends with a `⚠️ أخطاء شائعة` box. Granular scroll-reveal per block via one `IntersectionObserver` (threshold 0.05), `translateY(30px)→0`, `visible` class, `0.6s cubic-bezier(0.4,0,0.2,1)`. Keyboard arrow-nav. Legend boxes next to diagrams. Footer: both logos + encouraging line.

## Language rules
`dir="rtl"`, UI in فصحى, explanations in Egyptian Arabic matching the source's warm, direct, teacher-narrating tone (translate the English technical passages into the same Egyptian Arabic style as the Arabic passages already in the source). English terms wrapped `<span dir="ltr">`, "الـ" prefix rule at line/heading/list/table-cell start.

## Mandatory SVG / interactivity rules
No native SVG `<text>` (self-check via grep before finishing each section). One fixed flippable arrow icon. Any diagram with 4+ connections built from a JS data lookup, never hand-typed coordinates. Stable `data-id` + `DOMContentLoaded` binding. Checkpoint after each section. Staged build: skeleton → each section → final review.

## Quiz behavior (for the 5 short recall questions embedded in sections below)
Hidden by default, revealed by click. Immediate color feedback (green/red) + short explanation. Skip button always available.

## Activity behavior — IMPORTANT, different from quizzes
For both activities in this lesson: present the full scenario/report text to the student (already explained, nothing hidden), let them think and answer on their own (no per-item immediate feedback, no locking), and provide a single "اعرض كل الإجابات" (show all answers) button at the end of each activity that reveals the complete model answers (classification + reasoning + best defense) for every item at once. Do not do click-per-question color feedback here — this is a self-work-then-reveal pattern, not a scored quiz.

---

## Content

### [Hero] عنوان الدرس
Badge: "Threats & Attacks". Gradient-text title. Subtitle inviting the student from "مين بيهاجمنا؟" to "إزاي بيحصل الهجوم خطوة بخطوة؟"

### [Intro] مراجعة سريعة: الأصول وأنواع البيانات (accent: cyan)
Quick recap section (matches source's "Recap" framing — lighter touch than full sections). Cover: Asset (أي حاجة قيمة للشركة)، Data at Rest / in Transit / in Use (مع الأمثلة: ملفات على سيرفر / رسالة واتساب بتتبعت / ملف Excel مفتوح)، Systems، Applications، Infrastructure، Human Assets، ولمحة سريعة عن Broken Authentication وUnpatched Systems وLateral Movement (هيتم التعمق فيهم لاحقًا).
- **Interaction:** flip-card grid — one card per term (Data at Rest/Transit/Use, Systems, Applications, Human Assets), front shows the term, back shows the Egyptian-Arabic explanation + example from the source.

### Section 1 — Threat, Vulnerability, Risk, Attack: المعادلة الأساسية (accent: amber)
**Objective:** فهم الفرق بين الأربعة مصطلحات، وإن الـ Risk بيظهر بس لما الـ Threat والـ Vulnerability يجتمعوا.
- **Core content:** Threat (تهديد محتمل لسه ما حصلش) — مثال: مجموعة Ransomware أعلنت نيتها هجوم بنك، لسه ما هاجمتش. Vulnerability (ثغرة، زي قفل مكسور) — مثال: سيرفر Apache من غير تحديث أمني. Risk = Threat × Vulnerability × Impact. Attack (اللحظة اللي المهاجم يستغل فيها الثغرة فعلًا) — مثال: ضغطت على لينك مزيف وكتبت الباسورد.
- **Real-world example:** مجموعة Lazarus استغلت ثغرة في مكتبة JavaScript، استهدفت منصة عملات رقمية، وسرقت حوالي 625 مليون دولار.
- **Interaction:** "لو Threat لوحده، ولو Vulnerability لوحدها، مفيش Risk" — a two-slider setup (Threat present: yes/no, Vulnerability present: yes/no); a "Risk" indicator lights up red only when BOTH are set to yes, staying dim otherwise — visually reinforcing the AND relationship.
- **Quiz (embed the source's Q1 exactly):** الفرق الصحيح بين Threat و Vulnerability — options as in source, correct answer B (Threat = اللي بيهاجم، Vulnerability = الباب المفتوح).

### Section 2 — أنواع المهاجمين (Threat Actors) (accent: violet)
**Objective:** التفريق بين 5 أنواع مهاجمين حسب الدافع: Cybercriminals (فلوس)، Nation-State Actors (تجسس/دعم حكومي)، Hacktivists (رسالة سياسية/احتجاج)، Insider Threats (متعمد/غير متعمد)، Script Kiddies (فضول/أدوات جاهزة).
- **Examples:** REvil (Cybercriminal ransomware)، Anonymous (Hacktivist)، موظف يسرّب بيانات لشركة منافسة (Insider Deliberate) أو يضغط فيشنج بالغلط (Insider Accidental)، حد بيحمّل أداة DDoS جاهزة (Script Kiddie).
- **Interaction:** 5 profile cards, each with an icon + primary motivation; clicking reveals the source's "Interactive Question" for that pair where relevant (e.g. "مين ممكن يهاجم بنك علشان فلوس بس؟" → Cybercriminals) as a quick click-to-check.
- **Quiz (embed source's Q2 exactly):** سيناريو المجموعة المدعومة من دولة قاعدة 8 شهور بدون اكتشاف → Nation-State Actor، مع تفسير ليه باقي الاختيارات غلط.

### Section 3 — دورة حياة الهجوم (Attack Lifecycle) (accent: emerald)
**Objective:** فهم إن أي هجوم بيمر بمراحل متسلسلة: Reconnaissance → Initial Access → Execution → Persistence → Lateral Movement → Exfiltration.
- **Examples per stage** (use these exact ones from the source): Reconnaissance — الهاكر يجمع أسماء الموظفين من LinkedIn. Initial Access — موظف فتح ملف Word فيه ماكرو خبيث. Execution — تشغيل برنامج Ransomware. Persistence — Backdoor account / RAT / Scheduled Task (تشبيه: مفتاح إضافي مخفي حتى لو غيرت القفل). Lateral Movement — التنقل بين أجهزة الشركة (تشبيه: التنقل من مكتب لمكتب لحد السيرفر الرئيسي). Exfiltration — رفع البيانات على Cloud أو نقلها ببطء عشان ما تتكشفش، وربما مع Double Extortion.
- **Interaction — reuse the step-by-step reveal pattern (Next/Back + step counter):** 6 steps, each revealing its icon, definition, and example; a connecting line animates forward as the student progresses.
- **Quiz (embed source's Q3 exactly):** المهاجم دخل بفيشنج وعمل admin account جديد → أي مرحلة؟ → Persistence.

### Section 4 — هجمات الهندسة الاجتماعية (Social Engineering) (accent: pink)
**Objective:** التفريق بين 5 أنواع خداع بشري: Phishing (إيميل عام)، Spear Phishing (إيميل موجه لشخص معين)، Vishing (مكالمة صوتية)، Smishing (رسالة SMS)، Pretexting (سيناريو/قصة كاملة).
- **Examples (use exactly):** Phishing — "Your account is locked, click here to verify". Spear Phishing — إيميل باسم موظف معين بيتكلم عن اجتماع حقيقي. Vishing — مكالمة "أنا من البنك، محتاج الـ OTP بتاعك". Smishing — SMS "طردك اتأخر، اضغط هنا". Pretexting — حد بيدّعي إنه موظف IT جديد وعايز بيانات الدخول.
- **Interaction:** a "channel matcher" — 5 example messages (email look, phone icon, SMS bubble, story bubble) the student drags/clicks to match to the correct term.
- **Quiz (embed source's Q4 exactly):** رسالة SMS فيها لينك مزيف → Smishing، مع توضيح ليه مش Pretexting.

### Section 5 — أنواع البرمجيات الخبيثة (Malware Types) (accent: red)
**Objective:** التفريق بين 5 أنواع Malware: Virus (بيصيب ملفات، محتاج تشغيل من المستخدم)، Worm (بينتشر لوحده عبر الشبكة)، Trojan (بيتنكر كبرنامج شرعي، مش بيعمل Replication)، Spyware (بيراقب ويجمع معلومات بهدوء)، Ransomware (بيشفر الملفات ويطلب فدية، أحيانًا مع Double Extortion).
- **Use the source's exact school analogy** as the section's anchor illustration: Virus = ورقة غش (مش هتأثر غير لو الطالب فتحها بنفسه) · Worm = طالب عنده برد معدي (العدوى تنتشر لوحدها) · Trojan = هدية شكلها جميل (تكتشف المشكلة بعد ما تفتحها).
- **Real example:** WannaCry — كان Ransomware + Worm في نفس الوقت (شفّر ملفات وانتشر تلقائي عبر ثغرة أمنية).
- **Interaction — reuse the tabbed pattern:** 5 pill tabs (Virus/Worm/Trojan/Spyware/Ransomware); each panel shows the school-analogy icon, the one-line distinguishing sentence from the source's summary ("Virus → Infects Files"، etc.), and the real example.
- **Quiz (embed source's Q5 exactly):** WannaCry انتشر في 24 ساعة من غير أي ضغطة مستخدم → أي نوع؟ → Worm.

### Section 6 — DDoS، Man-in-the-Middle، وهجمات الشبكة (accent: cyan)
**Objective:** فهم DDoS (إغراق السيرفر بطلبات وهمية من Botnet)، MitM (المهاجم بيقف في نص الاتصال ويقدر يقرا/يعدل/يحذف/يضيف)، الفرق بينه وبين Packet Sniffing (مراقبة بس من غير تدخل)، ولمحة عن DNS Attack.
- **Examples (use exactly):** DDoS — تشبيه مطعم 50 كرسي فجأة 5000 شخص دخلوا مقعدوش يطلبوا بس احتلوا المكان. MitM — جواب بين صاحبين بيعدي على شخص في النص بيقراه ويغيره. Packet Sniffing — شخص عالطربيزة جنبك بيسمع بس مش بيتدخل. المفتاح للتفرقة (من السورس بالظبط): "MitM = أنا بقيت في النص" مقابل "Packet Sniffing = أنا بتفرج بس".
- **Interaction:** animated message-path diagram — a message travels from Person A to Person B; toggle "MitM attacker present" to show the message rerouting through an attacker node who can read/edit it, vs toggle "Packet Sniffer present" to show a passive eavesdropping icon watching the same direct path without intercepting it.
- **Quiz:** none (this section's distinction is reinforced by the interaction itself).

---

### [Activity 1] تحليل نوع المهاجم (Threat Actor Profiling) (accent: violet, dashed activity-card style)
Present all 5 Threat Intelligence Reports exactly as in the source, each as its own card the student reads and thinks about (who is the threat actor, and what's the best defense) — no per-report feedback. Reports:
1. Phishing → ransomware, $2.3M Bitcoin demand, dark web negotiation portal
2. 9 months silent access, data viewed but never touched, custom unseen tools
3. Website defaced with political message, publicly claimed within hours
4. DBA exported customer table to USB after resigning, off-hours, unapproved
5. Automated credential stuffing tool, default settings, no IP masking, stopped when banned

After all 5, a single "اعرض كل الإجابات" button reveals all 5 classifications + reasoning + best defenses at once (Cybercriminal/Nation-State Actor/Hacktivist/Insider Threat (Malicious)/Script Kiddie, with their respective best-defense lists exactly as given in the source).

### [Activity 2] رسم خريطة دورة حياة الهجوم (Attack Lifecycle Mapping) (accent: emerald, dashed activity-card style)
Present the 6-events, 3-week timeline exactly as in the source (each event its own card, in chronological order), student thinks through which Attack Lifecycle stage each belongs to. Events:
1. Employee opens malicious PDF attachment (Week 1, Day 2)
2. New scheduled task appears (Week 1, Day 2)
3. Hourly HTTPS calls to external IP (Week 1, Day 3)
4. Credentials used to log into 3 other servers overnight (Week 2, Day 1)
5. IT contractor's LinkedIn profile scraped (Week 2, Day 4)
6. 4.2GB uploaded to Dropbox at 3 AM (Week 3, Day 1)

After all 6, a single "اعرض كل الإجابات" button reveals the full model solution table (stage + best defense per event, exactly as in the source), plus the two closing reflection answers: **Earliest Detection Opportunity** (Week 1 Day 2 — Initial Access) and **Most Dangerous Stage** (Lateral Movement, with the source's reasoning).

---

### [Closing] الرحلة الكاملة
Visual: vertical step diagram summarizing: Threat + Vulnerability → Risk → Attack → Threat Actor type → Attack Lifecycle stages → Social Engineering / Malware / Network Attacks as the tools used along the way → دفاعك يبدأ من أول نقطة اكتشاف.

---
Build in the staged order above. Run the mandatory checkpoint after every section before moving to the next one.