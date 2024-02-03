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
    learn_more = ("To learn more about Halo before you start, type 'More' "
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
    return


def quiz():
    """This function is the meat of the quiz. Includes a loop that goes
    through each question and records the responses to each question"""
    os.system('clear')

    for qs in question_list:
        print(qs.get_question())
        for ans in qs.get_answers():
            print(ans)
        qs.set_response(input('> ').upper())
        for items in qs.get_mapping()[qs.get_response()]:
            items.increment_score()
        os.system('clear')


if __name__ == '__main__':
    home()
    quiz()

    for questions in question_list:
        print('Question:', questions.get_question())
        print('Options:', questions.get_answers())
        print('Response:', questions.get_response(), '\n')

    for species in species_list:
        print('Species:', species.get_species())
        print('Score:', species.get_score(), '\n')

