import requests
import folium

url = 'https://data.nasa.gov/resource/nj3a-8wq3.json'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Create a map centered on the United States
    m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

    # Add markers for each meteorite landing
    for d in data:
         if 'reclat' in d and 'reclong' in d and d['reclat'] and d['reclong']:
            folium.Marker(location=[float(d['reclat']), float(d['reclong'])],
                          popup=f"Name: {d['name']}<br>Mass: {d['mass']}<br>Year: {d['year']}").add_to(m)


    # Save the map as an HTML file
    m.save('meteorite_landings_map.html')

else:
    print(f'Error {response.status_code}: {response.reason}')
