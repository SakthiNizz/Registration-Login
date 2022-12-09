def valid(s):
    a = s.split('@')
    if len(a)>1:
        l=[]
        for e in a[0]:
            z = e.islower()
            if z == True:
                l.append(1)
            else:
                l.append(0)
        if len(set(l)) == 1:
            b = a[1]
            c = b.split('.')
            if len(c[0])>4:
                if c[1]=='com' or c[1]=='in':
                    print('Your E-Mail valid Successfully!')
            else:
                print('Invalid E-Mail Id!')
                print("Please Enter the valid Mail!")
                mail()
        else:
            print('Invalid E-Mail Id!')
            print("Please Enter the valid Mail!")
            mail()
    else:
        print('Invalid E-Mail Id!')
        print("Please Enter the valid Mail!")
        mail()
def mail():
    b = input("Enter the E-Mail id : ")
    valid(b)
    return b
