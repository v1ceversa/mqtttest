import time
from paho.mqtt.client import Client


client = Client('publisher', clean_session=False)
client.connect(host='167.172.169.242', port=1883)
#client.max_queued_messages_set(0)
init_time = time.time()
print(init_time)
i = 0
client.loop_start()
for i in range(250):
    client.publish(topic='test/pipe', payload=str(i+1), qos=1)
print(i+1)
client.loop_stop()

