from functions import *
a=['1','2','3']
b=['4','5','6']
c=['7','8','9']
print 'HEELO PLAYER'
print "WELCOME TO TIC TOK GAME"
print 'X for computer and O for your'
print a,'\n',b,'\n',c,'\n'
i=0
y=0
l=[]
while i<9:
    if i==0:
        x=5
    else:
        x=value(a,b,c,y)
    for z in range(0,len(l)):
            if l[z]==x:
                x=check_pc(l)
                break
    l.append(x)
    if x<=3:
        a[x-1]='X'
    elif x<=6:
        b[x-4]='X'
    elif x<=9:
        c[x-7]='X'
    print 'Computer choose this'
    print a,'\n',b,'\n',c,'\n'
    if check_col(a,b,c) or check_row(a,b,c) or check_diag(a,b,c):
        break
    i+=1
    if  i==9:
        print "Match is tie"
        break
    y=input("enter the location for O ")
    if y<0 or y>9:
        y=check_range()
    for w in range(0,len(l)):
            if l[w]==y:
                y=check_overriden(l)
                break
    l.append(y) 
    if y<=3:
        a[y-1]='O'
    elif y<=6:
        b[y-4]='O'
    elif y<=9:
        c[y-7]='O'
    print a,'\n',b,'\n',c
    if check_col(a,b,c) or check_row(a,b,c) or check_diag(a,b,c):
        break
    i+=1
   
    
