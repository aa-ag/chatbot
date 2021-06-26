############------------ IMPORT(S) ------------############
import nltk # https://www.nltk.org/
from nltk.chat.util import Chat, reflections

############------------ GLOBAL VARIABLES ------------############
rules = [
    r"hi|Hi|hey|Hey|hello|Hello",
    ["yo -- what's going on?", "well, hello there!",]
], [
    r"my name is (.*)",
    ["hi %1, what's up?"]
], [
    "yes",
    ["... and what else is new, %1?"]
], [
    "what's your name?",
    ["call me bot ;)"]
]

############------------ FUNCTION(S) ------------############
def chat_with_the_bot():
    print("this is bot -- you built me, remember?")


chat_with_the_bot()


############------------ GLOBAL VARIABLES ------------############
if __name__ == "__main__":
    chat = Chat(rules, reflections)
    chat.converse()
    