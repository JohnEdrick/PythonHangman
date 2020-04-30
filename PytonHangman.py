import random
import secrets
import os

clear = lambda: os.system('cls')
# Please Subscribe (J Edrick) For more videos.
# If you want to add new category create dictionary like this also make the all upper (highlight and ctrl + shift + u)
song = {"YOU KNOW YOU CAN MAKE MY WISH COME TRUE": "TITLE: TREASURE \n BY: BRUNO MARS",
        "I LOOK LIKE A VILLAIN OUTTA THOSE BLOCKBUSTERS": "TITLE: GODZILLA \n BY: EMINEM"}
phrase = {
    "SHORT END OF THE STICK": "MEANING: GETTING THE BAD END OF A DEAL, OR RECEIVING THE LEAST DESIRABLE OUTCOME FROM SOMETHING.",
    "ON CLOUD NINE": "MEANING: HAVING STRONG FEELINGS OF HAPPINESS OR SATISFACTION.",
    "JACK OF ALL TRADES MASTER OF NONE": "MEANING: HAVING SUITABLE SKILL IN MULTIPLE THINGS, BUT NOT BEING AN EXPERT IN ANY OF THEM.",
    "TUG OF WAR": "MEANING: IT CAN REFER TO THE POPULAR ROPE PULLING GAME OR IT CAN MEAN A STRUGGLE FOR AUTHORITY.",
    "JAWS OF LIFE": "MEANING: USUALLY THIS REFERENCES A TOOL USED BY RESCUERS WHEN THEY PRY OR CUT OPEN A CAR TO SAVE THE OCCUPANT."}

# Don't forget to add the name of your dictionary/category in this list
list_category = ["phrase", "song"]


def randomizer(category):
    if category == "SONG":
        return secrets.choice(list(song.keys()))
    elif category == "PHRASE":
        return secrets.choice(list(phrase.keys()))
    else:
        pass

# Please Subscribe (J Edrick) For more videos.
def main():
    clear()
    category = ""
    for _ in range(10):
        clear()
        category = list_category[random.randrange(0, (list_category.__len__()))]
        print(category)
    str_category = category.upper()
    space = 0
    word = str(randomizer(str_category))

    hide_word = "".join(list(map(lambda x: "-" if x != " " else " ", word)))
    is_wrong = True
    count = 3
    user_guess_list = []
# Please Subscribe (J Edrick) For more videos.
    while is_wrong:
        clear()
        print("=" * 47)
        print(" " * 20, "HANGMAN\n")
        print(" " * 16, f"CATEGORY: {str_category.capitalize()}")
        print("=" * 47)
        print("LIFE:", "√" * count, end=" " * (18 + space))
        print("Created By: J Edrick")
        print("=" * 47, end="\n\n")
        print(f" " * (29 - word.__len__()), hide_word)
        if count < 1:
            print(f"YOU FAILED!\nCorrect Answer: {word}")
            if category == "phrase":
                print(phrase.get(word))
            elif category == "song":        # <-If you add new category just copy this condition
                print(song.get(word))
            break
        elif "-" not in list(hide_word):
            if category == "phrase":
                print(phrase.get(word))
            elif category == "song":         # <-If you add new category just copy this condition
                print(song.get(word))
            print("PANALO!")
            break

        print("\n" * 3)
        user_guess = input("Enter your guess: ").upper()

        if user_guess in list(word):
            user_guess_list.append(user_guess)
            hide_word = "".join(
                list(map(lambda x: x if x in user_guess_list else (" " if x == " " else "-"), word)))
        else:
            count -= 1
            space += 1

# Please Subscribe (J Edrick) For more videos.
if __name__ == '__main__':
    main()
