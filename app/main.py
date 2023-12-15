import utils
import read_csv
import chart

def run():
    data = read_csv.leer('./data.csv')
    world_population(data)
def world_population(data):
    #percentage_world_dict = { item["Country/Territory"] : float(item["World Population Percentage"]) for item in data }
    #keys = percentage_world_dict.keys()
    #values = percentage_world_dict.values()
    keys = list(map(lambda x: x['Country'], data))
    values = list(map(lambda x: x['World Population Percentage'], data))
    chart.generate_bar_chart(keys,values)
def by_country(data):
    country = input("Ingrese el nombre del país que desea ver la información (VEN/USA/COL/BOL/ARG): ")
    result = utils.population_by_country(data,country)
    if len(result) > 0:
        country = result[0]
        keys, values = utils.get_population(country)
        chart.generate_pie_chart(keys,values)
        chart.generate_bar_chart(keys,values)
if __name__ == '__main__':
    run()