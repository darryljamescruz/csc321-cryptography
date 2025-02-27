from bcrypt import *
from nltk.corpus import words
import base64

def crackPassword(hash_entry):
    crackedpass = None
    salthash = hash_entry.split(':')[1]
    salt = salthash[:29:].encode()
    hash = salthash[29::]

    # Approach:
    ## For each line of the shadowtext, separate the hash and the salt
    ## Hash every 6-10 letter word in the nltk corpus with the salt
    ## Whichever word hashes to the same string as the shadowtext is the password

    for word in words.words():
        word_hash = hashpw(word.encode(), salt)
        if word_hash == salthash:
            crackedpass = word
            break
    
    return crackedpass

def main():
    passwords = []
    with open('shadow.txt', 'r') as file:
        for line in file:
            passwords.append(crackPassword(line))
    print(passwords)

if __name__ == "__main__":
    main()