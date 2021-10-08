# Ek program banao jo 1 se 100 tak ke numbers ke saath yeh kare:

    # Jo 3 se divisible hain unki jagah "Nav" print kare

    # Jo 7 se divisible hain unki jagah "Gurukul" print kare

    # Jo 3 aur 7 dono se divisible hain, unki jagah "NavGurukul" print karein

    # Jo upar wale teen cases mein nahi aate, unki jagah sirf number print karvao.
i=1
while i<=100:
    if i%3==0 and i%7==0:
        print("NAVGURUKUL")
    elif i%7==0:
        print("GURUKUL")
    elif i%3==0:
        print("NAV")
    else:
        print(i)
    i+=1