# Master Prompt: Interactive HTML Explainer — Security Controls & Defense in Depth

## Role
Build a single self-contained HTML file for a CS teacher (Bilal) to present a Cybersecurity lesson on Security Controls (types and functions), Monitoring, the SOC, and Defense in Depth, to students aged 12–17, on a laptop connected to a projector.

## Hard requirements — deliverable format
- ONE `.html` file. All CSS/JS inline. Google Fonts link only external dependency.
- Two logo images provided separately (`bilal-icon.webp`, `bilal-wordmark.webp`, solid `#193cff` background baked in). Convert to base64, embed as `<img>` inside a small rounded badge.
- Filename: `security-controls-defense-in-depth.html`.

## Visual design system — Dark Animated Theme (reuse exactly)
```css
:root {
  --primary: #193cff; --accent: #00d4aa; --bg: #0a0e27;
  --card: #111638; --card-hover: #1a2050; --text: #fff; --dim: #8892b0;
  --success: #00ff88; --danger: #ff4757; --warn: #ffd700;
}
```
Animated radial-gradient background + ~30 floating particles. Cards rounded (24px/16px), hover lift + glow border, top gradient bar. Fixed nav hidden until scroll, blurred pill-nav, lists all section titles, clickable jump. Font Cairo. Section number badges. Per-section accent variables cycling: cyan `#06B6D4`, amber `#F59E0B`, violet `#8B5CF6`, emerald `#10B981`, pink `#EC4899`, red `#EF4444`, repeat. Code/English-heavy panels forced `dir="ltr"` + `unicode-bidi:isolate`. Every section ends with a `⚠️ أخطاء شائعة` box (e.g. section 2's box should include the source's explicit warning: students often confuse Control Type with Control Function — "إيه هو؟" vs "بيعمل إيه؟"). Granular scroll-reveal per block via one `IntersectionObserver` (threshold 0.05), `translateY(30px)→0`, `visible` class, `0.6s cubic-bezier(0.4,0,0.2,1)`. Keyboard arrow-nav. Legend boxes next to diagrams. Footer: both logos + encouraging line.

## Language rules
`dir="rtl"`, UI in فصحى, explanations in Egyptian Arabic matching the source's warm, direct, teacher-narrating tone. English terms wrapped `<span dir="ltr">`, "الـ" prefix rule at line/heading/list/table-cell start.

## Mandatory SVG / interactivity rules
No native SVG `<text>` (self-check via grep before finishing each section). One fixed flippable arrow icon. Any diagram with 4+ connections built from a JS data lookup, never hand-typed coordinates. Stable `data-id` + `DOMContentLoaded` binding. Checkpoint after each section. Staged build: skeleton → each section → final review.

## Quiz behavior (for short recall checks)
Hidden by default, revealed by click. Immediate color feedback (green/red) + short explanation. Skip button always available.

## Activity behavior — IMPORTANT
For both activities: present the full scenario text up front (nothing hidden), let the student think and answer on their own with no per-item feedback, then a single "اعرض كل الإجابات" button at the end reveals all model answers at once. No per-question color feedback for activities — that pattern is quiz-only.

---

## Content

### [Hero] عنوان الدرس
Badge: "Security Controls". Gradient-text title. Subtitle inviting the student from "إزاي نحمي نفسنا؟" to "لو طبقة حماية فشلت، إيه اللي بيمسك الموقف؟"

### [Intro] إيه هي الـ Security Controls (accent: cyan)
**Objective:** فهم إن الـ Security Controls هي مجموعة وسائل بتشتغل مع بعض لتقليل فرصة الهجوم واكتشافه بسرعة لو حصل — مش أداة واحدة سحرية. مراجعة سريعة: Cyber Threats (أي حاجة ممكن تسبب ضرر)، Security Risks (احتمال إن التهديد ينجح)، Layered Protection (طبقات حماية متعددة).
- **Example:** شركة مركبة Firewall + Antivirus + MFA، كل واحدة بتحمي بطريقة مختلفة. حتى لو الهاكر عرف الباسورد، هيقف عند الـ MFA.
- **Interaction:** house analogy visual (from the source) — a house with door/lock/camera/alarm/guard icons the student clicks one by one, each click adding a "layer of protection" label, building intuition before the formal terms.
- **Quiz:** none (this is the conceptual on-ramp).

### Section 1 — الضوابط الثلاثة: إدارية، تقنية، مادية (accent: amber)
**Objective:** التفريق بين 3 أنواع Control: Administrative (سياسات وتدريب — Policies, Procedures, Standards, Awareness Training)، Technical (برامج وأجهزة — Firewall, Antivirus, EDR, MFA, SIEM)، Physical (حماية المكان — Guards, CCTV, Locks, Access Badges).
- **Examples (use exactly):** Administrative — سياسة تمنع مشاركة الباسورد، معيار "12 حرف على الأقل". Technical — Antivirus بيدور على Signature معروفة (وممكن يفوت Malware جديد أو سلوك غريب بعد التشغيل)؛ EDR بيراقب سلوك الجهاز باستمرار (برامج شغالة، ملفات بتتغير، اتصالات خارجة، PowerShell) ويقدر يعزل الجهاز بنفسه. Physical — بطاقة دخول لموظف HR بتفتحله قسمه بس مش غرفة السيرفرات.
- **EDR vs SIEM comparison** (use the source's exact table): EDR يحمي Endpoint واحد ويقدر يعزله؛ SIEM يراقب المؤسسة كلها، بيجمع Logs من كل الأجهزة، وبيعمل Correlation (مثال السورس: نفس اليوزر دخل من القاهرة وبعدها بدقيقتين من ألمانيا + تنزيل ضخم = الـ SIEM يربطهم ويقول "دي Incident واحدة").
- **Interaction:** 3-column sorting board — a pool of control names (Firewall, Antivirus, EDR, MFA, SIEM, Policy, Training, Standards, Guards, CCTV, Locks, Badges) the student drags/clicks into the correct column (Administrative/Technical/Physical).
- **Quiz (1 question):** classify a new example control into one of the 3 types.

### Section 2 — وظائف الضوابط: تمنع، تكتشف، تصلح، تسترجع (accent: violet)
**Objective:** فهم إن الـ Control Function مختلفة عن الـ Control Type — Type يجاوب "إيه هو؟" (Technical/Administrative/Physical)، Function يجاوب "بيعمل إيه؟" (Preventive/Detective/Corrective/Recovery). **This distinction is the source's flagged most-confused point — emphasize it clearly.**
- **The 4 functions with examples (use exactly):** Preventive (يمنع من البداية، زي MFA وقفت مهاجم عرف الباسورد الغلط). Detective (بيكتشف بعد ما يحصل، زي SIEM لاحظ Login غريب وبعت Alert). Corrective (بيصلح بعد الحادثة، زي IT حذف Malware وسطب Patch). Recovery (بيرجع الأمور لطبيعتها، زي استرجاع Backup بعد Ransomware).
- **Interaction — 2-axis matrix (this is the core interaction of this section):** a grid with Type (Technical/Administrative/Physical) as rows and Function (Preventive/Detective/Corrective/Recovery) as columns. Clicking a control name from a list (Firewall, SIEM, Awareness Training, Backup, Door Lock — the source's exact worked examples) highlights its correct cell in the matrix with both its Type AND Function shown together (e.g. Firewall → Technical + Preventive).
- **Quiz (1 question):** given a control, identify its Function (not Type, since that was covered in section 1) — reinforcing the Type-vs-Function distinction.

### Section 3 — المراقبة، الاكتشاف، ومركز العمليات الأمنية (SOC) (accent: emerald)
**Objective:** فهم إن وجود Controls مش كفاية، لازم مراقبة مستمرة (Logging, Alerting, Monitoring, Threat Detection)، وإن فيه فريق متخصص اسمه SOC بيراقب 24/7 ويتعامل مع الحوادث، وإن شغل الـ SOC بيمشي بخطوات ثابتة.
- **Example:** نظام لاحظ آلاف محاولات تسجيل دخول في دقيقة واحدة → Alert لفريق الـ SOC.
- **SOC Workflow — reuse step-by-step reveal pattern (Next/Back + step counter), 5 steps exactly from the source:** Monitor (مراقبة مستمرة) → Detect (تحديد هل ده تهديد حقيقي) → Investigate (جمع الأدلة وتحليل السبب) → Respond (عزل الجهاز/إيقاف الحساب/حذف الملف) → Recover (رجوع الأنظمة تشتغل طبيعي).
- **Security Analyst role:** short recap card listing the 5 responsibilities from the source (Monitor Alerts, Investigate, Analyze, Respond, Protect Assets).
- **Quiz:** none (the workflow visual is the reinforcement).

### Section 4 — الدفاع متعدد الطبقات (Defense in Depth) (accent: pink)
**Objective:** فهم إن الأمان الحقيقي مش أداة واحدة، لكن طبقات بتشتغل مع بعض: People + Administrative + Technical + Physical + Monitoring = Secure Organization. لو طبقة فشلت، الطبقة اللي بعدها تمسك الموقف.
- **Example (use exactly):** حتى لو الهاكر عرف الباسورد، هيقابله MFA، ولو دخل هيكتشفه الـ SIEM، ولو بدأ يهاجم الجهاز الـ EDR هيعزله.
- **Interaction:** a horizontal "layer stack" — 5 labeled layers (People, Administrative, Technical, Physical, Monitoring); a small "attacker" icon tries to pass through from left to right, and the student can toggle any single layer "off" to see the attacker breach further before the next active layer stops it — visually demonstrating why more layers = better defense.
- **Quiz:** none.

### Section 5 — رحلة هجوم Phishing عبر كل طبقات الدفاع (accent: red)
**Objective:** ربط كل حاجة اتعلمناها في مثال واحد متكامل — نفس هجوم الـ Phishing بيتقابل بطبقة دفاع مختلفة في كل مرحلة.
- **Interaction — step-by-step reveal (this is the lesson's capstone visual, give it real weight):** 6 steps exactly from the source, each revealing the attack action + the defense that responds to it:
  1. **Phishing Email** يوصل للموظف ("Your account will expire... click here").
  2. **Awareness Training** — الموظف يلاحظ إن الإيميل من Gmail مش من الدومين الرسمي، يمسح الرسالة. *(لو فشلت هذه الطبقة، الهجوم يكمل للخطوة الجاية.)*
  3. **MFA** — لو الموظف كتب الباسورد غلط، المهاجم لسه محتاج كود من موبايل الموظف.
  4. **EDR** — لو ملف خبيث حاول يشتغل على الجهاز، الـ EDR يوقف العملية.
  5. **SIEM** — يجمع الـ Alerts من الإيميل واللابتوب والـ Firewall، ويربطهم ببعض.
  6. **SOC** — يستلم كل ده، يحقق، يعزل الجهاز، ويغيّر الباسورد قبل ما الهجوم ينتشر.
- **Quiz:** none (this section is a synthesis, not a new fact-check).

---

### [Activity 1] ابني دفاعك السيبراني (Build Your Cyber Defense) (accent: cyan, dashed activity-card style)
Present the scenario exactly as in the source: شركة ناشئة فيها 30 موظف، مكتب واحد، Cloud Email، Company Laptops، Customer Database، Wi-Fi Network. المطلوب: كل مجموعة تختار على الأقل Administrative Control واحد، Technical Control واحد، Physical Control واحد، وتشرح ليه اختارتهم، وتجاوب على سؤال: "أنهي Control بيقلل المخاطر أكتر؟"

After the student works through it, a single "اعرض كل الإجابات" button reveals the source's model solution: Administrative → Security Awareness Training (بيمنع أغلب الهجمات من الأساس لأنها بتبدأ بإنسان). Technical → MFA (لو الباسورد اتسرق، المهاجم لسه محتاج العامل التاني). Physical → Access Badges (يمنع أي حد غريب من الوصول). Final answer: مفيش إجابة واحدة صح، بس لشركات صغيرة، Security Awareness Training غالبًا بيحقق أكبر تأثير.

### [Activity 2] تحدي الدفاع السيبراني (Cyber Defense Challenge) (accent: violet, dashed activity-card style)
Present the 6-stage attack timeline exactly as in the source (each stage its own card), student thinks about the best Security Control for each stage:
1. Employee clicks a phishing email
2. Credentials are stolen
3. Malware is downloaded
4. Attacker accesses the server
5. Customer data is stolen
6. Security incident occurs

After all 6, a single "اعرض كل الإجابات" button reveals the model solution (Security Awareness Training → MFA → Antivirus/EDR → Firewall → SIEM + Continuous Monitoring → SOC, each with the source's reasoning), plus the closing discussion answers: **Could one control stop the entire attack?** لأ، كل Control بيحمي مرحلة مختلفة، عشان كده Defense in Depth. **Why is MFA important if a password is stolen?** لأن الباسورد لوحده مش كفاية. **Which control helps before the attack starts?** Security Awareness Training. **Which control helps after detection?** SOC/SIEM/EDR حسب المرحلة.

---

### [Closing] الدرس كله في جملة واحدة
Use the source's own closing line as the anchor: الهجوم الحقيقي مبيتوقفش بسبب Tool واحدة — الشركات الكبيرة بتبني Layers من الحماية (Training + MFA + Firewall + EDR + SIEM + SOC)، وده اسمه **Defense in Depth**. Visual: the same layer-stack from Section 4, now shown fully intact with a checkmark on every layer.

---
Build in the staged order above. Run the mandatory checkpoint after every section before moving to the next one.
