import json

in_file = open('US_fires_9_14.json', 'r')


US_fires = json.load(in_file)

print(type(US_fires))

#json.dump(eq_data, out_file, indent=4)

#list_of_fires = US_fires['features']

#print(type(list_of_fires))

print(len(US_fires))

bris,lons,lats = [], [], []

for fire in US_fires:
    bri = fire['brightness']
    lon = fire['longitude']
    lat = fire['latitude']

    if bri > 450:
        bris.append(bri)
        lons.append(lon)
        lats.append(lat)
    #hover_texts.append(title)


print("Bris")
print(bris)

print("Lons")
print(lons)

print("Lats")
print(lats)



from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    #'text':hover_texts,
    'marker': {
        'size':[0.05*bri for bri in bris],
        'color':bris,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    },

}]


my_layout = Layout(title='California Fires')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='Cali_Fires.html')