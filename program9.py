myfile = open('poem.txt','r')
ch =''
vcount = 0
ccount =0
while ch:
    ch = myfile.read(1)
    if ch in['a','A','e','E','i','I','o','O','u','U']:
        vcount = vcount+1
    else :
        ccount = ccount+1
print('Vowels in files :', vcount)
print('Consonants in the file :',ccount)
myfile.close()