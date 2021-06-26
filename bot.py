############------------ IMPORT(S) ------------############
import nltk # https://www.nltk.org/
from nltk.chat.util import Chat, reflections

############------------ GLOBAL VARIABLES ------------############
rules = [
    "my name is (.*)",
    ["hi %1, what's up?"]
],
[
    "what's your name?",
    ["call me bot ;)"]
]