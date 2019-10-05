def check_row(a,b,c):
    for i in range(1):
        if a[i]==a[i+1]==a[i+2]:
            print a[i],'in a'
            return 1
            break
        elif b[i]==b[i+1]==b[i+2]:
            print b[i],'in b'
            return 1
            break
        elif c[i]==c[i+1]==c[i+2]:
            print c[i],'in c'
            return 1
            break 
def check_col(a,b,c):
    for i in range(3):
        if a[i]==b[i]==c[i]:
            print a[i],'in column',i
            return 1
            break
def check_dia(a,b,c):
    for i in range(1):
        if a[i]==b[i+1]==c[i+2]:
            print a[i],'in diagonal',i
            return 1
            break
        if a[i+2]==b[i+1]==c[i]:
            print c[i],'in diagonal',i+2
            return 1
            break
import random
a=['1','2','3']
b=['4','5','6']
c=['7','8','9']
x=[]
i=0
k=0
r=5
z=0
y=1
x.append(5)
b[1]='O'
print a
print b
print c
while(k<9):
    if i==0:
        print 'ENTER PLAYER X'
        p='X'
        u=input()
        if u in x :
            print "invalid entry"
            y=0
        elif i==0:
            x.append(u)
            k=k+1
            if u<=3:
                a[u-1]=p
            elif u<=6:
                b[u-4]=p
            elif u<=9:
                c[u-7]=p
            if check_row(a,b,c)==1 or check_col(a,b,c)==1 or check_dia(a,b,c)==1:
                print 'PLAYER ',p,'wins'
                break
            i=1
            y=1
        if i==1 and y==1:
            p='O'
            if k==1:
                j=u
                if u%2==1:
                    if u==1 or u==9:
                        r=7
                    else:
                        r=1
                if u%2==0:
                    r=1
            if k==2:
                if j==1 or j==9:
                    if 3 not in x:
                        r=3
                    else:
                        if j==1:    
                            r=2
                        if j==9:
                            r=6
                if j==3 or j==7:
                    if 9 not in x:
                        r=1
                    else:
                        if j==3:
                            r=6
                        if j==7:
                            r=8
                if j%2==0:
                    if 9 not in x:
                        r=9
                    else:
                        if j==6 or j==4:
                            r=3
                        if j==2 or j==8:
                            r=7
            if k==3:
                if j==1 or j==7:
                    if 8 not in x:
                        r=8
                    if 2  not in x:
                        r=2
                    else:
                        r=4
                if j==9 or j==3:
                    if 4 not in x:
                        r=4
                    else:
                        r=8
                if j==2 or j==8:
                    if 4 in x:
                        r=3
                    else:
                        r=4
                if j==4 or j==6:
                    if 2 in x:
                        r=7
                    else:
                        r=2
            else:
                while r in x:
                    r=random.randint(1,9)
                print r
            x.append(r)
            if r<=3:
                a[r-1]=p
            elif r<=6:
                b[r-4]=p
            elif r<=9:
                c[r-7]=p
            print a
            print b
            print c
            if check_row(a,b,c)==1 or check_col(a,b,c)==1 or check_dia(a,b,c)==1:
                print 'COMPUTER wins'
                break
            i=0
            
            if k==4:
                print "draw "
                break
print a
print b
print c

