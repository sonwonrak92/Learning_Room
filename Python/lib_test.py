### 환율 변환
from currency_converter import CurrencyConverter

c = CurrencyConverter()
print (c.convert(100,'EUR', 'USD'))


### 날씨가져오기
import forecastio

api_key = "ee33053878a2d6e74ae39b61f2e9054c"
lat = 37.501354
lng = 127.039763

forecast = forecastio.load_forecast(api_key,lat,lng)
byHour = forecast.hourly()

print (byHour.summary)
print (byHour.icon)