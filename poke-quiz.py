print("\n---Adivinhe essas questões relacionadas a Pokémon---\n")
pergunta1 = str(input("Qual o primeiro pokémon de Ash ? \n\n A - Pikachu \n B - \
Bulbasaur \n C - Charizard \n\n Digite A letra em MAIUSCULO: "))

def resposta1() : # função base
    if pergunta1 == "A" :
        print("\nParabéns, Você acertou!\n")
    elif pergunta1 == "B" :
        print("\nQue Pena, Você errou!\n")
    elif pergunta1 == "C" :
        print("\nQue Pena, Você errou!\n")

resposta1() # chamando a função!

# depois adiciono mais questões