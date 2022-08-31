import pickle
stu = {}                         # declare empty dictionary object to hold read records
found = False
fin = open('Stu.dat','rb+')      # open binary file in read and write mode
# read from the file
try:
    while True:
        rpos = fin.tell()
        stu = pickle.load(fin)
        if stu['Roll no'] == 12:
          stu['Name'] = 'Gurnam'
          fin.seek(rpos)
          pickle.dump(stu,fin)
          found = True
except EOFError:
    if found == False:
        print('Sorry, no match found.')
    else:
        print('Record Succesfully updated.')
    fin.close()