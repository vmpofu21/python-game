# Mastermind Game (with numbers)
import random
def Code():
    secret_Code = ''
    for i in range(0, 4):
        secret_Code += str(random.randint(1, 9))
        code_list = list(secret_Code)
    return code_list

def user_guess():
    while True:
        user_Code = input('Enter a four digit number:')
        if len(user_Code) != 4:
            print ('Wrong code length!')
        elif '0' in user_Code:
            print ('Cannot use zero')
        else:
             user_list = list(user_Code)
        return user_list
    
def main():
    myCode = Code()
    chances = 0
    while True:
        userCode = user_guess()
        result = []
        if userCode == myCode:
            chances += 1
            print ('You won, in:', str(chances), ' turns.')
            break
        else:
            chances += 1
            for i in range(len(myCode)):
                if userCode[i] == myCode[i]:
                    result.append ('*')
                elif userCode[i] in myCode:
                    result.append ('-')
            print (result, 'chance:', chances)
            if chances == 5:
                print ('GAME OVER LOSER!!! The code is:', myCode)
                break
main()