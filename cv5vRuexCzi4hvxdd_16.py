
album_dict = {
  2015: ("Vulnicura", "Honeymoon", "Rebel Heart"),
  2016: ("Lemonade", "Blackstar", "A Moon Shaped Pool"),
  2017: ("Flower Boy", "Antisocialites"),
  2018: ("El Mal Querer", "Someone Out There", "Cranberry", "Kamikaze"),
  2019: ("thank u next", "Magdalene", "Ode to Joy"),
  2020: ("Rough and Rowdy Ways", "folklore", "Future Nostalgia", "Colores")
}
​
def release_year(album):
    
    for year in album_dict.keys():
        if album in album_dict[year]:
            return year
        
    return "Unknown"

