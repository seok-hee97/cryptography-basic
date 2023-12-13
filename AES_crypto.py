# # # https://velog.io/@t1mmy_t1m/Python%EC%9C%BC%EB%A1%9C-AES-%EC%95%94%ED%98%B8%ED%99%94
# # from Crypto.Cipher import AES
# # from secrets import token_bytes

# # key = token_bytes(16)

# # def encrypt(msg):
# #     cipher = AES.new(key, AES.MODE_CFB)
# #     nonce = cipher.nonce
# #     ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
# #     return nonce, ciphertext, tag

# # def decrypt(nonce, ciphertext, tag):
# #     cipher = AES.new(key, AES.MODE_CFB, nonce=nonce)
# #     plaintext = cipher.decrypt(ciphertext)
# #     try:
# #         cipher.verify(tag)
# #         return plaintext.decode('ascii')
# #     except:
# #         return False

# # nonce, ciphertext, tag = encrypt(input('Enter a message: '))
# # plaintext = decrypt(nonce, ciphertext, tag)
# # print(f'Cipher text: {ciphertext}')
# # if not plaintext:
# #     print('Message is corrupted')
# # else:
# #     print(f'Plain text: {plaintext}')


# from Crypto.Cipher import AES
# from Crypto.Cipher import get_random_bytes
# from Crypto.Util.Padding import pad, unpad

# # bs :block size
# pt= pad(msg.encode(),self.bs)
# iv= get_random_bytes(16)
# cipher = AES.new(self.sk, AES.MODE_CBC)


# class AESCipher:

#     def __init__(self, bs):
#         self.bs = bs
#         self.sk = #generate secret key

#     def encrypt(self, msg):
#         raw = pad(raw)
#         iv = Random.new().read( AES.block_size )
#         cipher = AES.new( self.key, AES.MODE_CBC, iv )
#         return base64.b64encode( iv + cipher.encrypt( raw.encode('utf-8') ) )

#     def decrypt(self, ct):
#         pass

# msg = "hello"
# aes = AESCipher()
# ct = aes.encrypt(msg)
# pt = aes.decrypt(ct)

# print(str(ct))
# print(str(pt))

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class AESCipher:
    def __init__(self, key):
        # self.bs = 16        #block size
        self.bs = AES.block_size
        self.sk = key
        self.iv = get_random_bytes(16)

    def encrypt(self, msg):
        pt = pad(msg.encode(), self.bs)
        # iv = get_random_bytes(16)
        cipher = AES.new(self.sk, AES.MODE_CBC, self.iv)
        enc = cipher.encrypt(pt)
        # return iv + ct
        return enc
    
    def decrypt(self, enc):
        ct =base64.b64decode(enc)
        self.iv = ct[:16]
        cipher = AES.new(self.sk, AES.MODE_CBC, self.iv)
        pt = unpad(cipher.decrypt(ct[16:]))
        # pt = cipher.decrypt(ct)
        return pt

# 사용법 예시
key = get_random_bytes(16)  # 16바이트 (128비트)의 무작위 키 생성
msg = "Hello, JenSeop!"     # 암호화할 메시지
cipher = AESCipher(key)     # AESCipher 객체 생성

# 암호화
encrypted = cipher.encrypt(msg)
print("암호문:", encrypted)

# 복호화
decrypted = cipher.decrypt(encrypted)
print("복호화된 평문:", decrypted)




# from Crypto.Random import get_random_bytes
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad

# class AESCipher:
#     def __init__(self, key):
#         self.bs = 16
#         self.sk = key

#     def encrypt(self, msg):
#         pt = pad(msg.encode(), self.bs)
#         iv = get_random_bytes(16)
#         cipher = AES.new(self.sk, AES.MODE_CBC, iv)
#         ct = cipher.encrypt(pt)
#         return iv + ct

#     def decrypt(self, ct):
#         iv = ct[:AES.block_size]
#         cipher = AES.new(self.sk, AES.MODE_CBC, iv)
#         pt = unpad(cipher.decrypt(ct[AES.block_size:]), self.bs).decode()
#         return pt

# # 사용법 예시
# key = get_random_bytes(16)  # 16바이트 (128비트)의 무작위 키 생성
# msg = "Hello, JenSeop!"     # 암호화할 메시지
# cipher = AESCipher(key)     # AESCipher 객체 생성

# # 암호화
# encrypted = cipher.encrypt(msg)
# print("암호문:", encrypted)

# # 복호화
# decrypted = cipher.decrypt(encrypted)
# print("복호화된 평문:", decrypted)