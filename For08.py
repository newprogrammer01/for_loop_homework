
def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    a=0
    b=0
    list=[]
    while a<N:
        list=list+[a+1]
        if list[a]>0:
            x=list[a]
            b+=1/x
        a+=1
    return b 
print(main(4))



