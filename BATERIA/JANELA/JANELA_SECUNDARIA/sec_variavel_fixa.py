## variaveis labels fixas da janelas secundaria main.py- janela_segunda

##################################################
## bibliotecas do sistema de python

import  sys

     #############################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )
from CONFIGURACOES.config_sec import LARGURA_2


class  Janela2Fixa( QMainWindow ):

    def __init__( self ):

        super ().__init__() # metodo construtor

        ##########################################
        ###BARRA DE MENUS JANELA 2
        
        self.LABEL_menus_janela2  = QLabel     ( self )

        # cor: RoyalBlue
        self.LABEL_menus_janela2.setStyleSheet ( 
            'QLabel{ background-color: #4169E1}' ) 

         # x,y externo
        self.LABEL_menus_janela2.move          ( 0, 5  )                     
        # x,y interno
        self.LABEL_menus_janela2.resize        ( LARGURA_2, 60 )  