import csv
fh = open("Student.csv", "w")
stuwriter = csv.writer(fh)
stuwriter.writerow([ 'Rollno', 'Name', 'Marks'])
for i in range(5):
    print("Student record", (i+1))
    rollno = int(input("Enter rollno:"))
    name = input("Enter name:")
    marks = float(input("Enter marks: "))
    sturec = [rollno, name, marks]
    stuwriter.writerow(sturec)
fh.close()