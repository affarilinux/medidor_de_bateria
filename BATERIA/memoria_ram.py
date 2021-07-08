from main_loop   import 


total  = informacao.total
usada  = informacao.active

# calculo % de memoria ram usada
calculo_por_centagem = (usada * 100) / total

# transforma os decimais em apenas 2
cal = round(calculo_por_centagem, 2)



