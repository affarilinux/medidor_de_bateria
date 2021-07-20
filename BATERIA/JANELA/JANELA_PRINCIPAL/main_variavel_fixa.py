## variaveis labels fixas da janelas principal main.py

##################################################
## bibliotecas do sistema de python

import  sys

     #############################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )

##################################################
##arquivos.py sistema app

from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.config_jan  import ( 
    POR_CENTAGEM )


class Janela1Fixa( QMainWindow ):

    def __init__( self ):

        super ().__init__()    # metodo construtor

        ##########################################
        ##########################################
        ##tempo 

        self.LABEL_tempo_uso  = QLabel     ( self )

        self.LABEL_tempo_uso.setText       ( " TEMPO:" )

        # cor: Wheat
        self.LABEL_tempo_uso.setStyleSheet ( 
            'QLabel { font: bold; font-size:15px; background-color: #F5DEB3}' ) 

        self.LABEL_tempo_uso.move          ( 10, 5  )      # x,y externo
        self.LABEL_tempo_uso.resize        ( 80, 30 )      # x,y interno

        ##########################################
        ##########################################
        ## estado bateria

        self.LABEL_estado_carga  = QLabel     ( self )

        self.LABEL_estado_carga.setText       ( " ESTADO:" )

        # cor: Wheat
        self.LABEL_estado_carga.setStyleSheet ( 
            'QLabel { font: bold; font-size:15px; background-color: #F5DEB3 }' ) 

        self.LABEL_estado_carga.move          ( 10, 40 )   # x,y externo
        self.LABEL_estado_carga.resize        ( 80, 30 )   # x,y interno

        ##########################################
        ##########################################
        ##### memoria ram

        self.LABEL_nome_ram  = QLabel        ( self )

        self.LABEL_nome_ram.setText          ( " RAM:" )
        # cor: Wheat
        self.LABEL_nome_ram.setStyleSheet    ( 
            'QLabel { font: bold; font-size:15px; background-color: #00BFFF}' ) 

        self.LABEL_nome_ram.move             ( 260, 70 )   # x,y externo
        self.LABEL_nome_ram.resize           ( 105, 20 )   # x,y interno

          
        self.LABEL_porct_ram  = QLabel      ( self )

        self.LABEL_porct_ram.setText        ( POR_CENTAGEM )

        # cor: Wheat
        self.LABEL_porct_ram.setStyleSheet  ( 
            'QLabel { font: bold; font-size:25px; background-color: #00BFFF}' ) 

        self.LABEL_porct_ram.move           ( 335, 95 )    # x,y externo
        self.LABEL_porct_ram.resize         ( 30,  25 )    # x,y interno

        ##########################################
        ##########################################
        ## bateria

        self.LABEL_porcentagem_bateria  = QLabel      ( self )

        self.LABEL_porcentagem_bateria.setText        ( " BATERIA:" )

        #cor Line
        self.LABEL_porcentagem_bateria.setStyleSheet  ( 
            'QLabel { font: bold; font-size:15px; background-color: #00FF00}' ) 

        # x,y externo
        self.LABEL_porcentagem_bateria.move           ( 260, 5  )
         # x,y interno
        self.LABEL_porcentagem_bateria.resize         ( 105, 20 )           

          
        self.LABEL_porcentagem_1  = QLabel      ( self )

        self.LABEL_porcentagem_1.setText        ( POR_CENTAGEM  )

        #cor Line
        self.LABEL_porcentagem_1.setStyleSheet  ( 
            'QLabel { font: bold; font-size:35px; background-color: #00FF00}' ) 

        self.LABEL_porcentagem_1.move           ( 330, 30 )# x,y externo
        self.LABEL_porcentagem_1.resize         ( 35,  35 )# x,y interno