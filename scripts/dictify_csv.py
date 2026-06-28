import csv
import json

from pathlib import Path

EPIC_TRAGIC_CSV = Path(__file__).parent / "epic_tragic.csv"
EPIC_TRAGIC_JSON = Path(__file__).parent / "epic_tragic.json"


def main():
    with EPIC_TRAGIC_CSV.open() as f:
        reader = csv.reader(f)
        as_dict = {row[0]: row[1] for row in reader}

        with EPIC_TRAGIC_JSON.open("w") as g:
            json.dump(as_dict, g, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
