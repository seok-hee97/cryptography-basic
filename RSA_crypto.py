# https://www.thesecuritybuddy.com/cryptography-and-python/how-to-encrypt-and-decrypt-data-in-python-using-the-rsa-module-of-pycryptodome/2/



#https://stackoverflow.com/questions/44223479/how-to-use-rsa-or-similar-encryption-in-python-3

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
# from Crypto.Cipher import PKCS1_v1_5  is broken
from Crypto.Random import new as Random
from base64 import b64encode
from base64 import b64decode

class RSA_Cipher:
  def __init__(self):
    # assert key_length in [1024,2048,4096]
    key_length = 2048
    rng = Random().read
    self.key = RSA.generate(key_length,rng)

#   def generate_key(self,key_length):
#     # assert key_length in [1024,2048,4096]
#     key_length = 2048
#     rng = Random().read
#     self.key = RSA.generate(key_length,rng)

  def encrypt(self,data):
    plaintext = b64encode(data.encode())
    rsa_encryption_cipher = PKCS1_OAEP.new(self.key)
    ciphertext = rsa_encryption_cipher.encrypt(plaintext)
    return b64encode(ciphertext).decode()

  def decrypt(self,data):
    ciphertext = b64decode(data.encode())
    rsa_decryption_cipher = PKCS1_OAEP.new(self.key)
    plaintext = rsa_decryption_cipher.decrypt(ciphertext,16)
    return b64decode(plaintext).decode()
  

cipher = RSA_Cipher()
# =cipher.generate_key(1024) #key length can be 1024, 2048 or 4096
ct=cipher.encrypt("hello world") #automatically uses generated key
# cipher.decrypt("nt3vNNqzyAo2SINPgsb/eOLU2PD0DF0EstvnIHUmYGX4CVAvS0pDEboqGcuitYAzSV10Ii+fliwihu/L0ISrL6w/tRDQILHFM5PrN2pqzK+Lu6QHKUShFdQtikduo1KHXGlJNd25sVlDOhWAq/FK/67Yeoyz6fSP6PNXRjX7Q+Q=")
pt =cipher.decrypt(ct)