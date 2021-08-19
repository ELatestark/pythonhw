# !/usr/bin/env python3
# recursive functions, shows integer until insert 'cancel'
def ask_for_int( prompt = "Please enter an integer:\n" ):
    user_input = input( prompt ).strip()

    if user_input.isdigit():
        if int(user_input) % 2 == 0:
            print(int(user_input) // 2)
            ask_for_int()
        else:
            print(int(user_input) * 3 + 1)
            ask_for_int()
    elif user_input == 'cancel':
        print('Bye!')
        exit(0)
    else:
        ask_for_int( prompt = "You need to pass an integer:\n" )


some_number = ask_for_int()
print(some_number)
