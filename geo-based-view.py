import folium
from geopy.geocoders import Nominatim
import time

team = [
    {"name": "Brian", "city": "Denver, Colorado"},
    {"name": "Abhra", "city": "Kolkata, India"},
    {"name": "Ritika", "city": "Bangalore, India"},
    {"name": "Anusha/Suhasini", "city": "Hyderabad, India"},
    {"name": "Manju", "city": "Pune, India"},
    {"name": "Akhilesh", "city": "Indore, India"},
    {"name": "Jannette", "city": "Wisconsin"},
    {"name": "Alex", "city": "Tlaquepaque"},
    {"name": "Tyler", "city": "Canmore"},
    {"name": "Jesus", "city": "Tijuana"},
    {"name": "Kristin", "city": "Oregon"},
    {"name": "Gunawan", "city": "Los Angeles"},
    {"name": "Vignesh", "city": "Chennai"},
    {"name": "Ashish", "city": "Bhopal"},
    {"name": "Dharmil", "city": "Mumbai"},

]

# Custom offsets for nearby cities (lat, lon)
offsets = {
    "Bangalore": (0.15, 0),   # Move label slightly north
    "Chennai": (-0.15, 0),    # Move label slightly south
}

# Create map
m = folium.Map(zoom_start=2)
geolocator = Nominatim(user_agent="team_mapper")
bounds = []

for member in team:
    city = member["city"]
    location = geolocator.geocode(city)
    if location:
        lat, lon = location.latitude, location.longitude
        bounds.append([lat, lon])

        folium.CircleMarker(
            location=[lat, lon],
            radius=6,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.7,
            tooltip=member['name']
        ).add_to(m)

    time.sleep(1)

# Fit view to all cities
m.fit_bounds(bounds)

# Save the map
m.save("team_map.html")
