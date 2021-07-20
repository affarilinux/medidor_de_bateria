## variaveis label janela  principal temporizador main.py

##################################################
## bibliotecas do sistema de python

import  sys

import psutil

    ##############################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )

from PyQt5.QtCore        import QTimer


class janela1NivelBateria( QMainWindow ):

    def __init__( self ):

        super ().__init__()  #metodo construtor

        ##########################################
        #label

        self.LABEL_atualizacao_nivel  = QLabel     ( self )

        #cor Line
        self.LABEL_atualizacao_nivel.setStyleSheet ( 
            'QLabel { font: bold; font-size:30px; background-color: #00FF00}' ) 

        # x,y externo
        self.LABEL_atualizacao_nivel.move          ( 260, 30 )   
        # x,y interno     
        self.LABEL_atualizacao_nivel.resize        ( 65,  35 )         

        ##########################################
        # primeira chamada de apresentação label

        self.Sistema_Bateria()

        ##########################################
        #loop

        self.TIMER_loop_nivel = QTimer        ( self )

        self.TIMER_loop_nivel.setInterval     ( 5000 )
        self.TIMER_loop_nivel.start           ()

        #chamada de funçãO
        self.TIMER_loop_nivel.timeout.connect ( self.Sistema_Bateria ) 

    #função chamada interna do sistema operacional

    def Loop_Timer_Bateria( self ):

        #chama os dados para a janela
        self.BATERIA_sistema = psutil.sensors_battery()

        #chama o tipo de informação
        self.nivel_bateria   = self.BATERIA_sistema.percent

        # transforma em int
        self.entrada_informacao = int(self.nivel_bateria)

    # chamada do loop
    def Sistema_Bateria( self ):

        self.Loop_Timer_Bateria()

        #string
        self.medida = str(self.entrada_informacao)
        #print para janela
        self.LABEL_atualizacao_nivel.setText( self.medida )