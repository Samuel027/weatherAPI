APIKEY = "a0cd1df4eb4bb58e8c88e9e174fe9b6b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

import json
import urllib.request


def main():
    city = input("Please enter the name of your City: ")
    url = BASE_URL.format(city=city, apikey=APIKEY)
    data = urllib.request.urlopen(url).read()
    data = json.loads(data.decode('utf-8'))
    city_name = data['name']
    temperature = data['main']['temp']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']

    print("City:{}\t Temperature:{}\t Pressure:{}\t Humidity{}".format(city_name, temperature, pressure, humidity))


if __name__ == '__main__':
    main()