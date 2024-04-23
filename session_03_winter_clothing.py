from urllib.request import urlopen
url = "https://wttr.in/Vienna?format=%t"
temperature = int(urlopen(url).read().decode().strip("°C"))

print("The temperature, is ", temperature, " °C.")

if temperature >= 20:
    print("It's warm, you don't need a jacket")
elif temperature >=10:
    print("Maybe carry a light jacket")
elif temperature >=0:
    print("Take a cosy wintercoat, it's cold outside")
else:
    print("it's freezing, send the dog!")