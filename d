from urllib import request
print(request.urlopen("http://158.160.6.201/api/weather/temp.php").read().decode())
print(request.urlopen("http://158.160.6.201/api/weather/wind.php").read().decode())
print(request.urlopen("http://158.160.6.201/api/weather/humidity.php").read().decode())
