# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Read invited_names.txt file
with open("./Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()
    for i in range(len(names)):
        names[i] = names[i].replace("\n", "")

for name in names:
    # Read starting letter.txt file
    with open("./Input/Letters/starting_letter.txt", mode="r") as file:
        letter = file.read()

    letter = letter.replace("[name]", name)

    with open(f"./Output/ReadyToSend/LetterTo{name}", mode="x") as file:
        file.write(letter)
