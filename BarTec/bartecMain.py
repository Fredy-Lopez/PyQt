import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QSize, QTimer, QIODevice
from PyQt5.QtGui import QMovie
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

# Importaciones de los recursos
from Bebidas import Bebidas_rc
from Bebidas import bebidasJugo_rc
from Bebidas import bebidasVodka_rc
from Bebidas import bebidasCachaza_rc
from Bebidas import bebidasRon_rc

if getattr(sys, 'frozen', False):
    # Estamos corriendo desde un .exe
    BASE_DIR = sys._MEIPASS
else:
    # Estamos corriendo desde Python
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(os.path.join(BASE_DIR, "ventanas", "ventanaMenu.ui"), self)  
        
        self.showFullScreen()

        self.serial = QSerialPort()
        self.serial.setBaudRate(115200)
        
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
        ("PIÑA COOLER", "Jugo de piña, jugo de limón, agua tonica.", "A"),
        ("NARANJA SUNRISE", "Jugo de naranja, jugo de limón.", "B"),
        ("LIMONETTO", "Jugo de limón, agua tonica.", "C"),
        ("NARANJADA", "Jugo de naranja, agua tonica.", "D"),
        ("CITRUS PUNCH", "Jugo de limón, jugo de piña, jugo de naranja.","E"),
        ("CITRUS BURST", "Jugo de limón, jugo de pomelo.", "F"),
        ("PIÑA COLADA SIN ALCOHOL", "Jugo de piña, jugo de limón.", "G")
        ]
        vent = "Jugo"
        QTimer.singleShot(200, self.ocultarVentana)
        self.ventana_jugo = QMainWindow()
        loadUi(os.path.join(BASE_DIR, "ventanas", "ventanaJugo.ui"), self.ventana_jugo)

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

        self.ventana_jugo.jCitrusBurst.setCursor(Qt.PointingHandCursor)
        self.ventana_jugo.jCitrusBurst.clicked.connect(lambda: self.vConfirmar(bebidasOpJugo[5], vent))

        self.ventana_jugo.jPinaColada.setCursor(Qt.PointingHandCursor)
        self.ventana_jugo.jPinaColada.clicked.connect(lambda: self.vConfirmar(bebidasOpJugo[6], vent))

        # Conectar el botón para volver a la ventanaMenu
        self.ventana_jugo.jBoton.setCursor(Qt.PointingHandCursor)
        self.ventana_jugo.jBoton.clicked.connect(self.volverAMenu)

        self.ventana_jugo.showFullScreen()
        

    def AbrirVentanaVodka(self):
        bebidasOpVodka = [
        ("DESTORNILLADOR", "Vodka, jugo de naranja.", "H"),
        ("VODKA TONIC", "Vodka, agua tónica.", "I"),
        ("CAIPIROSKA", "Vodka, jugo de limón.", "J"),
        ("SALTY DOG", "Vodka, jugo de pomelo.", "K"),
        ("CITRUS VODKA PUNCH", "Vodka, jugo de limón, jugo de naranja.", "L"),
        ("VODKA CITRUS BREEZE", "Vodka, jugo de pomelo, jugo de limón.", "M")
        ]
        vent = "Vodka"
        QTimer.singleShot(200, self.ocultarVentana)
        self.ventana_vodka = QMainWindow()
        loadUi(os.path.join(BASE_DIR, "ventanas", "ventanaVodka.ui"), self.ventana_vodka)

        # Configurar el cursor de mano para los botones
        self.ventana_vodka.vDestornillador.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vDestornillador.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[0], vent))

        self.ventana_vodka.vTonic.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vTonic.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[1], vent))

        self.ventana_vodka.vCaipiroska.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vCaipiroska.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[2], vent))

        self.ventana_vodka.vSaltyDog.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vSaltyDog.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[3], vent))

        self.ventana_vodka.vCitrusPunch.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vCitrusPunch.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[4], vent))

        self.ventana_vodka.vCitrusBreeze.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vCitrusBreeze.clicked.connect(lambda: self.vConfirmar(bebidasOpVodka[5], vent))


        # Conectar el botón para volver a la ventanaMenu
        self.ventana_vodka.vBoton.setCursor(Qt.PointingHandCursor)
        self.ventana_vodka.vBoton.clicked.connect(self.volverAMenu)
        
        self.ventana_vodka.showFullScreen()

    def AbrirVentanaCachaza(self):
        bebidasOpCachaza = [
        ("CAIPIRINHA", "Cachaza, jugo de limón.", "N"),
        ("CAIPIFRUTA", "Cachaza, jugo de piña, jugo de limón.", "O"),
        ("CACHAZA TONIC", "Cachaza, jugo de pomelo, agua tónica.", "P"),
        ("TROPICAL CAIPIRINHA", "Cachaza, jugo de piña, jugo de limón.", "Q"),
        ("CAIPIRINHA POMELO", "Cachaza, jugo de limón, jugo de pomelo.", "R"),
        ("BATIDA CITRUS", "Cachaza, jugo de naranja, jugo de limón.", "S"),
        ("CACHAZA COOLER", "Cachaza, jugo de limón, agua tónica, \njugo de naranja.", "T")
        ]
        vent = "Cachaza"
        QTimer.singleShot(200, self.ocultarVentana)
        self.ventana_cachaza = QMainWindow()
        loadUi(os.path.join(BASE_DIR, "ventanas", "ventanaCachaza.ui"), self.ventana_cachaza)

        # Configurar el cursor de mano para los botones
        self.ventana_cachaza.cCaipirinha.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cCaipirinha.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[0], vent))

        self.ventana_cachaza.cCaipifruta.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cCaipifruta.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[1], vent))

        self.ventana_cachaza.cCachazaTonic.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cCachazaTonic.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[2], vent))

        self.ventana_cachaza.cTropicalCaipirinha.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cTropicalCaipirinha.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[3], vent))

        self.ventana_cachaza.cCaipirinhaPomelo.setCursor(Qt.PointingHandCursor)
        self.ventana_cachaza.cCaipirinhaPomelo.clicked.connect(lambda: self.vConfirmar(bebidasOpCachaza[4], vent))

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
        ("PIÑA COLADA", "Ron, jugo de piña.", "U"),
        ("POMELO RUM SPLASH", "Ron, jugo de pomelo, jugo de limón.", "V"),
        ("TROPICAL PUNCH", "Ron, jugo de piña, jugo de limón.", "W"),
        ("RON PUNCH", "Ron, jugo de piña, jugo de limón, jugo de naranja.", "X"),
        ("RON TONIC TROPICAL", "Ron, agua tónica, jugo de piña, jugo de limón.", "Y"),
        ("TROPICAL RUM STORM", "Ron, jugo de pomelo, jugo de piña, jugo de limón.", "Z")
        ]
        vent = "Ron"
        QTimer.singleShot(200, self.ocultarVentana)
        self.ventana_ron = QMainWindow()
        loadUi(os.path.join(BASE_DIR, "ventanas", "ventanaRon.ui"), self.ventana_ron)

        # Configurar el cursor de mano para los botones
        self.ventana_ron.rPinaColada.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rPinaColada.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[0], vent))

        self.ventana_ron.rPomeloRumSplash.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rPomeloRumSplash.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[1], vent))

        self.ventana_ron.rTropicalPunch.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rTropicalPunch.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[2], vent))

        self.ventana_ron.rRonPunch.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rRonPunch.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[3], vent))

        self.ventana_ron.rRonTonic.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rRonTonic.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[4], vent))

        self.ventana_ron.rTropicalRumStorm.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rTropicalRumStorm.clicked.connect(lambda: self.vConfirmar(bebidasOpRon[5], vent))

        # Conectar el botón para volver a la ventanaMenu
        self.ventana_ron.rBoton.setCursor(Qt.PointingHandCursor)
        self.ventana_ron.rBoton.clicked.connect(self.volverAMenu)
        
        self.ventana_ron.showFullScreen()

    def ocultarVentana(self):
        self.hide()  # Oculta la ventana

    def delay(self):
        pass
        
    def volverAMenu(self):
        # Mostrar la ventana principal y cerrar la ventana actual
        self.show()  # Mostrar la ventanaMenu
        if hasattr(self, 'ventana_jugo'):
            QTimer.singleShot(200, self.ventana_jugo.close)
        if hasattr(self, 'ventana_vodka'):
            QTimer.singleShot(200, self.ventana_vodka.close)
        if hasattr(self, 'ventana_cachaza'):
            QTimer.singleShot(200, self.ventana_cachaza.close)
        if hasattr(self, 'ventana_ron'):
            QTimer.singleShot(200, self.ventana_ron.close)
        if hasattr(self, 'ventana_listo'):
            QTimer.singleShot(200, self.ventana_listo.close)

    def vConfirmar(self, bebidasOp, vent):
        Bebida, Contenido, CodigoBebida = bebidasOp
        tipVent = vent
        # Crear la ventana de confirmación
        self.Confirmar = QDialog()
        loadUi(os.path.join(BASE_DIR, "ventanas", "vConfirmar.ui"), self.Confirmar)
        # Configurar propiedades de la ventana de confirmación
        self.Confirmar.setWindowFlags(Qt.FramelessWindowHint)
        self.Confirmar.setAttribute(Qt.WA_TranslucentBackground)
        self.Confirmar.setWindowOpacity(0.95)
        self.Confirmar.setGeometry(550, 270, 750, 600)
        
        self.Confirmar.jBebida.setText(f"Seleccionaste: {Bebida}")
        self.Confirmar.jContenido.setText(f"Contiene: {Contenido}")

        self.Confirmar.jCambiar.setCursor(Qt.PointingHandCursor)
        self.Confirmar.jConfirmar.setCursor(Qt.PointingHandCursor)
        self.Confirmar.jCambiar.clicked.connect(self.Confirmar.close)
        if tipVent == "Jugo":
            self.Confirmar.jConfirmar.clicked.connect(self.Confirmar.close)
            self.Confirmar.jConfirmar.clicked.connect(lambda: self.vEspera(Bebida, tipVent, CodigoBebida))
        elif tipVent == "Vodka" or "Cachaza" or "Ron":
            self.Confirmar.jConfirmar.setText("CONFIRMAR Y CONTINUAR")
            self.Confirmar.jConfirmar.clicked.connect(self.Confirmar.close)
            self.Confirmar.jConfirmar.clicked.connect(lambda: self.vIntensidad(Bebida, tipVent, CodigoBebida))

        # Mostrar la ventana de confirmación
        self.Confirmar.exec_()

    def vIntensidad(self, Bebida, tipVent, CodigoBebida):
        Bebida = Bebida
        tipVent = tipVent
        CodigoBebida = CodigoBebida
        self.intensidad = ""
        self.intensidadArduino = ""
        self.Intensidad = QDialog()
        loadUi(os.path.join(BASE_DIR, "ventanas", "vIntensidad.ui"), self.Intensidad)
        # Configurar propiedades de la ventana de confirmación
        self.Intensidad.setWindowFlags(Qt.FramelessWindowHint)
        self.Intensidad.setAttribute(Qt.WA_TranslucentBackground)
        self.Intensidad.setWindowOpacity(0.95)
        self.Intensidad.setGeometry(550, 270, 750, 600)
        
        self.Intensidad.Bebida.setText(f"Seleccionaste: {Bebida}")
        self.Intensidad.Cambiar.setCursor(Qt.PointingHandCursor)
        self.Intensidad.Cambiar.clicked.connect(self.Intensidad.close)

        self.Intensidad.Confirmar.setEnabled(False)

        self.Intensidad.Suave.toggled.connect(self.HabilitarBotonConfirmar)
        self.Intensidad.Normal.toggled.connect(self.HabilitarBotonConfirmar)
        self.Intensidad.Fuerte.toggled.connect(self.HabilitarBotonConfirmar)

        self.Intensidad.Confirmar.clicked.connect(self.Intensidad.close)
        self.Intensidad.Confirmar.clicked.connect(lambda: self.vEspera(Bebida, tipVent, CodigoBebida))

        # Mostrar la ventana de confirmación
        self.Intensidad.exec_()

    def HabilitarBotonConfirmar(self):
        # Habilitar el botón de confirmar si al menos un radio button está seleccionado
        self.Intensidad.Confirmar.setEnabled(self.Intensidad.Suave.isChecked() or self.Intensidad.Normal.isChecked() or self.Intensidad.Fuerte.isChecked())
        self.Intensidad.Confirmar.setCursor(Qt.PointingHandCursor)
        if self.Intensidad.Suave.isChecked():
            self.intensidad = "SUAVE"
            self.intensidadArduino = "S"
        if self.Intensidad.Normal.isChecked():
            self.intensidad = "NORMAL"  
            self.intensidadArduino = "N"  
        if self.Intensidad.Fuerte.isChecked():
            self.intensidad = "FUERTE"    
            self.intensidadArduino = "F"
        print(f"intensidad: {self.intensidadArduino}")

    def vEspera(self, Bebida, tipVent, CodigoBebida):
        Bebida = Bebida
        tipVent = tipVent
        CodigoBebida = CodigoBebida
        if tipVent == "Vodka":
            QTimer.singleShot(200, self.ventana_vodka.close)
        elif tipVent == "Cachaza":
            QTimer.singleShot(200, self.ventana_cachaza.close)
        elif tipVent == "Ron":
            QTimer.singleShot(200, self.ventana_ron.close)
        elif tipVent == "Jugo":
            QTimer.singleShot(200, self.ventana_jugo.close)

        self.detectarPuerto(Bebida)
        
        if self.serial.isOpen():
            if tipVent == "Jugo":
                bebida_bytes = (CodigoBebida + "\n").encode('utf-8')  # Convertir el mensaje a bytes
                self.serial.write(bebida_bytes)
                print(f"Mensaje enviado al Arduino: {CodigoBebida}") 
            elif tipVent == "Cachaza" or tipVent == "Ron" or tipVent == "Vodka" :
                # Concatenar bebida y intensidad en una sola cadena antes de enviarla
                comando_completo = f"{CodigoBebida},{self.intensidadArduino}"
                comando_bytes = (comando_completo + "\n").encode('utf-8')  # Convertir a bytes

                self.serial.write(comando_bytes)  # Enviar el comando completo
                print(f"Comando completo enviado al Arduino: {comando_completo}")
        else:
            print("El puerto serial no está abierto.")
        self.ventana_espera = QMainWindow()
        loadUi(os.path.join(BASE_DIR, "ventanas", "vEspera.ui"), self.ventana_espera)
        # Cargar el GIF usando barras inclinadas
        self.movie = QMovie(os.path.join(BASE_DIR, "Bebidas", "Gifs", "cargar.gif"))
        self.ventana_espera.gifCargar.setMovie(self.movie)
        self.movie.start()  # Iniciar la animación del GIF
        self.movie.setScaledSize(QSize(115, 115))
        self.ventana_espera.showFullScreen()

    def detectarPuerto(self, Bebida):
        Bebida = Bebida
        # Obtener la lista de puertos seriales disponibles
        available_ports = QSerialPortInfo.availablePorts()
        
        for port in available_ports:
            # Puedes imprimir la información del puerto para depurar
            print(f"Puerto: {port.portName()}, Descripción: {port.description()}, Fabricante: {port.manufacturer()}")

            # Intentar identificar el puerto correcto basándote en la descripción o fabricante
            if "Arduino" in port.description() or "Arduino" in port.manufacturer():
                # Si encuentras el puerto, intenta abrirlo
                self.serial = QSerialPort(port)
                self.serial.setBaudRate(115200)
                
                if self.serial.open(QIODevice.ReadWrite):
                    print(f"Conectado al puerto: {port.portName()}")
                    # Conectar la señal de lectura serial
                    self.serial.readyRead.connect(lambda: self.serialRecibido(Bebida))
                    return
                else:
                    print(f"No se pudo abrir el puerto: {port.portName()}")
        
        # Si no se encuentra el puerto Arduino
        print("No se encontró un Arduino conectado.")
    
    def serialRecibido(self, Bebida):
        Bebida = Bebida
        # Leer los datos del puerto serial
        if self.serial.canReadLine():
            data = self.serial.readLine().data().decode().strip()
            print(f"Datos recibidos del puerto serial: {data}") 
            # Verificar si el dato recibido es el que estamos esperando
            if data == "LISTO":  # Ajustar según el mensaje enviado por el Arduino
                self.vListo(Bebida)

    
    def vListo(self, Bebida):
        Bebida = Bebida
        QTimer.singleShot(200, self.ventana_espera.close)
        self.ventana_listo = QMainWindow()
        loadUi(os.path.join(BASE_DIR, "ventanas", "vListo.ui"), self.ventana_listo)
        # Cargar el GIF usando barras inclinadas
        self.movieFin = QMovie(os.path.join(BASE_DIR, "Bebidas", "Gifs", "bebidaFinalizar.gif"))
        self.ventana_listo.gifbebidaFin.setMovie(self.movieFin)
        self.movieFin.start()  # Iniciar la animación del GIF
        self.movieFin.setScaledSize(QSize(350, 350))

        self.ventana_listo.gracias.setText(f"Por favor, recoge tu {Bebida}\nGRACIAS POR SU COMPRA")
        self.ventana_listo.btnFin.clicked.connect(self.volverAMenu)
        self.ventana_listo.btnFin.setCursor(Qt.PointingHandCursor)
        self.ventana_listo.showFullScreen()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()  # Mostrar la ventana principal
    sys.exit(app.exec_())

