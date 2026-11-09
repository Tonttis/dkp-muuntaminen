import pandas as pd
# TODO: Tuo data_tansform-paketin transform-moduulin funktiot

def main():
	file_path = "data/countries_noisy.json"
	save_path = "data/countries_cleaned.json"

	# TODO: Lue data JSON-tiedostosta DataFrameen

	# TODO: Tulosta 10 ensimmäistä riviä datasta ja rivimäärä ennen siivousta
	print("Original data sample:")


	# Suorittaa kaikki siivousvaiheet peräkkäin
	data = clean_strings(data)
	data = handle_missing(data)
	data = remove_duplicates(data)
	data = fix_types_and_sort(data)

	# TODO: Tallenna puhdistettu data uuteen JSON-tiedostoon, käytä save_path-muuttujaa

	# TODO: Tulosta 10 ensimmäistä riviä puhdistetusta datasta ja rivimäärä siivouksen jälkeen
	print("Cleaned data sample:")

if __name__ == "__main__":
	main()
