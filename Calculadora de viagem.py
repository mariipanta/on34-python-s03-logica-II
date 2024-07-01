"""
Pedir para o usuário descrever quantos km ele vai percorrer
Até 200km - R$0,75 por km
Até 500km - R$0,60 por km
Acima de 500km - R$0,50 por km
Não calcular abaixo de 50km 
Não pode incluir número negativo
Não pode caracter especiais
"""
km = input("Quantos km de distancia? ")

def calcula_viagem(km):
    try:
        km = int(km)
    except ValueError:
        return "não pode caracter especial"
    if km <0:
        return "proibido numero negativo"
    if km <50:
        return "lancar valor maior que 50km"

    preco_inicial = 20
    preco_por_km = 0
    if km <=200:
        preco_por_km = km*0.75
    elif km <=500:
        preco_por_km = km*0.60
    else:
        preco_por_km = km*0.50
    return preco_inicial + preco_por_km

print(calcula_viagem(km))
