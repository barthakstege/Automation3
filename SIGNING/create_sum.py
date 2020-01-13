import os
import subprocess

def create_sum():
	os.chdir("/root/")
	cmd = "sha1sum /root/Scripts/* > /root/Scripts/.sha1"
	return_value = subprocess.call(cmd, shell=True) # returned exit code
	if return_value == 0:
		print("Succesfully made a SHA1 sum!")
	else:
		print("Failed to make SHA1 sum. Please try again.")	

create_sum()
