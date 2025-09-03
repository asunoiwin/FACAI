"""Load project configuration from JSON file."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.json"


def load_config(path: Path | None = None) -> Dict[str, Any]:
    """Load configuration dictionary from a JSON file.

    Parameters
    ----------
    path: Path | None
        Optional override for the config path. Defaults to project level
        ``config.json``.
    """
    cfg_path = path or CONFIG_PATH
    with cfg_path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


config = load_config()
