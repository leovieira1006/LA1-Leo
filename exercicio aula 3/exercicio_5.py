# 5) Escreva um script que **receba um número**, se esse número for ímpar mostre na tela
# o quadrado do número digitado. No final do script mostrar na tela "Programa finalizado..."

# 	**Exemplo 01**  
# 	**Entrada:**  
# 	10  
# 	**Saída**: 
# 	Programa finalizado...  
	
# 	**Exemplo 02**  
# 	**Entrada:**  
# 	9   
# 	**Saída**:  
#   3
# 	Programa finalizado...  

numero = int(input('Digite um numero:'))

if numero % 2 != 0:
    print(numero ** (1/2))

print('Programa finalizado...')