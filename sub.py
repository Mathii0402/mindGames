#!/usr/bin/python3
import subprocess
svc = "sshd"
check_process = subprocess.call(["ps","-C",svc])
if check_process==0:

	print("process is active")
	subprocess.call(["systemctl","close","sshd"])
#	subprocess.call(["ps","-C",svc])
	print("is inactive")
else:
	print("process is inactive")
	subprocess.call(["systemctl","start","sshd"])
	print("is alive")
#	subprocess.call(["ps","-C",svc])
