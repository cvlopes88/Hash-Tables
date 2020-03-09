import hashlib




n = 10
# This 2 keys are being hashed the same way but using different methods
key = b"string"
key2 = "string".encode()

index = hash(key) % 8
print(index)

# for i in range(n):
#  print(hash(key))
#  print(hashlib.sha256(key).hexdigest())