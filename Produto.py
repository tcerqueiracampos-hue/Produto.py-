produto = input ("digite o produto: ")
preco = float(input ("qual o preço do produto"))
desconto = (preco * 15 )/100
preco_final = preco - desconto

print(f"Produto: {produto}")
print(f"Preço: R$ {preco:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
