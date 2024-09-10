# +++ Function that greets a user with it,s name passed through Parameter, but if no Name Provided then it should use default name +++

def greetUser(Name = 'User'):
    return 'Hello, ' + Name + ' !'


print(greetUser('Abdullah'))