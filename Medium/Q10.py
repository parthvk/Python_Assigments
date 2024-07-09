#We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must have more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.

def stone_piles(n):
    piles = []
    for i in range(0, n):
        piles.append(2*i + n)
    return piles

print(stone_piles(6))