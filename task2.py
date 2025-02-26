from bcrypt import *
from nltk.corpus import words

def crackPassword(user):
    crackedpass = None
    salthash = user.split(':')[1]
    salt = salthash[:29:]
    hash = salthash[29::]

    # Approach:
    ## For each line of the shadowtext, separate the hash and the salt
    ## Hash every 6-10 letter word in the nltk corpus with the salt
    ## Whichever word hashes to the same string as the shadowtext is the password

    for word in words.words():
        word_hash = hashpw(word.encode(), salt.encode())
        if word_hash == salthash:
            crackedpass = word
            break
    
    return crackedpass
