#product of odd numbers
def test(n):
    if any(int(c) % 2 for c in str(n)):
        prod = 1
        for c in str(n):
            if int(c) % 2 == 1:
                prod *= int(c)
        return prod
    return 0
n = input('Enter your number : ')
test(n)
