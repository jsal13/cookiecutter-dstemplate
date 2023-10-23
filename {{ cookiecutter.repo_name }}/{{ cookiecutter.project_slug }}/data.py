import datetime
from typing import Iterable

import numpy as np
import pandas as pd


def generate_timeseries(n: int) -> pd.DataFrame:
    """
    Generate a sample timeseries dataset.

    Args:
        n (int): Number of rows.

    Returns:
        list[tuple[datetime.datetime, float]]: list of (date, val).
    """
    date_range = pd.date_range("2000-01-01", periods=n, freq="D").to_numpy()

    # Generate a less stochastic dataset.
    vals = [np.random.rand() * 10]

    for idx in range(n - 1):
        delta = np.random.normal(loc=0, scale=3)
        vals.append(vals[idx] + delta)

    return pd.DataFrame({"dt": date_range, "vals": vals})
