def user_guess(list):
    ''' user code = input("Enter a four digit number:") '''
    pass
def user_guess_test():
    print("Cannot use zero!", user_guess([10, 9, 5, 0]))
    print("Wrong code length.", user_guess([2, 6, 3, 8, 7]))
user_guess_test()