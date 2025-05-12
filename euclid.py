def euclid(a: int, b:int) -> int:
    while a != 0 and b != 0:
        if a >= b:
            a = a - b
        else:
            b = b - a
    if a != 0:
        return a
    else:
        return b
    
print("Ingrese número A:")
a = int(input())
print("Ingrese número B:")
b = int(input())
print(f"El mayor común divisor de {a} y {b} es {euclid(a,b)}.")
