print('Bem-vindo a loja da Raiany Cristina!')

# variáveis:
valor_produto = float(input('Coloque o valor do produto: '))
quantidade_produto = int(input('Coloque a quantidade desejada: '))
desconto_produto = 0

# Até 9, 0% de desconto:
if quantidade_produto <= 9:
  desconto_produto = 0.00

# Entre 10 e 99, 5% de desconto:
elif 10 <= quantidade_produto < 100:
  desconto_produto = 0.05
  print('(Desconto 5%)')

# Entre 100 e 999, 10% de desconto:
elif 100 <= quantidade_produto < 1000:
  desconto_produto = 0.10
  print('(Desconto 10%)')

# De 1000 para mais, 15% de desconto:
else:
  desconto_produto = 0.15
  print('(Desconto 15%)')

# Calculando o total sem desconto:
sub_total = valor_produto * quantidade_produto
print('O valor total sem desconto foi: R$ {:.2f}' .format(sub_total))

# Calculando o total com desconto:
total_desconto = sub_total - sub_total * desconto_produto
print('O valor total com desconto é de: R$ {:.2f}' .format(total_desconto))