import csv
from geopy.geocoders import Nominatim
import webbrowser
import folium
import json
import pandas as pd
import plotly.express as px


barcelonaCom=["Alt Penedès", "Anoia", "Bages", "Baix Llobregat", "Barcelonès", "Berguedà", "Maresme", "Garraf", "Moianès", "Osona", "Vallès Occidental", "Vallès Oriental"]
lleidaCom=["Alta Ribagorça", "Alt Urgell", "Cerdanya", "Garrigues", "Noguera", "Pallars Jussà", "Pallars Sobirà", "Pla d'Urgell", "Segarra", "Segrià", "Solsonès", "Urgell", "Val d'Aran"]
tarragonaCom=["Alt Camp", "Baix Camp", "Baix Ebre", "Baix Penedès", "Conca de Barberà", "Ribera d'Ebre", "Montsià", "Priorat", "Tarragonès", "Terra Alta"]
gironaCom=["Alt Empordà", "Baix Empordà", "Garrotxa", "Gironès", "Pla de l'Estany", "Selva", "Ripollès"]
Comarca=["Alt Penedès", "Anoia", "Bages", "Baix Llobregat", "Barcelonès", "Berguedà", "Maresme", "Garraf", "Osona", "Selva", "Vallès Oriental","Vallès Occidental",
"Alta Ribagorça", "Alt Urgell", "Cerdanya", "Garrigues", "Noguera", "Pallars Jussà", "Pallars Sobirà", "Pla d'Urgell", "Segarra", "Segrià", "Solsonès", "Urgell", "Val d'Aran",
"Alt Camp", "Baix Camp", "Baix Ebre", "Baix Penedès", "Conca de Barberà", "Ribera d'Ebre", "Montsià", "Priorat", "Tarragonès", "Terra Alta",
"Alt Empordà", "Baix Empordà", "Garrotxa", "Gironès", "Pla de l'Estany", "Ripollès"]

loc = Nominatim(user_agent="sergio08301@gmail.com")
def exercise1():
    with open('file.csv', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        reader = csv.DictReader(csvfile)
        barcelonanum=0
        lleidanum=0
        tarragonanum=0
        gironanum=0
        for row in reader:
            if row['COMARCA'] in barcelonaCom:
                barcelonanum=barcelonanum+1
            elif row['COMARCA'] in lleidaCom:
                lleidanum=lleidanum+1
            elif row['COMARCA'] in tarragonaCom:
                tarragonanum=tarragonanum+1
            elif row['COMARCA'] in gironaCom:
                gironanum=gironanum+1
    print("En barcelona hi ha "+str(barcelonanum)+", en lleida hi ha "+str(lleidanum)+
    ", en tarragona hi ha "+str(lleidanum)+", en girona hi ha "+str(gironanum))





def exercise2():
    with open('file.csv', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        reader = csv.DictReader(csvfile)
        modalitats=[]
        modalitatsTimes=[]
        for row in reader:
            if row['MODALITATS'].find(",")=="-1": #Solo hay una modalidad
                if row['MODALITATS'] in modalitats:
                    modalitatsTimes[modalitats.index(row['MODALITATS'])]=modalitatsTimes[modalitats.index(row['MODALITATS'])]+1
                else:
                    modalitats.append(row['MODALITATS'])
                    modalitatsTimes.append(1)
            else:
                mods=row['MODALITATS'].split(",")
                for mod in mods:
                    if mod=="": break
                    if mod[0]==" ":
                        mod=mod[1:len(mod)]
                    if mod in modalitats:
                        modalitatsTimes[modalitats.index(mod)]=modalitatsTimes[modalitats.index(mod)]+1
                    else:
                        modalitats.append(mod)
                        modalitatsTimes.append(1)
        orderModalitats=[modalitats for _,modalitats in sorted(zip(modalitatsTimes,modalitats))]
        modalitatsTimes.sort(key=int)    
        for num in range(0,len(modalitats)):
            print(str(orderModalitats[num])+" un total de "+str(modalitatsTimes[num]))

def exercise3():
    print("Which provincia you want to look for? ")
    provincia = str(input())
    if provincia=="Barcelona":
        print("Escull quina comarca vols")
        for num in range(0,len(barcelonaCom)):
            print(str(num)+". "+str(barcelonaCom[num]))
        comarca = str(input())
        comarca = barcelonaCom[int(comarca)]
    elif provincia=="Tarragona":
        print("Escull quina comarca vols")
        for num in range(0,len(tarragonaCom)):
            print(str(num)+". "+str(tarragonaCom[num]))
        comarca = str(input())
        comarca = tarragonaCom[int(comarca)]
    elif provincia=="Lleida":
        print("Escull quina comarca vols")
        for num in range(0,len(lleidaCom)):
            print(str(num)+". "+str(lleidaCom[num]))
        comarca = str(input())
        comarca = lleidaCom[int(comarca)]
    elif provincia=="Girona":
        print("Escull quina comarca vols")
        for num in range(0,len(gironaCom)):
            print(str(num)+". "+str(gironaCom[num]))
        comarca = str(input())
        comarca = gironaCom[int(comarca)]
    else :
        print("Next time put a real provincia")
        sys.exit()


    with open('file.csv', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        reader = csv.DictReader(csvfile)
        modalitats=[]
        modalitatsTimes=[]
        for row in reader:
            if row['COMARCA']==comarca:
                if row['MODALITATS'].find(",")=="-1": #Solo hay una modalidad
                    if row['MODALITATS'] in modalitats:
                        modalitatsTimes[modalitats.index(row['MODALITATS'])]=modalitatsTimes[modalitats.index(row['MODALITATS'])]+1
                    else:
                        modalitats.append(row['MODALITATS'])
                        modalitatsTimes.append(1)
                else:
                    mods=row['MODALITATS'].split(",")
                    for mod in mods:
                        if mod=="": break
                        if mod[0]==" ":
                            mod=mod[1:len(mod)]
                        if mod in modalitats:
                            modalitatsTimes[modalitats.index(mod)]=modalitatsTimes[modalitats.index(mod)]+1
                        else:
                            modalitats.append(mod)
                            modalitatsTimes.append(1)
    orderModalitats=[modalitats for _,modalitats in sorted(zip(modalitatsTimes,modalitats))]
    modalitatsTimes.sort(key=int)    
    for num in range(0,len(modalitats)):
        print(str(orderModalitats[num])+" un total de "+str(modalitatsTimes[num]))

def exercise4():
    print("Which comarca you want to look for? ")
    comarca = str(input())
    with open('listaMunicipio.csv', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        reader = csv.DictReader(csvfile)
        municipis=[]
        for row in reader:
            if row['Nom de la comarca']==comarca:
                municipis.append(row['Nom del municipi'])
    for num in range(0,len(municipis)):
        print(str(num)+". "+str(municipis[num]))
    print("Which municipi you want to look for? (Enter the number)")
    municipi = str(input())
    municipi = municipis[int(municipi)]
    print("Choose from one of the following entities on "+municipi+":")
    with open('file.csv', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        reader = csv.DictReader(csvfile)
        entitiesInMunicipi=[]
        for row in reader:
            if row['MUNICIPI']==municipi:
                entitiesInMunicipi.append(row['NOM_ENTITAT'])
    for num in range(0,len(entitiesInMunicipi)):
        print(str(num)+". "+str(entitiesInMunicipi[num]))
    print("Which entity you want to look for? (Enter the number)")
    entity = str(input())
    entity = entitiesInMunicipi[int(entity)]
    print("Printing on map the following entity: "+entity)
    with open('file.csv', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        reader = csv.DictReader(csvfile)
        direccion=""
        for row in reader:
            if row['NOM_ENTITAT']==entity:
                direccion=row['ADREÇA']+", "+row['CP']+", "+row['MUNICIPI']
    print("The direction of: "+entity+" is "+direccion)

    
    getLoc = loc.geocode(direccion)
    
    m = folium.Map(location=[getLoc.latitude,getLoc.longitude], zoom_start=15)
    folium.Marker(location=[getLoc.latitude,getLoc.longitude], popup="<i>"+entity+"</i>").add_to(m)
    m.save('map.html')
    webbrowser.open_new_tab('map.html')

def exercise5():
    print("Tell me a postal code")
    postalc = str(input())
    with open('file.csv', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        reader = csv.DictReader(csvfile)
        postallist=[]
        for row in reader:
            if row['CP']==postalc:
                postallist.append(row['NOM_ENTITAT'])
    with open('file.csv', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        reader = csv.DictReader(csvfile)
        direcciones=[]
        for row in reader:
            for num in range(0,len(postallist)):
                if row['NOM_ENTITAT']==postallist[num]:
                    direcciones.append(row['ADREÇA']+", "+row['MUNICIPI'])
    getLoc = loc.geocode(direcciones[0])
    m = folium.Map(location=[getLoc.latitude,getLoc.longitude], zoom_start=15)
    for num in range(0,len(postallist)):
        getLoc = loc.geocode(direcciones[num])
        try:
            folium.Marker(location=[getLoc.latitude,getLoc.longitude], popup="<i>"+postallist[num]+"</i>").add_to(m)
        except: 
            print(postallist[num]+ " could not be found")
    m.save('map.html')
    webbrowser.open_new_tab('map.html')

def exercise6():
    content="Comarca,Entidades\n"
    Nentitats=[]
    for num in range(0,len(Comarca)):
        Nentitats.append(1)
    for num in range(0,len(Comarca)):
        with open('file.csv', newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['COMARCA']==Comarca[num]:
                    Nentitats[num]=Nentitats[num]+1
            
    orderComarca=[Comarca for _,Comarca in sorted(zip(Nentitats,Comarca))]
    Nentitats.sort(key=int)  
    for num in range(0,len(orderComarca)):
        if num<len(orderComarca)-10:
            content=content+orderComarca[num]+","+"0"+"\n"
        else: 
            content=content+orderComarca[num]+","+str(Nentitats[num])+"\n"

    text_file = open("ranking.csv", "wt")
    n = text_file.write(content)
    text_file.close()

    catalunya_comarcas = json.load(open("catalunya_comarcas.geojson", "r"))

    #Now the map representation
    state_id_map = {}
    for feature in catalunya_comarcas["features"]:
        feature["id"] = feature["properties"]["comarca"]
        state_id_map[feature["properties"]["nom_comar"]] = feature["id"]

    df = pd.read_csv("ranking.csv")

    df["id"] = df["Comarca"].apply(lambda x: state_id_map[x])

    fig = px.choropleth(
        df,
        locations="id",
        geojson=catalunya_comarcas, #nombre del geojson usado
        color="Entidades",#la fila que quieres representar
        hover_name="Comarca",
        title="Entitats esportives por comarca en Catalunya",
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

def exercise7():
    content="Comarca,Entidades\n"
    Nentitats=[]
    for num in range(0,len(Comarca)):
        Nentitats.append(1)
    for num in range(0,len(Comarca)):
        with open('file.csv', newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['COMARCA']==Comarca[num]:
                    Nentitats[num]=Nentitats[num]+1
            
    orderComarca=[Comarca for _,Comarca in sorted(zip(Nentitats,Comarca))]
    Nentitats.sort(key=int)  
    for num in range(0,len(orderComarca)):
        if num>10:
            content=content+orderComarca[num]+","+"0"+"\n"
        else: 
            content=content+orderComarca[num]+","+str(Nentitats[num])+"\n"

    text_file = open("ranking.csv", "wt")
    n = text_file.write(content)
    text_file.close()

    catalunya_comarcas = json.load(open("catalunya_comarcas.geojson", "r"))

    #Now the map representation
    state_id_map = {}
    for feature in catalunya_comarcas["features"]:
        feature["id"] = feature["properties"]["comarca"]
        state_id_map[feature["properties"]["nom_comar"]] = feature["id"]

    df = pd.read_csv("ranking.csv")

    df["id"] = df["Comarca"].apply(lambda x: state_id_map[x])

    fig = px.choropleth(
        df,
        locations="id",
        geojson=catalunya_comarcas, #nombre del geojson usado
        color="Entidades",#la fila que quieres
        hover_name="Comarca",
        #hover_data="Entidades",
        title="Entitats esportives por comarca en Catalunya",
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

def exercise8():
    content="Comarca,Entidades\n"
    Nentitats=[]
    for num in range(0,len(Comarca)):
        Nentitats.append(1)
    for num in range(0,len(Comarca)):
        with open('file.csv', newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['COMARCA']==Comarca[num]:
                    Nentitats[num]=Nentitats[num]+1
            
    orderComarca=[Comarca for _,Comarca in sorted(zip(Nentitats,Comarca))]
    Nentitats.sort(key=int)  
    for num in range(0,len(orderComarca)):
        if orderComarca[num]=="Barcelonès":
            content=content+orderComarca[num]+","+"0"+"\n"
        else: 
            content=content+orderComarca[num]+","+str(Nentitats[num])+"\n"

    text_file = open("ranking.csv", "wt")
    n = text_file.write(content)
    text_file.close()

    catalunya_comarcas = json.load(open("catalunya_comarcas.geojson", "r"))

    #Now the map representation
    state_id_map = {}
    for feature in catalunya_comarcas["features"]:
        feature["id"] = feature["properties"]["comarca"]
        state_id_map[feature["properties"]["nom_comar"]] = feature["id"]

    df = pd.read_csv("ranking.csv")

    df["id"] = df["Comarca"].apply(lambda x: state_id_map[x])

    fig = px.choropleth(
        df,
        locations="id",
        geojson=catalunya_comarcas, #nombre del geojson usado
        color="Entidades",#la fila que quieres
        hover_name="Comarca",
        #hover_data="Entidades",
        title="Entitats esportives por comarca en Catalunya",
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

def exercise9():
    content="Comarca,Entidades\n"
    Nentitats=[]
    for num in range(0,len(Comarca)):
        Nentitats.append(1)
    for num in range(0,len(Comarca)):
        with open('file.csv', newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['COMARCA']==Comarca[num]:
                    Nentitats[num]=Nentitats[num]+1
            
    orderComarca=[Comarca for _,Comarca in sorted(zip(Nentitats,Comarca))]
    Nentitats.sort(key=int)  
    for num in range(0,len(orderComarca)):
            content=content+orderComarca[num]+","+str(Nentitats[num])+"\n"

    text_file = open("ranking.csv", "wt")
    n = text_file.write(content)
    text_file.close()

    catalunya_comarcas = json.load(open("catalunya_comarcas.geojson", "r"))

    #Now the map representation
    state_id_map = {}
    for feature in catalunya_comarcas["features"]:
        feature["id"] = feature["properties"]["comarca"]
        state_id_map[feature["properties"]["nom_comar"]] = feature["id"]

    df = pd.read_csv("ranking.csv")

    df["id"] = df["Comarca"].apply(lambda x: state_id_map[x])

    fig = px.choropleth(
        df,
        locations="id",
        geojson=catalunya_comarcas, #nombre del geojson usado
        color="Entidades",#la fila que quieres
        hover_name="Comarca",
        #hover_data="Entidades",
        title="Entitats esportives por comarca en Catalunya",
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

def exercise10():
    content="Comarca,Entidades\n"
    Nentitats=[]
    for num in range(0,len(Comarca)):
        Nentitats.append(1)
    for num in range(0,len(Comarca)):
        with open('file.csv', newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024),delimiters=',')
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['COMARCA']==Comarca[num]:
                    Nentitats[num]=Nentitats[num]+1
            
    orderComarca=[Comarca for _,Comarca in sorted(zip(Nentitats,Comarca))]
    Nentitats.sort(key=int)  
    for num in range(0,len(orderComarca)):
            content=content+orderComarca[num]+","+str(Nentitats[num])+"\n"

    text_file = open("ranking.csv", "wt")
    n = text_file.write(content)
    text_file.close()

    data = pd.read_csv("ranking.csv")
    entidades = data['Entidades']
    comarcas = data['Comarca']

    fig = px.bar(x=comarcas, y = entidades,labels=dict(x="Comarcas",y="Entidades"))
    fig.update_xaxes(type='category')

    fig.show()


def retry():
    print("Want to try another option?")
    answer= str(input())
    if answer=="yes":
        selector()
    else:
        print("Okay, bye")

def selector():
    print("Which exercise you want to execute? ")
    exercise = str(input())
    if exercise=="1":
        exercise1()
        retry()
    elif exercise=="2":
        exercise2()
        retry()
    elif exercise=="3":
        exercise3()
        retry()
    elif exercise=="4":
        exercise4()
        retry()
    elif exercise=="5":
        exercise5()
        retry()
    elif exercise=="6":
        exercise6()
        retry()
    elif exercise=="7":
        exercise7()
        retry()
    elif exercise=="8":
        exercise8()
        retry()
    elif exercise=="9":
        exercise9()
        retry()
    elif exercise=="10":
        exercise10()
        retry()
    else:
        print("Not a valid number of exercise")
        selector()


print("Lab 2 Python")
selector()