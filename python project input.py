k=[]
s=[]
subject_total = {}
def stu_marks(a,b,c,d,e):
    student = {
        'Name': a,
        'Roll': b,
        'Sub': c,
        'Marks': d,
        'TMarks': e
    }
    k.append(student)
    
n=int(input())
A=input("enter school name: ")
B=int(input("No.of students: "))
C=input("Section: ")
for i in range(n):
    a=input("enter student name: ")
    b=int(input("enter roll number: "))
    c=tuple(map(str,input("enter sub names: ").split()))
    d=list(map(int,input("enter marks: ").split()))
    e=sum(d)
    stu_marks(a,b,c,d,e)
print("School name: ",A)
print("No.of students: ",B)
print("Section: ",C)
print('\tName\t\tRoll.no\t\t\t\tsubjects\t\t\t\t\tMarks\t\tTotal marks')
for i in range(n):
    print(k[i])
    
for _ in range(len(c)):
    subject=c[i]
    marks=d[i]
    subject_total[subject]=subject_total.get(subject,0) + marks
    
max_marks=max(k,key=lambda x:x['TMarks'])
print('\nhighest marks')
print("name:",max_marks['Name'])
print("roll:",max_marks['Roll'])
print("sub:",max_marks['Sub'])
print("marks:",max_marks['Marks'])
print("Tmarks:",max_marks['TMarks'])
min_marks=min(k,key=lambda x:x['TMarks'])
print('\nlowest marks')
print("name:",min_marks['Name'])
print("roll:",min_marks['Roll'])
print("sub:",min_marks['Sub'])
print("marks:",min_marks['Marks'])
print("Tmarks:",min_marks['TMarks'])

print('\nhighest subject marks ')
for subject, total_marks in subject_total.items():
    print(subject,":",total_marks)

for i in range(n):
    l=k[i]['TMarks']
    s.append(l)
s.sort()
print('\nsorted total marks:',s)





























      
