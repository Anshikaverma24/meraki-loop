# Yeh pattern print karo.

#
##
###
####
#####

# WHILE LOOP
i=1
while i<=5:
    j=1
    while j<=i:
     print("#", end=" ")
     j+=1
    print()
    i+=1

# FOR LOOP
for i in range(1,6):
    for j in range(1,i+1):
        print("#", end=" ")
    print()