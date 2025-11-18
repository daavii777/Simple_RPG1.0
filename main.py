
from dragao_gaia import Gaia
from dragao_apache import Apache
from batalha import batalha

from colorama import init, Fore, Style
init(autoreset=True)


def main():
    print(f"{Fore.RED}{Style.BRIGHT}___RPG DE DRAGÕES___")

    java = Gaia("Java")
    feroz = Apache("Feroz")

    batalha(java, feroz)

    print("Batalha finalizada")

if __name__ == "__main__":
    main()