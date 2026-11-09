import pandas as pd

def clean_strings(df: pd.DataFrame) -> pd.DataFrame:
    """
    TODO: Siivoa tekstisarakkeet kuten 'name' ja 'capital'.

    Ohjeet:
    - Käytä pandasin `.str`-metodeja
    - Poista ympäröivät välilyönnit
    - Muuta title-caseen (iso alkukirjain aina)

    Palauta siivottu DataFrame.
    """

    return df


def handle_missing(df):
    """
    TODO: Käsittele puuttuvat arvot.

    Ohjeet:
    - Lisää funktioon type hint, joka kertoo, että funktio ottaa syötteenä on DataFramen ja myös palautettaa DataFramen
    - Tee df-kopio, jotta funktio ei muokkaa alkuperäistä DataFramea
    - Korvaa "N/A" ja vastaavat merkeillä `pd.NA`
    - Tulosta kuinka monta puuttuvaa arvoa sarakkeissa on

    Palauta DataFrame, jossa puuttuvat arvot käsitelty.
    """

    return df


def remove_duplicates(df):
    """
    # TODO: Poista duplikaatit.

    Ohjeet:
    - Lisää funktioon type hint, joka kertoo, että funktio ottaa syötteenä on DataFramen ja myös palautettaa DataFramen
    - Tee df-kopio, jotta funktio ei muokkaa alkuperäistä DataFramea
    - Poista päällekkäiset rivit perustuen 'name'-sarakkeeseen
    - Palauta puhdistettu DataFrame
    """

    return df


def fix_types_and_sort(df):
    """
    TODO: Korjaa sarakkeiden tyypit ja järjestä.

    Ohjeet:
    - Lisää funktioon type hint, joka kertoo, että funktio ottaa syötteenä on DataFramen ja myös palautettaa DataFramen
    - Tee df-kopio, jotta funktio ei muokkaa alkuperäistä DataFramea
    - Muunna numeromuotoiset sarakkeet numeerisiksi
    - Järjestä DataFrame nimen mukaan
    """

    return df


"""
Alla oleva lista määrittelee moduulin julkiset funktiot, eli mitkä funktionimet tuodaan mukaan, 
kun käytetään from module import * -syntaksia.
"""
__all__ = [
    "clean_strings",
    "handle_missing",
    "remove_duplicates",
    "fix_types_and_sort"
]
