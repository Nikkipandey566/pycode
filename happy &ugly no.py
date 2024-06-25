  #happy number and ugly number
def is_happy_number(n):
    def get_next(number):
        return sum(int(x) ** 2 for x in str(number))
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1

def is_ugly_number(n):
    if n <= 0:
        return False
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
    return n == 1
num = 27
print(f"Is {num} a happy number? {is_happy_number(num)}")
print(f"Is {num} an ugly number? {is_ugly_number(num)}")

