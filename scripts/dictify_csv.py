import csv
import json

from pathlib import Path

SPEECH_NARRATIVE_CSV = Path(__file__).parent / "speech_narrative.csv"
SPEECH_NARRATIVE_JSON = Path(__file__).parent / "speech_narrative.json"


def main():
    with SPEECH_NARRATIVE_CSV.open() as f:
        reader = csv.reader(f)
        my_dict = {}

        for row in reader:
            try:
                # FIXME: we need to swap the polarity for speech and narrative only; don't do this
                # for epic and tragedy
                my_dict[row[0]] = -float(row[1])
            except Exception:
                continue

        with SPEECH_NARRATIVE_JSON.open("w") as g:
            json.dump(my_dict, g, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
