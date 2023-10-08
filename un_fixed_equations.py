def un_fix(n,c):
    '''RHS=c; LHS has n variables, coefficient of each variable is 1'''
    '''Only positive value returned'''
    if n==1:
        return [[c]]
    else:
        general=[]
        t=0
        while t<=c:
            pre_fix=un_fix(n-1,c-t)
            push_in=[[t]+pre_fix[i] for i in range(0,len(pre_fix))]
            general=general+push_in
            t+=1 #easy to forget this step
    return general

#Now try to build a printer function to print results in a human friendly format
def unfix_solution_printer(n,c):
    results=un_fix(n,c)
    n=1
    while n<=len(results):
        solu=results[n-1]
        print('solution',n)
        t=1
        while t<=len(solu):
            print("x",t,"\t",solu[t-1])
            t+=1
        n+=1

def unfix_solu_counter(n,c):
    '''count the number of solutions'''
    results=un_fix(n,c)
    print("solution numbers:",len(results)) 

#Now bulid a more powerful function allowing coefficient of variables do not equal to 1
def gene_unfixed(s,c):
    '''s is the set containing coefficient of each variablesin LHS; c is the constant in RHS'''
    if len(s)==1:
        if c%s[0]==0:
            return [[c//s[0]]]
        else:
            return None
    else:
        larg=c//s[0]
        t=0
        general=[]
        while t<=larg:
            pre_fix=gene_unfixed(s[1:],c-t*s[0])
            for pre in pre_fix:
                if pre!=None:
                    pre=[t]+pre
                    general.append(pre)
            t+=1
        return general
#Once again, try to build a printer function to print results in a human friendly format
def geunfix_printer(s,c):
    results=gene_unfixed(s,c)
    print("number of solutions:",len(results))
    n=1
    while n<=len(results):
        solu=results[n-1]
        print('solution',n)
        t=1
        while t<=len(solu):
            print("x",t,"\t",solu[t-1])
            t+=1
        n+=1