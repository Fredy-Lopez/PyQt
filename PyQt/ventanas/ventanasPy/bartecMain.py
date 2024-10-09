import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt 

# Importaciones de los recursos
sys.path.append(r'C:\Users\fredy\Desktop\Estudios\Programacion\Python\PyQt\Bebidas')
import Bebidas_rc
sys.path.append(r'C:\Users\fredy\Desktop\Estudios\Programacion\Python\PyQt\Bebidas\bebidasJugo')
import bebidasJugo_rc
sys.path.append(r'C:\Users\fredy\Desktop\Estudios\Programacion\Python\PyQt\Bebidas\bebidasVodka')
import bebidasVodka_rc 
sys.path.append(r'C:\Users\fredy\Desktop\Estudios\Programacion\Python\PyQt\Bebidas\bebidasCachaza')
import bebidasCachaza_rc 
sys.path.append(r'C:\Users\fredy\Desktop\Estudios\Programacion\Python\PyQt\Bebidas\bebidasRon')
import bebidasRon_rc

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/ventanaMenu.ui", self)  
        self.showMaximized()
        
        # Configurar el cursor de mano para los botones
        self.bJugo.setCursor(Qt.PointingHandCursor)  
        self.bJugo.clicked.connect(self.AbrirVentanaJugo)

        self.bVodka.setCursor(Qt.PointingHandCursor)  
        self.bVodka.clicked.connect(self.AbrirVentanaVodka)

        self.bCachaza.setCursor(Qt.PointingHandCursor)  
        self.bCachaza.clicked.connect(self.AbrirVentanaCachaza)

        self.bRon.setCursor(Qt.PointingHandCursor)  
        self.bRon.clicked.connect(self.AbrirVentanaRon)

    def AbrirVentanaJugo(self):
        self.ocultarVentana()  # Ocultar la ventana principal
        self.ventana_jugo = QMainWindow()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/ventanaJugo.ui", self.ventana_jugo)

        self.jPinaCooler = self.ventana_jugo.findChild(QPushButton, "jPinaCooler")
        self.jNaranjaSunrise = self.ventana_jugo.findChild(QPushButton, "jNaranjaSunrise")
        self.jLimonada = self.ventana_jugo.findChild(QPushButton, "jLimonada")
        self.jNaranjada = self.ventana_jugo.findChild(QPushButton, "jNaranjada")
        self.jCitrusPunch = self.ventana_jugo.findChild(QPushButton, "jCitrusPunch")
        self.jLimonadaEspumosa = self.ventana_jugo.findChild(QPushButton, "jLimonadaEspumosa")
        self.jPinaColada = self.ventana_jugo.findChild(QPushButton, "jPinaColada")

        # Configurar el cursor de mano para los botones
        self.jPinaCooler.setCursor(Qt.PointingHandCursor)
        self.jPinaCooler.clicked.connect(self.vConfirmarJugo)

        self.jNaranjaSunrise.setCursor(Qt.PointingHandCursor)
        self.jNaranjaSunrise.clicked.connect(self.vConfirmarJugo)

        self.jLimonada.setCursor(Qt.PointingHandCursor)
        self.jLimonada.clicked.connect(self.vConfirmarJugo)

        self.jNaranjada.setCursor(Qt.PointingHandCursor)
        self.jNaranjada.clicked.connect(self.vConfirmarJugo)

        self.jCitrusPunch.setCursor(Qt.PointingHandCursor)
        self.jCitrusPunch.clicked.connect(self.vConfirmarJugo)

        self.jLimonadaEspumosa.setCursor(Qt.PointingHandCursor)
        self.jLimonadaEspumosa.clicked.connect(self.vConfirmarJugo)

        self.jPinaColada.setCursor(Qt.PointingHandCursor)
        self.jPinaColada.clicked.connect(self.vConfirmarJugo)

        # Conectar el botón para volver a la ventanaMenu
        self.ventana_jugo.jBoton = self.ventana_jugo.findChild(QPushButton, "jBoton")
        self.ventana_jugo.jBoton.clicked.connect(self.volverAMenu)

        self.ventana_jugo.showMaximized()

    def AbrirVentanaVodka(self):
        self.ocultarVentana()  # Ocultar la ventana principal
        self.ventana_vodka = QMainWindow()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/ventanaVodka.ui", self.ventana_vodka)

        # Conectar el botón para volver a la ventanaMenu
        self.ventana_vodka.vBoton = self.ventana_vodka.findChild(QPushButton, "vBoton")
        self.ventana_vodka.vBoton.clicked.connect(self.volverAMenu)
        
        self.ventana_vodka.showMaximized()

    def AbrirVentanaCachaza(self):
        self.ocultarVentana()  # Ocultar la ventana principal
        self.ventana_cachaza = QMainWindow()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/ventanaCachaza.ui", self.ventana_cachaza)

        # Conectar el botón para volver a la ventanaMenu
        self.ventana_cachaza.cBoton = self.ventana_cachaza.findChild(QPushButton, "cBoton")
        self.ventana_cachaza.cBoton.clicked.connect(self.volverAMenu)
        
        self.ventana_cachaza.showMaximized()

    def AbrirVentanaRon(self):
        self.ocultarVentana()  # Ocultar la ventana principal
        self.ventana_ron = QMainWindow()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/ventanaRon.ui", self.ventana_ron)

        # Conectar el botón para volver a la ventanaMenu
        self.ventana_ron.rBoton = self.ventana_ron.findChild(QPushButton, "rBoton")
        self.ventana_ron.rBoton.clicked.connect(self.volverAMenu)
        
        self.ventana_ron.showMaximized()

    def ocultarVentana(self):
        self.hide()  # Oculta la ventana

    def volverAMenu(self):
        # Mostrar la ventana principal y cerrar la ventana actual
        self.show()  # Mostrar la ventanaMenu
        if hasattr(self, 'ventana_jugo'):
            self.ventana_jugo.close()
        if hasattr(self, 'ventana_vodka'):
            self.ventana_vodka.close()
        if hasattr(self, 'ventana_cachaza'):
            self.ventana_cachaza.close()
        if hasattr(self, 'ventana_ron'):
            self.ventana_ron.close()

    def vConfirmarJugo(self):
        self.vConfirmarJugo = QDialog()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/vConfirmarJugo.ui", self.vConfirmarJugo)

        self.vConfirmarJugo.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.vConfirmarJugo.setGeometry(660, 270, 600, 600)
        self.vConfirmarJugo.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()  # Mostrar la ventana principal
    sys.exit(app.exec_())

