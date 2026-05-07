from robodk import robolink
RDK = robolink.Robolink()

import paho.mqtt.client as mqtt
import RobotController as rc

broker = "mqtt.dsic.upv.es"
port = 1883
user = "giirob"
passwd = "UPV2024"

topic_sub = "giirob/pr2/station/demo/commands"
topic_pub = "giirob/pr2/station/demo/status"


def on_message(mqttc, obj, msg):
    payload = msg.payload.decode('utf-8')
    topic = msg.topic
    qos = msg.qos
    rc.handle_message(mqttc, topic, payload)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_message = on_message

mqttc.username_pw_set(username=user, password=passwd)
mqttc.connect(broker, port, 60)
mqttc.subscribe(topic_sub, 0)

mqttc.publish(topic_pub, "ready 1")


mqttc.loop_forever()
