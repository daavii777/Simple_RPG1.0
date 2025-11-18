
from colorama import init, Fore, Style
init(autoreset=True)

def batalha(dragao1, dragao2):
    print(f"{Fore.RED}{Style.BRIGHT}\| {dragao1.nome} ({dragao1.tipo}) vs {dragao2.nome} ({dragao2.tipo}) |/")

    dragao1.atacar()
    dragao2.atacar()
    print()

    dano1 = max(dragao1.ataque - dragao2.defesa, 0)
    dano2 = max(dragao2.ataque - dragao1.defesa, 0)

    print(f"{Fore.RED}{Style.BRIGHT}Dano efetivo causado:")
    print(f"{Fore.BLUE}{dragao1.nome} → {dragao2.nome}: {dano1}")
    print(f"{Fore.GREEN}{dragao2.nome} → {dragao1.nome}: {dano2}")
    print()

    if dano1 > dano2:
        print(f"{Fore.BLUE}{dragao1.nome} ({dragao1.tipo}) VENCEU!!!")
    elif dano2 > dano1:
        print(f"{Fore.GREEN}{dragao2.nome} ({dragao2.tipo}) VENCEU!!!")
    else:
        print(f"{Fore.RED}{Style.BRIGHT}EMPANADO! Os dois são muito equilibrados!")