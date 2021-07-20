



## janela  principal temporizador main.py

##################################################
## bibliotecas do sistema de python

import  sys

import psutil

    ##############################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )

from PyQt5.QtCore        import QTimer

class Janela1CalculoRam ( QMainWindow ):

    def __init__( self ):

        super ().__init__()    # metodo construtor

        ##########################################
        #label

        self.LABEL_usado_de_ram  = QLabel     ( self )

        # cor: Wheat
        self.LABEL_usado_de_ram.setStyleSheet ( 
            'QLabel { font: bold; font-size:25px; background-color: #00BFFF}' ) 

        self.LABEL_usado_de_ram.move          ( 260, 95 )  # x,y externo
        self.LABEL_usado_de_ram.resize        ( 70,  25 )  # x,y interno

        ##########################################
        # primeira chamada de apresentação label

        self. Sistema_Ram_Por_centagem ()
        
        ##########################################
        #loop

        self.TIMER_loop_calculo = QTimer        ( self )

        self.TIMER_loop_calculo.setInterval     ( 5000 )
        self.TIMER_loop_calculo.start           ()

        # chamada de função
        self.TIMER_loop_calculo.timeout.connect ( 
            self.Sistema_Ram_Por_centagem ) 

    ##############################################
    #informações ram

    def  Computador_Sistema( self ):

        #informações da memoria ram
        self.informacao           = psutil.virtual_memory ()

        # puxa as iformações e adiciona nas variaveis
        self.total                = self.informacao.total
        self.usada                = self.informacao.active

        #calcula porcentagm
        self.calculo_por_centagem      = ( self.usada * 100 ) / self.total

        #filtra o float
        self.calculo_filtro_informacao = round ( self.calculo_por_centagem, 2 )

    ##############################################
    #apresentação label do sistema

    def Sistema_Ram_Por_centagem( self ):
                  
        self.Computador_Sistema() # chamada de função
        
        #transforma em string a informação float
        self.string_dados = str         ( self.calculo_filtro_informacao) 
        # apresentação
        self.LABEL_usado_de_ram.setText ( self.string_dados ) 

    
          
        




