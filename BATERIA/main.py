#comentario # '''
#python3 xxxx.py

####################################################################
### bibliotecas do sistema de python

import  sys

     ###################################################################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow )

#######################################################################
### arquivos.py do sistema

from tamanho_janela      import largura, altura

######################################################################3###########
### arquivos.py da janela

from main_variavel_fixa    import Label_fixo            ## variaveis fixas

from main_botao            import Botao_janela          ## botao da janela

from main_tempo            import Temporizador_carga    ## relogio de tempo de carga

from main_estado_bateria   import Estado_carga_bateria  ## carregando ou descarregando True/False

from main_calculo_ram      import Calculo_ram           ## calculo de porcentagem ram

from main_nivel_bateria    import Nivel_bateria         ## nivel de carga da bateria



#######################################################################################################
# inicio janela

class Window  ( Label_fixo, Botao_janela, Temporizador_carga, Estado_carga_bateria, Calculo_ram, 
               Nivel_bateria, QMainWindow ):

     def __init__          (self):

          super ().__init__()  #metodo construtor

          self.title  = "MEDIDOR DE BATERIA"            #titulo

          self.top    = 1500                            #topo - esquerda para direita
          self.left   = 200                             #esquerda-cima para baixo

          self.width  = largura                         #largura
          self.height = altura                          #altura

          self.cor_fundo = 'background-color: #A9A9A9'  #cor DarkGray

          self.jan_fixo_larg = largura                  #largura
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
         
          self.show                     ()


########################################################################################
############################ execução interna janela

def main               ():
          
     App = QApplication (sys.argv)
     window = Window    ()

     sys.exit           (App.exec_ ( ))

if __name__ == "__main__":

     main()
