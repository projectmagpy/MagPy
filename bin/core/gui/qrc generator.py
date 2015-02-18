import os
dir = raw_input("Enter image directory name: ")
open(dir+".qrc", "w").write("<!DOCTYPE RCC><RCC version=\"1.0\">\n\t<qresource>")
for i in os.listdir(dir):
	open(dir+".qrc","a").write("\n\t\t<file>"+dir+"/"+i+"</file>")
open(dir+".qrc", "a").write("\n\t</qresource>\n</RCC>")