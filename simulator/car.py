import paho.mqtt.client as mqtt


class Car:
    def __init__(self, cam, denm, ip):
        self.baterry = 0
        self.latitude = 0
        self.longitude = 0
        self.cam = cam
        self.denm = denm
        self.ip = ip
        self.mqttc = mqtt.Client()
        self.mqttc.connect(ip)
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_message = self.on_message
        self.mqttc.loop_start()

    def updateLocation(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.denm["management"]["eventPosition"]["latitude"] = latitude
        self.denm["management"]["eventPosition"]["longitude"] = longitude
        self.cam["latitude"] = latitude
        self.cam["longitude"] = longitude

    def updateEvent(self, causeCode, subCauseCode):
        self.denm["situation"]["eventType"]["causeCode"] = causeCode
        self.denm["situation"]["eventType"]["subCauseCode"] = subCauseCode

    def on_connect(self, client, userdata, flags, rc):
        self.mqttc.subscribe([("vanetza/out/cam", 0), ("vanetza/out/denm", 0)])

    def on_message(self, client, userdata, msg):
        print("car")
        # print(str(msg.payload))
