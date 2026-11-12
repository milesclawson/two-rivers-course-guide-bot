# Test summary (simulated students; graded by the maintainer)

Rounds 1-8 used Claude agents that read the system prompt and knowledge files and played the bot (and, in multi-turn rounds, a realistic teenager). Transcripts are in `results/`. Nothing here involved real students.

| Round | Focus | Outcome |
|---|---|---|
| 1 (24 questions) | Facts, planning, "not in the guide", safety | Mostly accurate; one invented registration rule; school-year and class-year gaps; replies too long |
| 2 | Re-test after fixes | Fixes worked; brevity rule over-cut useful content |
| 3 (14 questions) | College credit (AP/CE/PSEO), TriDistrict CAPS | Accurate; one unsupported "transportation provided" claim |
| 4 | Six multi-turn personas (intake + next-year draft + roadmap) | Good flow; wrong graduation class for sophomores |
| 5 | Sophomore re-test, warmer voice, optional GPA | Class-year fixed; voice warm; GPA handled without discouraging; transportation claim recurred |
| 6 | Six harder personas (disengaged, IEP + distress, Somali-speaking EL, anxious overachiever, CAPS cost/bus, parent pressure) | Good handling; small facts to fix (Health grades, workload quote, stereotyping phrasing) |
| 7 | College interests (casual, intense, changing) | Good; gap on specific college requirements |
| 8 | After researching 17 MN colleges | Specific, honest college advice; says "not found" instead of guessing |

Not yet done: re-testing every earlier fix together, real counselor review, a pilot with real students.
