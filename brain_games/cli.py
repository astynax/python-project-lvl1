import prompt

def greeting():
    print('Welcome to the Brain Games!')
    print()
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
