import tkinter as tk
import json
from tkinter import ttk, scrolledtext, Radiobutton
from tkinter.ttk import Combobox
import re
import folium
from folium import plugins, LayerControl, Map, Marker, FeatureGroup
from folium.plugins import HeatMap, MarkerCluster
import webbrowser
from IPython.display import HTML

# Window
win = tk.Tk()
win.title("Forensic Tweet Analyser")
win.minsize(width=900, height=500)
win.maxsize(width=1900, height=1500)
win.configure(background="#eaeaea")

# Defining Search Templates
beer_template = ["beer", "lager", "stout", "pilsner", "ale", "stout", "mead", "porter", "trappist"]
university_template = ["university", "degree", "dissertation", "MMU", "UoM"]
gym_template = ["gym", "workout", "exercise", "treadmill", "weights"]

# Defining variable for use in radio boxes
marker_cluster_enabled = tk.IntVar(value=1)

# Button Click Function
def SearchJSON(clustered):
    scr.delete(1.0, tk.END)
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645], tiles='Open Street Map')
    marker_cluster = MarkerCluster().add_to(map_osm)
    heat_data = list()
    with open(jsonFileName, encoding="utf-8") as data_file:
        countt = 0
        for row in data_file:
            data = json.loads(row)
            tempText = data['text']
            latt = data['geoLocation']['latitude']
            longg = data['geoLocation']['longitude']          
            if name.get() in tempText:
                    # changing where we add the results to - if clustered results are added we use the cluster plugin and if not we add them directly to the map
                    if clustered == 1:
                        countt = countt + 1
                        StringToScroll = "\n\n["+str(countt)+"]"  + "\nName: " + data['user']['name'] + "\nDate/Time: " + data['createdAt']['$date'] + "\nTweet Text: " "\n" + data['text']
                        folium.Marker([latt,longg], popup=tempText).add_to(marker_cluster)
                        scr.insert(tk.INSERT,StringToScroll) 
                        heat_data.append([latt, longg])
                    else:
                        countt = countt + 1
                        StringToScroll = "\n\n["+str(countt)+"]"  + "\nName: " + data['user']['name'] + "\nDate/Time: " + data['createdAt']['$date'] + "\nTweet Text: " "\n" + data['text']
                        folium.Marker([latt,longg], popup=tempText).add_to(map_osm)
                        scr.insert(tk.INSERT,StringToScroll) 
                        heat_data.append([latt, longg])
        map_osm.save('plotted.html')
        HeatMap(heat_data).add_to(map_osm)
        map_osm.save('plotted_heat.html')

def SearchJSONDate(clustered):
    scr.delete(1.0, tk.END)
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645], tiles='Open Street Map')
    marker_cluster = MarkerCluster().add_to(map_osm)
    heat_data = list()
    with open(jsonFileName, encoding="utf-8") as data_file:
        countt = 0
        for row in data_file:
            data = json.loads(row)
            tempText = data['createdAt']['$date']
            latt = data['geoLocation']['latitude']
            longg = data['geoLocation']['longitude']          
            if name.get() in tempText:
                    # changing where we add the results to - if clustered results are added we use the cluster plugin and if not we add them directly to the map
                    if clustered == 1:
                        countt = countt + 1
                        StringToScroll = "\n\n["+str(countt)+"]"  + "\nName: " + data['user']['name'] + "\nDate/Time: " + data['createdAt']['$date'] + "\nTweet Text: " "\n" + data['text']
                        folium.Marker([latt,longg], popup=tempText).add_to(marker_cluster)
                        scr.insert(tk.INSERT,StringToScroll) 
                        heat_data.append([latt, longg])
                    else:
                        countt = countt + 1
                        StringToScroll = "\n\n["+str(countt)+"]"  + "\nName: " + data['user']['name'] + "\nDate/Time: " + data['createdAt']['$date'] + "\nTweet Text: " "\n" + data['text']
                        folium.Marker([latt,longg], popup=tempText).add_to(map_osm)
                        scr.insert(tk.INSERT,StringToScroll) 
                        heat_data.append([latt, longg])
        map_osm.save('plotted.html')
        HeatMap(heat_data).add_to(map_osm)
        map_osm.save('plotted_heat.html')

# Button Click Function
def SearchJSONRegex(clustered):
    scr.delete(1.0, tk.END)
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645], tiles='Open Street Map')
    marker_cluster = MarkerCluster().add_to(map_osm)
    heat_data = list()
    regex = re.compile(name.get())
    with open(jsonFileName, encoding="utf-8") as data_file:
        countt = 0
        for row in data_file:
            data = json.loads(row)
            tempText = data['text']
            latt = data['geoLocation']['latitude']
            longg = data['geoLocation']['longitude']
            results = regex.findall(data['text'])
            for result in results:
                    if clustered == 1:
                        countt = countt + 1
                        StringToScroll = "\n\n["+str(countt)+"]"  + "\nName: " + data['user']['name'] + "\nDate/Time: " + data['createdAt']['$date'] + "\nTweet Text: " "\n" + result
                        folium.Marker([latt,longg], popup=tempText).add_to(marker_cluster)
                        scr.insert(tk.INSERT,StringToScroll) 
                        heat_data.append([latt, longg])
                    else:
                        countt = countt + 1
                        StringToScroll = "\n\n["+str(countt)+"]"  + "\nName: " + data['user']['name'] + "\nDate/Time: " + data['createdAt']['$date'] + "\nTweet Text: " "\n" + result
                        folium.Marker([latt,longg], popup=tempText).add_to(map_osm)
                        scr.insert(tk.INSERT,StringToScroll) 
                        heat_data.append([latt, longg])
        map_osm.save('plotted.html')
        HeatMap(heat_data).add_to(map_osm)
        map_osm.save('plotted_heat.html')

def SearchTemplate(template, clustered):
    scr.delete(1.0, tk.END)
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645])
    marker_cluster = MarkerCluster().add_to(map_osm)
    heat_data = list()
    with open(jsonFileName, encoding="utf-8") as data_file:
        for row in data_file:
			# Using "countt" variable to store whether or not we've found a trigger word in this tweet yet
            countt = 0
            data = json.loads(row) 
            tempText = data['text']
            latt = data['geoLocation']['latitude']
            longg = data['geoLocation']['longitude']
            for word in template:
				# "countt" variable is checked, if it's not 0 we don't re-print the string as it's already been pushed to the console once.
                if word in tempText and countt == 0:
                    # changing where we add the results to - if clustered results are added we use the cluster plugin and if not we add them directly to the map
                    if clustered == 1:
                        countt = countt + 1
                        StringToScroll = "\n\n"  + "Name: " + data['user']['name'] + "\nDate/Time: " + data['createdAt']['$date'] + "\nTweet Text: " "\n" + data['text']
                        folium.Marker([latt,longg], popup=tempText).add_to(marker_cluster)
                        scr.insert(tk.INSERT,StringToScroll) 
                        heat_data.append([latt, longg])
                    else:
                        countt = countt + 1
                        StringToScroll = "\n\n" + "Name: " + data['user']['name'] + "\nDate/Time: " + data['createdAt']['$date'] + "\nTweet Text: " "\n" + data['text']
                        folium.Marker([latt,longg], popup=tempText).add_to(map_osm)
                        scr.insert(tk.INSERT,StringToScroll) 
                        heat_data.append([latt, longg])
        map_osm.save('plotted.html')
        HeatMap(heat_data).add_to(map_osm)
        map_osm.save('plotted_heat.html')
    
def ShowPlottedSearchResults():
    webbrowser.open_new_tab('plotted.html')

def ShowPlottedSearchHeatmap():
    webbrowser.open_new_tab('plotted_heat.html')

def ClearText():
    scr.delete(1.0, tk.END)

# Select File Label
ttk.Label(win, text="File Name:").place(x=5, y=1)

# User selected file text box
jsonFile = tk.StringVar()
jsonFile.set("tweets.json")
jsonFileNameEntered = ttk.Entry(win, width=30, textvariable=jsonFile,)
jsonFileNameEntered.place(x=5, y=20)
jsonFileName = str(jsonFile.get())

# Search Label
ttk.Label(win, text="Search String:").place(x=5, y=45)

# String Search Text Box
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=30, textvariable=name,)
nameEntered.place(x=5, y=65)

# This button calls the SearchJSON function, passing in the value of the radioboxes for whether the results should be clustered or not
action = ttk.Button(win, width=30, text="Search String", command=lambda : SearchJSON(marker_cluster_enabled.get()))
action.place(x=5, y=90)

actionRegex = ttk.Button(win, width=30, text="Regex Search", command=lambda : SearchJSONRegex(marker_cluster_enabled.get()))
actionRegex.place(x=5, y=115)

actionDate = ttk.Button(win, width=30, text="Search Date [YYYY-MM-DD]", command=lambda : SearchJSONDate(marker_cluster_enabled.get()))
actionDate.place(x=5, y=140)

# Scrolled Text Box
scrolW = 84
scrolH = 30
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD, background="#f0f0f0")
scr.place(x=200, y=1)

# Search Limit Label
ttk.Label(win, text="Search Limit:").place(x=10, y=175)

# Textbox Entry Search Limit
searchLimit = tk.StringVar()
searchLimitEntry = ttk.Entry(win, width=15, textvariable=searchLimit,)
searchLimitEntry.place(x=95, y=173)

# Search Label Beer
ttk.Label(win, text="Search Template:").place(x=40, y=200)

# Note: Using a Lambda function to avoid triggering the command when creating the button and calling the SearchTemplate argument with an array of words to search for as well as the radiobox value
# Beers Template
action = ttk.Button(win, width=30, text="Beers", command=lambda : SearchTemplate(beer_template, marker_cluster_enabled.get()))
action.place(x=5, y=220)

action = ttk.Button(win, width=30, text="University", command=lambda : SearchTemplate(university_template, marker_cluster_enabled.get()))
action.place(x=5, y=245)

action = ttk.Button(win, width=30, text="Gym", command=lambda : SearchTemplate(gym_template, marker_cluster_enabled.get()))
action.place(x=5, y=270)

# Adding radio boxes for toggling clustered markers
clusterOnButton = Radiobutton(win, text="Clustered Markers", variable=marker_cluster_enabled, value=1)
clusterOnButton.place(x=5, y=300)
clusterOffButton = Radiobutton(win, text="Individual Markers", variable=marker_cluster_enabled, value=0)
clusterOffButton.place(x=5, y=325)

# Show Heatmap Button
loadingJsonButton = ttk.Button(win, width=30, text=" Show Plotted Search Heatmap ", command=ShowPlottedSearchHeatmap)
loadingJsonButton.place(x=5, y=350)

# Show Normal Map Button
loadingJsonButton = ttk.Button(win, width=30, text=" Show Plotted Search Results ", command=ShowPlottedSearchResults)
loadingJsonButton.place(x=5, y=375)

# Clear Console Button
clearButton = ttk.Button(win, width=30, text=" Clear Console ", command=ClearText)
clearButton.place(x=5, y=400)

# Set nameEntered as focus
nameEntered.focus()

# Run GUI
win.mainloop()