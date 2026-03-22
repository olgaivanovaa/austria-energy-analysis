# austria-energy-analysis

Analysis of Austria's energy consumption and mix using open data.

---

## License

MIT License

Copyright (c) 2026 olgaivanovaa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Scope

This project analyses Austria's yearly energy consumption mix using open data
from the Energy Institute – Statistical Review of World Energy (2025).

---

## Data

**Source:** Energy Institute – Statistical Review of World Energy (2025),
via Our World in Data.

**Download:**
https://ourworldindata.org/grapher/energy-consumption-by-source-and-country.csv?v=1&csvType=full&useColumnShortNames=true

**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) —
free to use and share with attribution.

The dataset contains yearly energy consumption in TWh broken down by source
from 2004 to 2024. This repository includes a filtered version for Austria
only at `data/austria_energy.csv`.

---

## Functions

### `load_data(filepath)`
Loads the CSV file from the given path and returns a pandas DataFrame.
This is the entry point — all other functions expect the DataFrame this
function returns.

### `total_consumption(df, year)`
Returns the total energy consumption in TWh for a given year by summing
all energy sources (renewables + fossils). Raises a `ValueError` if the
year is not present in the data.

### `renewable_share(df, year)`
Returns the share of energy from renewable sources as a proportion between
0.0 and 1.0 (e.g. 0.25 means 25% renewable). Raises a `ValueError` if the
year is not present in the data.

### `plot_energy_mix(df, year)`
Displays a bar chart of energy consumption by source for a given year.
Green bars represent renewables, red bars represent fossil fuels.
Raises a `ValueError` if the year is not present in the data.

---

## How to run

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the analysis:**
```bash
python main.py
```

**Run the tests:**
```bash
pytest
```

---

## Repository structure

```
austria-energy-analysis/
├── .github/
│   └── workflows/
│       └── ci.yml            # runs ruff and pytest automatically on GitHub
├── data/
│   └── austria_energy.csv    # Austrian energy data file
├── tests/
│   └── test_energy_analysis.py  # tests for functions
├── .gitignore                # tells Git which files to ignore for repo
├── energy_analysis.py        # main code with functions
├── LICENSE                   # MIT open source license
├── main.py                   # runs all functions and shows results
├── pyproject.toml            # ruff linter settings
├── README.md                 # project description and usage
└── requirements.txt          # dependencies: pandas, matplotlib, pytest, ruff
```
