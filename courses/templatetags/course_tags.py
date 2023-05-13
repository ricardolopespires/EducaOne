from dateutil.relativedelta import *
from datetime import datetime, timedelta
from django import template
import math
register = template.Library()

'''
@register.simple_tag
def discount_calculation(price,discount):
    if discount is None or discount is 0:
        return price    
    sellprice = price - (price * discount/100)
    return math.floor(sellprice)
	
	

'''
@register.simple_tag
def discount_calculation(price,discount):    
    if discount is None or discount is 0:
        return int(price)
    else:  
        porcetagem = 100
        calculo = porcetagem / discount
        resultado = price * calculo
        return int(resultado)    



@register.simple_tag
def review_calculation(valor):    
    if valor is None or valor is 0:
        return 0
    else:       
        resultado = 100/ valor            
        return int(resultado)    



@register.simple_tag
def date_calculation(inicio, fim):

    data_inicial = str(inicio)[:10] 
    data_final = str(fim)[:10]    

    f = "%Y-%m-%d"
    inicio = datetime.strptime(data_inicial, f)
    fim = datetime.strptime(data_final, f)
    di = abs(relativedelta(inicio, fim))
    
    print(di.months)
    return di.days





@register.filter
def duration(td):
    if td == None:
        td = timedelta()
        return td
    else:
        segundos = int(td.total_seconds())
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        return '{}h {}min '.format(horas, minutos, segundos)





@register.simple_tag
def percent(atual, novo):    
    if novo is None or novo is 0:
        return int(atual)
    else:        
        return int((novo / atual)*100)    
