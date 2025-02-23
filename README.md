# HaloQuiz

    Halo Quiz is based on the First Person Shooter game from my childhood, Halo. This concise command line 
    quiz asks questions about the user's personality, and displays a picture of the character the user is 
    most like. Of course, it's all based on how I think the different characters' personalities are, like
    whether Elite's like Rock & Roll.
    The application was created in the monolithic-style architecture, while one microservice was supplied
    by a parter. Once the quiz is complete, the application passes the name of the character that most
    closely matches the user to pipe.txt, where it is read my the microservice and the name of the image
    file with that character's picture is returned.
    In addition to the variations in architectures, the quiz was made with the Inclusivity Heuristics as a
    driving force behind the UI. Users are given the option to go directly from the quiz to a webpage with
    Halo Wiki, go back and modify their answers during the quiz, and retake the quiz with predictable 
    results.
