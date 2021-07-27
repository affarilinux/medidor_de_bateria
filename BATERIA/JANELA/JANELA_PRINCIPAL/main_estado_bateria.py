## janela  principal temporizador main.py

##################################################
## bibliotecas do sistema de python

import  sys
import psutil

     #############################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )
from PyQt5.QtCore        import QTimer

##################################################
##arquivos.py sistema app

#SISTEMA EXTERNO
from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
     VERTICAL_CENTER_1X, HORIZONTAL_2Y
)
#SISTEMA INTERNO
from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
     INTERNO_VERTICAL_2X, INTERNO_HORIZONTAL_1Y
)

##################################################
# arquivo.py

from TEMPORIZADOR.timer  import CHAMADA_5000


#-------------------------------------------------
#################################################

class Janela1EstadoCargaBateria ( QMainWindow ):

     def __init__ ( self ):

          super ().__init__()  # metodo construtor

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

          ##########################################
          # primeira chamada de apresentação label

          self.Chamada_Sistema_Interno()  

          ##########################################
          # loop

          self.TIMER_estado_chamada = QTimer        ( self )

          self.TIMER_estado_chamada.setInterval     ( CHAMADA_5000 )
          self.TIMER_estado_chamada.start           ()

          #chamada de funçãO
          self.TIMER_estado_chamada.timeout.connect ( self.Chamada_Sistema_Interno ) 

     def Chamada_Sistema_Interno( self ):

          # puxa os dado do sistema operacional
          self.informacao_bateria = psutil.sensors_battery()

          # puxa uma informação se esta plugado na internet
          self.informacao_carregamento = self.informacao_bateria.power_plugged      

          if self.informacao_carregamento   == True :

               self.Estado_True_Carregamento()

          elif self.informacao_carregamento == False :

               self.Estado_False_Carregamento()


     #############################################
     # estados

     def Estado_True_Carregamento( self ):                        # true

          self.LABEL_atualizacao_carregamento.setText ( " CARREGANDO" )

          ########################################

     def Estado_False_Carregamento( self ):                      # false

          self.LABEL_atualizacao_carregamento.setText ( " DESCARREGANDO" )