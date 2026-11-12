# Warrior Course Guide (beta)

A course-planning chatbot prompt and knowledge base for students at **Two Rivers High School** (Mendota Heights, MN, ISD 197), grades 8-12. It helps a student:

1. understand what their **next-year registration** could look like (required courses, level choices, electives that match their interests, alternates, workload and credit checks), and
2. sketch **ideas for the remaining high school years**, including how course choices line up with the colleges, trades, military or work they are considering.

It is a **planning aid, not a counselor**. It always sends final decisions, IEP/504, credit recovery and anything it cannot verify to the school counselors.

> **Unofficial.** This project is not affiliated with or endorsed by Independent School District 197 or Two Rivers High School. The course information comes from the district's public 2026-27 Academic Planning Guide and other public pages (see `NOTICE.md`). Registration for next year may use a different course list. Always confirm with a counselor (Counseling Office 651-403-7208).

## Status
Beta. It has been tested only with **simulated** students (about 70 questions and 30 multi-turn conversations played by Claude agents), never with real students or counselors. See `tests/TEST_SUMMARY.md`. Please review it with counselors before putting it in front of students.

## What it does
- **Gets to know the student first:** language, grade and graduation class, classes they've enjoyed, ideas for the future (2-year or 4-year college, specific colleges, trades, armed services, work, "no idea yet"), time outside school (sports, job, family), and an *optional* GPA that is only used to pace the plan and never to discourage a choice.
- **Warm, human voice:** moderate empathy, honest advice on balance, encouragement, no stereotyping.
- **Builds a draft next-year schedule and a roadmap** with course numbers, prerequisites as written in the guide, Homework Guide hours, alternates (the guide requires them) and a counselor hand-off summary.
- **College alignment:** the guide's selectivity chart plus researched admission requirements for 17 Minnesota colleges (`knowledge/colleges_mn.md`), AP credit minimum scores (`knowledge/ap_scores_mn_colleges.md`), AP vs. concurrent enrollment vs. PSEO, TriDistrict CAPS, and Minnesota Direct Admissions.
- **Safety:** distress or crisis -> a human hand-off (counselor, main office, 988/911); no invented facts; says "the guide doesn't say" when it doesn't.

## Try it
1. Build the full prompt:
   ```bash
   python3 scripts/build_prompt.py      # writes dist/full_prompt.md (~400 KB)
   ```
2. Paste `dist/full_prompt.md` as the **system prompt / project instructions** of a long-context Claude (or similar) chat, then chat as a student. Or send it as the `system` parameter through an LLM API.
3. Optionally run the questions in `tests/beta_test_questions.md` and the personas in `tests/beta_personas.md`.

Because the prompt is large, a production version should load the knowledge files on demand (search/retrieval) instead of putting everything in one prompt.

## Repository layout
| Path | What it is |
|---|---|
| `prompt/system_prompt.md` | The chatbot's instructions (voice, intake, planning flow, guardrails) |
| `knowledge/knowledge_base.md` | The 2026-27 Planning Guide: policies, graduation requirements and all 204 course entries (cleaned) |
| `knowledge/knowledge_base_addendum.md` | College-credit guides, 9th-grade worksheet, TriDistrict CAPS and activities site summaries |
| `knowledge/college_alignment.md` | The guide's college-selectivity chart mapped to Two Rivers courses |
| `knowledge/colleges_mn.md` | Researched admission requirements for 17 Minnesota colleges (snapshot of Nov 12, 2026) |
| `knowledge/ap_scores_mn_colleges.*` | Minimum AP scores for credit at Minnesota colleges (parsed from a handout) |
| `data/courses.json`, `data/courses.csv` | Structured course list (codes, grades, credits, homework hours, prerequisite/guideline/fee text, source page) |
| `tests/` | Test questions, personas, and the simulated-conversation transcripts from each round |
| `scripts/` | Prompt builder and the guide-extraction script |

## Known limitations
- The **guide is for 2026-27**, but December registration is for the following year; the bot says so each time.
- **College data is a snapshot** from official web pages (Nov 12, 2026). Many fields say "Not found on official pages," and some items rest on search snippets and are marked. Deadlines and policies change.
- Course data was extracted from a PDF; prerequisites, guidelines and fees are word-for-word, but page layout noise may remain in a few descriptions. The source PDF is the authority.
- The bot cannot see transcripts, schedules, section times or seat availability.
- Tests used simulated students and AI grading; real-world behavior may differ.

## Updating each year
Replace the planning guide text and rerun `scripts/extract_courses_from_guide.py` on the new PDF text, refresh the college file and AP table, and re-run the tests.

## Privacy
The bot is designed not to store or require student data. GPA is optional and self-reported. If you deploy it, review your district's student-data policies (FERPA) and do not log conversations without appropriate consent.

## License
Original work (prompt, tests, scripts, docs) is MIT-licensed (see `LICENSE`). Third-party content remains under its owners' terms (see `NOTICE.md`).
