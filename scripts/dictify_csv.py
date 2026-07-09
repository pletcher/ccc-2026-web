import csv
import json

from pathlib import Path

SPEECH_NARRATIVE_CSV = Path(__file__).parent / "speech_narrative.csv"
SPEECH_NARRATIVE_JSON = Path(__file__).parent / "speech_narrative.json"


def main():
    with SPEECH_NARRATIVE_CSV.open() as f:
        reader = csv.reader(f)
        as_dict = {row[0]: row[1] for row in reader}

        with SPEECH_NARRATIVE_JSON.open("w") as g:
            json.dump(as_dict, g, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
