## variaveis labels fixas da janelas principal main.py

########################################################################
## bibliotecas do sistema de python

import  sys

     ######################################################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )

############################################################################
##arquivos.py sistema app

from config_main         import por_centagem_label


class Label_fixo ( QMainWindow ):

     def __init__            ( self ):

          super ().__init__  ()                #metodo construtor

          #self.pc_ext = por_centagem_label

          #############################################################################
          #############################################################################
          ##tempo 

          self.label_temp_uso  = QLabel     ( self     )

          self.label_temp_uso.setText       ( " TEMPO:" )

          self.label_temp_uso.setStyleSheet ( ' QLabel { font: bold; font-size:15px; background-color: #F5DEB3} ' ) # cor: Wheat

          self.label_temp_uso.move          ( 10,5  )                   #x,y externo
          self.label_temp_uso.resize        ( 80,30 )                   #x,y interno

          #############################################################################
          #############################################################################
          ## estado bateria

          self.label_est_carg  = QLabel     ( self      )

          self.label_est_carg.setText       ( " ESTADO:" )

          self.label_est_carg.setStyleSheet ( ' QLabel { font: bold; font-size:15px; background-color: #F5DEB3 } ' ) # cor: Wheat

          self.label_est_carg.move          ( 10,40 )                   #x,y externo
          self.label_est_carg.resize        ( 80,30 )                   #x,y interno

          #############################################################################
          #############################################################################
          ##### memoria ram

          self.label_nom_ram  = QLabel        ( self )

          self.label_nom_ram.setText          ( " RAM:" )

          self.label_nom_ram.setStyleSheet    ( ' QLabel { font: bold; font-size:15px; background-color: #00BFFF} ' ) # cor: Wheat

          self.label_nom_ram.move             ( 260,70 )                 #x,y externo
          self.label_nom_ram.resize           ( 105,20 )                 #x,y interno

          
          self.label_porct_ram  = QLabel      ( self )

          self.label_porct_ram.setText        ( por_centagem_label )

          self.label_porct_ram.setStyleSheet  ( ' QLabel { font: bold; font-size:25px; background-color: #00BFFF} ' ) # cor: Wheat

          self.label_porct_ram.move           ( 335,95 )                  #x,y externo
          self.label_porct_ram.resize         ( 30,25  )                  #x,y interno

          ################################################################################
          ################################################################################
          ## bateria

          self.label_porcentagem_bat  = QLabel      ( self )

          self.label_porcentagem_bat.setText        ( " BATERIA:" )

          self.label_porcentagem_bat.setStyleSheet  ( ' QLabel { font: bold; font-size:15px; background-color: #00FF00} ' ) #cor Line
 
          self.label_porcentagem_bat.move           ( 260,5  )            #x,y externo
          self.label_porcentagem_bat.resize         ( 105,20 )            #x,y interno

          
          self.label_porcentagem_1  = QLabel        ( self )

          self.label_porcentagem_1.setText          ( por_centagem_label  )

          self.label_porcentagem_1.setStyleSheet    ( ' QLabel { font: bold; font-size:35px; background-color: #00FF00} ' ) #cor Line

          self.label_porcentagem_1.move             ( 330,30 )            #x,y externo
          self.label_porcentagem_1.resize           ( 35,35  )            #x,y interno