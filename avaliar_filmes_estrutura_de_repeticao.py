#Avaliador de filmes
filmes = ["A","B","C","D","E"]

print("Classificação de filmes")
print("Dê nota de 1 a 5 ou selecione 0 para encerrar")

#Loop de seleção de filmes a avaliar
for filme in filmes:
        classificacao = input (f"{filme} de 1 a 5? (ou 0 para parar): ")
        #Encerra a avaliação
        if classificacao == '0':
            print("Classificação encerrada.\n")
            break
        #converte classificação para inteiro
        classificacao = int(classificacao)
        
        #Solicita nota para o filme selecionado
        if classificacao < 1 or classificacao > 5:
            print("Selecione uma nota válida!")
        else:
            print(f"{filme} com {classificacao} estrelas.\n")

#Encerra a avaliação
print("Obrigado por avaliar os filmes.")