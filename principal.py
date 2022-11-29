import sys
from PyQt5 import uic, QtWidgets
from VentanasUI import loginui
import interfaz

class MyApp(QtWidgets.QMainWindow,loginui.Ui_MainWindow): # NameFile
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loginui.Ui_MainWindow.__init__(self) # NameFile
        self.setupUi(self)
        self.btnLog.clicked.connect(self.login)
        

    def login(self):             
        user = self.txtUser.text().__str__()
        passw = self.txtPass.text().__str__()
        # Podriamos recorrer un archivo con usuarios y contraseñas
        # y validar si coinciden los datos ingresados
        if(user == 'admin' and passw == '12345'):
            self.hide()
            self.label.setText('LOGIN ☺')
            guiWindow = interfaz.Interfaz(user, self)
            guiWindow.show()
        else:
            self.label.setText('Datos Invalidos!')

        self.txtUser.setText("")
        self.txtPass.setText("")

   
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())