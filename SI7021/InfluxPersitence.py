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

		d = datetime.datetime.now()

		data = []
		data.append({
			'points': [[time.mktime(d.timetuple()),cTemp, humidity]],
			'name': 'temp',
			'columns': ['time', 'temp', 'hum']
		})

#		now = datetime.datetime.today().isoformat() # .strftime('%s')
#
#		print now
#   	
#		hostName = "raspberryHA"
#	        tempPointValue = [{
#        	        "time": now,
#                	"measurement": "temp",
#	                'fields':  {
#        	            'temp': cTemp,
#			    'hum': humidity,
#	                },
#        	        'tags': {
#                	    "hostName": hostName,
#	                },
#        	    }]

		print data

		client = InfluxDBClient('localhost', 8086, 'root', 'root', 'TempHum')
		result = client.write_points(data)
		print result
		print("Result: {0}".format(result))


