from cryptography.fernet import Fernet

def load_key():
    file = open("key.key" , "rb")
    key = file.read()
    file.close()
    return key


# master_pwd=input("What is the master password? ")
key =load_key()
# +master_pwd.encode()
fer = Fernet(key)

# def write_key(): 
#     key = Fernet.generate_key()
#     with open("key.key" , "wb") as key_file:
#         key_file.write(key)

# write_key() to make a key once and to be done in the start!


# In any string reading or writing:
# Convert to bytes using .encode()
# Conversion by key using: fer.encrypt() for encryption
# Conversion by key using: fer.decrypt() for decryption
# Reconvert to string using: .decode()


def view():
    with open('passwords.txt','r') as f: 
        for line in f.readlines():
            data = line.strip()
            user , psswd = data.split("|")
            print("User: {} and password: {}".format(user,
            fer.decrypt(psswd.encode()).decode()
            ))


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    # file = open('passwords.txt','a')   Dont do this since you will need to manually close the file

    with open('passwords.txt','a') as f: 
        f.write(name+'|'+fer.encrypt(pwd.encode()).decode()+"\n")

    

while True:
    mode = input("Would you like to add a password or view existing ones (view,add)")
    if mode == "q":
        break

    elif mode  == "view":
        view()

    elif mode == "add":
        add()

    else: 
        print("Invalid mode")
        continue