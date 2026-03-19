# Data: Energy Institute – Statistical Review of World Energy (2025)
# via Our World in Data (CC BY 4.0) – https://ourworldindata.org

import pandas as pd
import matplotlib.pyplot as plt

RENEWABLES = ["Hydropower", "Wind", "Solar", "Biofuels", "Other renewables"]
FOSSILS = ["Gas", "Coal", "Oil"]
ALL_SOURCES = RENEWABLES + FOSSILS


def load_data(filepath: str) -> pd.DataFrame:
    """Load data from CSV to DataFrame."""
    return pd.read_csv(filepath)


def total_consumption(df: pd.DataFrame, Year: int) -> float:
    """Total energy consumption in TWh for a given year."""
    row = df[df["Year"] == Year]
    if row.empty:
        raise ValueError(f"No data for {Year}.")
    return round(row[ALL_SOURCES].sum(axis=1).values[0], 2)


def renewable_share(df: pd.DataFrame, Year: int) -> float:
    """Share of energy from renewables (0.0–1.0) for a given Year."""
    row = df[df["Year"] == Year]
    if row.empty:
        raise ValueError(f"No data for {Year}.")
    total = row[ALL_SOURCES].sum(axis=1).values[0]
    renewable = row[RENEWABLES].sum(axis=1).values[0]
    return round(renewable / total, 4)


def plot_energy_mix(df: pd.DataFrame, Year: int) -> None:
    """Display a bar chart of energy consumption by source for a given Year."""
    row = df[df["Year"] == Year]
    if row.empty:
        raise ValueError(f"No data for {Year}.")
    labels = [s.replace("_twh", "").replace("_", " ").title() for s in ALL_SOURCES]
    colors = ["#2ecc71"] * len(RENEWABLES) + ["#e74c3c"] * len(FOSSILS)
    plt.figure(figsize=(10, 5))
    plt.bar(labels, row[ALL_SOURCES].values[0], color=colors)
    plt.title(f"Austria Energy Mix {Year}  |  green = renewable, red = fossil")
    plt.ylabel("TWh")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()