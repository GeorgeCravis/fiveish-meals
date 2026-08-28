from pathlib import Path
import json
import re


ROOT = Path(__file__).resolve().parents[1]
MOTTO_FILE = ROOT / "motto.txt"
INDEX_FILE = ROOT / "frontend" / "prototype" / "index.html"


def read_mottos():
    mottos = []
    for raw_line in MOTTO_FILE.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("motto "):
            line = line[len("motto "):].strip()
        if line:
            mottos.append(line)
    return mottos


def main():
    mottos = read_mottos()
    if not mottos:
        raise SystemExit("No mottos found in motto.txt")

    source = INDEX_FILE.read_text(encoding="utf-8-sig")
    replacement = (
        "const summaryMottos = [\n"
        + ",\n".join(f"      {json.dumps(motto, ensure_ascii=False)}" for motto in mottos)
        + "\n    ];"
    )
    updated, count = re.subn(
        r"const summaryMottos = \[\n(?:      .+\n)+    \];",
        replacement,
        source,
        count=1,
    )
    if count != 1:
        raise SystemExit("Could not find summaryMottos block in index.html")

    INDEX_FILE.write_text(updated, encoding="utf-8")
    print(f"Synced {len(mottos)} mottos into {INDEX_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
