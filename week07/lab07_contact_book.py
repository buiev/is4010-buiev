from pathlib import Path
import json
from typing import List, Dict, Union


def save_contacts_to_json(contacts: List[Dict[str, str]], path: Union[str, Path]) -> None:
    """Save a list of contact dictionaries to a JSON file.

    Ensures the parent directory exists. `contacts` should be JSON-serializable.
    """
    p = Path(path)
    if p.parent and not p.parent.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)


def load_contacts_from_json(path: Union[str, Path]) -> List[Dict[str, str]]:
    """Load contacts from a JSON file and return the list.

    If the file does not exist, return an empty list.
    """
    p = Path(path)
    if not p.exists():
        return []
    try:
        with p.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If the file is empty or corrupted, treat as no contacts
        return []
