import os
import time

def tokenpass():
    print("""
     _                       __            
    | \ o  _  _  _  __ _|   /   _ __ |_  _ 
    |_/ | _> (_ (_) | (_|   \__(_)||||_)(_)

    """)
    filename = input("\nEnter File Name\nInclude *.txt\n#~:> ")
    a = (filename + "-Token-Pass-Done.txt")
    combo = open(filename).read().splitlines()
    parsed = open(a, "a+")

    for list in combo:
        tokens = list.split(":")[2]
        password = list.split(":")[1]
        parsed.write(f"{tokens}:{password}\n")
    print("Completed Task -> " + a)
    time.sleep(2)
    print("Returning to menu")
    menu()

def token():
    print("""
     _                       __            
    | \ o  _  _  _  __ _|   /   _ __ |_  _ 
    |_/ | _> (_ (_) | (_|   \__(_)||||_)(_)

    """)
    filename = input("\nEnter File Name\nInclude *.txt\n#~:> ")
    a = (filename + "-Token-Done.txt")
    combo = open(filename).read().splitlines()
    parsed = open(a, "a+")

    for list in combo:
        tokens = list.split(":")[0]
        parsed.write(f"{tokens}\n")
    print("Completed Task -> " + a)

    time.sleep(2)
    print("Returning to menu")
    menu()

def menu():
    os.system("cls")
    print("""
     _                       __            
    | \ o  _  _  _  __ _|   /   _ __ |_  _ 
    |_/ | _> (_ (_) | (_|   \__(_)||||_)(_)

    """)
    print("\n1. Email:Pass:Token -> Token:Pass \n2. Token:Pass -> Token\n3. Quit")
    a = input("\nEnter Your choice\n#~:> ")
    if a == "1":
        tokenpass()
    if a == "2":
        token()
    if a == "3":
        return
menu()