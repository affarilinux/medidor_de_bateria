## variaveis labels fixas da janelas principal main.py

##################################################
## bibliotecas do sistema de python

import  sys

     #############################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )

##################################################
##arquivos.py sistema app

from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.config_jan      import ( 
    POR_CENTAGEM 
)
# SISTERMA EXTERNO
from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
    ENTRY_VERTICAL_1Y, INTERNO_HORIZONTAL_1Y, INTERNO_HORIZONTAL_3Y, 
    VERTICAL_ESQUERDA_1X, VERTICAL_DIREITA_1X, HORIZONTAL_1Y, 
    HORIZONTAL_2Y, VERTICAL_DIREITA_2X, HORIZONTAL_3Y, VERTICAL_DIREITA_3Y,
    EXTERNO_VERTICAL_Y_1, EXTERNO_VERTICAL_Y_2
)
# SISTEMA INTERNO
from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
    INTERNO_VERTICAL_1X, INTERNO_VERTICAL_3X, INTERNO_HORIZONTAL_2Y )

    
class Janela1Fixa( QMainWindow ):

    def __init__( self ):

        super ().__init__()    # metodo construtor

        ##########################################
        ##tempo 

        self.LABEL_tempo_uso  = QLabel     ( self )

        self.LABEL_tempo_uso.setText       ( " TEMPO" )

        # cor: Wheat
        self.LABEL_tempo_uso.setStyleSheet ( 
            'QLabel { font: bold; font-size: 15px; background-color: #F5DEB3}' 
        ) 

        # x,y externo
        self.LABEL_tempo_uso.move          ( VERTICAL_ESQUERDA_1X, 
            HORIZONTAL_1Y  
        )   
        # x,y interno
        self.LABEL_tempo_uso.resize        ( INTERNO_VERTICAL_1X, 
            INTERNO_HORIZONTAL_1Y 
        )      


        ##########################################
        ## estado bateria

        self.LABEL_estado_carga  = QLabel     ( self )

        self.LABEL_estado_carga.setText       ( " ESTADO" )

        # cor: Wheat
        self.LABEL_estado_carga.setStyleSheet ( 
            'QLabel { font: bold; font-size: 15px; background-color: #F5DEB3 }' 
        ) 

        # x,y externo
        self.LABEL_estado_carga.move          ( VERTICAL_ESQUERDA_1X, 
            HORIZONTAL_2Y 
        ) 
        # x,y interno  
        self.LABEL_estado_carga.resize        ( INTERNO_VERTICAL_1X, 
            INTERNO_HORIZONTAL_1Y
        )   


        ##########################################
        ##### memoria ram

        self.LABEL_nome_ram  = QLabel        ( self )

        self.LABEL_nome_ram.setText          ( " RAM:" )
        # cor: Wheat
        self.LABEL_nome_ram.setStyleSheet    ( 
            'QLabel { font: bold; font-size: 15px; background-color: #00BFFF}' 
        ) 
        # x,y externo
        self.LABEL_nome_ram.move             ( VERTICAL_DIREITA_1X, 
            EXTERNO_VERTICAL_Y_2 
        ) 
        # x,y interno  
        self.LABEL_nome_ram.resize           ( INTERNO_VERTICAL_3X, 
            INTERNO_HORIZONTAL_2Y 
        )   

        # ----------------------------------------

        self.LABEL_porcentagem_ram  = QLabel      ( self )

        self.LABEL_porcentagem_ram.setText        ( POR_CENTAGEM )

        # cor: Wheat
        self.LABEL_porcentagem_ram.setStyleSheet  ( 
            'QLabel { font: bold; font-size: 25px; background-color: #00BFFF}' 
        ) 

        # x,y externo
        self.LABEL_porcentagem_ram.move           ( VERTICAL_DIREITA_2X, 
            EXTERNO_VERTICAL_Y_1
        )  
        # x,y interno  
        self.LABEL_porcentagem_ram.resize         ( INTERNO_HORIZONTAL_1Y,  
            INTERNO_HORIZONTAL_3Y 
        )    


        ##########################################
        ## bateria

        self.LABEL_porcentagem_bateria  = QLabel      ( self )

        self.LABEL_porcentagem_bateria.setText        ( " BATERIA:" )

        #cor Line
        self.LABEL_porcentagem_bateria.setStyleSheet  ( 
            'QLabel { font: bold; font-size: 15px; background-color: #00FF00}' 
        ) 

        # x,y externo
        self.LABEL_porcentagem_bateria.move           ( VERTICAL_DIREITA_1X, 
            HORIZONTAL_1Y  
        )
         # x,y interno
        self.LABEL_porcentagem_bateria.resize         ( HORIZONTAL_3Y, 
            INTERNO_HORIZONTAL_3Y 
        )           

        # ----------------------------------------
        
        self.LABEL_porcentagem_1  = QLabel      ( self )

        self.LABEL_porcentagem_1.setText        ( POR_CENTAGEM  )

        #cor Line
        self.LABEL_porcentagem_1.setStyleSheet  ( 
            'QLabel { font: bold; font-size: 35px; background-color: #00FF00}' 
        ) 

        # x,y externo
        self.LABEL_porcentagem_1.move           ( VERTICAL_DIREITA_3Y, 
            ENTRY_VERTICAL_1Y 
        )
        # x,y interno
        self.LABEL_porcentagem_1.resize         ( ENTRY_VERTICAL_1Y,  
            ENTRY_VERTICAL_1Y 
        )


        ##########################################
        # processador

        self.LABEL_nome_do_processador = QLabel (self)

        self.LABEL_nome_do_processador.setText  ( " PROCESSADOR" )

        # cor: Yellow1
        self.LABEL_nome_do_processador.setStyleSheet (
            'QLabel{ font: bold; font-size: 25px; background-color: #FFFF00  }'
        )

        self.LABEL_nome_do_processador.move     ( VERTICAL_ESQUERDA_1X, 
            INTERNO_VERTICAL_1X
        )
        self.LABEL_nome_do_processador.resize   ( 200, HORIZONTAL_2Y)


        #-----------------------------------------
        self.LABEL_porcentagem_2 = QLabel (self)

        self.LABEL_porcentagem_2.setText  ( POR_CENTAGEM )

        #cor: Yellow1
        self.LABEL_porcentagem_2.setStyleSheet (
            'QLabel{ font: bold; font-size: 30px; background-color: #FFFF00  }'
        )

        self.LABEL_porcentagem_2.move     ( 325, INTERNO_VERTICAL_1X )
        self.LABEL_porcentagem_2.resize   ( HORIZONTAL_2Y, HORIZONTAL_2Y)
        