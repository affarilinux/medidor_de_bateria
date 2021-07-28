#comentario # '''
#python3 xxxx.py
#resource

##################################################
### bibliotecas do sistema de python

import  sys
import sqlite3

    ##############################################

from PyQt5.QtWidgets  import ( QApplication, QMainWindow, QPushButton )
from PyQt5.QtGui      import QIcon
from PyQt5.QtCore     import pyqtSlot, QObject, pyqtSignal, QTimer


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
                                             COR_DARKGRAY 
                                            )


##################################################
### configurações da janela auxiliar

from CONFIGURACAO.config_janela_auxiliar import LARGURA_3, ALTURA_3
from TEMPORIZADOR.timer                  import CHAMADA_5000

##################################################
### arquivos.py da janela principal

## variaveis fixas
from JANELA.JANELA_PRINCIPAL.main_variavel_fixa     import Janela1Fixa   
## relogio de tempo de carga
from JANELA.JANELA_PRINCIPAL.main_tempo             import ( 
     jANELA1TemporizadorCarga 
)
## carregando ou descarregando True/False
from JANELA.JANELA_PRINCIPAL.main_estado_bateria    import (
    Janela1EstadoCargaBateria 
)
## calculo de porcentagem ram
from JANELA.JANELA_PRINCIPAL.main_calculo_ram       import Janela1CalculoRam           
## nivel de carga da bateria
from JANELA.JANELA_PRINCIPAL.main_nivel_bateria     import janela1NivelBateria 

from JANELA.JANELA_PRINCIPAL.main_nivel_processador import (
    janela1NivelFrequenciaProcessador 
)

# SISTEMA EXTERNO
from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
    VERTICAL_ESQUERDA_1X, EXTERNO_VERTICAL_Y_2
)

from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
    HORIZONTAL_2Y
)


##################################################
### arquivos.py da janela secundaria

#variaveis fixas
from JANELA.JANELA_SECUNDARIA.sec_variavel_fixa    import Janela2Fixa

##################################################
# banco de dados
from config_multi_janelas  import BANCO_INTERNO_SQLITE3

##################################################
### arquivos.py da janela auxiliar

#-------------------------------------------------
##################################################
### sinais do sistema
#class Sinal_Sec (QObject):

     #sinal_volta_tela = pyqtSignal ( name = "janelasecundaria" )

class Sinais ( QObject ):

    # entre aspa não pode ficar afastado se não da erro
    # janela pŕincial
    sinal1 = pyqtSignal( name = "Janelaprincipal"  ) 


class JanelaAuxialiar ( QMainWindow ):
    def __init__( self ):

        super ().__init__()  # metodo construtor

        self.TOP_3  = 700
        self.LEFT_3 = 350

        self.chamar()

    def chamar(self):

        # titulo
        self.setWindowTitle  ( TITULO )

        # informações da janela
        self.setGeometry     ( self.TOP_3, self.LEFT_3, LARGURA_3, ALTURA_3 )

        self.setFixedSize    ( LARGURA_3, ALTURA_3 ) 

        # cor de fundo 
        self.setStyleSheet   ( COR_DARKGRAY )                         


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

        # cor: SlateBlue2
        self.BUTON_janela2.setStyleSheet   ( 
            'QPushButton { font: bold; font-size:25px; background-color: #7A67EE }' )

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
               janela1NivelBateria,janela1NivelFrequenciaProcessador,
                QMainWindow,  ):

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
        self.Loop_Parte1()
         

     #############################################
     ### botao

    def Janela_a_Botao( self ):

        self.BUTON_janela1  = QPushButton  ( self     )

        self.BUTON_janela1.setText         ( "CONFIGURAÇÕES" )

        # cor: SlateBlue2
        self.BUTON_janela1.setStyleSheet   ( 
            ' QPushButton { font: bold; font-size:25px; background-color: #7A67EE } '
        ) 

        #x,y externo
        self.BUTON_janela1.move            ( VERTICAL_ESQUERDA_1X ,  
            EXTERNO_VERTICAL_Y_2 
        )  
        #x,y interno
        self.BUTON_janela1.resize          ( 230, HORIZONTAL_2Y  )  


        self.BUTON_janela1.clicked.connect ( self.Entrar_Janela_Sistema )


     ###função abrir janela
    def Entrar_Janela_Sistema( self ):

        #sela.Loguin - class controlador
        # chamar janela secundaria
        self.sinal_jan_1.sinal1.emit       () 
        # disconectar o sinal de abrir janela
        self.sinal_jan_1.sinal1.disconnect () 

    ##############################################
    ## janela auxiliar

    def Loop_Parte1(self):

        self.TIMER_auxiliar = QTimer        ( self )

        self.TIMER_auxiliar.setInterval     ( CHAMADA_5000 )
        self.TIMER_auxiliar.start           ()

        #chamada de funçãO
        self.TIMER_auxiliar.timeout.connect ( self.Janela_Auxiliar_Chamada )

    def Janela_Auxiliar_Chamada (self):

        self.main_banco_processador = sqlite3.connect ( BANCO_INTERNO_SQLITE3 )
        self.cursor_main            = self.main_banco_processador.cursor()

        # informação bateria

        self.MINIMO_BATERIA = 19
        self.MAXIMO_BATERIA = 90
        
        # informação processador

        self.cursor_main.execute('SELECT *FROM MONTANTE_PROCESSADOR where id = "1" ')
        self.resultado = self.cursor_main.fetchone()

        self.parte_1 = self.resultado[1]

        # informação ram

        self.NIVEL_RAM   = 90

        ## chama a janela auxiliar
        if self.parte_1 >= 10:
            self.tela_3 = JanelaAuxialiar()
            self.tela_3.show()


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

    window_ativar = Controlador  ()

    sys.exit              ( App.exec_ ( ) )


if __name__ == "__main__":

    main ()
