import pandas as pd 
from collections import defaultdict

data_insulation = pd.read_csv("isolamento.csv", sep=";", encoding='latin-1') 
data_insulation_array = data_insulation.values.tolist()

data = pd.read_csv("dados.csv", sep=";", encoding='latin-1')
data_array = data.values.tolist()

citys = []
citys = defaultdict(list)

for city in data_insulation_array:
    citys[city[0]].append(city)

for k, v in citys.items():
    count = 0
    tax_insulation = 0
    count = 0
    deaths = 0
    population = 0
    city = ''
    for x in v:
        count = count + 1
        insulation = float(x[5].replace(',', '.'))
        tax_insulation = tax_insulation + insulation
        population = x[2]
        city = x[0]
        
    for x in data_array:
        if x[0].lower() == k.lower():
            deaths = deaths + x[10]
                
    thousand_deaths = (deaths/population)*1000
    final_percent = round((tax_insulation/count)*100, 2)
    
    print('--------------------------'+str(city)+'--------------------------')
    print('Insulation rate: '+str(final_percent)+'%')
    print('Deaths: '+ str(deaths))
    print('Population:'+ str(population))
    print('Death/1000 Habitants: ' + str(round(thousand_deaths, 3)))
        


