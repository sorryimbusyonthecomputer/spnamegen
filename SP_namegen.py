import random

s_words = open('s_words.list', 'r')
n_words = open('n_words.list', 'r')

s_list = s_words.readlines()
n_list = n_words.readlines()



print(f'The name for today is: {random.choice(s_list).strip()}{random.choice(n_list).strip()}')
