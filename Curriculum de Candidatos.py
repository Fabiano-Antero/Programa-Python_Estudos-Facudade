print                                                      ('---------------------------------------------------')
print                                                      ('------------CURRICULUM DE CANDIDATOS---------------')
print                                                      ('---------------------------------------------------')
curiculos = []

while a != '0':

	qtd_c = int (input ("Digite a quantidade de curiculos a ser quardada"))

	for iqtd_c in range (qtd_c):    

		print         ("Opção 1 - Criar curriculum")
		print         ("Opção 2 - Visualizar curriculo dos  canditato")
		print         ("Opção 3 - Visualizar curriculo de um canditato")
		print         ("Opção 4 - Sair programa")
			
		opcao = input ("Entre com uma das opções acima: ")

		if opcao == '1':
			curriculo = []
			for icc in range (qtd_c):
				print ('CANDIDATO %D' % (qtd_c + 1))
				nome_candidato = input 	(print ('Digite o nome do candidato %d: ' %(icc+1)) 
				data_nacimento = input	(print ('Digite a data de nacimento do candidato %d: ' %(icc+1)))
				endereço = input 		(print ('Digite o endereço do candidato %d: ' %(icc+1)))
				curriculo.append (nome_candidato, data_nacimento, endereço)
				curiculos.append (curriculo)

		elif opcao == '2':
				for ivc in range (qtd_c):

					print ('CANDIDATO %i' % (ivc + 1))

					for ivce in range (3)

					print ('Nome candidato %d: %s' % ((ivc+1), (curriculos [ivc] [0] )))
					print ('Data de nacimento do candidato %d: %s' % ((ivc+1), (curriculos [ivc] [1] )))
					print ('Endereço candidato %d: %s' % ((ivc+1), (curriculos [ivc] [2] )))

		elif opcao == '3':
			candidato = int (input ("Digite o número de indentificação do canditato: ")) 
				
			print ('Nome candidato %d: %s' % ((candidato), (curriculos [canditato] [0] )))
			print ('Data de nacimento do candidato %d: %s' % ((ivc+1), (curriculos [candidato] [1] )))
			print ('Endereço candidato %d: %s' % ((ivc+1), (curriculos [candidato] [2] )))

		elif opcao == '4':
			a = 0
