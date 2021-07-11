## janela  principal main.py

############################################################################
## bibliotecas do sistema de python

import  sys
     
     ######################################################################
     
from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QPushButton )

############################################################################
##arquivos.py sistema app

class Botao_janela ( QMainWindow ):

     def __init__                ( self ):

          super ().__init__              ()                 #metodo construtor

          self.botao_jan  = QPushButton  ( self     )

          self.botao_jan.setText         ( "CONFIGURAÇÕES" )

          self.botao_jan.setStyleSheet   ( ' QPushButton { font: bold; font-size:25px; background-color: #98FB98 } ' ) # cor: PaleGreen

          self.botao_jan.move            ( 10,80    )       #x,y externo
          self.botao_jan.resize          ( 230,40   )       #x,y interno

          self.botao_jan.clicked.connect ( self.Entrar_Janela_Sistema )


     def Entrar_Janela_Sistema      (self):

          print("ola")
