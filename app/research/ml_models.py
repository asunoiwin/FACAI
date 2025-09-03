"""Placeholder ML model interfaces."""

from __future__ import annotations

import pandas as pd


def train_lightgbm(features: pd.DataFrame, label: pd.Series):
    """Train a LightGBM model (mock)."""
    # TODO: integrate LightGBM
    return None


def train_xgboost(features: pd.DataFrame, label: pd.Series):
    """Train an XGBoost model (mock)."""
    # TODO: integrate XGBoost
    return None


def train_lstm(features: pd.DataFrame, label: pd.Series):
    """Train an LSTM model (mock)."""
    # TODO: integrate deep learning model
    return None


__all__ = ["train_lightgbm", "train_xgboost", "train_lstm"]
