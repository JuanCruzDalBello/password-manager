# Password Manager
# Juan Cruz Dal Bello - Portfolio Project

import os
from cryptography.fernet import Fernet


def generate_key():
    """
    Generates a cryptography.fernet key if not previously created, and stores it in a key.txt file.
    """
    if not os.path.isfile(os.path.dirname(__file__) + '\key.txt'):
        with open('key.txt', 'wb') as key_file:
            key_file.write(Fernet.generate_key())


def get_key():
    """
    Returns the key from key.txt.
    """
    with open('key.txt', 'r') as key_file:
        return key_file.read()


def generate_master_pwd():
    """
    Asks and saves a master password if there was not one.
    """
    if not os.path.isfile(os.path.dirname(__file__) + '\master_password.txt'):
        print('If this is the first time using this program, please enter a master password for future access to the rest of your passwords.')
        master_pwd = input('Master password: ')
        with open('master_password.txt', 'w') as master_file:
            master_file.write(master_pwd)
        
        print('Master password saved correctly.\n')


def correct_master_pwd(password):
    with open('master_password.txt', 'r') as master_file:
        if password == master_file.read():
            return True
    
    return False


def valid(data):
    """
    Check if a username or password is valid. 
    """
    if not data:
        return False
    
    if len(data.split(' ')) != 1:
        return False
    
    return True


def pwd_file_created():
    """
    Check for the passwords.txt file on the same directory.
    """
    if not os.path.isfile(os.path.dirname(__file__) + '\passwords.txt'):
        return False

    return True


def encrypt(password):
    """
    Returns an encrypted version of a given password.
    """
    fernet = Fernet(get_key())
    enc_password = fernet.encrypt(password.encode())
    return enc_password


def decrypt(enc_password):
    """
    Returns an decrypted version of a previoulsy encrypted password.
    """
    fernet = Fernet(get_key())
    dec_password = str(fernet.decrypt(bytes(enc_password, 'utf-8')))[2:-1]
    return dec_password
    

def view_passwords():
    """
    Prints usernames and passwords on a table.
    """
    if not pwd_file_created():
        print('There is no passwords.txt file created, add at least one password.\n')
        return
    
    print('\nUser\t\tPassword')
    print('------------------------')

    with open('passwords.txt', 'r') as f:
        for line in f:
            user, password = line.split(' ')

            print(f'{user}\t\t{decrypt(password)}')

    print()


def add_password():
    """
    Takes data from the user and stores it as user and password on the passwords.txt file.
    """
    user = input('User: ')
    password = input('Password: ')

    if not valid(user) or not valid(password):
        print('User and Password must have no spaces.\n')
        return

    answer = input(f'User: {user}, Password: {password}, is correct? (Y/n): ')
    if answer.upper() != 'Y':
        print('Data input canceled.\n')
        return

    with open('passwords.txt', 'a') as f:
        f.write(f'{user} {str(encrypt(password), "utf-8")}\n')
    
    print('User and password saved correctly.\n')


def menu():
    while True:
        option = input('Select a mode: ').lower()

        if option == 'q':
            return

        if option == 'v':
            view_passwords()
        elif option == 'a':
            add_password()
        else:
            print('Selected option is not valid.\n')


def main():
    generate_master_pwd()
    generate_key()
    pwd =  input('Master password: ')
    
    if correct_master_pwd(pwd):
        menu()
    else:
        print('Incorrect master password.')


if __name__ == '__main__':
    main()
