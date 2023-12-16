import utils
import read_csv
import chart
import pandas as pd

def run():
    # 
    # obtener solo sur america para una mejor lectura de los datos
    # data = list(filter(lambda item: item['Continent'] == 'South America', data))
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'South America']
    print(df)
    # llamar el metodo deseado

    data = read_csv.leer('data.csv')
    world_population(data)

    by_country(df)

def world_population(data):
    #percentage_world_dict = { item["Country/Territory"] : float(item["World Population Percentage"]) for item in data }
    #keys = percentage_world_dict.keys()
    #values = percentage_world_dict.values()
    labels = list(map(lambda x: x['Country/Territory'], data))
    values = list(map(lambda x: float(x['World Population Percentage']), data))
    chart.generate_pie_chart(labels,values)

def by_country(df):
    country = input("Ingrese el nombre del país: ")
    result = df[df['Country/Territory'] == country]
    #result = utils.population_by_country(df,country)
    print(result)
    if len(result) > 0:
        country = result
        keys, values = utils.get_population(country)
        chart.generate_bar_chart(country['Country/Territory'].values,keys,values)
if __name__ == '__main__':
    run()