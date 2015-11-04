print ('---------------------------------------------------')
print ('------------CURRICULUM DE CANDIDATOS---------------')
print ('---------------------------------------------------')
curriculos = []
a = 'l'
quantidade_curriculos = int (input ("Digite a quantidade de curiculos a ser quardada: "))

while a != '0':

	print  ("Opção 1 - Criar curriculum")
	print  ("Opção 2 - Visualizar curriculo dos  canditato")
	print  ("Opção 3 - Visualizar curriculo de um canditato")
	print  ("Opção 0 - Sair programa")
			
	opcao = input ("Entre com uma das opções acima: ")

	if opcao == '1':
		
		for iquantidade_curriculo in range (quantidade_curriculos):
			curriculo = []
			nome = input ("Entre com o nome do candidato %i: " % (iquantidade_curriculo+1))
			curriculo.append (nome)
			endereço = input ("Entre com o endereço do candidato %i: " % (iquantidade_curriculo+1))
			curriculo.append (endereço)
			data_nacimento = input ("Entre com o data de nacimento do candidato %i: " % (iquantidade_curriculo+1))
			curriculo.append (data_nacimento)
			curriculos.append (curriculo)

	elif opcao == "2":

		pass

	elif opcao == '3':

		print ("Qual candidato deseja visualizar?")

		for iquantidade_curriculo in range (quantidade_curriculos):
			print ("Candidato %s numeração %d" % (curriculos [iquantidade_curriculo] [0], (iquantidade_curriculo + 1))
				
		#Com cada indice do "for" vai imprimir um candidato diferente com sua numeração em sequencia

        curriculo_individual = int (input ("Escolha um dos candidatos: "))

		print ('Nome: %s' %(curriculos [curriculo_individual] [0]))
		print ('Endereço: %s' %(curriculos [curriculo_individual] [1]))
		print ('Data de nacimento: %s' %(curriculos [curriculo_individual] [2]))
			
	elif opcao == '0':
		a = "0"
