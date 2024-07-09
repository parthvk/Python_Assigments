#A cafe has N computers. Several customers come to the cafe to use these computers. A customer will be serviced only if there is any unoccupied computer at the moment the customer visits the cafe. If there is no unoccupied computer, the customer leaves the cafe. 

#You are given an integer N representing the number of computers in the cafe and a sequence of uppercase letters S. Every letter in S occurs exactly two times. The first occurrence denotes the arrival of a customer and the second occurrence denotes the departure of the same customer if he gets allocated the computer. You have to find the number of customers that walked away without using a computer.

def customers_that_walked_away(N, S):
    count = 0
    customers = set()
    computers = set()
    for s in S:
        if s in customers:
            customers.remove(s)
            if s in computers:
                computers.remove(s)
        else:
            customers.add(s)
            if len(computers) < N:
                computers.add(s)
            else:
                count += 1
    return count

N = 3       
S = "GACCBDDBAGEE"
print(customers_that_walked_away(N, S))

N = 1       
S = "ABCBAC"
print(customers_that_walked_away(N, S))

