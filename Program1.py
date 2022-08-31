import pickle
stu = {}                                            # declaring an empty dictionary
stufile = open('stu.dat', 'ab')                     # opening the file
# get data to write onto the file
ans = 'y'
while ans == 'y':
    rno = int(input('Enter Roll number : '))
    name = (input('Enter Name : '))
    marks  = (input('Enter Marks : '))
    # add read data into dictionary
    stu['Roll no'] = rno
    stu['Name'] = name
    stu['Marks'] = marks
    # writing into the file
    pickle.dump(stu,stufile)
    ans = input('More records ?  (Y/N) ......')
stufile.close()       # closing the file
