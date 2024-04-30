# PROGRAMMER: Brandy Nguyen
import requests

class WeatherReport :
    # CONSTRUCTOR 
    def __init__(self, city, temperatureUnit, windSpeedUnit) :
        if city not in ["Costa Mesa, California", "Berlin, Germany", "Tokyo, Japan", "Paris, France", "Montreal, Canada"] :
            raise ValueError("Not a valid city")
        if temperatureUnit not in ["celsius", "fahrenheit"] :
            raise ValueError("Temperature unit is not valid")
        if windSpeedUnit not in ["kmh", "ms", "mph", "kn"] :
            raise ValueError("Wind speed unit is not valid")
        self.__city = city
        self.__temperatureUnit = temperatureUnit
        self.__windSpeedUnit = windSpeedUnit
        self.__dataDict = self.currentWeatherConditions()
    # METHODS
    def getCity(self) :
        return self.__city
    
    def getTemperatureUnit(self) :
        return self.__temperatureUnit 
    
    def getWindSpeedUnit(self) :
        return self.__windSpeedUnit
    
    def currentWeatherConditions(self) :
        PATH = "https://api.open-meteo.com/v1/forecast"
        coordinates = self.cityCoordinates()
        latitude, longitude = coordinates
        QUERY = f"?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(PATH + QUERY)
        retrievedData = response.json()
        return retrievedData

    def cityCoordinates(self) :
        if self.__city == "Costa Mesa, California" :
            self.__latitude = 33.641132
            self.__longitude = -117.91867
        elif self.__city == "Berlin, Germany" :
            self.__latitude = 33.67
            self.__longitude = -117.91
        elif self.__city == "Tokyo, Japan" :
            self.__latitude = 33.641132
            self.__longitude = -117.91
        elif self.__city == "Paris, France" :
            self.__latitude = 48.85
            self.__longitude = 2.35
        elif self.__city == "Montreal, Canada" :
            self.__latitude = 33.67
            self.__longitude = -117.91
        self.__cityCoordinates = (self.__latitude, self.__longitude)
        return self.__cityCoordinates
        
    def convertWeatherCode(self, weatherCode) :
        if weatherCode == 0 :
            self.__weather = "Clear sky"
        elif weatherCode == 1 : 
            self.__weather = "Mainly clear"
        elif weatherCode == 2 :
            self.__weather = "Partly cloudy"
        elif weatherCode == 3 :
            self.__weather = "Overcast"
        elif weatherCode == 45 :
            self.__weather = "Fog"
        elif weatherCode == 48 :
            self.__weather = "Depositing rime fog"
        elif weatherCode == 51 :
            self.__weather = "Drizzle: light"
        elif weatherCode == 53 :
            self.__weather = "Drizzle: moderate"
        elif weatherCode == 55 :
            self.__weather = "Drizzle: dense"
        elif weatherCode == 56 :
            self.__weather = "Freezing Drizzle: light"
        elif weatherCode == 57 :
            self.__weather = "Freezing Drizzle: dense"
        elif weatherCode == 61 :
            self.__weather = "Rain: slight"
        elif weatherCode == 63 :
            self.__weather = "Rain: moderate"
        elif weatherCode == 65 :
            self.__weather = "Rain: heavy"
        elif weatherCode == 66 :
            self.__weather = "Freezing rain: light"
        elif weatherCode == 67 :
            self.__weather = "Freezing rain: heavy"
        elif weatherCode == 71 :
            self.__weather = "Snow fall: slight"
        elif weatherCode == 73 :
            self.__weather = "Snow fall: moderate"
        elif weatherCode == 75 :
            self.__weather = "Snow fall: heavy"
        elif weatherCode == 77 :
            self.__weather = "Snow grains"
        elif weatherCode == 80 :
            self.__weather = "Rain showers: slight"
        elif weatherCode == 81 :
            self.__weather = "Rain showers: moderate"
        elif weatherCode == 82 :
            self.__weather = "Rain showers: violent"
        elif weatherCode == 95 :
            self.__weather = "Thunderstorm: slight or moderate"
        elif weatherCode == 85 :
            self.__weather = "Snow showers: slight"
        elif weatherCode == 86 :
            self.__weather = "Snow showers: heavy"
        elif weatherCode == 96 :
            self.__weather = "Thunderstorm: slight"
        elif weatherCode == 99 :
            self.__weather = "Thunderstorm: heavy hail"
        return self.__weather

    def convertIsDay(self, isDay) :
        if isDay == 1 :
            return "Daylight"
        elif isDay == 0 :
            return "Night"

    def convertCurrentWeatherCondition(self) :
        moreDetailedDict = self.currentWeatherConditions()
        moreDetailedDict['current_weather']['weather_description'] = self.convertWeatherCode(self.__dataDict['current_weather']['weathercode'])
        moreDetailedDict['current_weather']['is_day_description'] = self.convertIsDay(moreDetailedDict['current_weather']['is_day'])
        moreDetailedDict['current_weather']['windspeed'] = str(moreDetailedDict['current_weather']['windspeed']) + ' ' + self.getWindSpeedUnit()
        moreDetailedDict['current_weather']['temperature'] = str(moreDetailedDict['current_weather']['temperature']) + ' ' + self.getTemperatureUnit()
        return moreDetailedDict
