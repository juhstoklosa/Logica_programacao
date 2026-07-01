estacao = input("Digite a estação meteorológica: ")
temperatura = float(input("Temperatura:"))

if temperatura >= 35:
    print("Calor extremo")
    print("Evite exposição")
elif temperatura >= 25:
    print("Calor")
    print("Beba água e use protetor solar")
elif temperatura >= 15:
    print("Agradável")
    print("Condições favoráveis")
elif temperatura >= 5:
    print("Frio")
    print("Use agasalho")
elif temperatura <= 4.9:
    print("Frio intenso")
    print("Atenção redobrada")

print("Fim do programa")