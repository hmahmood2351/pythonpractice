import random

def helloworld():
    print("hello world")

def dice():
    return random.randint(1,6)

def rolldice():
    x = random.randint(1,6)
    y = random.randint(1,6)
    return x,y