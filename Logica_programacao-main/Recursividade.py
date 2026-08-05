def contador(n):
    if n == -26:
        print("Fim!")
        return 
    print(n)
    contador(n-1)
    return

contador(5)

print("—————————————————————————————————————————")

def soma_ate(n):
    if n == 0:
        return 0
    print(n)
    return n+soma_ate(n-1)

resultado = soma_ate(5)
print(f"Soma de 1 até 5 é: {resultado}")