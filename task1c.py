import hashlib

import random
import time
import matplotlib.pyplot as plt

def sha256_truncated(input_str, trunc_bits):
    '''
    input_str: the string to hash
    trunc_bits: the number of bits to truncate
    '''
    #encode the input string to bytes
    hash_obj = hashlib.sha256(input_str.encode('utf-8'))
    #get the digest as a byte string
    digest_int = int.from_bytes(hash_obj.digest(), byteorder='big')
    #create a mask to truncate the digest
    mask = (1 << trunc_bits) - 1
    #return the truncated digest
    return digest_int & mask

def find_collision(trunc_bits):
    '''
    trunc_bits: the number of bits to truncate
    '''
    seen_hashes = {}
    attempts = 0
    start_time = time.time()
    
    while True:
        rand_input = str(random.getrandbits(128))   #generate a random input
        trunc_hash = sha256_truncated(rand_input, trunc_bits)   #hash the input and truncate the digest
        if trunc_hash in seen_hashes:   #collision found
            elapsed_time = time.time() - start_time 
            return attempts, elapsed_time   
        else:   #add the hash to the dictionary and try again
            seen_hashes[trunc_hash] = rand_input
            attempts += 1
        
def main():
    bit_sizes = list(range(8, 52, 2))
    collision_times = []    #store the time taken to find a collision for each digest size
    collision_attempts = [] #store the number of attempts to find a collision for each digest size
    
    #run collision search for each digest size.
    for bits in bit_sizes:
        print(f"-- Running collision search for {bits}-bit truncated digest...")
        attempts, elapsed_time = find_collision(bits)
        collision_attempts.append(attempts)
        collision_times.append(elapsed_time)
        print(f"-- Digest size: {bits} bits, Attempts: {attempts}, Time: {elapsed_time:.4f} seconds\n")
        
    #plot digest size vs collision time
    plt.figure()
    plt.plot(bit_sizes, collision_times, marker='o', linestyle='-')
    plt.xlabel("Digest Size (bits)")
    plt.ylabel("Collision Time (seconds)")
    plt.title("Collision Time vs Digest Size")
    plt.grid(True)
    plt.savefig("collision_time_vs_digest_size.png")
    plt.show()
    
    # Plot digest size vs number of attempts (inputs)
    plt.figure()
    plt.plot(bit_sizes, collision_attempts, marker='o', linestyle='-')
    plt.xlabel("Digest Size (bits)")
    plt.ylabel("Number of Inputs (Attempts)")
    plt.title("Number of Inputs vs Digest Size")
    plt.grid(True)
    plt.savefig("attempts_vs_digest_size.png")
    plt.show()

if __name__ == "__main__":
    main()