import random
def traco():
    print("==============================================================")

traco()
print("                Jogo pedra, papel e tesoura")
traco()
voce = 0
pc = 0

while voce < 3 and pc < 3:
    jogada = input("pedra, papel ou tesoura? ")
    maquina = random.choice(["pedra", "papel", "tesoura"])
    print("Máquina:", maquina)

    if jogada == maquina:
        print("Empate")
        traco()
    elif (jogada == "pedra" and maquina == "tesoura") or (jogada == "papel" and maquina == "pedra") or (jogada == "tesoura" and maquina == "papel"):
        voce += 1
        traco ()
        print("Você ponto!")
        traco()
    else:
        pc += 1
        traco()
        print("Máquina ponto!")
        traco()

    print("Placar:", voce, "x", pc)
    traco()

if voce == 3:
    print("Você ganhou!")
else:
    print("A máquina ganhou!")
