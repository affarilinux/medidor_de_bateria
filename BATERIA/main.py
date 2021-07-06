#comentario #'''
#python3 xxxx.py

####################################################################
### bibliotecas do sistema
import  sys
import  time
import psutil 

from PyQt5.QtWidgets     import (QApplication, QMainWindow, QPushButton,  QLabel )
from PyQt5.QtCore        import QTimer, pyqtSlot, QObject, pyqtSignal

#######################################################################
### arquivos do sistema

from medidor_bateria     import med

from tamanho_janela      import largura, altura

from informacao_bateria  import informacao_carregamento

#from memoria_ram         import cal

######################################################################3###########

from main_variavel_fixa  import Label_fixo # janela principal variaveis fixas label
from main_botao  import Botao_janela # janela principal variaveis fixas label

###############################################
# inicio janela

class Window  (Label_fixo, Botao_janela, QMainWindow):

     def __init__          (self):

          super ().__init__()  #metodo construtor

          self.title  = "MEDIDOR DE BATERIA"           #titulo

          self.top    = 1500                           #topo - esquerda para direita
          self.left   = 200                            #esquerda-cima para baixo

          self.width  = largura                            #largura
          self.height = altura                           #altura

          self.cor_fundo = 'background-color: #A9A9A9' #cor DarkGray

          self.jan_fixo_larg = largura                     #largura
          self.jan_fixo_alt  = altura                   #altura

          
          

          ######################################################################
          #@@@@@@@@@@@@@@@@@@ chamar função

          self.InitWindow        ()

###############################################################################
######## execução de janela

     def InitWindow               (self):

          self.setWindowTitle      (self.title)                             # titulo

          self.setGeometry         (self.top, self.left, 
                                            self.width, self.height)             # informações da janela
          self.setFixedSize        (self.jan_fixo_larg, self.jan_fixo_alt)  # tamanho fixo da janela

          self.setStyleSheet       ( self.cor_fundo)                        #cor de fundo

          ##################################################################################
          #@@@@@@@@função sistema

          
          self.Label_Funcao_Janela      () 
          

          
          
          self.Uso_Sistema_bateria      ()     # estado da bateria e uso da bateria
          #self.Sistema_Ram_Por_centagem ()     # quantidade de uso do sistema ram

          self.Memoria_Ram              ()

          


          self.show                     ()

     def inwi (self):
          #import time

#from main import loop_while, tp


# (####main.py####)

# - janela principal

# puxa os dado do sistema operacional

          self.informacao = psutil.virtual_memory()

# puxa as iformações e adiciona nas variaveis
          self.total  = self.informacao.total
          self.usada  = self.informacao.active

          self.calculo_por_centagem = (self.usada * 100) / self.total
          self.cal = round(self.calculo_por_centagem, 2)


          self.resultado = self.cal

     ###########################################################################################
     ###########################################################################################
     # uso de bateria

     ######################################################################################
     # controle de processos de tempo de uso de bateria
     #sistema central

     def Uso_Sistema_bateria          (self):

          self.dados_estado     =  informacao_carregamento

          if self.dados_estado  == True :

               self.Estado_True_Carregamento  ()

               self.Tempo_Bateria             ()
               

          elif self.dados_estado == False :

               self.Estado_False_Carregamento ()

               self.Tempo_Bateria             ()
               
     

     
          ############################
          #################################################################################################
          ####### estado de bateria

     def Estado_True_Carregamento  (self):

          self.Estado_Bateria_Atual       ()

          self.label_tempo_carga.setText  (" CARREGANDO" )

     #######################################################

     def Estado_False_Carregamento (self):

          self. Estado_Bateria_Atual      ()

          self.label_tempo_carga.setText  (" DESCARREGANDO" )


          ###############################################
          ##############################################################################################
          ####### função variaveis

          ###########################################################################################
          # estado bateria

          '''#############tempo de bateria############'''

     def Tempo_Bateria                    (self):

          #label variavel
          self.label_tempo_carga  = QLabel     (self)

          self.label_tempo_carga.setText       (" 01H 20M 30s " )

          self.label_tempo_carga.setStyleSheet ('QLabel { font: bold; font-size:15px; background-color: #F5DEB3 }') # cor: Wheat

          self.label_tempo_carga.move          (100,5)                   #x,y externo
          self.label_tempo_carga.resize        (140,30)                  #x,y interno

          
     def Estado_Bateria_Atual           (self):
          #label variavel
          self.label_tempo_carga  = QLabel     (self)

          self.label_tempo_carga.setStyleSheet ('QLabel { font: bold; font-size:15px; background-color: #F5DEB3 }') # cor: Wheat

          self.label_tempo_carga.move          (100,40)                   #x,y externo
          self.label_tempo_carga.resize        (140,30)                   #x,y interno

               

     ####################################################################################################
     ####################################################################################################
     ######### sistema ram

     ##########################################
     ############################################################################
     ### sistema de controle principal

     

     ############################################################################
     #memoria ram

     def Memoria_Ram                 (self):
          
          self.label_nome_ram  = QLabel     (self)

          self.label_nome_ram.setStyleSheet ('QLabel { font: bold; font-size:25px; background-color: #00BFFF}') # cor: Wheat

          self.label_nome_ram.move          (260,95)                    #x,y externo
          self.label_nome_ram.resize        (70,25)                     #x,y interno

                    
          self.timer = QTimer(self)
          self.timer.setInterval(5000)
          self.timer.timeout.connect(self.Sistema_Ram_Por_centagem)
          self.timer.start()

     def Sistema_Ram_Por_centagem(self):
          #print("certo")
          
          self.inwi()
          
          self.resultado_ram = str (self.resultado)
          self.label_nome_ram.setText        (self.resultado_ram )

          

     ###################################################################################
     #@@@@@@@@@@@@@@@@@@@@@@@funções do sistema

     def Label_Funcao_Janela             (self):

          
          at = med
          self.medida = str(at)

          #label variavel
          self.label_num_var  = QLabel          (self)

          self.label_num_var.setText            (self.medida )

          self.label_num_var.setStyleSheet      ('QLabel { font: bold; font-size:35px; background-color: #00FF00}') #cor Line


          self.label_num_var.move               (260,30)         #x,y externo
          self.label_num_var.resize             (65,35)          #x,y interno


          
          
    


########################################################################################
############################

def main               ():
          
     App = QApplication (sys.argv)
     window = Window    ()

     sys.exit           (App.exec_ ( ))

if __name__ == "__main__":

     main()
