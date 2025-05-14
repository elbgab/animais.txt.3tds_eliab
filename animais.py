animais = ["Leão", "Tigre", "Elefante", "Girafa", "Zebra"]

with open("animais.txt", "w") as file:
 
    for animal in animais:
        file.write(animal + "\n")
    