from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

user_msg = "/root/Automation3/SERVER_CLIENT/SERVER.py"

with open (user_msg, "rb") as f:
	message = f.read().replace('\n', '')
key = RSA.import_key(open("private.pem").read())
h = SHA256.new(message)
signature = pkcs1_15.new(key).sign(h)


#print(signature)

signature_file = open("signature.txt", "wb")
signature_file.write(signature)
