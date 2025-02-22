import hashlib

#part 1a: hasing arbituary inputs with sha256
def sha256_hash(input_str):
    #encode the input string to bytes
    hash_obj = hashlib.sha256(input_str.encode('utf-8'))
    #return the hexadecimal representation of the hash
    return hash_obj.hexdigest()

if __name__ == '__main__':
    #test sha256_hash function
    print("-- task 1a: sha256 hash")
    user_input = input("-- enter a string to hash: ")
    print("-- sha 256 digest: ", sha256_hash(user_input))