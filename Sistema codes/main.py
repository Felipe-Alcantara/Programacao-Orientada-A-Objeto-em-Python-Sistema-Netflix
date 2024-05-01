from Cliente import Cliente
from Filme import Filme

try:
    cliente = Cliente("teste da senha", "Felixo@Gmail.com", "Basic", 18, "semja")
    print(cliente.__str__())  # Aqui deve ser cliente, não PrimeiroCliente
    print()
except Exception as e:
    print("Erro: ", e)
print()

filme = Filme("Filme teste txt", 10, "Basic")
filme.salvar_filme()
print()

resultado = cliente.verificar(filme)
print(resultado)
print()

if resultado == True:
    print("Disponível")
else:
    print("indisponível")
print()

cliente.mudar_plano("Premium", "semja")
print(cliente.Nome)
print()