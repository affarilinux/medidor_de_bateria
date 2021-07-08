## janela  principal temporizador main.py

##########################################################################
## bibliotecas do sistema de python

import  sys

import psutil

    #######################################################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )

from PyQt5.QtCore        import QTimer

class Calculo_ram ( QMainWindow ):

    def __init__                  ( self ):

        super ().__init__                 ()              #metodo construtor

        ####################################################
        #label

        self.label_nome_ram  = QLabel     ( self )

        self.label_nome_ram.setStyleSheet ( ' QLabel { font: bold; font-size:25px; background-color: #00BFFF} ' ) # cor: Wheat

        self.label_nome_ram.move          ( 260,95 )      #x,y externo
        self.label_nome_ram.resize        ( 70,25  )      #x,y interno

        ##################################################
        # primeira chamada de apresentação label

        self. Sistema_Ram_Por_centagem ()
        
        ################################################
        #loop

        self.timer = QTimer        ( self )

        self.timer.setInterval     ( 5000 )
        self.timer.start           ()

        self.timer.timeout.connect ( self.Sistema_Ram_Por_centagem ) #chamada de função

    ####################################################
    #informações ram

    def inwi ( self ):

        #informações da meoria ram
        self.informacao = psutil.virtual_memory ()

        # puxa as iformações e adiciona nas variaveis
        self.total  = self.informacao.total
        self.usada  = self.informacao.active

        #calcula porcentagm
        self.calculo_por_centagem = ( self.usada * 100 ) / self.total

        #filtra o float
        self.cal = round ( self.calculo_por_centagem, 2 )

    ##################################################################
    #apresentação label do sistema

    def Sistema_Ram_Por_centagem ( self ):
                  
        self.inwi                        ()                 # chamada de função
        
        self.resultado = str             ( self.cal       ) #transforma em string a informação float
        self.label_nome_ram.setText      ( self.resultado ) # apresentação

    
          
        




