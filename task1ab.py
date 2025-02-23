import hashlib

#part 1a: hasing arbituary inputs with sha256
def sha256_hash(input_str):
    '''
    input_str: the string to hash
    '''
    #encode the input string to bytes
    hash_obj = hashlib.sha256(input_str.encode('utf-8'))
    #return the hexadecimal representation of the hash
    return hash_obj.hexdigest()

#part 1b: hash two strings that differ by exactly 1 bit
def flip_bit(s, char_index, bit_index):
    '''
    s: the originasl string
    char_index: the index of the character to flip
    bit_index: the index of the bit to flip
    '''  
    #get oroginal char and its ascii value
    original_char = s[char_index]
    original_val = ord(original_char)
    
    #flip the specified bit using XOR
    flipped_val = original_val ^ (1 << bit_index)
    #convert the new ascii value to a character
    flipped_char = chr(flipped_val)
    
    #return the new string with the bit flipped
    return s[:char_index] + flipped_char + s[char_index+1:]


if __name__ == '__main__':
    #test sha256_hash function
    print("-- task 1a: sha256 hash")
    #user_input = input("-- enter a string to hash: ")
    user_input = "Hello World!"
    print("-- user input: ", user_input)
    print("-- sha 256 digest: ", sha256_hash(user_input))
    
    #test flip_bit function
    print("\n-- task 1b: flip a bit")
    original_str = "Hello World!"
    
    #flip the lsb of the first char
    modified_str = flip_bit(original_str, 0, 0)
    
    print("-- original string: ", original_str)
    print("-- modified string: ", modified_str)
    
    #hash the original and modified strings
    original_hash = sha256_hash(original_str)
    modified_hash = sha256_hash(modified_str)

    print("-- original sha256 hash: ", original_hash)
    print("-- modified sha256 hash: ", modified_hash)
    
    
    