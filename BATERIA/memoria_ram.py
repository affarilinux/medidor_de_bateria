import psutil 

# (####main.py####)

# - janela principal

# puxa os dado do sistema operacional

informacao = psutil.virtual_memory()

# puxa as iformações e adiciona nas variaveis
total  = informacao.total
usada  = informacao.active

# calculo % de memoria ram usada
calculo_por_centagem = (usada * 100) / total

# transforma os decimais em apenas 2
cal = round(calculo_por_centagem, 2)



