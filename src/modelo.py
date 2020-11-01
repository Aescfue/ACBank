"""
Exclusion mutua, lista por grupo, varias cajas?, 
"""
def existeBancoGrupo(chatId):
    existe=false
    for banco in dw.bancos:
        if chatId === banco.idGroup:
            existe=true
    return existe
    

def anadirCaja(chatId,nombre):
    if !existeBancoGrupo(chatId):
        b1=bank(chatId)
        dw.bancos.append(b1)
    c1=caja(nombre)
    b2=getBanco(chatID) #TODOTODOTODO TODO
    b2.cajas.append(c1)

#distintos grupos    
class datosGrupos:
    bancos=[]

#objeto cofre
class banco():
    idGroup = ''
    cajas= []
    
    def __init__(self,id):
        self.idGroup=id
        
    def existeCaja(chatId):
        existe=false
            for banco in dw.bancos:
                if chatId === banco.idGroup:
                    existe=true
        return existe

#cajas dentro de cofre
class caja:
    nombre=""
    elementos=[]
    usuarios=[]
    claveUso=""
    
    def __init__(self,nombre):
        self.nombre=nombre

#cad objeto en caja
class elemento:
    idPersona=""
    nombre=""
    tipo=""
    variacion=""
    cantidad=""
    estado""

dw=datosGrupos()