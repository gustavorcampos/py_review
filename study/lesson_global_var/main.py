# main.py
import global_var
from fluxo_alternativo import incrementar_fluxo_alternativo


def login(usuario):
    global_var.usuario_logado = usuario
    global_var.status_sistema = "ativo"
    print(f"Usuário {usuario} logado.")


def incrementar():
    global_var.contador += 1
    print(f"Contador: {global_var.contador}")


# Executando
login("Alice")
incrementar()
incrementar()
incrementar_fluxo_alternativo()

print(f"Status final: {global_var.status_sistema}")
print(f"Usuário atual: {global_var.usuario_logado}")
print(f"Contador: {global_var.contador}")
