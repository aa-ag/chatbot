############------------ IMPORT(S) ------------############
import nltk # https://www.nltk.org/
from nltk.chat.util import Chat, reflections

############------------ GLOBAL VARIABLES ------------############
rules = [
    [
        r"hi|Hi|hey|Hey|hello|Hello",
        ["yo -- what's going on?", "well, hello there!",]
    ],
    [
        r"what's your name ?",
        ["call me bot ;) \n\n how bout you -- what's your name?"]
    ], 
    [
        r"my name is (.*)",
        ["hi %1, what brings you here today?"]
    ],
    [
        r"quit|Quit|QUIT|exit|Exit|bye|Bye|BYE",
        ["buh-bye"]
    ],
]


############------------ FUNCTION(S) ------------############
def chat_with_the_bot():
    print("this is bot -- you built me, remember?")


############------------ GLOBAL VARIABLES ------------############
chat = Chat(rules, reflections)
chat.converse()
if __name__ == "__main__":
    chat_with_the_bot()
    
    
    