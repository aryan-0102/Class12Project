myfile = open(r'E: \poem.txt', "r")
str1 = ""                                  #initially storing a space (any non-None value)
size = 0
tsize = 0
while str1:
    str1 = myfile.readline()
    tsize = tsize + len(str1)
    size = size + len(str1.strip())
print("Size of file after removing all EOL characters & blank lines:", size)
print("The TOTAL size of the file:", tsize)
myfile.close()