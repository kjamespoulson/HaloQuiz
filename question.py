from covenant import *


class Question:

    def __init__(self, question, answers, mapping):

        self.__question = question
        self.__answers = answers
        self.__mapping = mapping
        self.__response = None

    def get_question(self):
        return self.__question

    def get_answers(self):
        return self.__answers
    
    def get_response(self):
        return self.__response
    
    def set_response(self, user_input):
        self.__response = user_input

    def get_mapping(self):
        return self.__mapping


q1_answers = ['A: introvert', 'B: extrovert']
q1_mapping = {'A': [jackal, hunter], 'B': [elite, grunt]}
q1 = Question('Are you an more of an introvert or an extrovert?',
              q1_answers, q1_mapping)

q2_answers = ['A: leader', 'B: follower']
q2_mapping = {'A': [elite], 'B': [grunt, hunter, jackal]}
q2_question = ('In a group setting, such as in a group project or a sports '
               'team,\n'
               'are you more of a leader or a follower?')
q2 = Question(q2_question, q2_answers, q2_mapping)

q3_answers = ['A: comedian', 'B: stoic']
q3_mapping = {'A': [grunt], 'B': [elite, jackal, hunter]}
q3 = Question('Are you more of a comedian or a stoic?', q3_answers,
              q3_mapping)

q4_answers = ['A: rock', 'B: rap', 'C: pop', 'D: country', 'E: EDM']
q4_mapping = {'A': [elite], 'B': [hunter], 'C': [grunt], 'D': [flood],
              'E': [jackal]}
q4 = Question('Which genre of music do you like most?', q4_answers,
              q4_mapping)

q5_answers = ['A: fight', 'B: flight']
q5_mapping = {'A': [hunter, flood], 'B': [grunt, jackal]}
q5 = Question('Do you fight or flight?', q5_answers, q5_mapping)

q6_answers = ['A: 0', 'B: 1', 'C: 2', 'D: 3', 'E: 4+']
q6_mapping = {'A': [hunter], 'B': [elite], 'C': [jackal], 'D': [grunt],
              'E': [flood]}
q6 = Question('How many bones have you broken?', q6_answers, q6_mapping)

q7_answers = ['A: <5\'', 'B: 5\'1" - 5\'4"',
              'C: 5\'5" - 5\'8"', 'D: 5\'9" - 6\'', 'E: >6\'']
q7_mapping = {'A': [grunt], 'B': [jackal], 'C': [flood], 'D': [elite],
              'E': [hunter]}
q7 = Question('How tall are you?', q7_answers, q7_mapping)

q8_answers = ['A: scaredy-cat', 'B: reckless', 'C: prideful', 'D: clingy']
q8_mapping = {'A': [grunt], 'B': [hunter], 'C': [elite], 'D': [flood]}
q8 = Question('What not-so-nice quality do you most relate with?',
              q8_answers, q8_mapping)

q9_answers = ['A: football', 'B: soccer', 'C: baseball', 'D: basketball',
              'E: hockey']
q9_mapping = {'A': [hunter], 'B': [jackal], 'C': [elite], 'D': [elite],
              'E': [hunter, elite]}
q9 = Question('What is your favorite sport?', q9_answers, q9_mapping)

q10_answers = ['A: milk', 'B: cereal']
q10_mapping = {'A': [flood], 'B': [elite]}
q10 = Question('What do you pour first, the milk or the cereal?',
               q10_answers, q10_mapping)

q11_answers = ['A: Coke', 'B: Pepsi']
q11_mapping = {'A': [elite], 'B': [flood]}
q11 = Question('Coke or Pepsi?', q11_answers, q11_mapping)

question_list = [q7, q1, q8, q2, q10, q4, q3, q11, q5, q6, q9]
