def is_Prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return "Not prime number"
    return "Prime number"
print(is_Prime(int(input("Enter a number: "))))