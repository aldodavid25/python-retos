import math

def area_triangulo():
    base = int(input('Ingrese el valor de la base: '))
    altura = int(input('Ingrese el valor de la altura: '))
    
    area = base * altura

    area_equilatero = math.sqrt( ( 4 * (math.sqrt(3) ) ) * area )
    
    side_isosceles = math.sqrt( pow( (2 * area ) / (base), 2 ) + ( pow(base, 2) / 4 ) )
    area_isosceles = ( base * math.sqrt( ( pow(side_isosceles, 2) - (pow ( base, 2 ) / 4  ) ) ) ) / 2 
    
    if area == area_equilatero: 
        print(' Triangulo equilatero')
    elif area == area_isosceles:
        print(' Triangulo isosceles')
    else:
        print('Triangulo escaleno')
    return area

def run():
    area = area_triangulo()
    print(f'El area del triangulo  es: {area} ') 
    

if __name__ == '__main__':
    run()