import os, subprocess


inputdirectory = "/bin/"


outputwriter = open("resultsOpenSource.txt", "w+")

for filename in os.listdir(inputdirectory):
	f = os.path.join(inputdirectory, filename)

	inputpath = "/bin/" + filename
	print(inputpath + "\n")
	outputwriter.write(inputpath + "\n")


	outputpath = "OpenSourceTests/" + filename + ".gtirb" 


	outputpath2 = outputpath[:-6] + "_recompiled"

	if os.path.isfile(f):
		try:
			print(subprocess.check_output(["sudo", "ddisasm", inputpath,"--ir", outputpath]))

			result = "Success, gtirb: " + filename + "\n"
			print(result)
			outputwriter.write(result)
		except:
			result = "Failed, gtirb: " + filename + "\n"
			print(result)
			outputwriter.write(result)


		try:
			print(subprocess.check_output(["sudo", "gtirb-pprinter", outputpath, "--binary", outputpath2]))

			result = "Success, recompile: " + filename + "\n"
			print(result)
			outputwriter.write(result)

		except:
			result = "Failed, recompile: " + filename + "\n"
			print(result)
			outputwriter.write(result)

outputwriter.close()
