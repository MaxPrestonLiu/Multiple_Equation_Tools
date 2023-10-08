'''First need to build up abstraction of fractions,otherwise, not widely used'''
'''All calculation will be rationalized to fraction format, integers divided by 1'''
def simplifier(x):
    '''modify fraction to most simplified version'''
    n,d=x[0],x[1]
    if n<0 and d<0:
        n,d=-n,-d
    s,t=abs(n),abs(d)
    for m in range(1,min(s,t)+1):
        if n%m==0 and d%m==0:
            n,d=n//m,d//m
    return [n,d]

def adder(x,y):
    nx,dx=x[0],x[1]
    ny,dy=y[0],y[1]
    new_n,new_d=nx*dy+ny*dx,dx*dy
    return simplifier([new_n,new_d])

def multier(x,y):
    nx,dx=x[0],x[1]
    ny,dy=y[0],y[1]
    new_n,new_d=nx*ny,dx*dy
    return simplifier([new_n,new_d])

def divisor(x,y):
    nx,dx=x[0],x[1]
    ny,dy=y[0],y[1]
    new_n,new_d=nx*dy,dx*ny
    return simplifier([new_n,new_d]) 

def negativer(x):
    '''only negative the numerator here'''
    return [-x[0],x[1]]

def substier(x,y):
    return simplifier(adder(x,negativer(y)))

'''For number 0, we also need an expression of it's fraction'''
zero=[0,1]

'''Bulid a calculator for one degree multiple variable multiple equations'''


def do_for_all(f,s):
    '''calculate f(x) for all x in s, return new set'''
    return [f(x) for x in s]

def cut_one(c1,c2):
    ''' return 2 new lists of coefficient with one variable cut'''
    '''This is a generally applicable function no matter how many variable an equation has'''
    fractor=divisor(c1[0],c2[0])
    q=do_for_all(lambda x: multier(fractor,x),c2)
    return [substier(c1[i],q[i]) for i in range(0,len(c1))]

'''First to build a two variable equation calculator'''
def calculate(c1,c2):
    '''c1,c2 are two lists of coefficient'''
    new_list=cut_one(c1,c2)
    c=negativer(new_list[2])
    e=new_list[1]
    ans2=divisor(c,e)
    ans1=divisor(negativer(adder(c1[2],multier(c1[1],ans2))),c1[0])
    return [ans1,ans2]

'''Build more abstractions for next preparation'''
def slash_one(s):
    '''
    s is a list of lists of conefficients
    this aims to reduce number of variables'''
    with_0= [cut_one(s[i],s[i+1]) for i in range(0,len(s)-1)]
    without_0=[m[1:] for m in with_0]
    return without_0

def get_value(c,v):
    '''get value of one variable when the value of other variables all known'''
    '''c--->list of coefficients; v--->list of variable values'''
    '''Be aware that the variable corresponding to coefficient of c[-1] is always 1'''
    others=c[1:]
    compose=[multier(others[i],v[i]) for i in range(0,len(v))]
    total=[0,1]
    i=0
    while i<len(compose):
        total=adder(total,compose[i])
        i+=1
    return divisor(negativer(total),c[0])

'''Now can construct the general case with arbitrary number of variables'''

def final_calculator(s):
    ''' s is a set with this formality:
    s=[c1,c2,c3......]
    where c means a list of coefficients in each func
    if equation has n variables, then len(c) should be n+1
    '''
    if len(s)==1:
        return [get_value(s[0],[[1,1]]),[1,1]]
    else:
        new_s=slash_one(s)
        v=final_calculator(new_s)
        return [get_value(s[0],v)]+[t for t in final_calculator(new_s)]

def print_result(s):
    k=0
    solu=final_calculator(s)
    while k<len(solu)-1:
        if solu[k][1]==1 or solu[k][1]==-1:
            print("x",k+1,"=",(solu[k][0])*(solu[k][1]))
        elif solu[k][0] %solu[k][1]==0:
            print("x",k+1,"=",(solu[k][0])//(solu[k][1]))
        else:
            print("x",k+1,"=",solu[k][0],"/",solu[k][1])
        k+=1
