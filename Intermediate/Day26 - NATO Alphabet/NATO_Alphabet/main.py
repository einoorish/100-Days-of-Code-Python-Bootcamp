import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

word = input("Enter a word: ").upper()

result = [phonetic_dict[letter] for letter in word]

print(result)
