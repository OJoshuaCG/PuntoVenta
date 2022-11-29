from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super(TableModel, self).__init__(parent)
        self.data = data
        self.headerdata = ['Nombres','Cantidad','$ Precio']

    def data(self, index, role):
        if role == Qt.DisplayRole:        
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self.data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self.data)

    def columnCount(self, index):
        return 3
    # ---------- FIN funciones obligatorias --------- #

    def headerData(self, col, orientation, role):
        # Modificamos el encabezado de las columnas
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QtCore.QVariant(self.headerdata[col])
        #return QtCore.QVariant()

    def cleanTable(self):
        # Limpiamos todos los datos de la tabla
        self.data.clear()
        self.layoutChanged.emit()


    def addRow(self, row):
        # Añadimos una nueva fila
        self.data.append(row)
        self.layoutChanged.emit()


    def popRow(self, index):
        # Eliminamos el ultimo valor de la tabla
        self.data.pop(index)
        self.layoutChanged.emit()
    

    def popIndexRow(self, indexRow = -1):
        # Eliminamos un valor especifico de la tabla
        # Se invoca al eliminar un producto con el click derecho
        # Además de llamar una función de la clase padre
        # Que es interfaz.py
        self.parent().deleteProduct(indexRow)
        self.layoutChanged.emit()