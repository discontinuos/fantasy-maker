import csv

# Define la función para crear el ID
def crear_id_fantasia(cueanexo):
    # 1. Separa en dos partes
    if len(cueanexo) < 9:
        raise ValueError("Todos los cueanexo deben tener nueve dígitos");
    part1, part2 = cueanexo[:5], cueanexo[4:9]
    base = int(cueanexo[5:7])
    # 2. Multiplicador e inversión
    if base > 10 or int(cueanexo) >= 500010000:
        val_part2_trans = int(part1) * (base + 4)
        val_part1_trans = int(part2) * (base + 4)
    else:
        val_part1_trans = int(part1) * (base + 1)
        val_part2_trans = int(part2) * (base + 1)
    # 3. Une ambas partes
    result = f"{val_part1_trans}{val_part2_trans}"
    # 4. Replica para llegar a la longitud buscada. 
    # Para garantizar 15 dígitos lo hace tres veces, 
    # porque algunos cueanexo pueden producir resultados de 7 dígitos. 
    ret = result + result + result
    # 5. Devuelve los primeros quince dígitos
    return ret[:15]

def procesar_archivo(archivo_entrada, archivo_salida):
  # Lee el archivo CSV y crea el archivo de salida
  archivo_salida_win = archivo_salida.replace('.', '-excel.')
  with open(archivo_entrada, 'r', encoding='utf-8') as entrada, open(archivo_salida, 'w', encoding='utf-8', newline='') as salida, open(archivo_salida_win, 'w', encoding='windows-1252', newline='') as salida_windows:
    # Crea los objetos de lectura y escritura CSV
    lector_csv = csv.reader(entrada)
    escritor_csv = csv.writer(salida, quoting=csv.QUOTE_NONNUMERIC)
    escritor_csv_win = csv.writer(salida_windows, quoting=csv.QUOTE_NONNUMERIC)
    # Lee el encabezado
    encabezado = next(lector_csv)
    # soporte a archivos con BOM al inicio
    encabezado[0] = encabezado[0].lstrip('\ufeff')
    # Añade la columna 'id' al encabezado
    encabezado.append('id')
    # Encuentra la posición de la columna 'cueanexo' en el encabezado
    indice_cueanexo = encabezado.index('cueanexo')
    # Escribe el encabezado en el archivo de salida
    escritor_csv.writerow(encabezado)
    escritor_csv_win.writerow(encabezado)
    # Procesa cada fila del archivo de entrada
    for fila in lector_csv:
        # Obtiene el valor de 'cueanexo'
        cueanexo = fila[indice_cueanexo]
        # Aplica la función crear_id
        id_generado = crear_id_fantasia(cueanexo)
        # Añade el valor de 'cueanexo' y el ID generado a la fila
        fila.append(id_generado)
        # Escribe la fila en el archivo de salida
        escritor_csv.writerow(fila)
        fila_cp1252 = [str(elemento).encode('cp1252', errors='ignore').decode('cp1252') for elemento in fila]
        escritor_csv_win.writerow(fila_cp1252)
  print(f"Se ha creado el archivo {archivo_salida} con éxito.")

procesar_archivo("cue-2014.csv", "cue-2014-salida.csv")
procesar_archivo("cue-2017.csv", "cue-2017-salida.csv")
procesar_archivo("cue-2021.csv", "cue-2021-salida.csv")
