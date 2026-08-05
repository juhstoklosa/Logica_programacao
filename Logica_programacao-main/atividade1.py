playlist =['Vem cá','Latino Americano','Papoulas', 'Flamingos',
           'Imprevisto']
n = 0
print(f"As músicas são: {playlist}")

print("----------------Minha Playlist----------------")
for i in playlist:
    n +=1
    print(f"Música {n}. -> {i}")

print("------------------------------")
print(f"Total: {len(playlist)} faixas")
