import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from VentanasUI import interfazui
#from datetime import datetime
import tools, tableModel

class Interfaz(QtWidgets.QMainWindow,interfazui.Ui_MainWindow):
    def __init__(self, vendedor, parent=None):
        super(Interfaz, self).__init__(parent)
        #QtWidgets.QMainWindow.__init__(self)

        interfazui.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnSearch.clicked.connect(self.searchID)
        self.btnAdd.clicked.connect(self.addProduct)
        self.btnDel.clicked.connect(self.deleteLastProduct)
        self.btnPaid.clicked.connect(self.paid)  
        self.btnOff.clicked.connect(self.logout)
        self.btnAdmin.clicked.connect(self.settings)
        self.spCant.valueChanged.connect(self.setPrices)
        self.cbNames.currentIndexChanged.connect(self.chooseProduct)       
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.context_menu)
        
        self.products, self.idList, self.nameList = [], [], []   
        self.data = [['-', '-', '-']]
        self.model = tableModel.TableModel(self.data, self)
        self.prices = []
        self.price = ""
        self.index = -1        
        self.fillcbNames()     
        self.setTable()
        self.vendedor = vendedor
        
        
    def searchID(self): # Boton BUSCAR
        ide = self.txtID.text().__str__()
        if ide in self.idList:
            self.index = self.idList.index(ide) # Obtenemos el indice
            self.cbNames.setCurrentIndex(self.index)
            self.setPrices()
            self.txtID.setPlaceholderText("ID")
        
        else: 
            self.cleanData()
            self.txtID.setPlaceholderText("ID 404")
           

    def setPrices(self): # Accion Spinner
        if(self.index < 0): # Si NO hay articulo seleccionado...
            return
        # Actualizamos el $ total del articulo
        ammount = int(self.spCant.text())
        subPrice = float(self.products[self.index][2])
        subPrice *= ammount
        self.price = subPrice
        subPrice = "{0:.2f}".format(subPrice)
        self.lbPrice.setText(self.price.__str__())
    

    def chooseProduct(self): # Accion ComboBox
        # Actualizamos los datos
        self.index = self.cbNames.currentIndex()
        self.txtID.setText(self.idList[self.index])
        self.txtID.setPlaceholderText("ID")
        self.setPrices()


    def addProduct(self): # Boton Añadir
        if(self.index < 0): # Si NO hay articulo seleccionado...
            return
        nombre = self.nameList[self.index]
        cantidad = self.spCant.text()
        precio = self.lbPrice.text()
        producto = [nombre, cantidad, precio]
        self.model.addRow(producto)
        self.checkData(1)


    def deleteLastProduct(self): # Boton Eliminar
        self.deleteProduct(-1)
    

    def deleteProduct(self, index = -1): # Accion Eliminar
        empty = ['-', '-', '-']
        if(not empty in self.data):            
            self.prices.pop(index)
            self.model.popRow(index)
            self.checkData(0)


    def checkData(self, delORadd): 
        empty = ['-', '-', '-']
        if(delORadd): # Si hay que añadir    
            if len(self.data) == 2 and empty in self.data:
                self.model.popRow(0)
            self.setTotal(1)
            self.cleanData()

        else: 
            if len(self.data) == 0 and not empty in self.data:    # Si toca eliminar
                self.model.addRow(empty)
            self.setTotal(0)
        

    def setTotal(self, delORadd):
        if delORadd: # Si hay que añadir
            subTotal = self.lbPrice.text().__str__()
            subTotal = float(subTotal)
            self.prices.append(subTotal)
        
        total = sum(self.prices)
        self.lbTotal.setText(total.__str__())


    def cleanData(self):
        # Limpiamos toda la informacion dejandola vacia
        self.index = -1
        self.cbNames.setCurrentIndex(self.index)
        self.txtID.setText("")
        self.lbPrice.setText("")
        self.price = ""


    def fillcbNames(self):
        # Llenamos el comboBox
        # con los nombres de los articulos
        self.setLists() 
        self.cbNames.clear()
        self.cbNames.addItems(self.nameList)
        self.cleanData() 
    

    def paid(self): # Boton Pagar
        empty = ['-', '-', '-']
        if empty in self.data:
            return
        compraTotal = float(self.lbTotal.text())
        #fechaYhora = datetime.now()
        # Se puede añadir a un archivo y almacenar
        # idVendedor, idCompra, $ venta
        # En idCompra, → los articulos, cantidades y $
        self.cleanTable()
        

    def cleanTable(self):
        # Limpiamos la tabla dejandola vacia
        empty = ['-', '-', '-']
        self.prices.clear()
        self.lbTotal.setText("")
        self.model.cleanTable()
        self.model.addRow(empty)
        self.cleanData()


    def setLists(self):
        # Establecemos las listas
        # Articulos completos, id's y nombres
        file = open("articulos.txt", "a")
        file.close()
        file = open("articulos.txt", "r") 
        lista, ides, names = [], [], []
        for i in file:
            aux = list(i.split(","))
            price = aux[2].__str__()
            price = price[0:-2]
            aux[2] = price
            lista.append(aux)
            ides.append(aux[0])
            names.append(aux[1])
        file.close()
        self.products, self.idList, self.nameList = lista, ides, names

         
    def setTable(self):  
        # Inicializamos la tabla     
        self.table.setModel(self.model)
        self.table.setColumnWidth(0,300)    #511
        self.table.setColumnWidth(1,100)
        self.table.setColumnWidth(2,100)
        self.table.setSortingEnabled(True)       


    def context_menu(self):
        # Mini menu para eliminar un producto
        # Dando click derecho en el articulo
        menu = QtWidgets.QMenu()
        if self.table.selectedIndexes():
            # Añadimos una acción
            delOption = menu.addAction("Eliminar")
            # Agregamos un icono
            icon = QtGui.QIcon() 
            icon.addPixmap(QtGui.QPixmap("icons/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            delOption.setIcon(icon)
            # Obtenemos el indice y realizamos la eliminación en caso de seleccionarse la opcion
            index = self.table.currentIndex().row()
            delOption.triggered.connect(lambda: self.model.popIndexRow(index))
            
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())


    def settings(self):
        toolWindow = tools.Tools(self)
        toolWindow.show()

    def logout(self):
        self.parent().show()
        self.close()
