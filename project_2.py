# Your second task now is to write a Python program to accept a filename from the user and print the extension of that.

fname = input("Enter the Filename with extension: ")
extn = fname.split(".")
print("The extension of ", fname, " is : " + extn[-1])
