## janela  principal temporizador main.py

##################################################
## bibliotecas do sistema de python

import  sys

    ##############################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )

##################################################
# ARQUIVOS.PY

#SISTEMA EXTERNO
from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
    INTERNO_HORIZONTAL_1Y, VERTICAL_CENTER_1X, HORIZONTAL_1Y
)
#SISTEMA INTERNO
from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
    INTERNO_VERTICAL_2X
)


#-------------------------------------------------
##################################################

class jANELA1TemporizadorCarga ( QMainWindow ):

    def __init__             (self):

        super ().__init__    ()   # metodo construtor

        #label variavel
        self.LABEL_tempo_carga  = QLabel     ( self )

        self.LABEL_tempo_carga.setText       (" 01H 20M 30s " )

        # cor: Wheat
        self.LABEL_tempo_carga.setStyleSheet ( 
            'QLabel { font: bold; font-size:15px; background-color: #F5DEB3 }'
        ) 

        # x,y externo
        self.LABEL_tempo_carga.move          ( VERTICAL_CENTER_1X, 
            HORIZONTAL_1Y  
        )   
        # x,y interno
        self.LABEL_tempo_carga.resize        ( INTERNO_VERTICAL_2X, 
            INTERNO_HORIZONTAL_1Y 
        )   
