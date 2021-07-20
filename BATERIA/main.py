#comentario # '''
#python3 xxxx.py
#resource

##################################################
### bibliotecas do sistema de python

import  sys

    ##############################################

from PyQt5.QtWidgets  import ( QApplication, QMainWindow, QPushButton )
from PyQt5.QtGui      import QIcon
from PyQt5.QtCore     import pyqtSlot, QObject, pyqtSignal


##################################################
### configurações da janela principal.

from CONFIGURACAO.config_main      import LARGURA, ALTURA


##################################################
### configurações da janela SECUNDARIA


###  JANELA_SEGURANÇA
from CONFIGURACAO.config_sec       import LARGURA_2, ALTURA_2


##################################################
# multi janela

#arquivo.py- Bateria
from config_multi_janelas           import ( QICONE_BARRA_DE_TAREFA, TITULO, 
                                             COR_DARKGRAY )


##################################################
### arquivos.py da janela principal

## variaveis fixas
from JANELA.JANELA_PRINCIPAL.main_variavel_fixa    import Janela1Fixa   
## relogio de tempo de carga
from JANELA.JANELA_PRINCIPAL.main_tempo            import ( 
     jANELA1TemporizadorCarga )
## carregando ou descarregando True/False
from JANELA.JANELA_PRINCIPAL.main_estado_bateria   import (
    Janela1EstadoCargaBateria )
## calculo de porcentagem ram
from JANELA.JANELA_PRINCIPAL.main_calculo_ram      import Janela1CalculoRam           
## nivel de carga da bateria
from JANELA.JANELA_PRINCIPAL.main_nivel_bateria    import janela1NivelBateria         


##################################################
### arquivos.py da janela secundaria

#variaveis fixas
from JANELA.JANELA_SECUNDARIA.sec_variavel_fixa    import Janela2Fixa


#-------------------------------------------------
##################################################
### sinais do sistema
#class Sinal_Sec (QObject):

     #sinal_volta_tela = pyqtSignal ( name = "janelasecundaria" )

class Sinais ( QObject ):

    # entre aspa não pode ficar afastado se não da erro
    # janela pŕincial
    sinal1 = pyqtSignal( name = "Janelaprincipal"  ) 


#-------------------------------------------------
##################################################
### janela secundaria
class JanelaSegunda ( Janela2Fixa, QMainWindow ):

    def __init__( self ):

        super ().__init__()  # metodo construtor

        self.TOP_2  = 500    # topo - esquerda para direita
        self.LEFT_2 = 200    # esquerda-cima para baixo

        ##########################################
        ###chamar função

        self.Init_janela()


     #############################################
     ######## execução de janela

    def Init_janela( self ):

        # titulo
        self.setWindowTitle  ( TITULO )                        

        # informações da janela
        self.setGeometry     ( self.TOP_2, self.LEFT_2, LARGURA_2, ALTURA_2 )  
        # tamanho fixo da janela
        self.setFixedSize    ( LARGURA_2, ALTURA_2 ) 

        # cor de fundo 
        self.setStyleSheet   ( COR_DARKGRAY )                        

        # icone da barra de tarefa
        self.setWindowIcon   ( QIcon ( QICONE_BARRA_DE_TAREFA ))     

        ##########################################
        ###@@@@@@@@ função sistema

        # chamada do sinal da janela
          #self.sinal_jan_secundaria = Sinal_Sec ()

        # chamadado botao da janela
        self.Janela_Buton_Voltar_Principal()


    ##############################################
    ### botao

    def Janela_Buton_Voltar_Principal( self ):

        self.BUTON_janela2  = QPushButton  ( self )

        self.BUTON_janela2.setText         ( "JANELA PRINCIPAL" )

        # cor: PaleGreen
        self.BUTON_janela2.setStyleSheet   ( 
            'QPushButton { font: bold; font-size:25px; background-color: #98FB98 }' )

        # x,y externo
        self.BUTON_janela2.move            ( 630, 15 ) 
        # x,y interno 
        self.BUTON_janela2.resize          ( 250, 45 )      

        self.BUTON_janela2.clicked.connect ( self.Entrar_Janela_Principal )


    def Entrar_Janela_Principal( self ):

        print("ola")

          #self.sinal_jan_secundaria.sinal_volta_tela.emit       () # chamar janela secundaria
          #self.sinal_jan_secundaria.sinal_volta_tela.disconnect () # disconectar o sinal de abrir janela


#-------------------------------------------------
##################################################
#### inicio janela

class Window ( Janela1Fixa, jANELA1TemporizadorCarga, 
               Janela1EstadoCargaBateria, Janela1CalculoRam, 
               janela1NivelBateria, QMainWindow ):

    def __init__( self ):

        super ().__init__ ()  # metodo construtor

        self.TOP   = 1500     # topo - esquerda para direita
        self.LEFT  = 200      # esquerda-cima para baixo
          
        ##########################################
        #@@ chamar função

        self.InitWindow()

    ##############################################
    ### execução de janela


    def InitWindow( self ):

         # titulo
        self.setWindowTitle ( TITULO )                   

        # informações da janela
        self.setGeometry    ( self.TOP, self.LEFT, LARGURA, ALTURA )  
        # tamanho fixo da janela
        self.setFixedSize   ( LARGURA, ALTURA )                    

         #cor de fundo
        self.setStyleSheet  ( COR_DARKGRAY )                   

        # icone da barra de tarefa
        self.setWindowIcon  ( QIcon ( QICONE_BARRA_DE_TAREFA ))    

        ##########################################
        ### função sistema

        # chamada do sinal da janela
        self.sinal_jan_1 = Sinais()

        # chamadado botao da janela
        self.Janela_a_Botao()
         

     #############################################
     ### botao

    def Janela_a_Botao( self ):

        self.BUTON_janela1  = QPushButton  ( self     )

        self.BUTON_janela1.setText         ( "CONFIGURAÇÕES" )

        # cor: PaleGreen
        self.BUTON_janela1.setStyleSheet   ( 
            ' QPushButton { font: bold; font-size:25px; background-color: #98FB98 } ' ) 

        self.BUTON_janela1.move            ( 10,  80  )  #x,y externo
        self.BUTON_janela1.resize          ( 230, 40  )  #x,y interno


        self.BUTON_janela1.clicked.connect ( self.Entrar_Janela_Sistema )


     ###função abrir janela
    def Entrar_Janela_Sistema( self ):

        #sela.Loguin - class controlador
        # chamar janela secundaria
        self.sinal_jan_1.sinal1.emit       () 
        # disconectar o sinal de abrir janela
        self.sinal_jan_1.sinal1.disconnect () 


#-------------------------------------------------
##################################################
### execução interna janela

class Controlador:

    def __init__( self ):

        self.Show_Login()


     #janela principal
    @pyqtSlot()                 # decoreto
    def Show_Login( self ):

        # chamar janela principal
        self.Login = Window()   
        # chamada de sinal- class Sinais
        self.Login.sinal_jan_1.sinal1.connect ( self.Show_2 ) 
        # abrir janela principal
        self.Login.show()       

        #self.tela_2.close()


     #janela secundaria
     #@pyqtSlot ()
    def Show_2( self ):

          #self.Login.close()
        # chamar janela principal
        self.tela_2 = JanelaSegunda()         


          #self.tela_2.sinal_jan_secundaria.sinal_volta_tela.connect ( self.Show_Login )
        # abrir janela principal
        self.tela_2.show()                     

          
#-------------------------------------------------
##################################################
###execução main da janela

def main():
          
    App    = QApplication ( sys.argv )

    window = Controlador  ()

    sys.exit              ( App.exec_ ( ) )


if __name__ == "__main__":

    main ()
