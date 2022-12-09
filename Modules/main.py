from registration import reg
from mail import mail
from passwd import password
from cred import user
def main():
    print("Welcome to ABC center!")
    print("For Registration Press '1'")
    print("For Login press '2'")
    a = int(input())
    if a == 1:
        reg()
        b = mail()
        with open('mail.xlsx','a') as f:
            f.write(b)
            f.write('\n')
        print("Set Your Password")
        c = password()
        with open('password.xlsx','a') as f:
            f.write(c)
            f.write('\n')
        d = f'{b} {c}'
        with open('databse.xlsx','a') as f:
            f.write(d)
            f.write('\n')
    elif a == 2:
        m = input("Enter your E-Mail id : ")
        p = input("Enter your password : ")
        q = f'{m} {p}\n'
        with open('databse.xlsx','r') as f:
            z=0
            for e in f:
                if e == q:
                    z+=1
                else:
                    continue
            if z>0:
                print('Login Successfully!')
            else:
                print("User E-main id or Password Wrong!")
                user()  
    else:
        print("Invalid Choice...")  
        print("Please try again!")
        main()