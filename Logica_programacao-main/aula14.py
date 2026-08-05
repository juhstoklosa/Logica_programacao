nota = float(input("Digite a nota:"))

while nota < 5:
    print("Nota inválida!")
    nota = float(input("Digite a nota: "))

print(f"Nota Registrada {nota}")