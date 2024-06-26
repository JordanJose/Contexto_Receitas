from datetime import datetime

def get_partDay(hora_atual):
    if hora_atual >= 5 and hora_atual < 12:
        return "Morning"
    elif hora_atual >= 12 and hora_atual < 18:
        return "Afternoon"
    elif hora_atual >= 18 and hora_atual < 23:
        return "Evening"
    else:
        return "Midnight"

    
def get_station(data_atual):
    ano_atual = data_atual.year
    equinocio_de_primavera = datetime(ano_atual, 9, 23)
    solsticio_de_verao = datetime(ano_atual, 12, 22)
    equinocio_de_outono = datetime(ano_atual, 3, 20)
    solsticio_de_inverno = datetime(ano_atual, 6, 21)

    if data_atual >= equinocio_de_primavera and data_atual < solsticio_de_verao:
        return "Spring"
    elif data_atual >= solsticio_de_verao and data_atual < equinocio_de_outono:
        return "Summer"
    elif data_atual >= equinocio_de_outono and data_atual < solsticio_de_inverno:
        return "Fall"
    else:
        return "Winter"