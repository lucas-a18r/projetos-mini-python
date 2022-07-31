print("---CALCULADORA BÁSICA---")

opcao = input("\nEscolha uma opção: \n + somar \n - subtrair \n * multiplicar \n / dividir \n\n Digite O Sinal Aqui: ")

numero1 = int(input("\nDigite O primeiro valor: "))
numero2 = int(input("\nDigite O segundo valor: "))

if opcao == '+':
    print('\nresultado é:',numero1 + numero2) # para o código ficar organizado, coloquei desta forma!
elif opcao == '-':
    print('\nresultado é:',numero1 - numero2)
elif opcao == '*':
    print('\nresultado é:',numero1 * numero2)
elif opcao == '/':
    print('\nresultado é:',numero1 / numero2)
else:
    print("\ndigite um valor válido!") # depois faço uma funçao, para dar uma melhorada.