from dateutil import relativedelta 
from calendar import monthrange
from datetime import datetime
from datetime import date





def calculo_entre_datas():

    #Pegando data de hoje
    data_atual = date.today()
    
    data_inicial = str(date.today())+" 23:59:59"
    if data_atual.day + 1 < 10 and data_atual.month < 10:
        datas = '0{}-0{}-{} 00:00:00'.format(data_atual.year, data_atual.month, data_atual.day)

    elif data_atual.day + 1 > 9 and data_atual.month < 10:
        datas = '{}-0{}-{} 00:00:00'.format(data_atual.year, data_atual.month, data_atual.day)

    elif data_atual.day + 1 > 9 and data_atual.month > 10:
        datas = '{}-{}-{} 00:00:00'.format(data_atual.year, data_atual.month, data_atual.day)

    data_final = str(datetime.strptime(datas, "%Y-%m-%d %H:%M:%S"))
    f = "%Y-%m-%d %H:%M:%S"
    inicio = datetime.strptime(data_inicial, f)
    fim = datetime.strptime(data_final, f)
    di = abs(relativedelta(inicio, fim))
    return di
