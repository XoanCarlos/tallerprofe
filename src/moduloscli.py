# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from zipfile import ZipFile, BadZipfile
import re

def limpiarc(entmatri, entdni, entnome, entmarca, entmodelo):
    entmatri.set_text("")
    entdni.set_text("")
    entnome.set_text("")
    entmarca.set_text("")
    entmodelo.set_text("")
    
def limpiarr(entconcepto, entunidades, entpreciounidad):
	#no interesa limpiar todo solo que cambiamos en cada factura
    entconcepto.set_text("")
    entunidades.set_text("")
    entpreciounidad.set_text("")
    
def zipbackup(fichero):
    if fichero != "":
        try:
            with ZipFile(fichero + '.zip', 'w') as filezip:
                filezip.write(fichero)
                filezip.close()
        except BadZipfile:
            print "algun error al comprimier"
    else:
        print "no existe el fichero %s" %fichero
        
def limpiarcheck(revision, motor, chapa):
    revision.set_active(False)
    motor.set_active(False)
    chapa.set_active(False)
    
def correo(mail):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',mail.lower()):
        return True
