#comentario #'''
#python3 xxxx.py

import  sys

from PyQt5.QtWidgets     import (QApplication, QMainWindow, QPushButton,  QLabel )

from medidor_bateria     import med

from tamanho_janela      import largura, altura

from informacao_bateria  import informacao_carregamento

###############################################
# inicio janela

class Window             (QMainWindow):

	def __init__         (self):

		super ().__init__()  #metodo construtor

		self.title  = "MEDIDOR DE BATERIA"           #titulo

		self.top    = 1500                           #topo - esquerda para direita
		self.left   = 200                            #esquerda-cima para baixo
		self.width  = largura                            #largura
		self.height = altura                           #altura

		self.cor_fundo = 'background-color: #A9A9A9' #cor DarkGray

		self.jan_fixo_larg = largura                     #largura
		self.jan_fixo_alt  = altura				 #altura

		######################################################################
		#@@@@@@@@@@@@@@@@@@ chamar função

		self.InitWindow        ()
		

	def InitWindow               (self):

		self.setWindowTitle      (self.title)                             # titulo

		self.setGeometry         (self.top, self.left, 
							         self.width, self.height)             # informações da janela
		self.setFixedSize        (self.jan_fixo_larg, self.jan_fixo_alt)  # tamanho fixo da janela


		self.setStyleSheet       ( self.cor_fundo)                        #cor de fundo

		##################################################################################
		#@@@@@@@@função sistema

		self.Label_Funcao_Janela () 
		self.Botao_janela        () 
		
		self.Memoria_ram         ()


		self.Uso_Sistema_bateria ()     # estado da bateria e uso da bateria

		self.show                ()

	###########################################################################################
	###########################################################################################
	# uso de bateria

	######################################################################################
	# controle de processos de tempo de uso de bateria

	def Uso_Sistema_bateria (self):

		self.dados_estado = informacao_carregamento

		if self.dados_estado == True :

			self.Estado_True_Carregamento()

			self.Tempo_Bateria()
			self.Variaveis_Fixa_Uso_bateria()

		elif self.dados_estado == False :

			self.Estado_False_Carregamento()

			self.Tempo_Bateria()
			self.Variaveis_Fixa_Uso_bateria()

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

		#############################################
		###############################################################################################
		######### fução fixa

	def Variaveis_Fixa_Uso_bateria     (self):

		#label fixa
		self.label_inf_bateria  = QLabel     (self)

		self.label_inf_bateria.setText       (" TEMPO:" )
		self.label_inf_bateria.setStyleSheet ('QLabel { font: bold; font-size:15px; background-color: #F5DEB3}') # cor: Wheat

		self.label_inf_bateria.move          (10,5)                    #x,y externo
		self.label_inf_bateria.resize        (80,30)                   #x,y interno

		#label fixa
		self.label_tempo_carga  = QLabel     (self)

		self.label_tempo_carga.setText       (" ESTADO:" )

		self.label_tempo_carga.setStyleSheet ('QLabel { font: bold; font-size:15px; background-color: #F5DEB3 }') # cor: Wheat

		self.label_tempo_carga.move          (10,40)                   #x,y externo
		self.label_tempo_carga.resize        (80,30)                   #x,y interno

	###################################################################################
	#@@@@@@@@@@@@@@@@@@@@@@@funções do sistema

	def Label_Funcao_Janela             (self):

		#label fixa
		self.label_porcentagem  = QLabel     (self)

		self.label_porcentagem.setText       (" BATERIA:" )

		self.label_porcentagem.setStyleSheet ('QLabel { font: bold; font-size:15px; background-color: #00FF00}') #cor Line

		self.label_porcentagem.move          (260,5)          #x,y externo
		self.label_porcentagem.resize        (105,20)         #x,y interno

		#label fixa
		self.label_porcentagem  = QLabel     (self)

		self.label_porcentagem.setText       ("%" )

		self.label_porcentagem.setStyleSheet ('QLabel { font: bold; font-size:35px; background-color: #00FF00}') #cor Line

		self.label_porcentagem.move          (330,30)          #x,y externo
		self.label_porcentagem.resize        (35,35)           #x,y interno

		#fat = janela()

		at = med
		self.medida = str(at)

		#label variavel
		self.label_num_var  = QLabel          (self)

		self.label_num_var.setText            (self.medida )

		self.label_num_var.setStyleSheet      ('QLabel { font: bold; font-size:35px; background-color: #00FF00}') #cor Line


		self.label_num_var.move               (260,30)         #x,y externo
		self.label_num_var.resize             (65,35)          #x,y interno


		
	###################################################################################
	#janela secundaria

	def Botao_janela              (self):

		self.botao_jan  = QPushButton  (self)

		self.botao_jan.setText         ("ENTRAR" )

		self.botao_jan.setStyleSheet   ('QPushButton { font: bold; font-size:25px; background-color: #98FB98}') # cor: PaleGreen

		self.botao_jan.move            (10,80)                       #x,y externo
		self.botao_jan.resize          (230,40)                      #x,y interno

		self.botao_jan.clicked.connect (self.Entrar_Janela_Sistema)


	def Entrar_Janela_Sistema          (self):
		print("ola")

	############################################################################
	#memoria ram

	def Memoria_ram                 (self):

		#label fixa
		self.label_nome_ram  = QLabel     (self)

		self.label_nome_ram.setText       (" RAM:" )
		self.label_nome_ram.setStyleSheet ('QLabel { font: bold; font-size:15px; background-color: #00BFFF}') # cor: Wheat

		self.label_nome_ram.move          (265,70)                    #x,y externo
		self.label_nome_ram.resize        (80,20)                     #x,y interno

		#label fixa
		self.label_nome_ram  = QLabel     (self)

		self.label_nome_ram.setText       ("%" )
		self.label_nome_ram.setStyleSheet ('QLabel { font: bold; font-size:25px; background-color: #00BFFF}') # cor: Wheat

		self.label_nome_ram.move          (315,95)                    #x,y externo
		self.label_nome_ram.resize        (30,25)                     #x,y interno

		#label variavel
		self.label_nome_ram  = QLabel     (self)

		self.label_nome_ram.setText       ("100" )
		self.label_nome_ram.setStyleSheet ('QLabel { font: bold; font-size:25px; background-color: #00BFFF}') # cor: Wheat

		self.label_nome_ram.move          (260,95)                    #x,y externo
		self.label_nome_ram.resize        (50,25)                     #x,y interno



	###################################################################################
	#222222222222222222222222222222 botoes

	'''#entrar no sistema
	def entrar_sist_click (self):
		se = 100
		
		self.sek = str(se)
		
		self.label_porcentagem.setText (self.sek )'''

########################################################################################
############################

def main               ():
		
	App = QApplication (sys.argv)
	window = Window    ()
	sys.exit           (App.exec_ ( ))

if __name__ == "__main__":

	main()
