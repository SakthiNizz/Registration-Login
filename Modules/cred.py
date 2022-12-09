from registration import reg
from mail import mail
from passwd import password
def user():
    print("Choose...")
    print("Forgotten Password Press '1' ")
    print("For New Registration Press '2' ")
    A = int(input())
    if A == 1:
        B = input('Enter your Registered E-Mail Id : ')
        C = f'{B}\n'
        with open('mail.xlsx','r') as f:
            z = 0
            for e in f:
                print(e)
                if C == e:
                    z+=1
                else:
                    continue
            if z>=1:
                print("E-Mail id verified!")
                print("Please Enter the new password")
                D = password()
                E = f'{D}\n'
                with open('password.xlsx','r') as f:
                    z=0
                    for e in f:
                        if E == e:
                            z+=1
                        else:
                            continue
                    if z>=1:
                        print("This password Already Exist!")
                    else:
                        print("Password set Successfully!")
                        R = f'{B} {D}\n'
                        with open('databse.xlsx','a') as f:
                            f.write(R)
                        with open('mail.xlsx','a') as f:
                            f.write(C)
                        with open('password.xlsx','a') as f:
                            f.write(E)

            else:
                print("E-mail id Does'nt Exist!")
                print("Please go for new Registration ")
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
    elif A == 2:
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
    else:
        print('Invalid Choice...')
        print('Please try again!')
        user()