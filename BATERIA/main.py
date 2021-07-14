#comentario # '''
#python3 xxxx.py

####################################################################
### bibliotecas do sistema de python

import  sys

     ###################################################################################

from PyQt5.QtWidgets        import ( QApplication, QMainWindow, QPushButton )

from PyQt5.QtGui            import QIcon

from PyQt5.QtCore           import pyqtSlot, QObject, pyqtSignal


##################################################################################
### configurações da janela principal.

from config_main            import largura, altura, Titulo, QIcon_janelas, cor_DarkGray

##################################################################################
### configurações da janela secundaria

from JANELA_SECUNDARIA.config_sec      import LARGURA_sec_principal, ALTURA_sec_principal

######################################################################3###########
### arquivos.py da janela

from main_variavel_fixa    import Label_fixo            ## variaveis fixas

from main_tempo            import Temporizador_carga    ## relogio de tempo de carga

from main_estado_bateria   import Estado_carga_bateria  ## carregando ou descarregando True/False

from main_calculo_ram      import Calculo_ram           ## calculo de porcentagem ram

from main_nivel_bateria    import Nivel_bateria         ## nivel de carga da bateria


###########################################################################################
### sinais do sistema

class Sinais(QObject):

     sinal1 = pyqtSignal ( name = " janelaprincipal " )

##################################################################################################
###################################################################################################
### janela secundaria
class Janela_segunda ( QMainWindow ):

     def __init__          ( self ):

          super ().__init__ ()                                                      # metodo construtor

          self.top_2     = 500                                                     # topo - esquerda para direita
          self.left_2    = 200                                                     # esquerda-cima para baixo

          ######################################################################
          ###@@@@@@@@@@@@@@@@@@ chamar função

          self.Init_janela ()

     ###############################################################################
     ######## execução de janela

     def Init_janela ( self ):

          self.setWindowTitle      ( Titulo                )                         # titulo

          self.setGeometry         ( self.top_2, self.left_2, LARGURA_sec_principal, ALTURA_sec_principal )  # informações da janela
          self.setFixedSize        ( LARGURA_sec_principal, ALTURA_sec_principal )  # tamanho fixo da janela

          self.setStyleSheet       ( cor_DarkGray          )                        # cor de fundo

          self.setWindowIcon       ( QIcon ( QIcon_janelas ) )                      # icone da barra de tarefa

#######################################################################################################
#######################################################################################################
#### inicio janela

class Window  ( Label_fixo, Temporizador_carga, Estado_carga_bateria, Calculo_ram, 
               Nivel_bateria, QMainWindow ):

     def __init__          ( self ):

          super ().__init__ ()                                   # metodo construtor

          self.top           = 1500                              # topo - esquerda para direita
          self.left          = 200                               # esquerda-cima para baixo
          
          ######################################################################
          #@@@@@@@@@@@@@@@@@@ chamar função

          self.InitWindow ()

     ###############################################################################
     ######## execução de janela

     def InitWindow        ( self ):

          self.setWindowTitle      ( Titulo                )       # titulo

          self.setGeometry         ( self.top, self.left, largura, altura )  # informações da janela
          self.setFixedSize        ( largura, altura       )       # tamanho fixo da janela

          self.setStyleSheet       ( cor_DarkGray          )       #cor de fundo

          self.setWindowIcon       ( QIcon ( QIcon_janelas ) )     # icone da barra de tarefa

          ##################################################################################
          ###@@@@@@@@ função sistema

          # chamada do sinal da janela
          self.sinais_jan_1 = Sinais ()

          # chamadado botao da janela
          self.Janela_a_Botao        ()
         
     ##########################################################################################
     ### botao
     def Janela_a_Botao(self):

          self.botao_jan  = QPushButton  ( self     )

          self.botao_jan.setText         ( "CONFIGURAÇÕES" )

          self.botao_jan.setStyleSheet   ( ' QPushButton { font: bold; font-size:25px; background-color: #98FB98 } ' ) # cor: PaleGreen

          self.botao_jan.move            ( 10, 80   )       #x,y externo
          self.botao_jan.resize          ( 230, 40  )       #x,y interno


          self.botao_jan.clicked.connect ( self.Entrar_Janela_Sistema )

     ###função abrir janela
     def Entrar_Janela_Sistema       ( self ):

          #sela.Loguin - class controlador
          self.sinais_jan_1.sinal1.emit       () # chamar janela secundaria
          self.sinais_jan_1.sinal1.disconnect () # disconectar o sinal de abrir janela
     
########################################################################################
########################################################################################
############################ execução interna janela

class controlador:

     def __init__ ( self ):

          self.Show_Login ()

     #janela principal
     @pyqtSlot ()                                # decoreto
     def Show_Login ( self ):

          self.Login = Window                    ()              # chamar janela principal

          self.Login.sinais_jan_1.sinal1.connect ( self.Show_2 ) # chamada de sinal- class Sinais

          self.Login.show                        ()              # abrir janela principal

     #janela secundaria
     def Show_2 ( self ):

          self.tela_2 = Janela_segunda ()         # chamar janela principal

          self.tela_2.show             ()         # abrir janela principal

#######################################################################
#######################################################################
###execução main da janela

def main                ():
          
     App = QApplication   ( sys.argv )
     window = controlador ()

     sys.exit             ( App.exec_ ( ) )

if __name__ == "__main__":

     main ()
