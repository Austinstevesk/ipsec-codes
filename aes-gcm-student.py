from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

from binascii import hexlify

## secret key shared by Alice and Bob
key = b"\xf1\x6a\x93\x0f\x52\xa1\x9b\xbe\x07\x1c\x6d\x44\xb4\x24\xf3\x03"
## Alice
alice_plaintext = b"secret"	
print("Alice plaintext is: %s"%alice_plaintext)
alice_cipher = AES.new(key, AES.MODE_GCM,\
                       nonce=b"0000000000000001", mac_len=16)
##    - 2. encryption, authentication
ciphertext, icv = \
  alice_cipher.encrypt_and_digest(alice_plaintext)

print("The encrypted message sent by Alice to Bob is:")
print("    - ciphertext: %s"%hexlify(ciphertext))
print("    - icv: %s"%hexlify(icv))
print("    - nonce: %s"%hexlify(alice_cipher.nonce))

#Getting the size of nonce
print("Size of nonce is: %s"%len(alice_cipher.nonce))

## Bob
bob_cipher = AES.new(key, AES.MODE_GCM,\
                     nonce=alice_cipher.nonce,\
                     mac_len=16)

bob_plaintext = \
  bob_cipher.decrypt_and_verify(ciphertext, icv)
print("Bob plaintext is: %s"%bob_plaintext)

