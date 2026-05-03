from colorama import Fore, Style, init

# Inicializa o colorama
init()

# Lista com os níveis e mensagens do reservatório
niveis_reservatorio = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]


# Função responsável por definir a cor conforme o nível informado
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Style.RESET_ALL


# Simulação do monitoramento do reservatório
print("Sistema de Monitoramento do Reservatório de Água")
print("-" * 55)

for indice, mensagem in enumerate(niveis_reservatorio):
    nivel = indice + 1
    cor = definir_cor(nivel)

    print(cor + mensagem + Style.RESET_ALL)

print("-" * 55)
print(Style.RESET_ALL + "Monitoramento finalizado.")