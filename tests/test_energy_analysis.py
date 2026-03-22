from io import StringIO
from unittest.mock import patch

import matplotlib
import pandas as pd
import pytest

matplotlib.use("Agg")  # non-interactive backend for CI

from energy_analysis import load_data, plot_energy_mix, renewable_share, total_consumption

# ── Shared fixture ────────────────────────────────────────────────────────────

CSV = """Year,Hydropower,Wind,Solar,Biofuels,Other renewables,Gas,Coal,Oil
2023,40.0,20.0,10.0,5.0,5.0,100.0,80.0,60.0
"""
# totals: renewables = 80, fossils = 240, grand total = 320


@pytest.fixture
def df():
    return pd.read_csv(StringIO(CSV))


@pytest.fixture
def tmp_csv(tmp_path):
    p = tmp_path / "energy.csv"
    p.write_text(CSV)
    return str(p)


# ── Tests ─────────────────────────────────────────────────────────────────────

def test_load_data(tmp_csv):
    result = load_data(tmp_csv)
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns[:3]) == ["Year", "Hydropower", "Wind"]


def test_total_consumption(df):
    assert total_consumption(df, 2023) == 320.0


def test_total_consumption_missing_year(df):
    with pytest.raises(ValueError, match="No data for 1800."):
        total_consumption(df, 1800)


def test_renewable_share(df):
    # 80 renewables / 320 total = 0.25
    assert renewable_share(df, 2023) == 0.25


def test_plot_energy_mix(df):
    with patch("matplotlib.pyplot.show") as mock_show:
        plot_energy_mix(df, 2023)
        mock_show.assert_called_once()
