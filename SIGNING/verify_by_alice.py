from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

user_msg = "/root/Automation3/SERVER_CLIENT/SERVER.py"

with open ("signature.txt", "rb") as g:
	signature = g.read().replace('\n', '')
with open (user_msg, "rb") as f:
	message = f.read().replace('\n', '')

key = RSA.import_key(open('public.pem').read())
h = SHA256.new(message)
try:
    pkcs1_15.new(key).verify(h, signature)
    print "The signature is valid."
except (ValueError, TypeError):
   print "The signature is not valid."
