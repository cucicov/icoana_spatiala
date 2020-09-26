#ps -ef | grep iss.py
import RPi.GPIO as GPIO
import urllib, json, time, math, random
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
url = "https://api.wheretheiss.at/v1/satellites/25544"
currentLat = 44.440567
currentLon = 26.103563
currRadiansLat = currentLat * math.pi / 180
currRadiansLon = currentLon * math.pi / 180
f = open("/home/pi/log.txt", "w+")
while 1:
    time.sleep(1)
    lat = 0
    lon = 0
    try:
        response = urllib.urlopen(url)
        f.write(str(response.getcode()) + ":::")
        f.flush()
        print(str(response.getcode()) + ":::")
    except:
        pass
    try:
        data = json.loads(response.read())
        lat = data['latitude']
        lon = data['longitude']
    except:
        pass
    radiansLat = lat * math.pi / 180
    radiansLon = lon * math.pi / 180
    distance = 6371 * math.acos(math.sin(currRadiansLat) * math.sin(radiansLat) + math.cos(currRadiansLat) * math.cos(radiansLat) * math.cos(radiansLon - currRadiansLon))
    #if random.randint(0,1) > 0:
    if distance > 2200:
        f.write(str(time.ctime(time.time())) + ":" + str(distance) + "\n")
        f.flush()
        print(str(time.ctime(time.time())) + " : \n" + str(distance))
        GPIO.output(26, GPIO.LOW)
    else:
        f.write(str(time.ctime(time.time())) + " : " + "OVER" + "\n")
        f.flush()
        print(str(time.ctime(time.time())) + " : " + "OVER")
        GPIO.output(26, GPIO.HIGH)