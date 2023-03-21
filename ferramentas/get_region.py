def consulta_regiao(estado):

    if estado in ["AC", "AM", "AP", "PA", "RO", "RR", "TO"]:
        regiao = "North"
    elif estado in ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]:
        regiao = "Northeast"
    elif estado in ["DF", "GO", "MT", "MS"]:
        regiao = "Central-West"
    elif estado in ["ES", "MG", "RJ", "SP"]:
        regiao = "Southeast"
    elif estado in ["PR", "RS", "SC"]:
        regiao = "South"

    return regiao