#!/usr/bin/env python3
"""Combine the system prompt and knowledge files into one ready-to-use prompt.

Usage:  python3 scripts/build_prompt.py            -> writes dist/full_prompt.md
Paste dist/full_prompt.md as the system prompt (or Project instructions) of a
Claude (or other LLM) chat. It is large (about 400 KB), so use a long-context model.
"""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
prompt = (root / "prompt" / "system_prompt.md").read_text(encoding="utf-8")
files = ["knowledge_base.md", "knowledge_base_addendum.md", "college_alignment.md",
         "colleges_mn.md", "ap_scores_mn_colleges.md"]
kb = "\n\n".join(f"<!-- FILE: {f} -->\n" + (root / "knowledge" / f).read_text(encoding="utf-8") for f in files)
placeholder = "[Insert contents of knowledge_base.md here]"
assert placeholder in prompt, "placeholder not found in system_prompt.md"
out = root / "dist"
out.mkdir(exist_ok=True)
(out / "full_prompt.md").write_text(prompt.replace(placeholder, kb), encoding="utf-8")
print("wrote", out / "full_prompt.md")
