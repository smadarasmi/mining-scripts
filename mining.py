import hashlib
import argparse
import random
import threading, os
import time

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--threads", help="Number of threads to run")
parser.add_argument("-f", "--file", help="Path to file")
parser.add_argument("-t", "--target", help="Target address")

args = parser.parse_args()

start = time.time()

# default target, latest hash mine at the time of writing
target = "00000000000000000004cd8ded26a588b80d487ebb38391aac60a81934031f8b"
if args.target != None:
    target = args.target

print(target)

def mine(data):
    rng = random.Random(threading.current_thread().ident)
    while(True):
        nonce = rng.randint(0, 9223372036854775807)
        # how we append the nonce to the data does not really matter, as long
        # as we producing different hash results. It serves the same purpose
        # for illustration
        hash = hashlib.sha256(str.encode(data) + str.encode(str(nonce))).hexdigest()
        if hash < target:
            print(hash)
            end = time.time()
            print("it took " + str(end - start) + " seconds")
            os._exit(1)

f = open(args.file, "r")
data = f.read()

thread_list = []
for i in range(int(args.threads)):
    thread = threading.Thread(target=mine, args=(data,))
    #thread.daemon = True
    thread_list.append(thread)
for thread in thread_list:
    print("starting thread...")
    thread.start()
