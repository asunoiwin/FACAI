"""In-memory feature store placeholder."""

from __future__ import annotations

from typing import Dict

import pandas as pd

_STORE: Dict[str, pd.DataFrame] = {}


def save_features(name: str, df: pd.DataFrame) -> None:
    _STORE[name] = df


def load_features(name: str) -> pd.DataFrame | None:
    return _STORE.get(name)


__all__ = ["save_features", "load_features"]
