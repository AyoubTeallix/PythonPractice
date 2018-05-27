# -*-coding:utf-8 -*
"""Created by : EL HASSANI AYOUB
    In : 27/05/2018
    Reason : Practice python
    Details : check this link to get more details about this Exercice
    Link Contains Details : https://openclassrooms.com/courses/apprenez-a-programmer-en-python/tp-un-bon-vieux-pendu"""

from simple_hangman_game.functions import *
from simple_hangman_game.data import *

def start_game_process():
    print("Fetch word from dictionary ...")
    try:
        word_generated = fetch_word(dict_of_word)
    except Exception as e:
        print(e)
    else:
        print("-------- Prepare the user info --------")
        user_name = prepare_user_info()
        user_score = start_user_attemp(word_generated, max_shots)
        # update the file
        update_file(user_key=user_name, user_score=user_score, filename=file_name)
        print("----- All users scores -------")
        # get all users score
        print(get_all_scores())

start_game_process()