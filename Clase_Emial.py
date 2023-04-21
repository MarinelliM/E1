class Email:
    __idCuenta: str
    __dominio: str
    __tipo_de_dominio: str
    __contraseña = 'contraseña'

    def __init__(self, idCuenta, dominio, tipo_de_dominio, contraseña) -> None:
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipo_de_dominio = tipo_de_dominio
        self.__contraseña = contraseña
        pass

    def retornaEmail(self):
        return self.__idCuenta + '@' + self.__dominio + '.' + self.__tipo_de_dominio
    
    def getDominio(self):
        return self.__dominio
    
    @staticmethod
    def crearCuenta(direc, con):
        var = direc.split("@")
        var1 = var[1].split(".")
        return Email(var[0], var1[0], var1[1], con)
    
    def cambiarcontra(self, contr):
        self.__contraseña = contr

    def getcontraseña(self):
        return self.__contraseña
    
    def getid(self):
        return self.__idCuenta
