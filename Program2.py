myfile = open('Answer.txt', 'r')
ch = ' '
lcount = 0
ucount = 0
while ch:
    ch = myfile.read(1)
    if ch.isupper():
        ucount = ucount + 1
    else:
        lcount = lcount + 1
print('Number of Uppercase letters : ', ucount)
print('Number of Lowercase letters : ', lcount)
# close the file
myfile.close()
