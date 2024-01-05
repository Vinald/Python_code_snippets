master_pwd = input('What is your master password? \n')


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line, end='')
            
def add(**args):
    name = input('Enter your name:\n')
    pwd = input('Enter your password:\n')

    with open('password.txt', 'a') as f:
        f.write('Name: ' + name + '\n' + 'Password: ' + pwd + '\n')


while True:
    mode = input('Would you like to add a new password or view the existing password? (add/view) or q to quit\n').lower()
    if mode == 'q':
        break
    elif mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print('invalid mode')
        continue
