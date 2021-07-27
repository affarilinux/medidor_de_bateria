##################################################
### bibliotecas do sistema de python

import  sys
import psutil
import sqlite3

    ##############################################

from PyQt5.QtWidgets  import ( QApplication, QMainWindow, QLabel )
from PyQt5.QtCore        import QTimer

##################################################
# arquivo.py

# SISTEMA INTERNO
from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
    INTERNO_VERTICAL_1X
)
# SISTEMA INTERNO
from JANELA.JANELA_PRINCIPAL.CONFIGURACOES_PRIMARIA.dimensionamento import (
    VERTICAL_CENTER_1X , HORIZONTAL_2Y 
)

##################################################
# banco de dados
from config_multi_janelas  import BANCO_INTERNO_SQLITE3



class janela1NivelFrequenciaProcessador( QMainWindow ):

    def __init__( self ):
        

        super ().__init__()    # metodo construtor

        self.LABEL_nivel_processador_center  = QLabel ( self )

        # cor: Yellow1
        self.LABEL_nivel_processador_center.setStyleSheet ( 
            'QLabel { font: bold; font-size:30px; background-color: #FFFF00 }' 
        ) 

        # x,y externo
        self.LABEL_nivel_processador_center.move      ( 220, 
            INTERNO_VERTICAL_1X 
        )   
        # x,y interno     
        self.LABEL_nivel_processador_center.resize    ( VERTICAL_CENTER_1X,  
            HORIZONTAL_2Y
        )     


        self.processador_conexao = sqlite3.connect ( BANCO_INTERNO_SQLITE3 )
        self.cursor              = self.processador_conexao.cursor()

        self.cursor.execute (
            '''CREATE TABLE if not exists MONTANTE_PROCESSADOR( id integer primary key,
                                                 QUANTIDADE REAL                                      
                                                )'''
        )
        ##########################################
        # primeira chamada de apresentação label

        self. Print_Informacoes_Loop ()

        ##########################################
        #loop

        self.TIMER_loop_processador = QTimer        ( self )

        self.TIMER_loop_processador.setInterval     ( 1000 )
        self.TIMER_loop_processador.start           ()

        #chamada de funçãO
        self.TIMER_loop_processador.timeout.connect ( 
            self.Print_Informacoes_Loop 
        ) 


    def Psutil_Chamada ( self ):

        # chama os dados para a janela
        self.informacao_sistema_1 = psutil.cpu_freq ()

        # puxa as informações e adiciona nas variaveis
        self.maximo_processador   = self.informacao_sistema_1.max
        self.dados_presente       = self.informacao_sistema_1.current

         # calcula porcentagm
        self.calculo_processos_dados     = ( self.dados_presente * 100 ) / self.maximo_processador

        # filtra o float
        self.filtra_calculo_sistema = round ( self.calculo_processos_dados, 2 )

        ##########################################
        # banco de dados

        

    ##############################################
    #apresentação label do sistema

    def Print_Informacoes_Loop ( self ):

        self.Psutil_Chamada ()
        

        # transforma em string a informação float
        self.string_para_print = str ( self.filtra_calculo_sistema) 
        # apresentação
        self.LABEL_nivel_processador_center.setText( self.string_para_print )
        self.banco()

    
    def banco(self):

        self.cursor.execute( 'INSERT INTO MONTANTE_PROCESSADOR(QUANTIDADE) VALUES(?)', (self.string_para_print,))

        self.processador_conexao.commit()
        #cursor.close()
        #processador_conexao.close()