# -*-coding:utf-8 -*
from random import randrange
import pickle

"""function that fetch word from dictionary"""
def fetch_word(dict_of_word):
    list_of_index = list(range(len(dict_of_word)))
    while len(list_of_index) != 0:
        random_index = randrange(len(list_of_index))
        list_of_index.remove(random_index)
        if len(dict_of_word[random_index]) <= 8:
            return dict_of_word[random_index]
    raise Exception("Word non generated, check your dictionary if it's contains legal data")

"""function that get username from user in order to save it when game is finished"""
def prepare_user_info():
    user_name = ""
    while len(user_name) == 0 or not user_name.isalpha():
        print("Enter a valid username, (username must be in letters **only**)")
        user_name = input("\tType your name : ")
    return user_name

"""function that check the number of letter given by user & return it if it's respect the robot rule"""
def get_user_attemp(max_letter_to_attemp = 1):
    user_attemp = input("Type your letter : ")
    try:
        assert len(user_attemp) == max_letter_to_attemp and user_attemp.isalpha()
    except AssertionError:
        print ("\tYou must type one letter")
        return get_user_attemp()
    else:
        return user_attemp

"""function that contains the implementation of hangman process"""
def start_user_attemp(word_generated, max_shots=8):
    result = ["*"]*len(word_generated)
    user_score = 0
    while max_shots >= 1 and "*" in result:
        print("\t\tYou have only", max_shots, "shots to leave")
        user_attemp = get_user_attemp()
        max_shots -=1
        if user_attemp in word_generated:
            letter_index = word_generated.find(user_attemp)
            word_generated = word_generated[:letter_index]+"*"+word_generated[letter_index+1:]
            result[letter_index] = user_attemp
            print("\tcorrect", result)
            max_shots += 1
            user_score +=1
            if "*" in result:
                print("\t\t\tBonus !!! one shot added to you")
        else:
            print("\tnot correct", result)

    if "*" in result:
        print("\n******GAME OVER******\n")
    else:
        print("\n******You win******\n")
    return user_score

"""function that create empty file"""
def create_empty_file(user_key, user_score, filename="scores"):
    with open(filename, "wb") as my_file:
        my_pickler = pickle.Pickler(my_file)
        new_player = {user_key:user_score}
        my_pickler.dump(new_player)

"""function that update the score for user"""
def update_file(user_key, user_score, filename="scores"):
    try:
        temp_user_score = get_file(user_key)
    except FileNotFoundError:
        create_empty_file(user_key, user_score)
    else:
        user_score += temp_user_score
        old_player = get_all_scores()
        old_player[user_key] = user_score
        with open(filename, "wb") as my_file:
            my_pickler = pickle.Pickler(my_file)
            my_pickler.dump(old_player)

"""function that get the score by user"""
def get_file(user_key, filename="scores"):
    with open(filename, "rb") as my_file:
        try:
            my_unpickler = pickle.Unpickler(my_file)
            return my_unpickler.load()[user_key]
        except Exception:
            return 0

"""function that get all users scores"""
def get_all_scores(filename="scores"):
    with open(filename, "rb") as my_file:
        my_unpickler = pickle.Unpickler(my_file)
        return my_unpickler.load()