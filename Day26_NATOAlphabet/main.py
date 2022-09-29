import pandas as pd

NATO_ALPHABET_FILEPATH = "Day26_NATOAlphabet/nato_phonetic_alphabet.csv"


def get_nato_alphabet(filepath):
    nato_file = pd.read_csv(filepath)
    return {row.letter:row.code for (_, row) in nato_file.iterrows()}


if __name__ == "__main__":
    nato_alphabet = get_nato_alphabet(NATO_ALPHABET_FILEPATH)
    user_word = input("Enter a word: ").upper()
    nato_word = [nato_alphabet[letter] for letter in user_word]
    print(nato_word)