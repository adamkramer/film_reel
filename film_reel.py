import subprocess
import sys
import time

full_list = []

while True:
	out = subprocess.check_output(sys.argv[2], shell=True)

	for each_line in out.splitlines():
		if each_line not in full_list:
			full_list.append(each_line)
			print time.strftime("%H:%M:%S") + " " + each_line

	time.sleep(float(sys.argv[1]))

