def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    a=price
    b=10*price
    
    list=[]
    while a<b :
        list=list+[a]
        a+=price
    return list
print(main(2.25))