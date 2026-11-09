
import pandas as pd


def clean_strings(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    for column in ("name", "capital"):
        if column in cleaned.columns:
            cleaned[column] = (
                cleaned[column]
                .astype("string")
                .str.strip()
                .str.title()
            )

    return cleaned


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    cleaned = cleaned.replace(
        r"(?i)^\s*(?:n/?a|none|null|nan|unknown|-)?\s*$",
        pd.NA,
        regex=True,
    )

    print("Puuttuvat arvot sarakkeittain:")
    print(cleaned.isna().sum())

    return cleaned


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    cleaned["name"] = (
        cleaned["name"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    cleaned = cleaned.drop_duplicates(
        subset="name",
        keep="first"
    )

    return cleaned.reset_index(drop=True)


def fix_types_and_sort(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    if "population" in cleaned.columns:
        cleaned["population"] = pd.to_numeric(
            cleaned["population"],
            errors="coerce"
        )

    return cleaned.sort_values(
        by="name",
        kind="stable"
    ).reset_index(drop=True)


__all__ = [
    "clean_strings",
    "handle_missing",
    "remove_duplicates",
    "fix_types_and_sort",
]
