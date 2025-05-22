palavra_correta = "python"
letra = ""
letras_acertadas = set()

while True:
    letra = input("Digite sua letra: ")

    while len(letra) > 1:
        letra = input("Digite só uma letra!")

    if letra in palavra_correta:
        letras_acertadas.add(letra)
    else:
        print("letra errada!")

    palavra_formada = ""
    for i in palavra_correta:
        if i in letras_acertadas:
            palavra_formada += i
        else:
            palavra_formada += "*"

        print("Palavra: ", palavra_formada)

    if palavra_formada == palavra_correta:
        print("Parabens, voce acertou a palavra: ", palavra_correta)
        break
