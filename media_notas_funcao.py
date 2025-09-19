#Funçao que calcula a média de notas
def calcular_media(notas):
    total = sum(notas)
    media = total/len(notas)
    return media

#arredondar média
arrendondar_media = lambda media: round(media, 2)

#Lista de notas
notas = []

#Inserção de notas na lista
print("Insira as cinco notas do aluno abaixo.\n")
for nota in range(5):
    nota = float(input())
    notas.append(nota)

#Definição de média
media = calcular_media(notas)
media_arrendondada = arrendondar_media(media)

#Situação do estudante pelas notas
situacao = "Aprovado" if media_arrendondada >= 7 else "Reprovado"

#Resultado do estudante
print("Notas do Estudante:")
print(notas)
print("Média das notas:")
print(media_arrendondada)
print("Resultado na matéria:")
print(situacao)