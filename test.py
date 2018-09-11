import os
import ring
from Crypto.PublicKey import RSA

# Size of ring 
size = 5

# Message to encrypt/sing
message = 'hello', 'world!'

# Function for create a pair of RSA keys  
def create_keys_RSA(_):
  return RSA.generate(2048, os.urandom)

# This a list of public a private keys 
key = map(create_keys_RSA, range(size))

#Class Ring (of public keys)
r = ring(key)

# Create signature
for i in range(size):
    signature = r.sign(message, i)

print(signature)

# Verify the signature
if r.verify(message, signature):
	print("Workig Perfect")
else:
	print("")