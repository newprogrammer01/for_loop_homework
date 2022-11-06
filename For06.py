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

    list1=[]
   
    while a<A:
        list1=list1+[a]
        if list1[a]%1==0:
            x=list1[a]
            b+=x
            a+=1
    
    list2=[]
    f=0
    p=0
    while f<B:
        list2=list2+[f]
        if list2[f]%1==0:
            y=list2[f]
            p+=y
            f+=1
    return p-b
print(main(-6,8))




    
  
