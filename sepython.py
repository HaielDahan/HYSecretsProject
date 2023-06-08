import subprocess

def py_stegExpose():
	arr_steg = ['StegExpose.jar', 'testFolder', 'default', '0.3','check.csv']  # Any number of args to be passed to the jar file
	try:
		subprocess.call(['java', '-jar', arr_steg[0],arr_steg[1],arr_steg[2],arr_steg[3],arr_steg[4]])
	except:
		print("StegExpose - Error!")

	print("py_stegExpose finished")