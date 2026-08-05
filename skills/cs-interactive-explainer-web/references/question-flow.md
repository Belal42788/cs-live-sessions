# Question Flow — How to Interview Bilal

Run this after the content is received and before writing the master prompt. Ask in Egyptian Arabic, matching Bilal's usual style: short questions, multiple-choice-style options where a question naturally has a few likely answers, batched per section rather than one lonely question at a time.

## Step A — Section breakdown confirmation
Read the full content and propose a section breakdown: one section per teachable concept, in a numbered list, each with a short title. Ask: "قسّمت الدرس كده، موافق ولا عايز تعدّل؟" Wait for confirmation or edits before continuing. Do not start per-section questions until the breakdown is confirmed.

## Step B — Per-section questions (repeat for each confirmed section)
For **each** section, ask about the following, batched together where possible:

1. **Learning objective** — "إيه أهم حاجة عايز الطالب يفهمها من الجزء ده؟"
2. **Examples/analogies** — "عندك أمثلة أو تشبيهات معينة عايز نستخدمها هنا، ولا أقترح؟"
3. **Common student mistakes** — "إيه أكتر غلطة بتتكرر مع الطلبة في النقطة دي؟"
4. **Interaction type** — what kind of click/step interaction fits this concept. Suggest from proven patterns if it fits:
   - **Cart with product selection** — for lessons involving shopping, pricing, discounts, calculations
   - **Teachable Machine simulator** — for AI/ML classification lessons (train → test → results)
   - **Parking/counter simulation** — for lessons with input/process/output, sensors, LEDs, counters
   - **Step-by-step reveal (Next/Back)** — for sequential processes (design steps, workflow stages)
   - **Bar chart with reveal** — for data analysis lessons (reveal max/min highlights)
   - Or describe a custom interaction if none of these fit. The AI agent will implement it — this is about intent, not pixels.
5. **Quiz decision** — "الجزء ده محتاج كويز صغير؟ لو أيوة، كام سؤال تقريبًا يناسب تعقيد الموضوع؟"

**Immediately after finishing a section's answers**, save them to the progress file (see `scripts/resume_check.py`) before moving to the next section. Do not wait until all sections are done to save.

## Step C — Final catch-all
After every confirmed section has been through Step B: "عايز تضيف حاجة تانية قبل ما أبني الـ prompt؟" Capture anything extra — attach it to the relevant section if it clearly belongs there, otherwise keep it as a general note for the master prompt.

## Step D — Validate
Run `scripts/validate_answers.py`. If it reports anything missing, go back and ask specifically for the missing piece(s) — don't re-ask everything, just the gaps.

## Notes on style
- Keep each round of questions short — this mirrors Bilal's general preference for efficient, low-token interactions with batched clarifying questions.
- If a section is simple/short, it's fine to combine steps B1–B5 into a single compact message rather than dragging it out.
- If Bilal answers "زي ما تشوف / إنت شايف إيه الأفضل" for a subjective design-ish sub-question, use good judgment and state the assumption briefly rather than re-asking.
