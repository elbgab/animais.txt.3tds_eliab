with open("animais.txt", "r") as file:
    
    animais = file.readlines()

for animal in animais:
    print(f"Animal: {animal.strip()}")