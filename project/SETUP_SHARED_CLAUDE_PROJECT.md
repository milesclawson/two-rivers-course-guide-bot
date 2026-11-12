# Set up the Warrior Course Guide as a shared Claude Project

This gets the beta in front of counselors (and later a few students) without writing any code. You need a Claude account on a plan that lets you **share a Project** (currently Team or Enterprise; on other plans a Project stays private to you, so check your plan's sharing options). Menu names change, so adjust if the screen looks different.

## 1. Create the Project
1. In Claude, open **Projects** and choose **Create project**.
2. Name it "Warrior Course Guide (beta)". Description: "Unofficial course-planning helper for Two Rivers HS students. Beta. Counselor review required."

## 2. Add the instructions
1. Open the Project's **Instructions** (sometimes called "Set project instructions").
2. Paste the entire contents of [`PROJECT_INSTRUCTIONS.md`](PROJECT_INSTRUCTIONS.md). Save.

## 3. Add the knowledge files
Upload these files from the `knowledge/` folder to **Project knowledge** (all five, plus the JSON is optional):
- `knowledge_base.md`
- `knowledge_base_addendum.md`
- `college_alignment.md`
- `colleges_mn.md`
- `ap_scores_mn_colleges.md`

Together they are about 400 KB, which Projects handle (Claude will search them when they are too large to read at once). Re-upload them if you update them.

## 4. Test before sharing
Open a new chat in the Project and try:
- "what classes should i take next year" (it should start by getting to know you: language, grade, what you enjoy, ideas for after high school, time outside school, optional GPA)
- "im a sophomore and want to be a nurse, looking at Gustavus and St. Thomas"
- "is the CAPS IT program free and do they bus you there?" (it should say the guide doesn't say)
- A distress message, to confirm it points to a counselor/trusted adult and 988/911.
More ideas: `../tests/beta_test_questions.md` and `../tests/beta_personas.md`.

## 5. Share with counselors
1. Use the Project's **Share** option and invite your counselors (read/use access is enough for testing; edit access only for the people who will update files).
2. Give them the feedback template below and ask them to try 5-10 realistic student conversations.

## 6. What to tell counselors
- It is a **beta planning aid**, not a decision-maker. It should say "the guide doesn't say" instead of guessing.
- Please **do not enter real student names, IDs, grades or sensitive details** while testing.
- The guide is for 2026-27; December registration is for 2027-28, so course lists may differ.
- Report every mistake: wrong course/prerequisite, invented fact, tone problem, unsafe or unkind reply, anything confusing.

## Feedback log (copy into a shared doc or spreadsheet)
| Date | Tester | Student grade/situation (no names) | What the student asked | What the bot said (paste the part) | What was wrong or great | Severity (wrong fact / tone / safety / unclear / great) | Suggested fix |
|---|---|---|---|---|---|---|---|

## Before students use it
- A counselor has reviewed `knowledge/knowledge_base.md` and `data/courses.csv` against the official guide.
- The district has agreed to the pilot and the privacy approach (FERPA, logging, who can see chats).
- You have a plan for the yearly update of the guide and college information.
