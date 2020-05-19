import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    on_message.i += 1
    print(str(on_message.i) + '| |' + str(time.time()) + '| |' + message.payload.decode())


on_message.i = 0

client = mqtt.Client('subscriber', clean_session=False)
client.on_message = on_message
client.reconnect_delay_set(min_delay=1, max_delay=120)
client.connect(host='167.172.169.242', port=1883)
client.subscribe(topic='test/pipe', qos=1)
client.loop_forever()
