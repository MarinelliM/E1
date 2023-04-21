from Clase_Email import Email

def test():
    em = Email('mauri', 'gmail', 'com', 'maf')
    print(em.retornaEmail())
    m = Email.crearCuenta('mauri@gmail.com', 'nfnf')
    print(m.retornaEmail())

if __name__ == '__main__':
    test()
    nombre = input('ingrese un nombre:')
    cuenta = input('ingrese su cuenta:')
    con = input('ingrese su contraseña:')
    cuentan = Email.crearCuenta(cuenta, con)
    print('Estimado {} te enviaremos tus mensajes a la direccion {}' .format(nombre, cuentan.retornaEmail()))

    contra1 = str(input('Para cambiar su contraseña debe ingresar la actual:'))
    if contra1 == cuentan.getcontraseña():
        contra2 = str(input('Ingrese su nueva contraseña:'))
        cuentan.cambiarcontra(contra2)
        print('Su nueva contraseña es: {}' .format(cuentan.getcontraseña()))
    else:
        print('La contraseña ingresada no coincide con la registrada')

    cuenta2 = Email.crearCuenta('juanLiendro1957@yahoo.com', 'contraseña')
    print(cuenta2.retornaEmail())



    with open('Cuentas.txt', 'r', encoding='utf8') as archivo:
        lista = archivo.readlines()
        listaobjetos = []
    for direccion in lista:
        direcciones = direccion.split(',')
        for dir in direcciones:
            cuenta = Email.crearCuenta(dir.strip(), 'contraseña')
            if cuenta is None:
                print('Error: La dirección de email', dir.strip(), 'no es válida')
            else:
                print('Se creó la cuenta', cuenta.getid())
                listaobjetos.append(cuenta)
    dominio = input('Ingrese el dominio a buscar:')
    contador = 0
    for ob in listaobjetos:
        if ob.getDominio() == dominio:
            contador += 1
    print('Existen un total de', contador,'cuentas con el dominio', dominio)
