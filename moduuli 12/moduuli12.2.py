import requests

kaupunki=input("kaupungin nimi?")


pyyntö=f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid=eaa8a65deb8653d3e4f2fcf3a43446f5"

vastaus = requests.get(pyyntö).json()

lämpötila=vastaus['main']['temp']-273.15
tyyppi=vastaus['weather'][0]['description']


print(f'Asteita on {lämpötila:.2f} astetta ja sää tila on {tyyppi}.')
