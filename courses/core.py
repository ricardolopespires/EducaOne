from datetime import datetime, date, timedelta
from pymediainfo import MediaInfo
import os







#soma o total de minutos
def minutos(atual, novo):
    # transforma a string em data

    if atual == None:
        data_inicio = datetime.strptime('00:00:00', "%H:%M:%S")
    else:
        data_inicio = datetime.strptime(str(atual), "%H:%M:%S")

    horas, minutos, segundos = map(int, str(novo)[:7].split(':'))

    # transforma a string em timedelta
    duracao = timedelta(hours=horas, minutes=minutos, seconds=segundos)

    # soma a data à duração
    termino = data_inicio + duracao

    minutos = termino.strftime('%H:%M:%S')    

    # formata o resultado
    return timedelta(hours=int(minutos[:2]), minutes=int((minutos[-5::1])[:2]), seconds=int(minutos[:2]))





def upload_file(file):
    arquivo = "D:/Desenvolvimento/EducaOne/media/video/"+str(file)    
    media_info = MediaInfo.parse(arquivo)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            duration = ("{} duration {}".format(track.track_type,track.to_data()["other_duration"][3][0:8]))[-8:]
            return duration


