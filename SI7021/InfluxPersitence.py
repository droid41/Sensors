from influxdb import InfluxDBClient
import datetime
import random
import time

class Writer:

        def __init__(self, msg):
                print self
		print msg

        def writeInflux(self, humidity, cTemp):
		print "Relative Humidity is : %.2f %%" %humidity
		print "Temperature in Celsius is : %.2f C" %cTemp

		now = int(datetime.datetime.today().strftime('%s'))
    	
    		series = []

		hostName = "raspberryHA"
	        tempPointValues = {
        	        "time": now,
                	"measurement": "temp",
	                'fields':  {
        	            'value': cTemp,
	                },
        	        'tags': {
                	    "hostName": hostName,
	                },
        	    }
	        series.append(tempPointValues)

		humPointValues = {
                        "time": now,
                        "measurement": "hum",
                        'fields':  {
                            'value': humidity,
                        },
                        'tags': {
                            "hostName": hostName,
                        },
                    }
                series.append(humPointValues)

		print series


		client = InfluxDBClient('localhost', 8086, 'root', 'root', 'TempHum')
		result = client.write_points(series)
		print result
		print("Result: {0}".format(result))


