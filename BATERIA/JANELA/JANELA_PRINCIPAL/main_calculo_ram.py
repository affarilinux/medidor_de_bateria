## janela  principal temporizador main.py

##################################################
## bibliotecas do sistema de python

import  sys

     #############################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )

##################################################
##arquivos.py sistema app

from .informacao_bateria  import informacao_carregamento

#SISTEMA EXTERNO
from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
     VERTICAL_CENTER_1X, HORIZONTAL_2Y
)
#SISTEMA INTERNO
from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
     INTERNO_VERTICAL_2X, INTERNO_HORIZONTAL_1Y
)


#-------------------------------------------------
#################################################

class Janela1EstadoCargaBateria ( QMainWindow ):

     def __init__ ( self ):

          super ().__init__()  # metodo construtor

          self.Estado_Bateria_Atual()

          self.dados_estado      =  informacao_carregamento

          if self.dados_estado   == True :

               self.Estado_True_Carregamento()

          elif self.dados_estado == False :

               self.Estado_False_Carregamento()

     #############################################
     #estados

     def Estado_True_Carregamento( self ):                        # true

          self.LABEL_atualizacao_carregamento.setText ( " CARREGANDO" )

          ########################################

     def Estado_False_Carregamento( self ):                      # false

          self.LABEL_atualizacao_carregamento.setText ( " DESCARREGANDO" )

    ##############################################
    ### label 

     def Estado_Bateria_Atual( self ):

          #label variavel
          self.LABEL_atualizacao_carregamento  = QLabel     ( self )

          # cor: Wheat
          self.LABEL_atualizacao_carregamento.setStyleSheet (
               'QLabel { font: bold; font-size:15px; background-color: #F5DEB3 }'
          ) 
          
          # x,y externo
          self.LABEL_atualizacao_carregamento.move          ( 
               VERTICAL_CENTER_1X, HORIZONTAL_2Y 
          )
          # x,y interno                   
          self.LABEL_atualizacao_carregamento.resize        ( 
               INTERNO_VERTICAL_2X, INTERNO_HORIZONTAL_1Y 
          )                   