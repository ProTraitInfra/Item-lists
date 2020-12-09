import os
import subprocess

for xlsFile in os.listdir(os.getcwd()):
    if xlsFile.endswith('.xlsx'):
       csvFile = xlsFile[0:-5] + ".csv"
       cmd =["in2csv", xlsFile, ">", csvFile, "-I", "--write-sheets -"]
       subprocess.call( ' '.join(cmd), shell=True)
       print("Converting file: " + xlsFile[0:-5])