print("*********Semester Attendance percentage calculator*********")
def calculator():
    att=[]
    t=[]
    k=1
    a=int(input("Enter no of total no of periods:"))
    while(k <=a):
        b=int(input("Enter attended hour duration for {} period:".format(k)))
        att.append(b)
        c=int(input("Enter total hour duration for {} period:".format(k)))
        t.append(c)
        k+=1
    total_att=sum(att)
    total=sum(t)
    return total_att,total
n=int(input("Enter total no of semester(1 or 2):"))
if(n==1):
    total_att1,total1=calculator()
    res=(total_att1/total1)*100
    print("Attendance percentage is : {} ".format(round(res,2)))
else:
    total_att1,total1=calculator()
    total_att2,total2=calculator()
    gtotal_att=total_att1+total_att2
    gtotal=total1+total2
    res=(gtotal_att/gtotal)*100
    print("Attendance percentage is : {} ".format(round(res,2)))

    



    
    
