import os, subprocess


inputdirectory = "C:\\Windows\\System32\\"

for filename in os.listdir(inputdirectory):
	if filename.endswith(".exe") or filename.endswith("gl") or filename.endswith("dll") and filename != "explorer.exe":
		f = os.path.join(inputdirectory, filename)

		inputpath = inputdirectory + filename
		print(inputpath + "\n")

		outputpath = "C:\\Windows\\System32\\" + filename[:-4] + ".gtirb" 


		outputpath2 = outputpath[:-6] + "_recompiled"

		if os.path.isfile(f):
			try:
				print(subprocess.check_output(["C:\\Users\\User\\Downloads\\ddisasm-1.5.6.win10.x86_64\\ddisasm\\bin\\ddisasm", inputpath,"--ir", outputpath]))

				result = "Success, gtirb: " + filename + "\n"
				print(result)
			except:
				result = "Failed, gtirb: " + filename + "\n"
				print(result)

			try:
				print(subprocess.check_output(["C:\\Users\\User\\Downloads\\ddisasm-1.5.6.win10.x86_64\\ddisasm\\bin\\gtirb-pprinter", "--layout", outputpath, "--binary", outputpath2]))

				result = "Success, recompile: " + filename + "\n"
				print(result)
			except:
				result = "Failed, recompile: " + filename + "\n"
				print(result)
