# Variáveis de entrada
nome_do_heroi = input("Digite o nome do herói: ")  # Solicita o nome do herói ao usuário
xp_do_heroi = int(input("Digite a quantidade de experiência do herói: "))  # Solicita a experiência do herói ao usuário e converte para inteiro

# Estrutura de decisão para determinar o nível do herói
if xp_do_heroi < 1000:
    nivel_do_heroi = "Ferro"
elif 1001 <= xp_do_heroi <= 2000:
    nivel_do_heroi = "Bronze"
elif 2001 <= xp_do_heroi <= 5000:
    nivel_do_heroi = "Prata"
elif 6001 <= xp_do_heroi <= 7000:
    nivel_do_heroi = "Ouro"
elif 7001 <= xp_do_heroi <= 8000:
    nivel_do_heroi = "Platina"
elif 8001 <= xp_do_heroi <= 9000:
    nivel_do_heroi = "Ascendente"
elif 9001 <= xp_do_heroi <= 10000:
    nivel_do_heroi = "Imortal"
else:
    nivel_do_heroi = "Radiante"

# Saída
print(f"O Herói de nome {nome_do_heroi} está no nível de {nivel_do_heroi}")
