from functions import *
a=['1','2','3']
b=['4','5','6']
c=['7','8','9']
cen=0
cor=0
edg=0
z=0
print a,'\n',b,'\n',c
for i in range(9) :
    #turn check
    if i%2==0 :
        print 'Computer`s Turn'
        #turn Computer
        if i==0 :
            c[0]='X'
        
        if comp_col(a,b,c) :
            print 'Computer Wins'
            z+=1
            break
        elif comp_row(a,b,c) :
            print 'Computer Wins'
            z+=1
            break
        elif comp_dia(a,b,c) :
            print 'Computer Wins'
            z+=1
            break
        
        if i==8 and z==0:
            print 'Match Ty'
            break

        #if i<2:
            #for i in range(1):
        
                
        if i<6:
            #center condition
            if cen>0:
                if a[0]=='X' :
                    c[2]='X'
                elif a[2]=='X' :
                    c[0]='X'
                elif c[0]=='X' :
                    a[2]='X'
                elif c[2]=='X' :
                    a[0]='X'
                if a[0]=='O' :
                    c[2]='X'
                elif a[2]=='O' :
                    c[0]='X'
                elif c[0]=='O' :
                    a[2]='X'
                elif c[2]=='O' :
                    a[0]='X'
                

        #edge condition
        if edg>0:
            if a[1]=='O' or b[0]=='O' or b[2]=='O' or c[1]=='O':
                if i<2:
                    if c[0]=='X' and c[1]=='O' and a[2]!='X':
                        a[2]='X'
                    elif c[0]=='X' and c[1]=='O' and a[0]!='X':
                        a[0]='X'
                    if c[0]=='X' and b[0]=='O' and a[2]!='X':
                        a[2]='X'
                    elif c[0]=='X' and b[0]=='O' and c[2]!='X':
                        c[2]='X'
                #corner condition
        if a[0]=='O' or a[2]=='O' or b[0]=='O' or b[2]=='O' or c[0]=='O' or c[2]=='O' :
            if a[2]!='O' and a[2]!='X':
                a[2]='X'
                
            elif a[0]!='O' and a[0]!='X':
                a[0]='X'
                
            elif c[0]!='X' and c[0]!='O':
                c[0]='X'
                
            elif c[2]!='X' and c[2]!='O':
                c[2]='X'
        print a,'\n',b,'\n',c
        i+=1
    else:
        print 'Player`s Turn'
        #location validity
        x=input('Enter Location : ')
        
        if x<=3:
            if a[x-1]=='X' or a[x-1]=='O':
                print " invalid location"
                continue
            a[x-1]='O'
        elif x<=6:
            if b[x-4]=='O' or b[x-4]=='X':
                print " invalid location"
                continue
            b[x-4]='O'
            center = x-1
            if center==4 :
                cen+=1;
        
        elif x<=9:
            if c[x-7]=='X' or c[x-7]=='O':
                print " invalid location"
                continue
            c[x-7]='O'
        if a[1]=='O' or b[0]=='O' or b[2]=='O':
            edg+=1
        
                
        
        check_col(a,b,c)
        check_row(a,b,c)
        check_diag(a,b,c)
        i+=1
        print a,'\n',b,'\n',c

    
   
        
print 'Game Over'
        
    
               
