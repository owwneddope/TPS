import folium


from folium.features import DivIcon

MM_m = folium.Map(location=[59.368412, 28.601065], zoom_start=12)

tooltip = 'Начальная станция'
tooltip_2 = 'Конечная станция'
tooltip_3 = 'Станция заказчика'


points_zakstart=[[59.368412, 28.601065],[59.806903, 30.388003]]
points_zakend=[[59.806903, 30.388003], [59.391806, 28.841122]]



folium.Marker([59.806903, 30.388003], popup='Шушары',tooltip=tooltip).add_to(MM_m)
folium.Marker([59.391806, 28.841122], popup='Веймарн',tooltip=tooltip_2).add_to(MM_m)
folium.Marker([59.368412, 28.601065], popup='Кингисепп',tooltip=tooltip_3).add_to(MM_m)

folium.PolyLine(points_zakend, color="green", weight=2.5, opacity=1).add_to(MM_m)
folium.PolyLine(points_zakstart, color="blue", weight=2.5, opacity=1).add_to(MM_m)

from math import sin, cos, sqrt, atan2, radians

def calculate_distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

coordinates = [
    [59.368412, 28.601065],           # координаты заказчика
    [59.391806, 28.841122]]           # координаты конечной станции

lines=folium.PolyLine(locations=coordinates, color="red", weight=1)
MM_m.add_child(lines)
distance = calculate_distance(coordinates[0][0], coordinates[0][1],
                              coordinates[1][0], coordinates[1][1])
distance_circle = folium.Marker(
    [59.368412, 28.601065],                          # координаты заказчика
    icon=DivIcon(
        icon_size=(50,50),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#252526;"><b>%s</b></div>' % "{:10.2f} KM".format(distance),
        )
    )
MM_m.add_child(distance_circle)

MM_m.save('Маршрут №248.html')