# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "jcarlos"
__date__ = "$Oct 27, 2017 9:09:03 AM$"

try:
    
    from Crypto.Cipher import DES
    import sqlite3 
    import time
      #creamos el cifrador
    cipher = DES.new('12345678')
    bbdd = 'taller.sqlite'
    conex = sqlite3.connect(bbdd)
    cur = conex.cursor()
    conex.text_factory = str
    print('conexion hecha')
   
except:
    print "Posibles errores de importacion"
    sys.exit(1)
        
        
        
def insertarc(fila):
    try: 
        registro = fila
        cur.execute("insert into cliente(matricula,dni,nombre,marca,modelo, motor) values (?,?,?,?,?,?)",registro)
        print('insertado')
        conex.commit()
    except:
        print("hubo un error alta clientes")
        conex.rollback()
        
def listarc():
    try:
        cur.execute("select * from cliente")
        listado = cur.fetchall()
        return listado
    except:
        print "er.message en cliente"
        conex.rollback()


def bajac(var):
    try:
        matri = var
        cur.execute("delete from cliente where matricula=?", (matri,))
        conex.commit()
    except:
        print "problemas borrado"
        conex.rollback()
  
    
def modificac(dn, nom, mar, model, mot, id):
    try:
        cur.execute("update cliente set dni=?, nombre=?, marca=?, modelo=?, motor=? WHERE matricula=?", (dn, nom, mar, model, mot, id))
        conex.commit()
    except:
        print "problemas de modificacion"
        conex.rollback()


#  ============= modulos reparacion ==============

def modificar(id, fecha, concepto, unidades, preciou, tipo):
    try:
        cur.execute("update reparacion set fecha=?, concepto=?, unidades=?, preciounidad=?, tipo=? WHERE codigo=?", (fecha, concepto, unidades, preciou, tipo, id))
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()

def bajar(mat):
    try:
        var = mat
        cur.execute("delete from reparacion where matricula=?", (var,))
        conex.commit()
    except:
        print "bara reparaciones"
        conex.rollback()

def bajarconcepto(cod):
    try:
        var = int(cod)
        cur.execute("delete from reparacion where codigo=?", (var,))
        conex.commit()
    except:
        print "bara reparaciones"
        conex.rollback()
        
        
def listarr(mat):
    try:
        
        cur.execute("select codigo, tipo, fecha, concepto, unidades, preciounidad, total from reparacion where matricula=?", (mat,))
        listador = cur.fetchall()
        return listador
    except:
        print("hubo un error en listarr")
        conex.rollback()

def listarf(mat,fech):
    try:
        cur.execute("select codigo, tipo, fecha, concepto, unidades, preciounidad, total from reparacion where matricula=? and fecha=?", (mat,fech,))
        listadof = cur.fetchall()
        return listadof
    except:
        print "hubo un error al listarf"
        conex.rollback()

def insertarr(fila):
    try: 
        
        registro = fila
        cur.execute("insert into reparacion(matricula, fecha, concepto, unidades, preciounidad, total, tipo) values (?,?,?,?,?,?,?)",registro)
        print('insertado')
        conex.commit()
    except:
        print "er.message grabar repar"
        conex.rollback()
        
        
        
# ===== control de usuarios ====== 

def altausuario(mail, password):
    try:
        
        c_pass = cipher.encrypt(password)
        
    # no tiene sentido encriptar el mail
        cur.execute("insert into acceso(correo, password) values (?,?)", (mail, c_pass,))
        print("insertado usuario")
        conex.commit()
        return True
    except sqlite3.OperationalError as e:
        print(e)
        return(e)
        conex.rollback()
        
def passuser(mail):
    try:
        
        cur.execute("select password from acceso where correo=?", (mail,))
        c_pass = cur.fetchone()
# para obtner el texto de una lista 
        c_pass2 = "".join(c_pass)
        d_pass = cipher.decrypt(c_pass2)
        
        return str(d_pass)
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        return(e)
        conex.rollback()