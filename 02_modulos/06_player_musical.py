import pygame

pygame.init() # para iniciar a biblioteca do pygame
pygame.mixer.init() # inicia o mixer de áudio pra tocar a musica

bk1 = 'musicas/01bkquemnaovolta.mp3'
bk2 = 'musicas/02bkcacosdevidro.mp3'

musicas = {        # abre um dicionario pra mapear as musicas
    '1' : bk1,
    '2' : bk2
}

print()
print()
print()
print("=== Músicas ===")
print("[1] BK Quem Não Volta")
print("[2] BK Cacos de Vidro")

escolhamusica = str(input("Escolha uma opção: "))

if escolhamusica in musicas:
    pygame.mixer.music.load(musicas[escolhamusica]) # carrega a musica
else:
    print("Opção inválida, encerrando programa")
    exit()

print()
print("=== Controle de Música ===")
print("[1] Tocar")
print("[2] Pausar")
print("[3] Retomar")
print("[4] Parar")
print("[0] Sair")

while True: # True cria um laço infinito
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        pygame.mixer.music.play()
        print("Música tocando...")
    elif opcao == '2':
        pygame.mixer.music.pause()
        print("Música pausada.")
    elif opcao == '3':
        pygame.mixer.music.unpause()
        print("Música retomada.")
    elif opcao == '4':
        pygame.mixer.music.stop()
        print("Música parada.")
    elif opcao == '0':
        pygame.mixer.music.stop()
        print("Encerrando...")
        break                  # encerra o loop
    else:
        print("Opção inválida.")
