# Ek loop banao jo user se 10 numbers ko input le. Input lene ke baad unn saare numbers ka sum print kare.

# WHILE LOOP

i=1
sum=0
while i <=10:
    userinput=int(input("enter the numbers"))
    sum=sum+userinput
    i+=1
print(sum)

# FOR LOOP

sum=0
for i in range(1,10+1):
    userinput=int(input("enter the numbers"))
    sum=sum+userinput
print(sum)