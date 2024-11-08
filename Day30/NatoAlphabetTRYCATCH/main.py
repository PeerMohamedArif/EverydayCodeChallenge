import pandas as pd
data=pd.read_csv("nato_phonetic_alphabet.csv")
data_dict={row.letter :row.code for index,row in data.iterrows()}
#print(data_dict)


def generate_phonetic():

    word=input("Enter a word: ").upper()

    try:
        output=[data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only Letters in the Alphabet Please.")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
