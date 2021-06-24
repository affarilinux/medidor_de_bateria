#comentario #'''
#python3 xxxx.py

import  sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,  QLabel )

class Window             (QMainWindow):

	def __init__         (self):

		super ().__init__()  #metodo construtor

		self.title  = "MEDIDOR DE BATERIA"           #titulo
		self.top    = 1500                           #topo - esquerda para direita
		self.left   = 200                            #esquerda-cima para baixo
		self.width  = 260                            #largura
		self.height = 70                             #altura
		self.cor_fundo = 'background-color: #A9A9A9' #cor DarkGray
		self.jan_fixo_larg = 260
		self.jan_fixo_alt  = 70

		
		#################################################################################
									###############senha
		cv = 25
		
		#label
		self.label_porcentagem  = QLabel     (self)

		self.label_porcentagem.setText       ("100 %")

		self.label_porcentagem.setStyleSheet ('QLabel { font: bold; font-size:50px}')

		self.label_porcentagem.move          (70,10)                   #x,y externo
		self.label_porcentagem.resize        (150,40)                  #x,y interno

		
		

		############################################################################
		##################esqueceu senha.

		
		######################################################################
		#@@@@@@@@@@@@@@@@@@ chamar função

		self.InitWindow    ()
		

	def InitWindow(self):
		self.setWindowTitle (self.title)
		self.setGeometry    (self.top, self.left, 
							self.width, self.height)
		self.setFixedSize   (self.jan_fixo_larg, self.jan_fixo_alt)
		self.setStyleSheet  ( self.cor_fundo)
		self.show  ()

	###################################################################################
	#222222222222222222222222222222 botoes

	#entrar no sistema
	def entrar_sist_click (self):
		self.label_ins_senha.setText ("concluido")

########################################################################################
############################

def main               ():
		
	App = QApplication (sys.argv)
	window = Window    ()
	sys.exit           (App.exec_ ( ))

if __name__ == "__main__":

	main()
