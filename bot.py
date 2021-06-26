############------------ IMPORT(S) ------------############
import nltk # https://www.nltk.org/
from nltk.chat.util import Chat, reflections

############------------ CODE ------------############
print(Chat)
# <class 'nltk.chat.util.Chat'>

print(reflections)
'''
{'i am': 'you are', 
'i was': 'you were', 
'i': 'you', 
"i'm": 'you are', 
"i'd": 'you would', 
"i've": 'you have', 
"i'll": 'you will', 
'my': 'your', 
'you are': 'I am', 
'you were': 'I was',
 "you've": 'I have', 
 "you'll": 'I will', 
 'your': 'my', 
 'yours': 'mine', 
 'you': 'me', 
 'me': 'you'}
'''