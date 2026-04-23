# Escopo Global e Local

var_global = "Curso Completo de Python"

def escreve_texto():
    var_global = "Banco de Dados"
    var_local = "Anakin Skywalker"
    print(f'Variável Global: {var_global}') # Acessa a variável global dentro da função
    print(f'Variável Local: {var_local}') # Acessa a variável local dentro da função

if __name__ == '__main__':
    print(f'Executar a funçao esvreve_texto()')
    escreve_texto()

    print('Tentar acessar as varáveis diretamente')
    print(f'Variável Global: {var_global}')
    #print(f'Variável Local: {var_local}') # Isso causará um erro, pois var_local não é acessível fora da função