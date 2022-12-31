import pandas


nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

code_dict = {value.letter: value.code for (index, value) in nato_dataframe.iterrows()}

# RECURSION 👌👌
def code():
    words = input("Enter a word: ").upper()
    try:
        coded_word = [code_dict[word] for word in words]
    except KeyError as error_message:
        print(f"Sorry the {error_message} key doesn't exist.Only letters in the alphabet please.")
        code()
    else:
        print(coded_word)
code()
# print(letter_list)
# print(code_list)
