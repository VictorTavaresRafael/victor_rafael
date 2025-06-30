# mascarador.py
import hashlib

def mascarar_dados():
    """
    Recebe uma string do usuário, gera o hash SHA-1 e o imprime.
    O processo se repete indefinidamente.
    """
    while True:
        try:
            # 1. Receber uma string via input
            dado_original = input("Digite o dado a ser mascarado (ou Ctrl+C para sair): ")

            # 2. Gerar o hash da string por meio do algoritmo SHA-1
            sha1 = hashlib.sha1()
            sha1.update(dado_original.encode('utf-8'))

            # 3. Imprimir o hash em tela, utilizando o método hexdigest
            print(f"Hash SHA-1: {sha1.hexdigest()}")

            # 4. Retornar ao passo 1 (o loop 'while' cuida disso)

        except KeyboardInterrupt:
            print("\nEncerrando o programa.")
            break

if __name__ == "__main__":
    mascarar_dados()