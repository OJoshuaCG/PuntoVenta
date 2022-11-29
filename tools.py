import sys
from PyQt5 import uic, QtWidgets
from VentanasUI import articuloui

class Tools(QtWidgets.QMainWindow,articuloui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Tools, self).__init__(parent)
        articuloui.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnBack.clicked.connect(self.back)
        self.btnAceptar.clicked.connect(self.accept)
        self.cbOption.currentIndexChanged.connect(self.changeOption)
        self.cbID.setVisible(False)
        self.cbID.currentIndexChanged.connect(self.changeProduct)

        self.products, self.idList = self.setLists()
        self.defineCbID()
        self.cleanData()
        self.option = 0
        self.product = 0 


    def changeOption(self): # comboBoxOpciones/acciones
        # Adaptamos la ventana segun la acción elegida
        self.option = self.cbOption.currentIndex()
        if(self.option == 0):   # Agregar
            self.setEnableds(1, 0, 1, 1)
            self.cleanData()
            pass
        
        else:
            if(self.option == 1):   # Modificar
                self.setEnableds(0, 1, 1, 1)
            else:                   # Eliminar
                self.setEnableds(0, 1, 0, 0)
            self.changeProduct()
   
   
    def changeProduct(self): # comboBox ID's
        # Actualizamos los txt dependiendo del cambio del CB ID
        if len(self.idList) == 0:
            self.txtName.setText("")
            self.txtPrice.setText("")
            return
        self.product = self.cbID.currentIndex()
        self.txtName.setText(self.products[self.product][1])
        self.txtPrice.setText(self.products[self.product][2])


    def defineCbID(self):
        # Actualizamos el ComboBox
        self.cbID.clear()
        self.cbID.addItems(self.idList)
        self.cbID.setCurrentIndex(0)
    

    def accept(self): # Boton Aceptar
        if(not self.verifyData()):
            self.lbMSG.setText('Ingrese los datos requeridos')
            return

        if(self.option == 0):
            self.addData()        
        elif(self.option == 1):
            self.updateData()
        else:
            if len(self.idList) == 0:
                self.lbMSG.setText('Operacion Rechazada')
                return
            self.removeData()

        self.lbMSG.setText('Operacion Exitosa!')
        self.products, self.idList = self.setLists()
        self.defineCbID()
        self.parent().fillcbNames()
        if(self.option == 0):
            self.cleanData()       
        else:
            self.changeProduct()
            self.parent().cleanTable()
     

    def setLists(self):
        # Establecemos las listas
        file = open("articulos.txt", "a")
        file.close()
        file = open("articulos.txt", "r") 
        a = []
        b = []
        for i in file:
            aux = list(i.split(","))
            price = aux[2].__str__()
            price = price[0:-1]
            aux[2] = price
            a.append(aux)
            b.append(aux[0])
        file.close()
        return a, b


    def addData(self):
        # Añadimos la información al archivo .txt
        ide = self.txtID.text().__str__()
        name = self.txtName.text().__str__()
        price = abs(float(self.txtPrice.text().__str__()))
        #price = f"{price:.2f}"
        price = "{0:.2f}".format(price)

        file = open("articulos.txt","a")
        line = ("{0},{1},{2}\n").format(ide, name, price)
        file.write(line)
        file.close()


    def updateData(self):
        # Actualizamos la información en el .txt
        index = self.product 
        ide = self.idList[index]
        name = self.txtName.text().__str__()
        price = abs(float(self.txtPrice.text().__str__()))
        line = ("{0},{1},{2}\n").format(ide, name, price)

        file = open("articulos.txt", "r")
        lines = file.readlines()
        lines[index] = line
        file.close()

        file = open("articulos.txt", "w")
        for line in lines:
            file.write(line)
        file.close()      


    def removeData(self):
        # Eliminamos el elemento elegido
        index = self.product
        file = open("articulos.txt", "r")
        lines = file.readlines()
        line = lines[index]
        lines.remove(line)
        file.close()

        file = open("articulos.txt", "w")
        for line in lines:
            file.write(line)
        file.close()
        

    def verifyData(self):
        # Verificamos que todo este bien
        # Cuando clickeemos el boton aceptar
        if(self.option == 0):
            if(self.txtID.text() and self.txtName.text() and self.txtPrice.text()):
                return True
        elif(self.option == 1):
            if (self.txtName.text() and self.txtPrice.text()):
                return True
        else:
            return True
        return False

    
    def setEnableds(self, ide, cbid, name, price):
        # Definimos la visibilidad y activación
        # de los elementos
        self.txtID.setVisible(ide)
        self.cbID.setVisible(cbid)
        self.txtName.setEnabled(name)
        self.txtPrice.setEnabled(price)


    def cleanData(self):
        # Limpiamos toda la información
        self.txtID.setText("")
        self.txtName.setText("")
        self.txtPrice.setText("")

    def back(self):
        # Cerramos la ventana 
        self.close()
    