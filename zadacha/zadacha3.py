a=0b1
b=int(input("Vuvedi chislo"))
c=int(input("Poziciq za proverqvane"))
a=a<<c
check=a&b
if(check!=0):
    print("Chisloto: "+str(b)+" ïma edinica v binaren zapis na poziciq: "+str(c))
else:
    print("Chisloto: "+str(b)+" nqma edinica v binaren zapis na poziciq: "+str(c ))

