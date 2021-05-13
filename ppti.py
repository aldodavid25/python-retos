def ppt(players):
    if (player[0] == 1) && (player[1] == 2) :
        print('Jugador 2 gana [Papel le gana a piedra]')
    elif (player[0] == 1) && (player[1] == 3):
        print('Jugador 1 gana')

    
def run():
    clave = str
    players = []
    clave = 'Y'
    while clave == 'Y':
        print('Elige [1] para piedra. ')
        print('Elige [2] para papel. ')
        print('Elige [3] para tijera. ')
        for i in range(2):
            players.append(f'Ingrese el jugador {i+1} su movimiento: ')
        
        ppt(players)
        clave = input('Quiere continuar? [Y/N]')
        
                


def __name__ == '__main__':
    run()