import sys
import datetime
import Adafruit_DHT
from influxdb import InfluxDBClient

# SET VARUABLES
host = "192.168.1.67"
port = 8086
user = "user"
password = "password" 
dbname = "readings"

# CREATE CLIENT OBJECT
client = InfluxDBClient(host, port, user, password, dbname)

# SENSOR DETAILS
sensor = Adafruit_DHT.DHT22
sensor_gpio = 17

# SET MEASUREMENT VARUABLES
measurement1 = "dht22-temperature"
measurement2 = "dht22-humidity"

# GET VARUABLES
humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_gpio)

temperature =  round(temperature * 9/5.0 + 32,2)
humidity = round(humidity,1)

# Print for debugging, uncomment the below line
#print("Temp: %s, Humidity: %s" % (temperature, humidity)) 

data1 = [
{
  "measurement": measurement1,
	  "fields": {
		  "temperature" : temperature
	  }
  } 
]

data2 = [
{
  "measurement": measurement2,
	  "fields": {
		  "humidity" : humidity
	  }
  } 
]

# WRITE DATA
client.write_points(data1)
client.write_points(data2)
