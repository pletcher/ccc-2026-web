import csv
import json

from pathlib import Path

EPIC_TRAGIC_CSV = Path(__file__).parent / "tragedy_urn_heat.csv"
EPIC_TRAGIC_JSON = Path(__file__).parent / "tragedy_urn_heat.json"


def main():
    with EPIC_TRAGIC_CSV.open() as f:
        reader = csv.reader(f)
        as_dict = {row[1]: row[3] for row in reader}

        with EPIC_TRAGIC_JSON.open("w") as g:
            json.dump(as_dict, g, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
