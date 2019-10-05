def check_col(a,b,c) :
    
    for i in range(3) :
        if a[i]==b[i]==c[i] :
            print a[i] , " winner"
         
            return 1
        else :
            return 0;

def check_row(a,b,c) :
    for i in range(1):
        if a[i]==a[i+1]==a[i+2] :
            print a[i] , " winner"
        
            return 1

        elif b[i]==b[i+1]==c[i+2] :
            print b[i] , " winner"
          
            return 1

        elif c[i]==c[i+1]==c[i+2] :
            print c[i], " winner"
        
            return 1

        else :
            return 0;

def check_diag(a,b,c) :
    for i in range(1) :
        if a[i]==b[i+1]==c[i+2] :
            print a[i] , " winner"
            return 1
        
        elif a[i+2]==b[i+1]==c[i] :
            print a[i+2] , " winner"
            
            return 1
        else :
            return 0;

def comp_col(a,b,c) :
    p=0
    for i in range(3):
        if a[i]==b[i] and c[i]!='O' :
            p+=1
            c[i]='X'
            break
        elif a[i]==c[i] and b[i]!='O':
            p+=1
            b[i]='X'
            break
        elif b[i]==c[i] and a[i]!='O':
            p+=1
            a[i]='X'
            break
            #print a[i] , ' Computer Wins'
    if p>0:
        print a,'\n',b,'\n',c
        return 1  

def comp_row(a,b,c) :
    r=0
    for i in range(1):
        if a[i]==a[i+1] and a[i+2]!='O' and a[i+2]!='X':
            #print a[i] , ' Computer Wins'
            r+=1
            a[i+2]='X'
            break
        elif a[i]==a[i+2] and a[i+1]!='O' and a[i+1]!='X' :
            r+=1
            a[i+1]='X'
            break
        elif a[i+1]==a[i+2] and a[i]!='O' and a[i]!='X' :
            r+=1
            a[i]='X'
            break
        #elif b[i]==b[i+1] and b[i+2]!='O' and b[i+2]!='X' :
            #print b[i] , ' Comouter Wins'
            #r+=1
            #b[i+2]='X'
            #break
       # elif b[i+2]==b[i+1] and b[i]!='O' and b[i]!='X' :
            #print b[i] , ' Comouter Wins'
            #r+=1
            #b[i]='X'
            #break
       # elif b[i]==b[i+2] and b[i+1]!='O' and b[i+1]!='X' :
            #print b[i] , ' Comouter Wins'
           ### b[i+1]='X'
            #break
        elif c[i]==c[i+1] and c[i+2]!='O' and c[i+2]!='X' : 
            #print c[i] , ' Computer Wins'
            r+=1
            c[i+2]='X'
            break
        elif c[i]==c[i+2] and c[i+1]!='O' and c[i+1]!='X' : 
            #print c[i] , ' Computer Wins'
            r+=1
            c[i+1]='X'
            break
        elif c[i+1]==c[i+2] and c[i]!='O' and c[i]!='X' : 
            #print c[i] , ' Computer Wins'
            r+=1
            c[i]='X'
            break
    if r>0:
        print a,'\n',b,'\n',c
        return 1

def comp_dia(a,b,c) :
    d=0
    for i in range(1):
        if a[i+2]==b[i+1] :
            if c[i]!='O' :
                #print a[i+2] , " a2Computer wins"
                d+=1
                c[i]='X'
                break
        elif a[i+2]==c[i]:
            if b[i+1]!='O':
                #print a[i+2] , ' b1Computer wins'
                d+=1
                b[i+1]='X'
                break
        elif c[i]==b[i+1] :
            if a[i+2]!='O' :
                #print c[i] , " a2Computer wins"
                d+=1
                a[i+2]='X'
                break
        elif a[i]==b[i+1] :
            if c[i+2]!='O' :
                #print a[i] , " c2Computer wins"
                d+=1
                c[i+2]='X'
                break
        elif a[i]==c[i+2]:
            if b[i+1]!='O':
                #print a[i] , ' b1Computer Wins'
                d+=1
                b[i+1]='X'
                break
        elif c[i+2]==b[i+1] :
            if a[i]!='O' :
                #print c[i+2] , " c2 Computer wins"
                d+=1
                a[i]='X'
                break
    if d>0:
        print a,'\n',b,'\n',c
        return 1
        
        
