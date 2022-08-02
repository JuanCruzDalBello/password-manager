# Password Manager
Terminal based password manager built with python
This program is purely for demostration purposes, should not replace a professionally made password manager.

## USAGE
python password_mgr.py
The first time the program is executed, the files key.txt and master_password.txt will be created.

Prompts the user for an input:
    a: add data.
    v: view the existing data.
    q: quit the program.

### Add data
The user is asked for a username and a password.

### View data
A table is shown with each username and its password.


## ADDITIONAL FILES
### passwords.txt
Stores the usernames and passwords.

### key.txt
Stores the key used to create a Fernet instanceto encrypt and decrypt data. It is created the first time the program is used.
If it is deleted the previouly saved passwords will become inaccessible.

### master_password.txt
Stores the master password, used to access the rest of the passwords. The user is prompted to create one the first the program is executed.


## FUNCTIONS
### view_passwords()
Prints a table with every username and its respective password on terminal.

### add_passwords()
Takes input from the user to get a user and a password, if any of the two happens to have a space or be an empty string the program will cancel the operation.

If both the username and the password are valid the program shows the data to the user before it is saved and ask him if it is correct. If so then the password is encrypted and both are written on the passwords.txt file.

### encrypt(string)
Encrypts a given string using the Fernet class from the cryptography module, and returns it as a bytes type.

### decrypt(string)
Decrypts an encrypted password and returns the result as a string.

### valid(string)
Checks if a string is valid as a username or password. It is considered valid if it does not have spaces and it is not an empty string. Returns True if the data is valid or False otherwise.

### pwd_file_created()
Returns True if the passswords.txt file is on the current directory, or False otherwise.

### correct_master_pwd(string)
Returns True if the given password is the same as the one stored on the master_password.txt file, or False otherwise.

### generate_master_pwd()
Creates the master_password.txt file and prompts the user for a master pasword to save. Intended to be used only the first time the program is executed.

### generate_key()
Generates the key.txt file and writes a key on it, using the method generate_key() from the Fernet class.

### get_key()
Opens the key.txt file and returns the key stored on it.
