# PROGRAMMER: Brandy Nguyen
from WeatherReport import WeatherReport

tester = WeatherReport("Costa Mesa, California", "fahrenheit", "mph")
print(tester.currentWeatherConditions())
print(tester.convertCurrentWeatherCondition())