# Ek program banao jo 1 se 100 tak ke beech mein woh numbers print kare jo 7 se divide ho jaate hain.

# WHILE LOOP
i=7
while i<=100:
    print(i)
    i+=7


i=1
while i<=100:
    if i%7==0:
        print(i)
    i+=1

# FOR LOOP

for i in range(7,100+1,7):
    print(i)


for i in range(1,100+1):
    if i%7==0:
        print(i)