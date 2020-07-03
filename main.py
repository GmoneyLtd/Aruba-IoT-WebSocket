from flask import Flask, request, abort
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket
from aruba_telemetry import aruba_iot_nb_pb2
from telemetry_view import telemetry_view
import re
from protodict2 import TYPE_CALLABLE_MAP, to_dict
from copy import copy
from google.protobuf.descriptor import FieldDescriptor



type_callable_map = copy(TYPE_CALLABLE_MAP)
type_callable_map[FieldDescriptor.TYPE_BYTES] = (lambda b : ":".join(re.compile(".{2}").findall(b.encode("hex"))))


app = Flask(__name__)


@app.route('/auth')
def auth():
    pass


@app.route('/data')
def data():
    ws = request.environ.get('wsgi.websocket')  #type:WebSocket
    try:
        while True:
            telemetry_bytes = ws.receive()# type:bytearray
            telemetry_bytes = bytes(telemetry_bytes)

            telemetry_str =aruba_iot_nb_pb2.Telemetry()
            telemetry_str.ParseFromString(telemetry_bytes)
            telemetry_dict = to_dict(telemetry_str,type_callable_map=type_callable_map)

            telemetry_view(telemetry_dict)

    except Exception as error:
        print(error)



if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0',6666),app,handler_class=WebSocketHandler)
    http_server.serve_forever()






