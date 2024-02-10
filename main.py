#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    import math 
    if len(list1) != len(list2):
        return 'error'
    else:
        products = []
        list1 = list1.replace(' ','')
        list2 = list2.replace(' ','')
        for a, b in zip(list1, list2):
            products.append(int(a) * int(b))
        return sum(products)





if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    list1 = input()
    list2 = input()
    print(sum_of_products(list1, list2))
    #test