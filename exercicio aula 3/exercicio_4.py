# <!-- 4) Escreva um script que **receba um número**, se esse número for par mostre na tela
# a metade do número digitado. No final do script mostrar na tela "Programa finalizado..."

# **Exemplo 01**  
# **Entrada:**  
# 10  
# **Saída**:  
# 5  
# Programa finalizado...  

# **Exemplo 02**  
# **Entrada:**  
# 9  
# **Saída**:  
# Programa finalizado...   -->

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(numero / 2)

print('Programa finalizado...')