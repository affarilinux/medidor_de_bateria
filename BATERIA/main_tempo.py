## janela  principal temporizador main.py

############################################################################
## bibliotecas do sistema de python

import  sys

    #########################################################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )


class Temporizador_carga ( QMainWindow ):

    def __init__             (self):

        super ().__init__    ()               #metodo construtor

        #label variavel
        self.label_tempo_carga  = QLabel     ( self )

        self.label_tempo_carga.setText       (" 01H 20M 30s " )

        self.label_tempo_carga.setStyleSheet ( ' QLabel { font: bold; font-size:15px; background-color: #F5DEB3 } ' ) # cor: Wheat

        self.label_tempo_carga.move          ( 100,5  )                   #x,y externo
        self.label_tempo_carga.resize        ( 140,30 )                   #x,y interno
