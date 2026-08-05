---
name: cs-interactive-explainer
description: Turns a raw CS lesson (pasted text or an uploaded lesson file, not pre-split into sections) into a detailed MASTER PROMPT for a separate AI coding agent to build a single-file, interactive HTML teaching site with clickable/animated SVG explanations. Use whenever Bilal hands over lesson content and wants an interactive explainer site, references building a "موقع تفاعلي" or "interactive explainer" for a lesson, or invokes /cs-interactive-explainer. Always run the full staged Q&A before generating the prompt — do NOT skip straight to writing the master prompt from the raw content alone. This is NOT the cs-weekly-self-learning skill and does not reuse its templates or file structure.
---

# CS Interactive Explainer

Produces a MASTER PROMPT (not the website itself) that Bilal sends to a separate AI coding agent, which then builds a single self-contained HTML file he presents from in class (desktop + projector). He is a CS educator for students aged 12–17.

Read `references/design-system.md` and `references/svg-technical-rules.md` before writing the final master prompt — they contain the non-negotiable visual and technical requirements that must be embedded in it. Read `references/question-flow.md` for the exact Q&A script to run with Bilal.

Committing and pushing is default behavior: commit AND push the files for every completed deliverable unless Bilal explicitly says otherwise. Do not wait to be asked.

## Workflow

### 1. Get the content
Accept either pasted text or an uploaded lesson file. Content may be a full raw lesson, not pre-split into sections.

### 2. Propose a section breakdown
Read the content and propose a section breakdown (one section per teachable concept). Show it as a numbered list and ask Bilal to confirm or adjust before continuing. Do not proceed to Q&A until he confirms.

### 3. Check for a resume-in-progress file
Before starting Q&A, run `scripts/resume_check.py` against the content (see script header for usage). If a progress file already exists for this content, ask Bilal: "لقيت شغل سابق على الموضوع ده، تكمل ولا تبدأ من جديد؟" If he wants to resume, skip straight to the first unanswered section.

### 4. Staged Q&A, one stage per section
Follow the exact question set in `references/question-flow.md` for each confirmed section. Ask about: learning objective, examples/analogies, common student mistakes, interaction type, and whether this section needs a mini quiz (and if so, roughly how many questions the topic warrants).

**Immediately after each section's questions are answered**, append the answers to the progress file (see `scripts/resume_check.py` for the save format). Do not hold answers in memory until the end — write as you go, so an interruption only loses the in-progress section.

Use short, clear multiple-choice-style questions where possible, matching how Bilal prefers to be asked. Keep questions batched per section rather than one at a time across the whole lesson.

### 5. Final catch-all
After all sections are done, ask: "عايز تضيف حاجة تانية؟" Capture anything extra and attach it to the relevant section(s) or as general notes for the master prompt.

### 6. Validate before writing the prompt
Run `scripts/validate_answers.py` against the collected answers. It checks that every confirmed section has: a learning objective, at least one example/analogy, at least one common mistake, an interaction type, and an explicit quiz decision (yes-with-count or no). If anything is missing, go back and ask for it — do not generate the master prompt with gaps.

### 7. Write the master prompt
Written primarily in English (technical instructions for the AI coding agent), with Arabic lesson content/examples embedded as-is where relevant. Medium detail level: specific about what each section requires (concept, interaction, examples, mistakes to address, quiz), flexible about exact pixel-level implementation. Must incorporate, as strict non-negotiable requirements (not suggestions):
- Everything in `references/design-system.md` — this includes the code panel LTR fix, activity grid layout, section accent colors, simulation patterns (cart, Teachable Machine, parking, step-by-step, bar chart), and common mistakes box
- Everything in `references/svg-technical-rules.md`
- The staged build instruction: skeleton → each section individually → final review pass
- Instruction to embed the two logo files from `assets/` (bilal-icon.webp, bilal-wordmark.webp) as base64 in the header/footer
- Auto-generated English-slug filename instruction, derived from the lesson title
- Each section's interaction type must match one of the established patterns from `references/design-system.md` (or a custom one if Bilal specified it during Q&A)

Deliver the master prompt two ways: (1) as plain text in the chat reply, and (2) saved as a `.md` file.

### 8. Validate prompt before execution
Before building a website from any master prompt (whether written by Bilal or generated by the skill), run a compatibility check against the design-system and svg-technical-rules references. Verify the prompt includes:
- Dark animated theme with the exact CSS variables from `references/design-system.md`
- Font Cairo, RTL direction, Arabic UI with English technical terms
- No native SVG `<text>` elements (enforced by svg-technical-rules)
- `data-id` attributes on all interactive elements for DOMContentLoaded binding
- At least one interaction simulation pattern from `references/design-system.md` (cart, Teachable Machine, parking, step-by-step, bar chart)
- Base64-embedded logos from `assets/`
- Header/footer logo `<img>` classes matching the CSS exactly (`.nav-logo` header 36px, `.footer-logo` footer 40px — see `references/design-system.md` Branding)
- Staged build instruction (skeleton → sections → final review)
- Each section ends with a `⚠️ أخطاء شائعة` box
- Quiz behavior: hidden by default, click-to-reveal, green/red feedback, skip button
- Activity behavior: self-work-then-reveal pattern (single "اعرض كل الإجابات" button), NOT click-per-question

If the prompt is missing any of these, annotate it with the missing items and ask Bilal before proceeding — do not build a site from an incompatible prompt.

### 9. Clean up
Once the master prompt has been delivered successfully, delete the progress file created in step 4.

### 10. Commit & push
After every completed deliverable (the master prompt file, and any site built from it), commit the changes with a descriptive message, then push to origin. Default: commit AND push every time unless Bilal explicitly says otherwise — do not wait to be asked. Use `D:\شغل\EYouth\cs-live-sessions\auto-push.bat` to push.

**Index.html update (mandatory):** Every time a new HTML file is added or a new week folder is created, add a link for it in `index.html` in the correct week slot — interactive link (`🌐 الموقع التفاعلي`) goes above the Speaker Notes link, following the existing pattern. Never skip this step.

## Notes
- If the given content is very long (spans more than one lesson), warn Bilal but do not refuse — proceed with a section breakdown that reflects the full scope.
- Never assume design decisions not covered in `references/design-system.md` — if something is genuinely unspecified and matters for the prompt, ask rather than guess.
