import random

def get_word_and_definition(rawstring: str):
    word, definition = rawstring.split(",", 1)
    return word, definition.strip('" \n')  # Updated to remove " and \n

def get_def_and_pop(word_list, word_dict):
    random_index = random.randrange(len(word_list))
    word = word_list.pop(random_index)
    definition = word_dict.get(word)
    return word, definition

def play_mode_with_lives(word_dict, lives):
    score = 0
    while lives > 0:
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
            print("\nCorrect!, Score: ", score, "\n")
        else:
            lives -= 1
            print("\nIncorrect! You have", lives, "lives remaining. Score:", score, "\n")

    print("Quiz Ended")
    print("Your Final Score:", score)

def play_mode_without_lives(word_dict):
    score = 0
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
            print("\nCorrect!, Score: ", score, "\n")
        else:
            print("\nIncorrect!, Score: ", score, "\n")

    print("Quiz Ended")
    print("Your Score:", score)

if __name__ == "__main__":
    fh = open("Vocabulary_list.csv", "r")
    wd_list = fh.readlines()
    fh.close()

    wd_set = set(wd_list)

    word_dict = dict()
    for rawstring in wd_set:
        word, definition = get_word_and_definition(rawstring)
        word_dict[word] = definition

    print("\n     Welcome to the Quiz Game!")
    print("Guess the meaning of each word \n")
    print("--------------------------------")

    while True:
        mode_choice = input("Choose a mode: 1 - With Lives, 2 - Without Lives, 0 - Exit: ")
        if mode_choice == "1":
            lives = int(input("Enter the number of lives you want: "))
            print("\n\n")
            play_mode_with_lives(word_dict, lives)
            break
        elif mode_choice == "2":
            print("\n\n")
            play_mode_without_lives(word_dict)
            break
        elif mode_choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose a valid mode (1, 2, or 0).")
