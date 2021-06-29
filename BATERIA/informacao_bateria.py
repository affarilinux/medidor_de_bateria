
import psutil 

# (####main.py####)

# - janela principal
# informações:


# puxa os dado do sistema operacional

informacao_bateria = psutil.sensors_battery()

#pula uma informação se esta plugado na internet

#def Uso_Sistema_bateria          (self):

informacao_carregamento = informacao_bateria.power_plugged

