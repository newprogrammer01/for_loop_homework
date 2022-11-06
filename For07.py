def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    list=[]
    a=0
    b=0
   
    while a<N:
         list=list+[a+1]
         if list[a]%2==1:
            x=list[a]
            b+=x

    
         a+=1

    return b
print(main(12))

