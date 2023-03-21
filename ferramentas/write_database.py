with open('/mnt/c/Users/jorda/Documents/fabio_ultimo_periodo/pyweb_codigo/bases/registros_usuarios.csv', mode='r') as arquivo:
    lines = arquivo.readlines()

def write_line(line):
    
    line = line[0] + ';' + line[1] + ';' + line[2] + ';' + line[3] + ';' + line[4] + ';' + line[5] + ';' + line[6] + ';' + line[7] + '\n'
    
    lines.append(line)
    
    with open('/mnt/c/Users/jorda/Documents/fabio_ultimo_periodo/pyweb_codigo/bases/registros_usuarios.csv', mode='w') as arquivo:
        arquivo.writelines(lines)


#[region, state, temp, weather, station, partOfDay, weekday, search]