# bold() adapted from the Text Styling Repl.it on 02.02.2024
# https://replit.com/@RedCoder/Text-Styling?v=1#main.py

from question import *
import sys
import os
import climage
import time
from PIL import Image


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
    if home_input == "BEGIN":
        quiz()
    return


def more():
    os.system('clear')
    learn_title = "Learning More...\n"
    bold(learn_title)
    background = ("The Halo video game series begins with Halo: Combat Evolved "
                  "and is based\non human-alien warfare in the 26th century."
                  " The first game follows one member\nof a collection of"
                  " advanced human soldiers, Master Chief, as he destroys\n"
                  "an ancient super weapon and religious artifact to the "
                  "race of aliens\nknown as the Covenant. The artifact itself "
                  "is known as 'Halo'. The Covenant\nis comprised of multiple "
                  "alien species that have the same religion, a\nreligion that"
                  " worships an ancient race of aliens called the "
                  "Forerunners, who\nwere believed to have created such "
                  "artifacts.\n\n")
    cov_back = ("The 4 main species of Covenant are Grunts, Jackals, Elites,"
                " and Hunters.\nGrunts are small, aggressive little aliens"
                " but flee if they hear a bullet.\nJackals are punk little"
                " aliens that love carrying around their own little shields"
                "and using sniper rifles.\nElites are the leaders of the pack"
                " and not run away. They throw grenades at you, smack the"
                " crap out\nof you and could just stick an energy sword in"
                "you.\nAnd lastly, Hunters are savages. They will chase you"
                "down and hit you with their giant metal arms that double"
                "as a plasma cannon.\n\n")
    learn_more = ("If you want to go down the rabbit hole, visit this site: "
                  "https://www.halopedia.org/Halo_universe\n"
                  "Tip: instead of copying and pasting the link in your web"
                  " browser, you can use this shortcut:\n"
                  "'Ctrl' (Control) + Left Click\n")
    keep_going = "To take the quiz, type 'Done' and hit Enter.\n"

    print(background)
    print(cov_back)
    print(learn_more)
    print(keep_going)
    more_input = input('> ').upper()
    while more_input != 'DONE':
        print("Type 'done' when you wish to take the quiz.")
        more_input = input('> ').upper()
    if more_input == 'DONE':
        quiz()
    return


def quiz():
    """This function is the meat of the quiz. Includes a loop that goes
    through each question and records the responses to each question"""
    previous = list()
    os.system('clear')
    tip = ("Tip: At any time, you may enter 'back' to change your answer on the"
           " most recently answered question.\n")
    print(tip)
    for qs in range(len(question_list)):
        print(question_list[qs].get_question())
        for ans in question_list[qs].get_answers():
            print(ans)
        answer_input = input('> ').upper()
        # Check for valid answer. If options are A or B and user enters C,
        # user is re-prompted to enter their response
        if answer_input == 'BACK':
            previous = back(qs - 1, previous)
        elif answer_input != 'BACK':
            while answer_input not in question_list[qs].get_mapping():
                print('Make sure to enter a letter corresponding to an answer '
                      'above.\n')
                answer_input = input('> ').upper()
            previous.clear()
            question_list[qs].set_response(answer_input)
            for items in (
                    question_list[qs].get_mapping()
            )[question_list[qs].get_response()]:
                items.increment_score()
                previous.append(items)
        os.system('clear')
    results()


def back(start, previous):
    """This function is called by quiz() and allows a user to redo their
    answer on the previous question"""
    for items in previous:
        items.decrement_score()
    for qs in range(start, start + 2):
        os.system('clear')
        print(question_list[qs].get_question())
        for ans in question_list[qs].get_answers():
            print(ans)
        answer = input('> ').upper()
        while answer not in question_list[qs].get_mapping():
            print('Make sure to enter a letter corresponding to an answer '
                  'above.\n')
            answer = input('> ').upper()
        previous.clear()
        question_list[qs].set_response(answer)
        for items in (
                question_list[qs].get_mapping()
        )[question_list[qs].get_response()]:
            items.increment_score()
            previous.append(items)
    return previous


def results():
    winner_score = -69
    winner = None
    for folks in species_list:
        if folks.get_score() > winner_score:
            winner = folks.get_species()
            winner_score = folks.get_score()
    file = open('pipe.txt', 'w')
    file.write(winner)
    file.close()
    while True:
        time.sleep(1)
        file = open('pipe.txt', 'r')
        if file.readline() == winner:
            file.close()
        else:
            open_image(winner)
            break
    bold(f'You are a {winner}!!!\n')
    print('Thank you for playing!!!\n'
          'Program shutting down...\n')


def open_image(keyword):
    # Function author: Joshua Warnick
    # This function to open the image was originally part of the microservice,
    # but was repurposed here when it was not found to meet the specs of
    # the assignment
    script_dir = os.path.abspath(os.path.dirname(__file__))
    image_path = os.path.join(script_dir, "images", f"{keyword.lower()}.jpg")

    if os.path.exists(image_path):
        filename = os.path.basename(image_path)
        image = Image.open(image_path)
        image.show()


if __name__ == '__main__':
    home()
