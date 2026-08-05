#Função!

def primeira_funcao():
    print("Ola Aluno!")

def teste():
    print("Oi!")

primeira_funcao()
teste()
print("———————————————")

#Função Com Parâmetro!

def escreve_nome(nome):
    print(f"O nome é: {nome}")

escreve_nome("Julia")
escreve_nome("Stoklosa")

def calcula(n1,n2):
    total = n1 + n2
    print(f"O total é: {total}")

calcula(5, 12)
print("———————————————")

#Return!

def calcula(n1,n2):
    total = n1 + n2
    resultado = total
    return resultado

resultado = 0
resultado = calcula(5,12)
print(f"O total é: {resultado}")

def verifica(nota,aluno):
    if nota >= 7:
        resultado = "Aprovado!"
        msg_aluno(resultado,aluno)
    elif nota >= 6:
        resultado = "Em Recuperação!"
        msg_aluno(resultado,aluno)
    elif nota < 6:
        resultado = "Reprovado!"
        msg_aluno(resultado,aluno)
    return resultado

def msg_aluno(resultado,nome):
    print(f"Aluno(a): {nome} | está: {resultado}")

verifica(9, "Julia")

#Variáveis!

def calcula_resul(n1,n2):
    resultado = n1 + n2
    print(f"Resultado: {resultado}")

calcula_resul(33,74)
print("———————————————")

#Variáveis Globais!

resultado = 0

def calcula_resul(n1,n2):
    global resultado
    resultado = n1 + n2
    print(f"Resultado: {resultado}")

calcula_resul(33,74)

