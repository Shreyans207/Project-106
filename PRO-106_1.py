import numpy as np
import csv
import random
import plotly.express as px 

color_graph = random.randint(0,7)

def getDataSource(data) : 
    CupsOfCoffee = []
    HoursOfSleep = []

    with open (data,newline = '') as f : 
        reader = csv.DictReader(f)
        for i in reader : 
            CupsOfCoffee.append(float(i['Coffee in ml']))
            HoursOfSleep.append(float(i['sleep in hours']))

        return{'x' : HoursOfSleep , 'y' : CupsOfCoffee}

def coRelation(dataSource) : 
    coRelation_1 = np.corrcoef(dataSource['x'])
    coRelation_2 = np.corrcoef(dataSource['y'])
    data_graph = px.scatter(dataSource , x = coRelation_1 , y = coRelation_2)
    data_graph.show()

def setup() : 
    file_name = 'PRO-106_2.csv'
    dataSource = getDataSource(file_name)
    coRelation(dataSource)
    plotFigure(dataSource)

setup()