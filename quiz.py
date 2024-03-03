# bold() adapted from the Text Styling Repl.it on 02.02.2024
# https://replit.com/@RedCoder/Text-Styling?v=1#main.py

from question import *
import sys
import os
import climage


def bold(string):
    sys.stdout.write("\033[1m" + string + "\033[0m\n")


def home():
    """This function introduces the quiz in a 'home page' fashion by calling
    print statements"""
    intro1 = "Welcome to the Halo Quiz!\n"
    intro2 = ("Take this quiz and learn which Covenant "
              "species you most resemble!\n")
    instructions = ("Each question is multiple choice. Type the letter "
                    "corresponding to\nyour answer, then hit Enter/Return "
                    "on your keyboard to advance to the next question.\n")
    learn_more = ("To learn more about Halo before you start,including "
                  "exploring Wiki pages, type 'More' "
                  "then hit Enter/Return\n")
    begin = "To begin, type 'Begin' then hit *you already know what to hit*\n"
    tip = '***** this quiz is not case-sensitive *****\n'
    image = climage.convert('./images/energy_sword.jpg', is_unicode=80)

    os.system('clear')
    bold(intro1)
    print(image)
    print(intro2)
    print(instructions)
    print(learn_more)
    print(begin)
    print(tip)

    home_input = input('> ').upper()
    home_options = ['MORE', 'BEGIN']
    while home_input not in home_options:
        print("Make sure you enter either 'More' or 'Begin'\n")
        home_input = input('> ').upper()
    if home_input == 'MORE':
        more()
    return


def more():
    os.system('clear')
    background = ("The Halo video game series begins with Halo: Combat Evolved,"
                  " and is based on human-alien warfare in the 26th century.\n"
                  "The first game follows one member of an advanced human "
                  "soldier, Master Chief, as he destroys an ancient super\n"
                  "weapon and religious artifact to the race of aliens known "
                  "as the Covenant.\nThe Covenant is comprised of multiple "
                  "alien species that have the same religion.\n")
    cov_back = ("The 4 main species of Covenant are Grunts, Jackals, Elites,"
                " and Hunters.\nGrunts are small, aggressive little aliens"
                " but flee if they hear a bullet.\nJackals are punk little"
                " aliens that love carrying around their own little shields"
                "and using sniper rifles.\nElites are the leaders of the pack"
                " and not run away. They throw grenades at you, smack the"
                " crap out\nof you and could just stick an energy sword in"
                "you.\nAnd lastly, Hunters are savages. They will chase you"
                "down and hit you with their giant metal arms that double"
                "as a plasma cannon.")

    print(background)
    print(cov_back)
    more_input = input('> ').upper()
    while more_input != 'DONE':
        print("Type 'done' when you wish to take the quiz.")
        more_input = input('> ').upper()
    return


def quiz():
    """This function is the meat of the quiz. Includes a loop that goes
    through each question and records the responses to each question"""
    os.system('clear')

    for qs in question_list:
        print(qs.get_question())
        for ans in qs.get_answers():
            print(ans)
        answer_input = input('> ').upper()
        # Check for valid answer. If options are A or B and user enters C,
        # user is re-prompted to enter their response
        while answer_input not in qs.get_mapping():
            print('Make sure to enter a letter corresponding to an answer '
                  'above.\n')
            answer_input = input('> ').upper()
        qs.set_response(answer_input)
        for items in qs.get_mapping()[qs.get_response()]:
            items.increment_score()
        os.system('clear')


if __name__ == '__main__':
    home()

    score = -69
    winner = None
    for buddies in species_list:
        if buddies.get_score() > score:
            score = buddies.get_score()
            winner = buddies.get_species()

    print(winner)
