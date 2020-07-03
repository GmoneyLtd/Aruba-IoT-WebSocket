from tabulate import tabulate


def telemetry_view(kw):
    telemetry = ['meta','reporter','reported','results','characteristics','bleData','wifiData','devCount','status']
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