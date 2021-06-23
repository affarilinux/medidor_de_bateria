#comentario #'''
#python3 xxxx.py
import  sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,  QLabel,
							 )




class Window (QMainWindow):

	def __init__ (self):

		super().__init__()  #metodo construtor

		self.title  = "SISTEMA DO COMPUTADOR"      #titulo
		self.top    = 700        #topo - esquerda para direita
		self.left   = 300        #esquerda-cima para baixo
		self.width  = 530        #largura
		self.height = 500        #altura
		self.cor_fundo = 'background-color: #A9A9A9' #cor DarkGray

		
		#################################################################################
									###############senha

		#label
		self.label_ins_senha  = QLabel     (self)
		self.label_ins_senha.setText       ("SENHA:")
		self.label_ins_senha.move          (60,120)                   #x,y
		self.label_ins_senha.setStyleSheet ('QLabel { font: bold; font-size:15px}')
		self.label_ins_senha.resize        (70,20)

		
		#botao
		self.entrar_sist = QPushButton   (self)
		self.entrar_sist.setText         ("ENTRAR")
		self.entrar_sist.move            (60,270)
		self.entrar_sist.resize          (150,40)
		self.entrar_sist.setStyleSheet   ('QPushButton { font: bold; font-size: 30px}')
		self.entrar_sist.clicked.connect (self.entrar_sist_click)

		############################################################################
		##################esqueceu senha.

		
		######################################################################
		#@@@@@@@@@@@@@@@@@@ chamar função

		self.InitWindow    ()
		

	def InitWindow(self):
		self.setWindowTitle (self.title)
		self.setGeometry    (self.top, self.left, 
							self.width, self.height)
		self.setStyleSheet  ( self.cor_fundo)
		self.show  ()

	###################################################################################
	#222222222222222222222222222222 botoes

	#entrar no sistema
	def entrar_sist_click (self):
		self.label_ins_senha.setText ("concluido")
		

		

			

App = QApplication (sys.argv)
window = Window    ()
sys.exit           (App.exec_ ( ))
