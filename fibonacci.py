def calc_fibonacci(limit):
    num1 = 0
    num2 = 1
    result = 0

    while result <= limit:
        result = num1+num2
        num1 = num2
        num2 = result
        if result == limit:
            print(f"O número {limit} faz parte da sequência Fibonacci")
            return
    
    print(f"O número {limit} não faz parte da sequência Fibonacci")

calc_fibonacci(int(input("Digite um número: ")))
        
        

