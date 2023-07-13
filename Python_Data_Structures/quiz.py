import random

fh = open("Vocabulary_list.csv", "r")
wd_list = fh.readlines()
# print(wd_list)

# remove the first line/entry from the word list array
# wd_list.pop(0)

# removing duplicates using sets
wd_set = set(wd_list)

# if the file does not exist, it is created
fh2 = open("Vocabulary_set.csv", "w")
fh2.writelines(wd_set)


# the file shows that the word is followed by a comma and then its definition.
# let us break this up
def get_word_and_definition(rawstring: str):
    word, definition = rawstring.split(",", 1)
    return word, definition.strip('" \n')  # Updated to remove " and \n


def get_def_and_pop(word_list, word_dict):
    """ Get the definition and pop so pop the list from the list so we don't repeat it"""

    # this will give us a random index between 0 and the length of the word_list
    random_index = random.randrange(len(word_list))
    word = word_list.pop(random_index)
    definition = word_dict.get(word)
    return word, definition

word_dict = dict()
for rawstring in wd_set:
    word, definition = get_word_and_definition(rawstring)
    # our word is the key and definition is the value
    word_dict[word] = definition


# Score Initialization
score = 0


print("\n     Weclome to the Quiz Game!")
print("Guess the meaning of each word \n")
print("--------------------------------")

# we will only get the keys - words with this list constructor, not the definitions - values 
while True:
    wd_list = list(word_dict)
    choice_list = []
    for x in range(4):
        word, definition = get_def_and_pop(wd_list, word_dict)
        choice_list.append(definition)
    random.shuffle(choice_list)


    
    print(word)
    print("--------------------------------")
    for idx, choice in enumerate(choice_list):
        print(idx+1, choice)
    
    
    # Input validation to catch non-integer inputs and inputs outside the range 0-4
    while True:
        try:
            choice = int(input("Enter 1, 2, 3, or 4; 0 to exit: "))
            if choice == 0:
                break
            elif 1 <= choice <= 4:
                break
            else:
                print("Invalid input. Please enter a valid choice (0, 1, 2, 3, or 4).")
        except ValueError:
            print("Invalid input. Please enter a valid choice (0, 1, 2, 3, or 4).")

    if choice == 0:
        break
    elif choice_list[choice - 1] == definition:
        score += 1
        print("\nCorrect!, Score: ",score, "\n")
    else:
        print("\nIncorrect!, Score: ",score, "\n")

# Display the final score
print("Quiz Ended")
print("Your Score:", score)