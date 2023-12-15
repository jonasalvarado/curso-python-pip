import csv

def leer(path):
  with open(path, 'r') as f:
    reader = csv.reader(f,delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      # obtener los encabeados de la primera fila
      iterable = zip(header, row)
     # print(list(iterable))
      # crear un iterable para convertir lo leido a diccionario
      country_dict = {key:value for key,value in iterable}
    # adicionar el diccionario a el retorno de la funcion
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
 