def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    a=0
    b=0
    r=range(A,B)
    while a<len(r):
        if r[a]%1==0:
            x=r[a]
            b+=x
        a+=1
    return b 
print(main(-6,8))




    
  
