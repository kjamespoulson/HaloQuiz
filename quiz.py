from covenant import *
from question import *
import os


def quiz():

    intro = ("Welcome to the Halo Quiz!\n\nTake this quiz and learn which "
             "Covenant species you most resemble!\n")

    instructions = ("Each question is multiple choice. Type the letter " 
                    "corresponding to\nyour answer, then hit Enter/Return "
                    "on your keyboard to advance to the next question.\n")

    learn_more = ("To learn more about Halo before you start, type 'More' "
                  "and hit Enter/Return\n")

    begin = "To begin, type 'Begin' and hit *you already know what to hit*\n"

    tip = '***** this quiz is not case-sensitive *****\n'

    print(intro)
    print(instructions)
    print(learn_more)
    print(begin)
    print(tip)

    home_input = input('> ').upper()
    home_options = ['MORE', 'BEGIN']
    while home_input not in home_options:
        print("Make sure you enter either 'More' or 'Begin'\n")
        home_input = input('> ').upper()

    os.system('clear')

    for qs in question_list:
        print(qs.get_question())
        for ans in qs.get_answers():
            print(ans)
        qs.set_response(input('> ').upper())
        for items in qs.get_mapping()[qs.get_response()]:
            items.increment_score()
        os.system('clear')

    for questions in question_list:
        print('Question:', questions.get_question())
        print('Options:', questions.get_answers())
        print('Response:', questions.get_response(), '\n')

    for species in species_list:
        print('Species:', species.get_species())
        print('Score:', species.get_score(), '\n')


if __name__ == '__main__':
    quiz()
