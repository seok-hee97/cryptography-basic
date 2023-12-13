# https://stackoverflow.com/questions/44223479/how-to-use-rsa-or-similar-encryption-in-python-3

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256      #for HASH
from Crypto.Hash import HMAC, SHA256


class Hmac:

    def __init__(self, key):
        self.h = HMAC.new(key.encode(), digestmod=SHA256)

    def update(self, msg):
        self.h.update(msg.encode())
    
    def verify(self,tag):
        try:
            self.h.hexverify(tag)
            return True
        except ValueError:
            return False
        
    def print(self):
        return self.h.hexdigest()
    


class RSA_Cipher:
    def __init__(self):
        self.key = RSA.generate(2048)
        self.public_key = self.key.publickey()
        self.private_key = self.key

    def encrypt(self, plaintext):
        cipher = PKCS1_OAEP.new(self.public_key)
        ciphertext = cipher.encrypt(plaintext.encode())
        return ciphertext.hex()

    def decrypt(self, ciphertext):
        cipher = PKCS1_OAEP.new(self.private_key)
        decrypted_message = cipher.decrypt(bytes.fromhex(ciphertext)).decode()
        return decrypted_message

# 사용 예시
rsa_cipher = RSA_Cipher()
msg = "Hello, ChatGPT!"
encrypted_msg = rsa_cipher.encrypt(msg)
print("Encrypted Message:", encrypted_msg)
decrypted_msg = rsa_cipher.decrypt(encrypted_msg)
print("Decrypted Message:", decrypted_msg)




key = 'secret key'
msg = 'Hello'

h = Hmac(key)
h.update(msg)
tag = h.print()
isValid = h.verify(tag)

print('key : ' +key)
print('msg : ' +msg)
print('isValid : ' +str(isValid))
