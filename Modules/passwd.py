def password():
    print("Password length must be 5 < password > 16")
    print("Must have minimum one special character")
    print("one digit, one uppercase, one lowercase character ")
    p = input()
    a,b,c=0,0,0
    if len(p)>=5:
        for e in p:
            s='[@_!#$%^&*()<>?/\|}{~:]'
            for i in s:
                if i == e:
                    c+=1
                else:
                    continue
            if e.islower()==True:
                a+=1
            elif e.isupper()==True:
                b+=1
            else:
                continue
        if a >= 1 and b >= 1 and c>=1:
            print("Password Set Successfully")
            return p
        else:
            print("Weak Password!")
            print("Try again...")
            password()
    else:
        print("Weak Password!")
        print("Try again...")
        password()