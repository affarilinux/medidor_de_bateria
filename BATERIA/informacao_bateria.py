
import psutil 

# (####main.py####)

# - janela principal
# informações:

''' - tamanho da janela '''

informacao_bateria = psutil.sensors_battery()

informacao_carregamento = informacao_bateria.power_plugged

