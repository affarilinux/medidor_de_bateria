## variaveis labels fixas da janelas principal main.py

import  sys

from PyQt5.QtWidgets     import ( QApplication, QMainWindow, QLabel )


class Label_fixo(QMainWindow):

     def __init__            (self):

          super ().__init__  ()  #metodo construtor

          ###################################################################
          ##### tempo bateria

          #label fixa
          self.label_inf_bateria  = QLabel     (self)

          self.label_inf_bateria.setText       (" TEMPO:" )

          self.label_inf_bateria.setStyleSheet ('QLabel { font: bold; font-size:15px; background-color: #F5DEB3}') # cor: Wheat

          self.label_inf_bateria.move          (10,5)                    #x,y externo
          self.label_inf_bateria.resize        (80,30)                   #x,y interno

          ###################################################################
          ##### estado bateria

          #label fixa
          self.label_tempo_carga  = QLabel     (self)

          self.label_tempo_carga.setText       (" ESTADO:" )

          self.label_tempo_carga.setStyleSheet ('QLabel { font: bold; font-size:15px; background-color: #F5DEB3 }') # cor: Wheat

          self.label_tempo_carga.move          (10,40)                   #x,y externo
          self.label_tempo_carga.resize        (80,30)                   #x,y interno

          ###################################################################
          ##### memoria ram

          #label fixa
          self.label_nome_ram  = QLabel        (self)

          self.label_nome_ram.setText          (" RAM:" )

          self.label_nome_ram.setStyleSheet    ('QLabel { font: bold; font-size:15px; background-color: #00BFFF}') # cor: Wheat

          self.label_nome_ram.move             (260,70)                    #x,y externo
          self.label_nome_ram.resize           (105,20)                     #x,y interno

          #label fixa
          self.label_nome_ram  = QLabel        (self)

          self.label_nome_ram.setText          ("%" )

          self.label_nome_ram.setStyleSheet    ('QLabel { font: bold; font-size:25px; background-color: #00BFFF}') # cor: Wheat

          self.label_nome_ram.move             (335,95)                    #x,y externo
          self.label_nome_ram.resize           (30,25)                     #x,y interno

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