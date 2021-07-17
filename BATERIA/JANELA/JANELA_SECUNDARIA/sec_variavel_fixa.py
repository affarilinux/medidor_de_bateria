## variaveis labels fixas da janelas secundaria main.py- janela_segunda

########################################################################
## bibliotecas do sistema de python

import  sys

     ######################################################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )

from CONFIGURACOES.config_sec import LARGURA_sec_principal

class SEc_fixo (QMainWindow):

    def __init__ (self):

        super ().__init__  () 

        self.label_temp_uso  = QLabel     ( self     )

        self.label_temp_uso.setStyleSheet ( 'QLabel{ background-color: #4169E1} ' ) # cor: RoyalBlue

        self.label_temp_uso.move          ( 0,5  )                      # x,y externo
        self.label_temp_uso.resize        ( LARGURA_sec_principal,60 )  # x,y interno
