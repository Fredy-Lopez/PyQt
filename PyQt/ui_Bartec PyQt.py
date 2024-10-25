# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Bartec PyQtLmHbzQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import Bebidas_rc

class Ui_ventanaMenu(object):
    def setupUi(self, ventanaMenu):
        if not ventanaMenu.objectName():
            ventanaMenu.setObjectName(u"ventanaMenu")
        ventanaMenu.resize(1019, 569)
        ventanaMenu.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(255, 220, 150, 255), /* Color claro, hacia la izquierda */\n"
"        stop:1 rgba(230, 134, 60, 255)  /* Color naranja oscuro, hacia la derecha */\n"
"    );\n"
"\n"
"}\n"
"")
        self.centralwidget = QWidget(ventanaMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget.setAutoFillBackground(False)
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(280, 10, 151, 31))
        self.titulo.setAutoFillBackground(False)
        self.titulo.setStyleSheet(u"QLabel {\n"
"    font-family: \"Calibri\";         /* Fuente Calibri */\n"
"    font-size: 20pt;                /* Tama\u00f1o de 20pt */\n"
"    color: #AC1F01;                 /* Color rojo oscuro especificado */\n"
"    font-weight: bold;            /* Normal, ajusta a bold si necesitas */\n"
"    text-align: left;               /* Alineaci\u00f3n izquierda, c\u00e1mbialo a center si es necesario */\n"
"	background: none;\n"
"}\n"
"")
        self.titulo.setTextFormat(Qt.AutoText)
        self.titulo.setMargin(0)
        self.titulo.setOpenExternalLinks(False)
        self.subTitulo = QLabel(self.centralwidget)
        self.subTitulo.setObjectName(u"subTitulo")
        self.subTitulo.setGeometry(QRect(280, 50, 271, 16))
        self.subTitulo.setAutoFillBackground(False)
        self.subTitulo.setStyleSheet(u"QLabel {\n"
"    font-family: \"Calibri\";         /* Fuente Calibri */\n"
"    font-size: 12pt;                /* Tama\u00f1o de 20pt */\n"
"    color: #AC1F01;                 /* Color rojo oscuro especificado */\n"
"    font-weight: bold;            /* Normal, ajusta a bold si necesitas */\n"
"    text-align: left;               /* Alineaci\u00f3n izquierda, c\u00e1mbialo a center si es necesario */\n"
"	background: none;\n"
"\n"
"}\n"
"")
        self.subTitulo.setTextFormat(Qt.AutoText)
        self.subTitulo.setMargin(0)
        self.subTitulo.setOpenExternalLinks(False)
        self.vodka = QLabel(self.centralwidget)
        self.vodka.setObjectName(u"vodka")
        self.vodka.setGeometry(QRect(530, 90, 191, 181))
        self.vodka.setCursor(QCursor(Qt.ArrowCursor))
        self.vodka.setStyleSheet(u"border-image: url(:/cct/Vodka.png);\n"
"background: none")
        self.cachaza = QLabel(self.centralwidget)
        self.cachaza.setObjectName(u"cachaza")
        self.cachaza.setGeometry(QRect(280, 290, 191, 181))
        self.cachaza.setStyleSheet(u"border-image: url(:/cct/Cachaza.png);\n"
"background: none")
        self.ron = QLabel(self.centralwidget)
        self.ron.setObjectName(u"ron")
        self.ron.setGeometry(QRect(530, 290, 191, 181))
        self.ron.setStyleSheet(u"border-image: url(:/cct/Ron.png);\n"
"background: none")
        self.jugo = QLabel(self.centralwidget)
        self.jugo.setObjectName(u"jugo")
        self.jugo.setGeometry(QRect(280, 90, 191, 181))
        self.jugo.setStyleSheet(u"border-image: url(:/cct/Jugo.png);\n"
"background: none;")
        ventanaMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ventanaMenu)
        self.statusbar.setObjectName(u"statusbar")
        ventanaMenu.setStatusBar(self.statusbar)

        self.retranslateUi(ventanaMenu)

        QMetaObject.connectSlotsByName(ventanaMenu)
    # setupUi

    def retranslateUi(self, ventanaMenu):
        ventanaMenu.setWindowTitle(QCoreApplication.translate("ventanaMenu", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("ventanaMenu", u"\u00a1Bienvenido!", None))
        self.subTitulo.setText(QCoreApplication.translate("ventanaMenu", u"Elija su bebida favorita para comenzar\u2026\n"
"", None))
        self.vodka.setText("")
        self.cachaza.setText("")
        self.ron.setText("")
        self.jugo.setText("")
    # retranslateUi

