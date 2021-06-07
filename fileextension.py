name=input("Input the Filename:")#Give the filename
file_extns=name[name.rfind("."):]
myDict={
        ".py":"Python",
        ".txt":"Text",
        ".jpg":"Image",
        ".cpp":"C++",
        ".c":"C",
        ".java":"Java"
       }                        #The following filenames' gives respected extensions
print("The extension of the file is:",myDict[file_extns])

