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

question_list = [q1, q2, q3]
