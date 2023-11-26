from Crypto.Util.number import getPrime
import time

seenNumbers = set()
#A larger bit size will result in less likelyhood of finding a repeat in a feasible amount of time
bitSize = 1024
#initialise the attempts at zero to display the results later
attempts = 0

start = time.time()

#while loop to continue printing prime numbers as long as they are not in seen numbers
#when number found in seen numbers loop will end 
while True:
    #generates random prime number with half bit specified bit length
    primes = getPrime(bitSize // 2)
    print(primes)
    attempts += 1
    #check to see if new number has been added to seen numbers
    if primes in seenNumbers:
        print(f"Repeat Found {primes}")
        break
    #adds numbers to seenNumbers
    seenNumbers.add(primes)


end = time.time()
duration = end - start

print(f"Number of attempts: {attempts}")
print(f"Time taken: {duration}")
