## variaveis label janela  principal temporizador main.py

##########################################################################
## bibliotecas do sistema de python

import  sys

import psutil

    ########################################################################

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )

from PyQt5.QtCore        import QTimer


class Nivel_bateria       (QMainWindow):

    def __init__          ( self ):

        super ().__init__ ()  #metodo construtor

        ####################################################
        #label

        self.label_num_var  = QLabel          ( self       )

        self.label_num_var.setStyleSheet      ( ' QLabel { font: bold; font-size:30px; background-color: #00FF00} ' ) #cor Line

        self.label_num_var.move               ( 260,30 )         #x,y externo
        self.label_num_var.resize             ( 65,35  )         #x,y interno

        ##################################################
        # primeira chamada de apresentação label

        self.Sistema_Bateria()

        ################################################
        #loop

        self.L_bat = QTimer        ( self )

        self.L_bat.setInterval     ( 5000 )
        self.L_bat.start           ()

        self.L_bat.timeout.connect ( self.Sistema_Bateria ) #chamada de função

    #função chamada interna do sistema operacional

    def Loop_Timer_Bateria(self):

        #chama os dados para a janela
        self.Bateria_sis   = psutil.sensors_battery()

        #chama o tipo de informação
        self.Nivel_bat     = self.Bateria_sis.percent

        # transforma em int
        self.ent_Nivel_int = int(self.Nivel_bat)

    # chamada do loop
    def Sistema_Bateria ( self ):

        self.Loop_Timer_Bateria()

        #string
        self.medida = str(self.ent_Nivel_int)
        self.label_num_var.setText            ( self.medida )