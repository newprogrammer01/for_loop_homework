def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    a=0
    
    list=[]
    while  a<N:
        list=list+[a+1]
        a+=1
    return list
print(main(9))

