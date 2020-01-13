import os
import subprocess

def check_sum():
	cmd = "sha1sum -c /root/Scripts/.sha1"
	return_value = subprocess.call(cmd, shell=True) # returned de exit code
	if return_value == 0:
		print("SHA1 sum is correct")
	else:
		print("Check failed")

check_sum()
