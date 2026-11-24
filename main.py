from pathlib import Path

# The joke turns an AI's endless generation into a charming choice to spend one token on them.
Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(
    "I can generate a thousand pickup lines, but you’re the only prompt I’d like to run again tonight.",
    encoding="utf-8",
)
