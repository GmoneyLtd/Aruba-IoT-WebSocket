#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 5:30 PM
# @Author  : Jinlin
# @File    : main.py
# @Project : WebSocket


from aruba_telemetry import aruba_iot_nb_pb2
from telemetry_view import telemetry_view,process_iterable
import re
import binascii
from protodict2 import TYPE_CALLABLE_MAP, to_dict
from copy import copy
from google.protobuf.descriptor import FieldDescriptor
import asyncio
import websockets


type_callable_map = copy(TYPE_CALLABLE_MAP)
#简单化将BYTES全部作为字节码处理，不做可视化(可能是UTF-8解码)的处理，实现data数据也需要作为字节码处理，序列化后再按照定制化解码
type_callable_map[FieldDescriptor.TYPE_BYTES] = (lambda b: ":".join(re.compile(".{2}").findall(binascii.hexlify(b).decode())))
# 简单化将UINT64全解析为时间戳，实际中有些问题，简单化可以这样出来，正确的处理方式应该是在序列化后的dict中针对时间戳的时间单独处理，可以参考process_iterable函数
# type_callable_map[FieldDescriptor.TYPE_UINT64] = (lambda value: datetime.fromtimestamp(value).strftime("%Y-%m-%d %H:%M:%S"))

# 定义时间戳的字段
eventTime = ['time','lastSeen']
async def authenticate(websocket):
    # 在此处编写认证逻辑，例如验证令牌或用户名/密码

    # 如果认证失败，可以关闭连接
    await websocket.close()


async def handle_msg(websocket, path):
    if path == '/auth':
        await authenticate(websocket)
    elif path == '/data':
        await process_msg(websocket)


async def process_msg(websocket):
    try:
        while True:
            message = await websocket.recv()
            telemetry_bytes = bytes(message)
            telemetry_str = aruba_iot_nb_pb2.Telemetry()
            telemetry_str.ParseFromString(telemetry_bytes)
            telemetry_dict = to_dict(telemetry_str, type_callable_map=type_callable_map)
            telemetry_dict = process_iterable(telemetry_dict,eventTime)
            # telemetry_view 可能不完整，有些数据没有变换,具体更新列表与aruba-iot-nb.proto对应关系
            telemetry_view(telemetry_dict)

            # 在这里编写处理收到消息的逻辑
            # response = '---- aruba_iot_sb_pb2.py ----'
            # await websocket.send(response)

    except websockets.exceptions.ConnectionClosedError:
        print('WebSocket连接已关闭....')


start_server = websockets.serve(handle_msg, '0.0.0.0', 6666)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
