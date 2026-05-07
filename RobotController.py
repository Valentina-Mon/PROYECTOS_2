from robodk import robolink
from robodk.robolink import ITEM_TYPE_PROGRAM
import threading

RDK = robolink.Robolink()

import paho.mqtt.client as mqtt

station_commands_topic = "giirob/pr2/station/demo/commands"
station_status_topic = "giirob/pr2/station/demo/status"


def handle_message(mqttc, topic, payload):
    msg = payload.strip()

    print(" Mensaje recibido:", msg)

    if topic == station_commands_topic:


        if msg == "1":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc, "1")
            )
            hilo.start()

        elif msg == "2":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc, "2")
            )
            hilo.start()


        elif msg == "3":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"3")
            )
            hilo.start()

        elif msg == "4":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"4")
            )
            hilo.start()

        elif msg == "5":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"5")
            )
            hilo.start()

        elif msg == "6":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"6")
            )
            hilo.start()

        elif msg == "7":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"7")
            )
            hilo.start()

        elif msg == "8":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"8")
            )
            hilo.start()

        elif msg == "9":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"9")
            )
            hilo.start()

        elif msg == "10":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"10")
            )
            hilo.start()

        elif msg == "11":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"11")
            )
            hilo.start()

        elif msg == "12":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"12")
            )
            hilo.start()

        elif msg == "13":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"13")
            )
            hilo.start()

        elif msg == "14":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"14")
            )
            hilo.start()

        elif msg == "15":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"15")
            )
            hilo.start()

        elif msg == "16":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"16")
            )
            hilo.start()

        elif msg == "17":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"17")
            )
            hilo.start()

        elif msg == "18":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"18")
            )
            hilo.start()

        elif msg == "19":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"19")
            )
            hilo.start()

        elif msg == "20":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"20")
            )
            hilo.start()

        elif msg == "21":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"21")
            )
            hilo.start()

        elif msg == "22":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"22")
            )
            hilo.start()

        elif msg == "23":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"23")
            )
            hilo.start()

        elif msg == "24":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"24")
            )
            hilo.start()

        elif msg == "25":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"25")
            )
            hilo.start()

        elif msg == "26":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"26")
            )
            hilo.start()

        elif msg == "27":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"27")
            )
            hilo.start()

        elif msg == "28":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"28")
            )
            hilo.start()

        elif msg == "29":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"29")
            )
            hilo.start()

        elif msg == "30":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"30")
            )
            hilo.start()

        elif msg == "31":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"31")
            )
            hilo.start()

        elif msg == "32":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"32")
            )
            hilo.start()

        elif msg == "33":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"33")
            )
            hilo.start()

        elif msg == "34":
            hilo = threading.Thread(
                target=ejecutar_programa,
                args=(mqttc,"34")
            )
            hilo.start()




       
         # else:
            #print("Comando no reconocido")


def ejecutar_programa(mqttc, nombre_programa):
    programa = RDK.Item(nombre_programa, ITEM_TYPE_PROGRAM)
    programa.RunProgram()

    
