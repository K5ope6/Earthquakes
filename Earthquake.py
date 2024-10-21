#Kevin Jesús Martin López Doblado
import requests
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext #interfaz

ventana = tk.Tk()
ventana.title('Terremotos')
ventana.geometry("800x400")

boxText = scrolledtext.ScrolledText(ventana, width=100, height=20)
boxText.pack(pady=10)

def ConsultarTerremotos():
    url =  'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=50' #url configurada
    solicitudGET = requests.get(url) #solicitud GET
    print(solicitudGET.status_code)
    datos = solicitudGET.json() #datos formato JSON
    earthquake = datos['features'] #info lista terremotos

    boxText.delete(1.0, tk.END)

    for terremoto in earthquake: #Iterar terremotos
        place = terremoto['properties']['place']
        mag = terremoto['properties']['mag']
        time = terremoto['properties']['time']
        fecha = datetime.utcfromtimestamp(time/1000).strftime('%Y-%m-%d %H:%M:%S')
        coordinates = terremoto['geometry']['coordinates']
        latitud = coordinates[0]
        longitud = coordinates[1]
        profundidad = coordinates[2]
        url = terremoto['properties']['url']

        boxText.insert(tk.END, 'Place: ' + place + '\n') #Ingresar datos al cuadro de Texto
        boxText.insert(tk.END, 'Mag: ' + str(mag) + '\n')
        boxText.insert(tk.END, 'Fecha: ' + fecha + '\n')
        boxText.insert(tk.END, 'Url: ' + url + '\n')
        boxText.insert(tk.END, 'Coordinates - ' + 'Latitud: ' + str(latitud) + 'Longitud: ' + str(longitud) + 'Profundidad: ' + str(profundidad) + '\n')
        boxText.insert(tk.END, '\n')

boton = tk.Button(ventana, text="Consultar Terremotos", command=ConsultarTerremotos)#Boton para consultar
boton.pack(pady=10) #Margen

ventana.mainloop()