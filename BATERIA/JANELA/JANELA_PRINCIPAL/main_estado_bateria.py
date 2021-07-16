## janela  principal temporizador main.py

###################################################################
## bibliotecas do sistema de python

import  sys

     ###################################################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )

############################################################################
##arquivos.py sistema app

from .informacao_bateria  import informacao_carregamento

class Estado_carga_bateria (QMainWindow):

     def __init__              (self):

          super ().__init__    ()  #metodo construtor

          self.Estado_Bateria_Atual ()

          self.dados_estado      =  informacao_carregamento

          if self.dados_estado   == True :

               self.Estado_True_Carregamento  ()

          elif self.dados_estado == False :

               self.Estado_False_Carregamento ()

     ##################################################################
     #estados

     def Estado_True_Carregamento     ( self ):                 #true

          self.label_tempo_carga.setText  (" CARREGANDO" )

          #######################################################

     def Estado_False_Carregamento (self):                      #false

          self.label_tempo_carga.setText  (" DESCARREGANDO" )

    ######################################################################################
    ### label 

     def Estado_Bateria_Atual          ( self ):

          #label variavel
          self.label_tempo_carga  = QLabel     ( self )

          self.label_tempo_carga.setStyleSheet (' QLabel { font: bold; font-size:15px; background-color: #F5DEB3 } ' ) # cor: Wheat

          self.label_tempo_carga.move          ( 100,40 )                   #x,y externo
          self.label_tempo_carga.resize        ( 140,30 )                   #x,y interno