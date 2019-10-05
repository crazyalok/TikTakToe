def check_col(a,b,c):
    for i in range(3):
        if a[i]==b[i]==c[i]:
            print a[i],'Congrats You are Winner'
            return 1
            break
def check_row(a,b,c):
    for i in range(1):
        if a[i]==a[i+1]==a[i+2]:
            print a[i],'Congrats You are Winner'
            return 1
            break
        elif b[i]==b[i+1]==b[i+2]:
            print b[i],'Congrats You are Winner'
            return 1
            break
        elif c[i]==c[i+1]==c[i+2]:
            print c[i],'Congrats You are Winner'
            return 1
            break
def check_diag(a,b,c):
    for i in range(1):
        if a[i]==b[i+1]==c[i+2]:
            print a[i],'Congrats You are Winner'
            return 1
            break
        elif c[i]==b[i+1]==a[i+2]:
            print c[i],'Congrats You are Winner'
            return 1
            break
     
def check_overriden(l):
     print "you enterd wrong index"
     s=input("enter again the location for ")
     for i in range(0,len(l)):
             if l[i]==s or s<0 or s>9:
                 s=check_overriden(l)
                 break
     return s
def check_range():
    print "you enterd wrong index"
    y=input("enter again the location for O")
    if y<0 or y>9:
        y=check_range()
    return y
def value(a,b,c,y):
    for i in range(3):
        if a[i]==b[i] and c[i]!='O' and c[i]!='X':
            return 7+i
            break 
        elif a[i]==c[i] and b[i]!='O' and b[i]!='X':
            return 4+i
            break
        elif b[i]==c[i] and a[i]!='O' and a[i]!='X':
            return 1+i
            break
    for i in range(1):
        if a[i]==b[i+1] and c[i+2]!='O' and c[i+2]!='X':
            return 9
            break
        elif a[i]==c[i+2] and b[i+1]!='O' and b[i+1]!='X':
            return 5
            break
        elif b[i+1]==c[i+2] and a[i]!='O' and a[i]!='X':
            return 1
            break
        elif a[i]==a[i+1] and a[i+2]!='O' and a[i+2]!='X' :
            return 3
            break
        elif a[i]==a[i+2] and a[i+1]!='O' and a[i+1]!='X':
            return 2
            break
        elif a[i+1]==a[i+2] and a[i]!='O' and a[i]!='X':
            return 1
            break
        elif a[i+2]==b[i+1] and c[i]!='O' and c[i]!='X':
            return 7
            break
        elif a[i+2]==c[i] and b[i+1]!='O' and b[i+1]!='X':
            return 5
            break
        elif b[i+1]==c[i] and a[i+2]!='O' and a[i+2]!='X':
            return 3
            break
        elif b[i]==b[i+1] and b[i+2]!='O' and b[i+2]!='X':
            return 6
            break
        elif b[i+1]==b[i+2] and b[i]!='O' and b[i]!='X':
            return 4
            break
        elif b[i]==b[i+2] and b[i+1]!='O' and b[i+1]!='X':
            return 5
            break
        elif c[i]==c[i+1] and c[i+2]!='O' and c[i+2]!='X':
            return 6
            break
        elif c[i+1]==c[i+2] and c[i]!='O' and c[i]!='X':
            return 4
            break
        elif c[i]==c[i+2] and c[i+1]!='O' and c[i+1]!='X':
            return 5
            break
    if y==1:
        return 5
    elif y==3:
        return 2
    elif y==8:
        return 4
    elif y==6:
        return 9
    elif y==5:
        return 1
    elif y==2:
        return 3
    elif y==4:
        return 7
    elif y==7:
        return 8
    elif y==9:
        return 6
    else:
        print'Devik'
import random
def check_pc(l):
    s=random.randint(1,9)
    for i in l:
        if s==i:
            s=check_pc(l)
        else:
            return s
                    
            
