## janela  principal temporizador main.py

##################################################
## bibliotecas do sistema de python

import  sys

    ##############################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )


class jANELA1TemporizadorCarga ( QMainWindow ):

    def __init__             (self):

        super ().__init__    ()   # metodo construtor

        #label variavel
        self.LABEL_tempo_carga  = QLabel     ( self )

        self.LABEL_tempo_carga.setText       (" 01H 20M 30s " )

        # cor: Wheat
        self.LABEL_tempo_carga.setStyleSheet ( 
            'QLabel { font: bold; font-size:15px; background-color: #F5DEB3 }' ) 

        self.LABEL_tempo_carga.move          ( 100, 5  )   # x,y externo
        self.LABEL_tempo_carga.resize        ( 140, 30 )   # x,y interno
