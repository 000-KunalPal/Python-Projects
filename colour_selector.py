import random

colours = ['red', 'black', 'blue', 'grey', 'pink', 'yellow','orange', 'violet', 'indigo']

selected = random.choice(colours)

answer = input('Which colour will suit you today? Wanna know, Type y fro yes and n for no : ')
if answer == 'y':
    print(selected)

else:
    print("Sorry try again!")