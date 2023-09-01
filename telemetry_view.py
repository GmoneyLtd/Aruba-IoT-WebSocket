#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 5:30 PM
# @Author  : Jinlin
# @File    : telemetry.py
# @Project : WebSocket


from tabulate import tabulate
from datetime import datetime

def telemetry_view(kw):
    telemetry = ['meta','reporter','reported','results','characteristics','bleData','wifiData','devCount','status','zigbee','nbSData','apHealth']
    table = []
    table_row = []
    iot_headers = []
    iot_header =[]
    iot_rows = []
    for key in telemetry:
        if isinstance(kw.get(key),dict):
            table_row.append(kw.get(key))
        elif isinstance(kw.get(key),list):
            table_row.append(key + '.msg')
            iot_header.append(key + '.msgDetail')
            iot_headers.append(iot_header)

            iot_row = [[x] for x in kw.get(key)]
            iot_rows.append(iot_row)
        else:
            table_row.append('None')
    table.append(table_row)
    print (tabulate(table, telemetry, tablefmt='grid'))
    for index in range(len(iot_headers)):
        print (tabulate(iot_rows[index],iot_headers[index],  tablefmt='grid'))


# 变更可迭代对象中特定key的值为日期格式(时间戳--->日期)
def process_iterable(iterable, keys):
    if isinstance(iterable, dict):
        for key in list(iterable.keys()):
            value = iterable[key]
            if isinstance(value, dict):
                process_iterable(value, keys)
            elif isinstance(value, list):
                process_iterable(value, keys)
            elif key in keys and isinstance(value, int):
                try:
                    iterable[key] = datetime.fromtimestamp(value).strftime("%Y-%m-%d %H:%M:%S")
                except ValueError:
                    pass
    elif isinstance(iterable, list):
        for item in iterable:
            if isinstance(item, dict):
                process_iterable(item, keys)
            elif isinstance(item, list):
                process_iterable(item, keys)

    return iterable
