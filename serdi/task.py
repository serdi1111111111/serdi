import random
import string
import hashlib

hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()

def hex_dig(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", rand_string)


hex_dig(10)

lines = [hex_dig(10), "string", "import string"]
with open(r"D:\randomfile.txt", "w") as file:
    file.writelines("%s\n" % line for line in lines)
