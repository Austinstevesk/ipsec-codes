from hashlib import sha256

text = "Steve"
print("Your hashed value is: ", sha256(text.encode('ascii')).hexdigest())