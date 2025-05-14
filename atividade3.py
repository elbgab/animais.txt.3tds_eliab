import random

with open("animais.txt", "r") as file:
    animais = file.readlines()


animal_sorteado = random.choice(animais).strip()


print(f"Animal sorteado: {animal_sorteado}")