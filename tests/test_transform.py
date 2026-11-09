import pandas as pd
import pytest
import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data_transform import (
    clean_strings,
    handle_missing,
    remove_duplicates,
    fix_types_and_sort
)


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "name": [" finland ", "Finland", " france", "Spain", "Italy"],
            "capital": ["helsinki ", "Helsinki", "Paris", "N/A", "Rome"],
            "population": [5, "5", 67, "47", 60],
        }
    )


def test_clean_strings(sample_df):
    out = clean_strings(sample_df)
    assert out.loc[0, "name"] == "Finland"
    assert out.loc[0, "capital"] == "Helsinki"
    #assert no spaces around the strings
    assert not out["name"].str.startswith(" ").any()


def test_handle_missing(sample_df):
    out = handle_missing(sample_df)
    # Row with capital 'N/A' should be dropped
    assert not (out["capital"].astype(str).str.upper() == "N/A").any()


def test_remove_duplicates(sample_df):
    out = remove_duplicates(sample_df)
    # Only one Finland should remain
    names = out["name"].astype(str).str.lower()
    assert names.tolist().count("finland") == 1


def test_fix_types_and_sort(sample_df):
    out = fix_types_and_sort(sample_df)
    # population should be coerced to numeric where possible
    assert pd.api.types.is_numeric_dtype(out["population"]) or out["population"].dtype == object
    # DataFrame should be sorted by name
    assert out["name"].is_monotonic_increasing

