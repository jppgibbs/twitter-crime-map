import tkinter as tk
import json
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.ttk import Combobox
import folium
import webbrowser

# Window
win = tk.Tk()
win.title("Forensic Tweet Analyser")
win.minsize(width=900, height=500)
win.maxsize(width=900, height=500)
win.configure(background="#eaeaea")
win.resizable(0,0)


# Button Click Function
def SearchJSON():
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645])
    searchkeyword = name.get()
    print("result for "+searchkeyword+": ")
    
    with open('tweets.json') as data_file:
        countt = 0
        for row in data_file:
            data = json.loads(row)
            tempText = data['text']
            latt = data['geoLocation']['latitude']
            longg = data['geoLocation']['longitude']


            print("you have entered ... "+tempText)
            
            if searchkeyword in tempText:
                countt = countt + 1
                StringToScroll = "\n\n["+str(countt)+"] Date: " + data['createdAt']['$date'] + "Tweet Text:" + data['text']
                folium.Marker([latt,longg], popup=tempText).add_to(map_osm)
                scr.insert(tk.INSERT,StringToScroll)

            else:
               # scr.insert(tk.INSERT,"Nothing Found")
                print("Nothing Found")    
        map_osm.save('plotted.html')
        
def SearchBeerTemplate():
    beerKeywords = ["beer", "lager", "stout", "pilsner", "ale", "stout", "mead", "porter", "trappist"]
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645])
    with open('tweets.json') as data_file:
        for row in data_file:
            countt = 0
            data = json.loads(row) 
            tempText = data['text']
            latt = data['geoLocation']['latitude']
            longg = data['geoLocation']['longitude']
            for word in beerKeywords:
                if word in tempText and countt == 0:
                        countt = countt + 1
                        StringToScroll = "\n\n["+str(countt)+"] Date: " + data['createdAt']['$date'] + " Tweet Text:" + data['text']
                        folium.Marker([latt,longg], popup="").add_to(map_osm)
                        scr.insert(tk.INSERT,StringToScroll) 
        map_osm.save('plotted.html')

"""     
def SearchBeerTemplate():
    beerKeywords = ["beer", "Beer", "lager", "Lager", "Stout", "stout", "Pilsner", "pilsner", "Ale", "ale", "Stout", "stout", "mead", "Mead", "porter", "Porter", "Trappist", "trappist"]
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645])
    with open('tweets.json',encoding = 'utf8') as data_file:
        countt = 0
        for row in data_file:
            data = json.loads(row)
            tempText = data['text']
            latt = data['geoLocation']['latitude']
            longg = data['geoLocation']['longitude']
        for word in beerKeywords:
            if word in tempText:
                countt = countt + 1
                StringToScroll = "\n\n["+str(countt)+"] Date: " + data['createdAt']['$date'] + "Tweet Text:" + data['text']
                folium.Marker([latt,longg], popup=tempText).add_to(map_osm)
                scr.insert(tk.INSERT,StringToScroll)
            else:
                print("Nothing Found")    
                map_osm.save('plotted.html')
"""
    
def ShowPlottedSearchResults():
    webbrowser.open_new_tab('plotted.html')

"""
    with open('tweets.json') as data_file:
        for row in data_file:
            data = json.loads(row)
            StringToScroll = "Date: " + data['createdAt']['$date'] + " latitude:" + str(data['geoLocation']['latitude']) + "Tweet Text:" + data['text']            
            createdAt= data['createdAt']['$date']
            #print("Geo-Location "+str(data['geoLocation']['latitude']))
            print("Tweet Text "+data['text'])
            print("Place Name: "+data['place']['name'])
            print("Place Full Name: "+data['place']['fullName'])
            print(" ...... Next Record ........")
            
    scr.insert(tk.INSERT,StringToScroll)

"""

# Search Label
ttk.Label(win, text="Search String:").place(x=50, y=50)

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=30, textvariable=name,)
nameEntered.place(x=5, y=70)

# Adding a Button
action = ttk.Button(win, width=30, text="Search!", command=SearchJSON)
action.place(x=5, y=93)

# Using a scrolled Text control
scrolW = 84
scrolH = 30
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD, background="#f0f0f0")
scr.place(x=200, y=1)

# Search Label Beer
ttk.Label(win, text="Search Template:").place(x=40, y=140)

# Adding a Button
action = ttk.Button(win, width=30, text="Beers", command=SearchBeerTemplate)
action.place(x=5, y=160)

# Adding a Button
loadingJsonButton = ttk.Button(win, width=30, text=" Show Plotted Search Results ", command=ShowPlottedSearchResults)
loadingJsonButton.place(x=5, y=250)

# Combobox
#combo = Combobox(win, width=28)
#combo['values']= ("Beer", 2, 3, 4, 5, "Text")
#combo.current(0) #set the selected item
#combo.place(x=5, y=160)
#combo.get()

# Place cursor into name Entry
nameEntered.focus()
#======================
# Start GUI
#======================
win.mainloop()