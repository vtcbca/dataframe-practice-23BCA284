import csv
f=open("D:\\23BCA284\\sqlite3\\csv\\result.csv","r") 
r=csv.reader(f)
for i in r:
    print(i)

f.close()
#print marksheet

with open('D:\\23BCA284\\sqlite3\\csv\\result.csv','r') as f:
    reader = csv.DictReader(f)
    for i in reader:
        i1=float(i['sub1'])
        i2=float(i['sub2'])
        i3=float(i['sub3'])
        i4=float(i['sub4'])
        i5=float(i['sub5'])
        total=i1+i2+i3+i4+i5
        per=total/5
        print(f"sid: {i['sid']}\t   Name: {i['sname']}\t   Total: {total}\t    Percentage: {per}")
          
