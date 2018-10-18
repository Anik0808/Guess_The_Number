import random

# creating a 3 digit random number
def create_sceretcode():
    '''
    Generates a 3 digit randon number.
    '''

    number = [str(num) for num in range(10)]
    random.shuffle(number)
    return number[:3]


def get_input():
    '''
    Takes input from the user.
    '''
    return list(input("Please Enter your Guess: \n"))


def logic(user_input, secret_code):
    if user_input == secret_code:
        return "CODE CRACKED"

    clue=[]

    for i,j in enumerate(user_input):
        if j==secret_code[i]:
            clue.append("Match")
        elif j in secret_code:
            clue.append("Close")
    if clue==[]:
        return "Nope"
    else:
        return clue


print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

secretCode=create_sceretcode()

print("Code has been generated, please guess a 3 digit number")

result=[]

while result !="CODE CRACKED":
    user_input=get_input()
    result=logic(user_input,secretCode)
    print("Your guess result is: ")
    for value in result:
        print (value)
