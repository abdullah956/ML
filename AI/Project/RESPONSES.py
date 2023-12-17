import random

#long responses
R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    #placee holder messages
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][random.randrange(4)] 
    #randon to give random response from above
    return response
