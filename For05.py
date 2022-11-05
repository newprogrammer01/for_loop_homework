def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    r=range(A,B+1)
   
    f=B-A
    return list(r[f:0:-1])+[A]
print(main(5,9))




   



