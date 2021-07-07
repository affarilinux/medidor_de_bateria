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

        self.label_nome_ram  = QLabel     ( self )

        self.label_nome_ram.setStyleSheet ( ' QLabel { font: bold; font-size:25px; background-color: #00BFFF} ' ) # cor: Wheat

        self.label_nome_ram.move          ( 260,95 )      #x,y externo
        self.label_nome_ram.resize        ( 70,25  )      #x,y interno

        self. Sistema_Ram_Por_centagem ()

                    
        self.timer = QTimer        ( self )

        self.timer.setInterval     ( 5000 )
        self.timer.start           ()

        self.timer.timeout.connect ( self.Sistema_Ram_Por_centagem )

    def inwi ( self ):

        self.informacao = psutil.virtual_memory ()

        # puxa as iformações e adiciona nas variaveis
        self.total  = self.informacao.total
        self.usada  = self.informacao.active

        self.calculo_por_centagem = ( self.usada * 100 ) / self.total

        self.cal = round ( self.calculo_por_centagem, 2 )

        

    def Sistema_Ram_Por_centagem ( self ):
          #print("certo")
          
        self.inwi                        ()
          
        self.resultado = str             ( self.cal )
        self.label_nome_ram.setText      ( self.resultado )

    
          
        




