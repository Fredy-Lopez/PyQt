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
        self.showFullScreen()
        
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
        bebidasOpJugo = [
        ("PIÑA COOLER", "Jugo de piña, jugo de limón, agua tonica."),
        ("NARANJA SUNRISE", "Jugo de naranja, jugo de limón."),
        ("LIMONADA", "Jugo de limón, agua tonica, azúcar."),
        ("NARANJADA", "Jugo de naranja, agua tonica."),
        ("CITRUS PUNCH", "Jugo de limón, jugo de piña, jugo de naranja."),
        ("LIMONADA ESPUMOSA", "Jugo de limón, Coca-Cola."),
        ("PIÑA COLADA SIN ALCOHOL", "Jugo de piña, jugo de limón.")
        ]
        vent = "Jugo"
        self.ocultarVentana()  # Ocultar la ventana principal
        self.ventana_jugo = QMainWindow()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/ventanaJugo.ui", self.ventana_jugo)

        # Configurar el cursor de mano para los botones
        self.ventana_jugo.jPinaCooler.setCursor(Qt.PointingHandCursor)
        self.ventana_jugo.jPinaCooler.clicked.connect(lambda: self.vConfirmar(bebidasOpJugo[0], vent))

        self.ventana_jugo.jNaranjaSunrise.setCursor(Qt.PointingHandCursor)
        self.ventana_jugo.jNaranjaSunrise.clicked.connect(lambda: self.vConfirmar(bebidasOpJugo[1], vent))

        self.ventana_jugo.jLimonada.setCursor(Qt.PointingHandCursor)
        self.ventana_jugo.jLimonada.clicked.connect(lambda: self.vConfirmar(bebidasOpJugo[2], vent))

        self.ventana_jugo.jNaranjada.setCursor(Qt.PointingHandCursor)
        self.ventana_jugo.jNaranjada.clicked.connect(lambda: self.vConfirmar(bebidasOpJugo[3], vent))

        self.ventana_jugo.jCitrusPunch.setCursor(Qt.PointingHandCursor)
        self.ventana_jugo.jCitrusPunch.clicked.connect(lambda: self.vConfirmar(bebidasOpJugo[4], vent))

        self.ventana_jugo.jLimonadaEspumosa.setCursor(Qt.PointingHandCursor)
        self.ventana_jugo.jLimonadaEspumosa.clicked.connect(lambda: self.vConfirmar(bebidasOpJugo[5], vent))

        self.ventana_jugo.jPinaColada.setCursor(Qt.PointingHandCursor)
        self.ventana_jugo.jPinaColada.clicked.connect(lambda: self.vConfirmar(bebidasOpJugo[6], vent))

        # Conectar el botón para volver a la ventanaMenu
        self.ventana_jugo.jBoton.setCursor(Qt.PointingHandCursor)
        self.ventana_jugo.jBoton.clicked.connect(self.volverAMenu)

        self.ventana_jugo.showFullScreen()

    def AbrirVentanaVodka(self):
        bebidasOpVodka = [
        ("DESTORNILLADOR", "Vodka, jugo de naranja."),
        ("VODKA TONIC", "Vodka, agua tónica."),
        ("CAIPIROSKA", "Vodka, jugo de limón."),
        ("VODKA COLLINS", "Vodka, jugo de limón, agua tónica."),
        ("CITRUS VODKA PUNCH", "Vodka, jugo de limón, jugo de naranja."),
        ("VODKA LIMON COLA", "Vodka, Coca-Cola, jugo de limón.")
        ]
        vent = "Vodka"
        self.ocultarVentana()  # Ocultar la ventana principal
        self.ventana_vodka = QMainWindow()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/ventanaVodka.ui", self.ventana_vodka)

        # Configurar el cursor de mano para los botones
        self.ventana_vodka.vDestornillador.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vDestornillador.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[0], vent))

        self.ventana_vodka.vTonic.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vTonic.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[1], vent))

        self.ventana_vodka.vCaipiroska.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vCaipiroska.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[2], vent))

        self.ventana_vodka.vCollins.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vCollins.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[3], vent))

        self.ventana_vodka.vCitrusPunch.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vCitrusPunch.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[4], vent))

        self.ventana_vodka.vLimonCola.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vLimonCola.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[5], vent))


        # Conectar el botón para volver a la ventanaMenu
        self.ventana_vodka.vBoton.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vBoton.clicked.connect(self.volverAMenu)
        
        self.ventana_vodka.showFullScreen()

    def AbrirVentanaCachaza(self):
        bebidasOpCachaza = [
        ("Caipirinha", "Cachaza, jugo de limón."),
        ("Caipifruta", "Cachaza, jugo de piña, jugo de limón, azúcar."),
        ("Cachaza Tonic", "Cachaza, jugo de limón, agua tónica."),
        ("Tropical Caipirinha", "Cachaza, jugo de piña, jugo de limón."),
        ("Caipirinha de Coca", "Cachaza, jugo de limón, Coca-Cola."),
        ("Batida Citrus", "Cachaza, jugo de naranja, jugo de limón."),
        ("Cachaza Cooler", "Cachaza, jugo de limón, agua tónica, \njugo de naranja.")
        ]
        vent = "Cachaza"
        self.ocultarVentana()  # Ocultar la ventana principal
        self.ventana_cachaza = QMainWindow()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/ventanaCachaza.ui", self.ventana_cachaza)

        # Configurar el cursor de mano para los botones
        self.ventana_cachaza.cCaipirinha.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cCaipirinha.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[0], vent))

        self.ventana_cachaza.cCaipifruta.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cCaipifruta.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[1], vent))

        self.ventana_cachaza.cCachazaTonic.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cCachazaTonic.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[2], vent))

        self.ventana_cachaza.cTropicalCaipirinha.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cTropicalCaipirinha.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[3], vent))

        self.ventana_cachaza.cCaipirinhaCoca.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cCaipirinhaCoca.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[4], vent))

        self.ventana_cachaza.cBatidaCitrus.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cBatidaCitrus.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[5], vent))

        self.ventana_cachaza.cCachazaCooler.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cCachazaCooler.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[6], vent))

        # Conectar el botón para volver a la ventanaMenu
        self.ventana_cachaza.cBoton.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cBoton.clicked.connect(self.volverAMenu)
        
        self.ventana_cachaza.showFullScreen()

    def AbrirVentanaRon(self):
        bebidasOpRon = [
        ("Piña Colada", "Ron, jugo de piña."),
        ("Cuba Libre", "Ron, Coca-Cola, jugo de limón."),
        ("Tropical Punch", "Ron, jugo de piña, jugo de limón."),
        ("Ron Punch", "Ron, jugo de piña, jugo de limón, jugo de naranja."),
        ("Ron Tonic Tropical", "Ron, agua tónica, jugo de piña, jugo de limón."),
        ("Tropical Cuba Libre", "Ron, Coca-Cola, jugo de piña, jugo de limón.")
        ]
        vent = "Ron"
        self.ocultarVentana()  # Ocultar la ventana principal
        self.ventana_ron = QMainWindow()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/ventanaRon.ui", self.ventana_ron)

        # Configurar el cursor de mano para los botones
        self.ventana_ron.rPinaColada.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rPinaColada.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[0], vent))

        self.ventana_ron.rCubaLibre.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rCubaLibre.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[1], vent))

        self.ventana_ron.rTropicalPunch.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rTropicalPunch.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[2], vent))

        self.ventana_ron.rRonPunch.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rRonPunch.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[3], vent))

        self.ventana_ron.rRonTonic.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rRonTonic.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[4], vent))

        self.ventana_ron.rTropicalCubaLibre.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rTropicalCubaLibre.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[5], vent))

        # Conectar el botón para volver a la ventanaMenu
        self.ventana_ron.rBoton.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rBoton.clicked.connect(self.volverAMenu)
        
        self.ventana_ron.showFullScreen()

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

    def vConfirmar(self, bebidasOp, vent):
        Bebida, Contenido = bebidasOp
        tipVent = vent
        # Crear la ventana de confirmación
        self.Confirmar = QDialog()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/vConfirmar.ui", self.Confirmar)
        # Configurar propiedades de la ventana de confirmación
        self.Confirmar.setWindowFlags(Qt.FramelessWindowHint)
        self.Confirmar.setAttribute(Qt.WA_TranslucentBackground)
        self.Confirmar.setWindowOpacity(0.95)
        self.Confirmar.setGeometry(550, 270, 750, 600)
        
        self.Confirmar.jBebida.setText(f"Seleccionaste: {Bebida}")
        self.Confirmar.jContenido.setText(f"Contiene: {Contenido}")

        self.Confirmar.jCambiar.clicked.connect(self.Confirmar.close)
        if tipVent == "Jugo":
            self.Confirmar.jConfirmar.clicked.connect(self.vEspera)
        elif tipVent == "Vodka" or "Cachaza" or "Ron":
            self.Confirmar.jConfirmar.setText("CONFIRMAR Y CONTINUAR")
            self.Confirmar.jConfirmar.clicked.connect(self.Confirmar.close)
            self.Confirmar.jConfirmar.clicked.connect(lambda: self.vIntensidad(Bebida))


        # Mostrar la ventana de confirmación
        self.Confirmar.exec_()

    def vIntensidad(self, Bebida):
        Bebida = Bebida
        self.Intensidad = QDialog()
        loadUi("C:/Users/fredy/Desktop/Estudios/Programacion/Python/PyQt/ventanas/vIntensidad.ui", self.Intensidad)
        # Configurar propiedades de la ventana de confirmación
        self.Intensidad.setWindowFlags(Qt.FramelessWindowHint)
        self.Intensidad.setAttribute(Qt.WA_TranslucentBackground)
        self.Intensidad.setWindowOpacity(0.95)
        self.Intensidad.setGeometry(550, 270, 750, 600)
        
        self.Intensidad.Bebida.setText(f"Seleccionaste: {Bebida}")

        self.Intensidad.Cambiar.clicked.connect(self.Intensidad.close)

        # Mostrar la ventana de confirmación
        self.Intensidad.exec_()


    def vEspera(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()  # Mostrar la ventana principal
    sys.exit(app.exec_())


