def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print("Please, remind me your name.")
    user_name = input()
    print(f"What a great name you have, {user_name}!")


def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    user_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {user_age}; that's a good time to start programming!")


def counting():
    print("Now I will prove to you that I can count to any number you want.")
    repeat = int(input())
    for i in  range(repeat + 1):
        print(f"{i} !")
    print("Completed, have a nice day!")


def test():
    print("""Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
    while True:
        answer = int(input())
        if answer == 2:
            print("Congratulations, have a nice day!")
            break
        else:
            print("Please, try again.")

greet("Aid", 2025)
remind_name()
guess_age()
counting()
test()