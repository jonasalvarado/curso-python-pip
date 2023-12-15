import utils
import read_csv
import chart

def run():
    data = read_csv.leer('data.csv')
    # obtener solo sur america para una mejor lectura de los datos
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    # llamar el metodo deseado
    world_population(data)

    by_country(data)

def world_population(data):
    #percentage_world_dict = { item["Country/Territory"] : float(item["World Population Percentage"]) for item in data }
    #keys = percentage_world_dict.keys()
    #values = percentage_world_dict.values()
    labels = list(map(lambda x: x['Country/Territory'], data))
    values = list(map(lambda x: float(x['World Population Percentage']), data))
    chart.generate_pie_chart(labels,values)

def by_country(data):
    country = input("Ingrese el nombre del país que desea ver la información (VEN/USA/COL/BOL/ARG): ")
    result = utils.population_by_country(data,country)

    if len(result) > 0:
        country = result[0]
        keys, values = utils.get_population(country)
        chart.generate_bar_chart(country['Country/Territory'],keys,values)
if __name__ == '__main__':
    run()