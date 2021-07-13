#comentario # '''
#python3 xxxx.py

####################################################################
### bibliotecas do sistema de python

import  sys

     ###################################################################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QPushButton )

from PyQt5.QtGui         import QIcon

from PyQt5.QtCore import pyqtSlot, QObject, pyqtSignal

#######################################################################
### arquivos.py do sistema

from config_main      import largura, altura, Titulo

######################################################################3###########
### arquivos.py da janela

from main_variavel_fixa    import Label_fixo            ## variaveis fixas

from main_tempo            import Temporizador_carga    ## relogio de tempo de carga

from main_estado_bateria   import Estado_carga_bateria  ## carregando ou descarregando True/False

from main_calculo_ram      import Calculo_ram           ## calculo de porcentagem ram

from main_nivel_bateria    import Nivel_bateria         ## nivel de carga da bateria

class Sinais(QObject):
     sinal1 = pyqtSignal(name = "janelaprincipal")

class Janela_segunda (QMainWindow):

     def __init__          ( self ):

          super ().__init__()  

          self.nome_jan  = Titulo

          self.top_2     = 500
          self.left_2    = 200

          self.width_2   = 200
          self.height_2  = 200

          self.cor_fundo_2 = ' background-color: #A9A9A9 '     #cor DarkGray

          self.jan_fixo_larg_2 = largura                           #largura
          self.jan_fixo_alt_2  = altura                            #altura

          self.ico_2           = QIcon("carregador.png")

          self.Init_janela()

     def Init_janela(self):
          self.setWindowTitle      ( self.nome_jan      )                               # titulo

          self.setGeometry         ( self.top_2, self.left_2, self.width_2, self.height_2 )  # informações da janela
          self.setFixedSize        ( self.jan_fixo_larg_2, self.jan_fixo_alt_2        )  # tamanho fixo da janela

          self.setStyleSheet       ( self.cor_fundo_2 )                                #cor de fundo

          self.setWindowIcon       ( self.ico_2 )

#######################################################################################################
# inicio janela

class Window  ( Label_fixo, Temporizador_carga, Estado_carga_bateria, Calculo_ram, 
               Nivel_bateria, QMainWindow ):

     def __init__          ( self ):

          super ().__init__()                                    #metodo construtor

          self.title         = Titulo           #titulo

          self.top           = 1500                              #topo - esquerda para direita
          self.left          = 200                               #esquerda-cima para baixo

          self.width         = largura                           #largura
          self.height        = altura                            #altura

          self.cor_fundo     = ' background-color: #A9A9A9 '     #cor DarkGray

          self.jan_fixo_larg = largura                           #largura
          self.jan_fixo_alt  = altura                            #altura

          self.ico           = QIcon("carregador.png")

          
          ######################################################################
          #@@@@@@@@@@@@@@@@@@ chamar função

          self.InitWindow        ()

     ###############################################################################
     ######## execução de janela

     def InitWindow        ( self ):

          self.setWindowTitle      ( self.title      )                               # titulo

          self.setGeometry         ( self.top, self.left, self.width, self.height )  # informações da janela
          self.setFixedSize        ( self.jan_fixo_larg, self.jan_fixo_alt        )  # tamanho fixo da janela

          self.setStyleSheet       ( self.cor_fundo  )                               #cor de fundo

          self.setWindowIcon       ( self.ico        ) 

          ##################################################################################
          #@@@@@@@@função sistema

          self.sinais_jan_1 = Sinais()
          self.Janela_a_Botao()
         
          #self.show                 ()

     def Janela_a_Botao(self):

          self.botao_jan  = QPushButton  ( self     )

          self.botao_jan.setText         ( "CONFIGURAÇÕES" )

          self.botao_jan.setStyleSheet   ( ' QPushButton { font: bold; font-size:25px; background-color: #98FB98 } ' ) # cor: PaleGreen

          self.botao_jan.move            ( 10,80    )       #x,y externo
          self.botao_jan.resize          ( 230,40   )       #x,y interno


          self.botao_jan.clicked.connect ( self.Entrar_Janela_Sistema )

     
     def Entrar_Janela_Sistema      (self):

          print("ola")

          self.sinais_jan_1.sinal1.emit()
          self.sinais_jan_1.sinal1.disconnect()
     
########################################################################################
############################ execução interna janela

class controlador:

     def __init__ (self):

          self.Show_Login()

     @pyqtSlot() # decoreto
     def Show_Login (self):

          self.Login = Window()
          self.Login.sinais_jan_1.sinal1.connect(self.Show_2)
          self.Login.show()

     def Show_2(self):

          self.tela_2 = Janela_segunda()
          self.tela_2.show()


def main                ():
          
     App = QApplication   ( sys.argv )
     window = controlador      ()

     sys.exit             ( App.exec_ ( ) )

if __name__ == "__main__":

     main()
