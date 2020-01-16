from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

user_msg = "/root/Automation3/SIGNING/message.txt"

#with open (user_msg, "rb") as f:
#	message = f.read().replace('\n', '')

with open (user_msg, "rb") as f:
	message = f.read().encode("utf-8")

#f = open(user_msg, "rb")
key = RSA.import_key(open("/root/Automation3/SIGNING/private.pem").read())
h = SHA256.new(message)
#h = SHA256.new(message)
signature = pkcs1_15.new(key).sign(h)


print(signature)

signature_file = open("/root/Automation3/SIGNING/signature.txt", "wb")
signature_file.write(signature)
