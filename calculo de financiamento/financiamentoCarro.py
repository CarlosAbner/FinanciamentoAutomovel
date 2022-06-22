carro = float(input('valor do carro R$: '))
salario = float(input('seu salário: '))
anos = int(input('quantos anos: '))

#calculando os anos para pagar multiplicando por mes e dividindo pelo valor do carro
prestacao = carro / (anos * 12)

#calculando o salario do comprador e validando os 40% 
minimo = salario * 40 / 100
print('seu carro carro custa R${:.2f} e seu salario é de R${}'.format(carro, salario), end='')
print('A prestacao do carro ficará R${}'.format(prestacao))

#validando se é possivel a compra do veiculo se nao atingir os 40% do salario do comprador 
if prestacao <= minimo:
	print('Solicitcao de compra APROVADA')
else:
	print('Solicitcao de compra NEGADA')
