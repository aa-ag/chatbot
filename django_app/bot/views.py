############----------- IMPORTS -----------############
from django.http import HttpResponse
import nltk
from nltk.chat.util import Chat, reflections


############------------ GLOBAL VARIABLES ------------############
rules = [
    [
        r"hi|Hi|hey|Hey|hello|Hello",
        ["yo -- what's going on?", "well, hello there!",]
    ],
    [
        r"what's your name ?",
        ["call me bot ;) \n\n how bout you: what's your name?"]
    ], 
    [
        r"my name is (.*)",
        [f"hi %1, what brings you here today?"]
    ],
    [
        r"ai|AI|Artificial Intelligence",
        [f"oh, i can't help with that -- that's scary"]
    ],
    [
        r"quit|Quit|QUIT|exit|Exit|bye|Bye|BYE",
        ["buh-bye"]
    ],
    [
        r"(.*)",
        ["hmmm... dunno how to process that; let's try again: how can I help you today?"]
    ],
]


############----------- VIEW(S) -----------############
def home(request):
    return HttpResponse("Hello, world")



############------------ FUNCTION(S) ------------############
def chat_with_the_bot():
    print("this is bot -- you built me, remember?")


############------------ GLOBAL VARIABLES ------------############
chat = Chat(rules, reflections)
chat.converse()
chat_with_the_bot()