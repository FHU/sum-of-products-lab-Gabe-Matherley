#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
    import math 
    if len(list1) != len(list2):
        return 'error'
    else:
        products = []
        for a, b in zip(list1, list2):
            products.append(int(a) * int(b))
        return sum(products)





if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    num1 = input()
    num2 = input()
    print(sum_of_products(num1, num2))