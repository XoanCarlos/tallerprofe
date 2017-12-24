# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "jcarlos"
__date__ = "$Oct 27, 2017 8:36:20 AM$"


import sys
import glib
import os
import conexion
import gi
import moduloscli
from time import sleep
os.environ['UBUNTU_MENUPROXY']='0'
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class taller():
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file("ventana.glade")
        #ventanas
        self.venprincipal = b.get_object("venprincipal")
        self.vtncalendar = b.get_object("vtncalendar")
        self.vtnarchivo = b.get_object("vtnarchivo")
        self.vtncontrol = b.get_object("vtncontrol")
        self.vtnuser = b.get_object("vtnuser")
        self.spinner = b.get_object("spinner")
        #self.vtnspinner = b.get_object("vtnspinner")
        self.btncontrol = b.get_object("btncontrol")
       
        #entry
        self.entmatri = b.get_object("entmatri")
        self.entdni = b.get_object("entdni")
        self.entnome = b.get_object("entnome")
        self.entmarca = b.get_object("entmarca")
        self.entmodelo = b.get_object("entmodelo")
        self.entmatrirep = b.get_object("entmatrirep")
        self.entfecha = b.get_object("entfecha")
        self.entconcepto = b.get_object("entconcepto")
        self.entunidades = b.get_object("entunidades")
        self.entpreciou = b.get_object("entpreciou")
        self.entcopia = b.get_object("entcopia")
        self.entpass = b.get_object("entpass")
        self.entmail = b.get_object("entmail")
        self.entpassword = b.get_object("entpassword")
        self.entcorreo = b.get_object("entcorreo")
        self.entpassword2 = b.get_object("entpassword2")
        #otros
        self.lblid = b.get_object("lblid")
        self.lblerror = b.get_object("lblerroracceso")
        self.lblerrorusu = b.get_object("lblerrorusu")
        self.treeclientes = b.get_object("treeclientes")
        self.listclientes = b.get_object("listclientes")
        self.treerepara = b.get_object("treerepara")
        self.listrepara = b.get_object("listrepara")
        self.calendar = b.get_object("calendar")
        self.lbltotal = b.get_object("lbltotal")
        self.lbliva = b.get_object("lbliva")
        self.lblTOT = b.get_object("lblTOT")
    
        
        #radio y check box
        self.rbtdiesel = b.get_object("rbtdiesel")
        self.rbtgasolina = b.get_object("rbtgasolina")
        self.rbthibrido = b.get_object("rbthibrido")
        self.rbtelectrico = b.get_object("rbtelectrico")
        self.chkrevision = b.get_object("chkrevision")
        self.chkmotor = b.get_object("chkmotor")
        self.chkchapa = b.get_object("chkchapa")
        #diccionario
        dic = {"on_venprincipal_destroy": self.salir, "on_btnalta_clicked": self.altacli,
        "on_btnsalir_clicked": self.salir, "on_treeclientes_cursor_changed": self.cargarcli,
        "on_btnbaja_clicked": self.bajacli, "on_bntsalirr_clicked": self.salir,
        "on_btnfecha_clicked": self.mostrarcal, "on_calendar_day_selected_double_click": self.tomarfecha,
        "on_btnaltar_clicked":self.altarep, "on_notebook_select_page": self.cargarepmat,
        "on_btnfac_clicked": self.verfactura, "on_btnbajar_clicked": self.bajarrep,
        "on_treerepara_cursor_changed": self.cargarrep, "on_btnmodif_clicked": self.modifc, 
        "on_btnmodifr_clicked": self.modifr, "on_isalir_activate": self.salir, 
        "on_vtnarchivo_destroy": self.filesalir, "on_ibackup_activate": self.backupshow,
        "on_btnbackup_clicked": self.backup, "on_btnfile_clicked": self.selfile,
        "on_chkchapa_toggled": self.chapa, "on_chkmotor_toggled": self.motor,
        "on_chkrevision_toggled": self.revision, "on_btncancel_clicked": self.salir, 
        "on_btncontrol_clicked": self.control, "on_iusuario_activate": self.usuario,
        "on_btnusualta_clicked": self.altausu, "on_vtncontrol _destroy": self.salir, 
        "on_btncancelusu": self.pechausu, "on_btncancelusu_clicked": self.cerraraltausu,
        "on_ibaja_activate": self.usuario, "on_btnbaja_clicked": self.bajausu,
        }
        b.connect_signals(dic)
        self.vtncontrol.show()
        
       
        
        
    #funciones generales
    def bajausu(self, widget):
        print "baja usuario"
            
      
    def control(self, widget):
        self.spinner.start()
        while True:
            sleep(4)
        self.correo = self.entmail.get_text()
        self.pacceso = self.entpass.get_text()
        self.paccesobbdd = conexion.passuser(self.correo)
        
        if moduloscli.correo(self.correo) and self.pacceso == self.paccesobbdd:
            
            self.vtncontrol.hide()
            self.venprincipal.show_all()
            self.venprincipal.maximize()
            self.listarclientes()
            
        else:
            self.lblerror.set_text("Correo o Password Error")
            
    def usuario(self, widget):
        self.vtnuser.show()
        
    def cerraraltausu(self, widget):
        self.vtnuser.hide()
    
    def altausu(self, widget):
        mail = self.entcorreo.get_text()
        password = self.entpassword.get_text()
        password2 = self.entpassword2.get_text()
        if password == password2:
            if conexion.altausuario(mail, password):    
                print "usuario dado de alta"
            else:
                print "Password no coinciden"
                error = conexion.altausuario(mail, password)
                self.lblerrorusu.set_text(error)
    
        
    def salir(self, widget):
        
        Gtk.main_quit()
        
    def backupshow(self, widget):
        self.vtnarchivo.show()
    
    def pechausu(self, widget):
        self.vtnuser.destroy()
    
    def filesalir(self, widget):
        self.vtnarchivo.destroy()
        
    def mostrarcal(self, widget):
        self.vtncalendar.show()
    
    def tomarfecha(self, widget):
        agno, mes, dia = self.calendar.get_date()
        mes = mes + 1
        self.fecha = "%s/" %dia + "%s/" %mes + "%s" %agno
        self.entfecha.set_text(self.fecha)
        self.vtncalendar.hide()
    
    #funciones backup    
    def selfile (self, widget):
        #extraer el nombre del fichero y no toda la ruta
        #self.filename = self.vtnarchivo.get_filename()
        self.filename = os.path.basename(self.vtnarchivo.get_filename())
        self.entcopia.set_text(self.filename)
    
    def backup (self, widget):
        moduloscli.zipbackup(self.filename)
    
    # funciones de gestion clientes
        
    def cargarcli(self, widget):
        model, iter = self.treeclientes.get_selection().get_selected()
#        model es el modelo de la tabla de dato, iter ese un numero que 
#        identifica que registro es
        if iter != None:
            smatri = model.get_value(iter, 0)
            sdni = model.get_value(iter, 1)
            snome = model.get_value(iter, 2)
            smarca = model.get_value(iter, 3)
            smodelo = model.get_value(iter, 4)
            smotor = model.get_value(iter, 5)
            self.entmatri.set_text(smatri)
            self.entdni.set_text(sdni)
            self.entnome.set_text(snome)
            self.entmarca.set_text(smarca)
            self.entmodelo.set_text(smodelo)
            self.entmatrirep.set_text(smatri)
            if smotor == "diesel":
                self.rbtdiesel.set_active(True)
            elif smotor == "gasolina":
                self.rbtgasolina.set_active(True)
            elif smotor == "hibrido":
                self.rbthibrido.set_active(True)
            elif smotor == "electrico":
                self.rbtelectrico.set_active(True)
            
            self.cargarepmat(smatri)
            
    def listarclientes(self):
        lista = conexion.listarc()
        for registro in lista:
            self.listclientes.append(registro)
    
    def modifc(self, widget):
        self.matri = self.entmatri.get_text()
        self.matri = self.matri.upper()
        self.dni = self.entdni.get_text()
        self.dni = self.dni.upper()
        self.nome = self.entnome.get_text()
        self.marca = self.entmarca.get_text()
        self.modelo = self.entmodelo.get_text()
        if self.rbtdiesel.get_active():
            self.varm = "diesel"
        elif self.rbthibrido.get_active():
            self.varm = "hibrido"
        elif self.rbtgasolina.get_active():
            self.varm = "gasolina"
        elif self.rbtelectrico.get_active():
            self.varm = "electrico"
        fila = (self.dni, self.nome, self.marca, self.modelo, self.varm)
        if self.matri != "":
            print "hola radiola"
            conexion.modificac(self.dni, self.nome, self.marca, self.modelo, self.varm, self.matri)
            self.listclientes.clear()
            self.listarclientes()
            moduloscli.limpiarc(self.entmatri, self.entdni, self.entnome, self.entmarca, self.entmodelo)
        else:
            print "error modificacion"
    
    def altacli(self, widget):
        self.matri = self.entmatri.get_text()
        self.matri = self.matri.upper()
        self.dni = self.entdni.get_text()
        self.dni = self.dni.upper()
        self.nome = self.entnome.get_text()
        self.marca = self.entmarca.get_text()
        self.modelo = self.entmodelo.get_text()
        if self.rbtdiesel.get_active():
            self.varm = "diesel"
        elif self.rbthibrido.get_active():
            self.varm = "hibrido"
        elif self.rbtgasolina.get_active():
            self.varm = "gasolina"
        elif self.rbtelectrico.get_active():
            self.varm = "electrico"
        
        fila = (self.matri, self.dni, self.nome, self.marca, self.modelo, self.varm)
        
        if self.matri != "" or self.dni != "":
            conexion.insertarc(fila)
            self.listclientes.clear()
            self.listarclientes()
            moduloscli.limpiarc(self.entmatri, self.entdni, self.entnome, self.entmarca, self.entmodelo)
        else:
            print "algun error"

    def bajacli(self, widget):
        self.matri = self.entmatri.get_text()
        if self.matri != "":
            conexion.bajac(self.matri)
            conexion.bajar(self.matri)
        else:
            print "el campo matricula no puede estar vacio"
        self.listclientes.clear()
        self.listarclientes()
        moduloscli.limpiarc(self.entmatri, self.entdni, self.entnome, self.entmarca, self.entmodelo)
    
#  ================ funciones de gestion de reparaciones ==================
    def motor(self, widget):
        self.motor = "motor"
        
    def chapa(self, widget):
        self.chapa = "chapa"
       
    def revision(self, widget):
        self.revision = "revision"
        
    def altarep(self, widget):
        self.reparaciones = []
        self.matrir = self.entmatri.get_text()
        var = self.matrir
        self.fecha = self.entfecha.get_text()
        self.concepto = self.entconcepto.get_text()
        self.unidades = self.entunidades.get_text()
        self.preciou = self.entpreciou.get_text()
        self.total = float(self.unidades) * float(self.preciou)
        if self.chkrevision.get_active():
            self.reparaciones.append(self.revision)    
        if self.chkmotor.get_active():
            self.reparaciones.append(self.motor)
        if self.chkchapa.get_active():
            self.reparaciones.append(self.chapa)
                
        var_repar = ' - '.join(self.reparaciones)
        filar = (self.matrir, self.fecha, self.concepto, self.unidades, self.preciou, self.total, var_repar)
        
        if self.matrir != "" or self.fecha != "":
            conexion.insertarr(filar)
            self.listrepara.clear()
            self.listarreparaciones(var)
            moduloscli.limpiarr(self.entconcepto, self.entunidades, self.entpreciou)
        else:
            print "algun error"
    
    def modifr(self, widget):
        self.reparaciones = []
        self.rcodigo = self.lblid.get_text()
        self.matrir = self.entmatri.get_text()
        var = self.matrir
        self.fecha = self.entfecha.get_text()
        self.concepto = self.entconcepto.get_text()
        self.unidades = self.entunidades.get_text()
        self.preciou = self.entpreciou.get_text()
        if self.chkrevision.get_active():
            self.reparaciones.append(self.revision)    
        if self.chkmotor.get_active():
            self.reparaciones.append(self.motor)
        if self.chkchapa.get_active():
            self.reparaciones.append(self.chapa)
        
        if self.matrir != "" or self.fecha != "":
            var_repar = ' - '.join(self.reparaciones)
            conexion.modificar(self.rcodigo, self.fecha, self.concepto, self.unidades, self.preciou, var_repar)
            self.listrepara.clear()
            self.listarreparaciones(var)
            moduloscli.limpiarr(self.entconcepto, self.entunidades, self.entpreciou)
        else:
            print "algun error"
    
    def listarreparaciones(self, var):
        listar = conexion.listarr(var)
        for registror in listar:
            self.listrepara.append(registror)    
    
    def cargarrep(self, widget):
        model, iter = self.treerepara.get_selection().get_selected()
#        model es el modelo de la tabla de rearaciones iter ese un numero que 
#        identifica que registro es
        moduloscli.limpiarcheck(self.chkrevision, self.chkmotor, self.chkchapa)
        if iter != None:
            self.rcodigo = model.get_value(iter, 0)
            self.tipo = model.get_value(iter, 1)
            # recorro la lista para buscar que tipo de reparciones estan almacenadas
            rep = self.tipo.split()
            for item in rep:
                if item == "revision":
                    self.chkrevision.set_active(True)
                if item == "motor":
                    self.chkmotor.set_active(True)
                if item == "chapa":
                    self.chkchapa.set_active(True)
            rfecha = model.get_value(iter, 2)
            rconcepto = model.get_value(iter, 3)
            runidades = model.get_value(iter, 4)
            rpreciouni = model.get_value(iter, 5) 
#            self.entmatrirep.set_text(self.rmatri)
            self.lblid.set_text(str(self.rcodigo))
            self.entfecha.set_text(rfecha)
            self.entconcepto.set_text(str(rconcepto))
            self.entunidades.set_text(str(runidades))
            self.entpreciou.set_text(str(rpreciouni))
            
                        
    
    def bajarrep(self, widget):
        if self.rcodigo != "":
            print self.rcodigo
            conexion.bajarconcepto(self.rcodigo)
        else:
            print "algun problema en eliminar linea factura"
        self.rmatri= self.entmatrirep.get_text()
        self.listrepara.clear()
        self.listarreparaciones(self.rmatri)
        
    
    def cargarepmat(self, mt):
        listar = conexion.listarr(mt)
        self.listrepara.clear()
        for registror in listar:
            self.listrepara.append(registror)
         
        
    def verfactura(self, widget):
        total = 0.0
        iva = 0.0
        TOT = 0.0
        fmatri = self.entmatri.get_text()
        fdata = self.entfecha.get_text()
        if fmatri != "" or fdata != "":
            listaf = conexion.listarf(fmatri, fdata)
            self.listrepara.clear()
            for registrof in listaf:
                total = total + registrof[6]
                self.listrepara.append(registrof)
            iva = float(total) * 0.21
            TOT = float(iva) + float(total)    
            self.lbltotal.set_text(str(total))
            self.lbliva.set_text(str(iva))
            self.lblTOT.set_text(str(TOT))
        else:
            print "matricula y fecha son obligatorios"
        moduloscli.limpiarr(self.entconcepto, self.entunidades, self.entpreciou)
if __name__ == "__main__":
    main = taller()
    Gtk.main()

