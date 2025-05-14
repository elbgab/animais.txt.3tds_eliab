erros = ["x", "z", "k"]

with open("erros.txt", "w") as file:
    for erro in erros:
        file.write(erro + "\n")