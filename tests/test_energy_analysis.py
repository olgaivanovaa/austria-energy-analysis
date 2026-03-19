"""Tests for energy_analysis.py"""

import pytest
import pandas as pd
from energy_analysis import load_data, total_consumption, renewable_share, plot_energy_mix

DATA_PATH = "data/austria_energy.csv"

