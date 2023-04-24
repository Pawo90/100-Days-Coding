import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
# print(dict_NATO)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    input_word = input("Type a word: ").upper()
    try:
        output_list = [phonetic_dictionary[letter] for letter in input_word]
    except KeyError:
        print("There is letter in word which aren't in dictionary")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
