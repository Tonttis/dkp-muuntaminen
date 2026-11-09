
import pandas as pd

from data_transform import (
    clean_strings,
    handle_missing,
    remove_duplicates,
    fix_types_and_sort,
)


def main():
    file_path = "data/countries_noisy.json"
    save_path = "data/countries_cleaned.json"

    # Lue alkuperäinen aineisto
    data = pd.read_json(file_path)

    # Näytä tiedot ennen siivousta
    print("Original data sample:")
    print(data.head(10))
    print(f"Rivejä ennen siivousta: {len(data)}")

    # Suorita puhdistusvaiheet
    data = clean_strings(data)
    data = handle_missing(data)
    data = remove_duplicates(data)
    data = fix_types_and_sort(data)

    # Tallenna aineisto sen muokkaukse jälkee
    data.to_json(
        save_path,
        orient="records",
        indent=4,
        force_ascii=False
    )

    # Näytä tiedot siivouksen jälkeen
    print("Cleaned data sample:")
    print(data.head(10))
    print(f"Rivejä siivouksen jälkeen: {len(data)}")
    print(f"Puhdistettu tiedosto: {save_path}")


if __name__ == "__main__":
    main()
