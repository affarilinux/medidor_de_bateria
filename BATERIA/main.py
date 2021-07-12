#comentario # '''
#python3 xxxx.py

####################################################################
### bibliotecas do sistema de python

import  sys

     ###################################################################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QPushButton )

from PyQt5.QtGui         import QIcon

#######################################################################
### arquivos.py do sistema

from config_main      import largura, altura

######################################################################3###########
### arquivos.py da janela

from main_variavel_fixa    import Label_fixo            ## variaveis fixas

from main_tempo            import Temporizador_carga    ## relogio de tempo de carga

from main_estado_bateria   import Estado_carga_bateria  ## carregando ou descarregando True/False

from main_calculo_ram      import Calculo_ram           ## calculo de porcentagem ram

from main_nivel_bateria    import Nivel_bateria         ## nivel de carga da bateria




#######################################################################################################
# inicio janela

class Window  ( Label_fixo, Temporizador_carga, Estado_carga_bateria, Calculo_ram, 
               Nivel_bateria, QMainWindow ):

     def __init__          ( self ):

          super ().__init__()                                    #metodo construtor

          self.title         = " MEDIDOR DE BATERIA "            #titulo

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

          self.setStyleSheet       ( self.cor_fundo )                                #cor de fundo

          self.setWindowIcon(self.ico)

          ##################################################################################
          #@@@@@@@@função sistema

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
########################################################################################
############################ execução interna janela

class controlador:

     def __init__ (self):

          self.Show_Login()

     def Show_Login (self):

          self.Login = Window()
          self.Login.show()


def main                ():
          
     App = QApplication   ( sys.argv )
     window = controlador      ()

     sys.exit             ( App.exec_ ( ) )

if __name__ == "__main__":

     main()
