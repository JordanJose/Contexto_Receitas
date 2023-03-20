

def consulta_regiao(estado):

    if estado in ["AC", "AM", "AP", "PA", "RO", "RR", "TO"]:
        regiao = "norte"
    elif estado in ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]:
        regiao = "nordeste"
    elif estado in ["DF", "GO", "MT", "MS"]:
        regiao = "centro-oeste"
    elif estado in ["ES", "MG", "RJ", "SP"]:
        regiao = "sudeste"
    elif estado in ["PR", "RS", "SC"]:
        regiao = "sul"

    return regiao