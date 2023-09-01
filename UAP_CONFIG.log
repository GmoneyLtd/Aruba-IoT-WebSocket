fc:7f:f1:cd:99:04# show ap debug ble-table all

BLE Device Table [APBs]
-----------------------
MAC                HW_Type   FW_Ver        Flags   Status  Radio Type  Tx_Power  Last Update  Uptime
---                -------   ------        -----   ------  ----------  --------  -----------  ------
6c:79:b8:12:2e:a9  BT-AP303  OAD B 1.2-42  0x00a3  LIA     Internal    14        5s           22h:6m:0s


BLE Device Table [Generic]
---------------------------
MAC                Address Type  RSSI  Last Update  Device Class  Generic Filter  BT-SIG Company IDs
---                ------------  ----  -----------  ------------  --------------  ------------------
e8:97:cc:5c:44:31  Static        -84   I:3330s      --            --              0x004C
18:ef:3a:74:42:32  Public        -98   I:26s        --            --              0x00CC
cd:98:d7:45:52:65  Static        -76   I:3342s      --            --              0x004C
cc:1a:b1:48:7c:a6  Static        -72   I:641s       --            --              0x004C
ff:d0:ab:2c:16:d4  Static        -64   I:1529s      --            --              0x004C
f7:06:fe:75:5e:e3  Static        -76   I:2427s      --            --              0x004C
c6:a6:f5:16:c6:f0  Static        -67   I:7s         --            --              0x004C
e2:c5:29:e4:b9:13  Static        -78   I:2442s      --            --              0x004C
b8:7c:6f:10:15:25  Public        -82   I:0s         --            --              --
fd:45:f7:1b:43:26  Static        -72   I:2s         --            --              0x004C
dc:b4:95:b0:cd:71  Static        -66   I:642s       --            --              0x004C
f1:b3:67:96:59:e2  Static        -73   I:1544s      --            --              0x004C

Generic BLE devices:12
Total BLE devices:12

Note: Battery level for LS-BT1USB devices is indicated as USB.
Note: Uptime is shown as Days hour:minute:second.
Note: Last Update is time in seconds since last heard update.
Note: Meas. Pow. is the averaged RSSI (in dBm) when the iBeacon is calibrated.
Note: Tx_Power is shown in dBm in the APBs section for radios that support radio profile type 1. For all other APB radios, Tx_Power is a discrete level from 0-15.
Status Flags:L:AP's local beacon; I:iBeacon; A:Beacon management capable
            :H:High power beacon; T:Asset Tag Beacon; U:Upgrade of firmware pending
            :u:Beacon management update received
Last Update Flags:I: Device observed by internal radio
                 :E: Device observed by external radio
Generic Filter:S:serviceUUIDFilter; C:companyIdentifierFilter
              :M:macOuiFilter; L:localNameFilter

//
fc:7f:f1:cd:99:04# show ap debug ble-config

============================================================
                     IOT Radio Profiles
============================================================
Profile Name              : poc
Radio Instance            : Internal
Radio Mode                : BLE
BLE Mode                  : beaconing scanning
BLE Console               : Dynamic
BLE/ZigBee Tx Power (dBm) : 0
-----------------------------------------------
============================================================
                  Zigbee Service Profiles
============================================================
No Zigbee service profiles currently configured.

============================================================
                      Attached Radios
============================================================
Radio Configuration
-------------------
Item                                    Value
----                                    -----
Radio Information                       TI ONBOARD Internal BLE
Radio Profile Type                      --
Zigbee Supported                        No
APB MAC Address                         6c:79:b8:12:2e:a9
Operational Mode                        Dynamic Console (APB: Dynamic Console)
Operational BluOS FW Version            OAD B 1.2-42
Bundled BluOS Upgrade                   Enabled (-1)
Bundled BluOS Images                    Bank A(/aruba/bin/UpgradeImage_AP_OAD-A_1.2-42.bin) Bank B(/aruba/bin/Beacon_AP_OAD-B_1.2-42.bin)
OTA FW BluOS Upgrade                    Disabled
FW Stack Supported                      No
IoT Coexistence Status                  Actual: -1 Desired: (Value not received from WiFi radio)..
IoT Coexistence Inputs                  0 -1 -1
IoT Antenna Type                        Internal
IoT Antenna Gain                        Unavailable (Default: 0dBm)
IoT Transmit Power Board Limit          Value unavailable for AP type
BLE Transmit Power Regulatory Limit     Unavailable (default:4dBm)
Zigbee Transmit Power Regulatory Limit  Unavailable (default:10dBm for all channels 11-26)
-----------------
============================================================
                        Misc. Config
============================================================
Miscellaneous Configuration
---------------------------
Item                            Value
----                            -----
FIPS Mode                       No
Conductor IP                    127.0.0.1
BLE Ready                       Yes
APB Info Update Intvl (in sec)  76 (306302/306255)
BLE debug log                   Enabled
Message Selector                0xffff (APB: 0xffff)
AP USB Power Override           Disabled (-1)
Uplink Status                   Up
Time Last Message to APB        1970-01-01 08:00:00
Current Log Level               { 0x901e1 : Error(0x0001), FW-Upgrade(0x0020), FW-UpgradeErr(0x0040), CfgUpdate(0x0080), CfgUpdateErr(0x0100), IOT-GW(0x10000), DevMgmt(0x80000) }
Log Mac Filter                  None



-----------------
============================================================
                   IOT Transport Profiles
============================================================
BLE IoT Transport Context Config ID: 20
Last Sync Time: 2023-09-01 22:41:05
----------------------------------------------
Name                       :test
Identifier                 :1693400229
ServerType                 :Telemetry Websocket
Last Update Sent           :2023-09-01 22:41:15
Num. Updates Sent          :130766
ReportingInterval          :5 second
DeviceClassFilter          :iBeacon(8),Unclassified(11),sBeacon(19),Aruba Beacons(0),Google(26),Ability Smart Sensors(14),Aruba Tags(1),Aruba Sensors(13),Polestar(27),Wiliot(20),MySphera(18),ZF Tags(2),Blyott(28)
RSSI Reporting             :Average
EnvironmentType            :office
CustomFadingFactor         :20
bleDataForwarding          :TRUE
DataFilter                 :00 00
companyIdentifierFilter    :947b
============================================================
Notes: - Setting Message Selector value to 0x0 will cause the APB to function improperly. Use the knob with caution.
       - An active Meridian Beacons Management profile will override the iBeacon configuration setting on an AP's BLE radio.
       - Uplink status is applicable only when console is set to dynamic

Log Levels Available: { All(0xffffff), Info(0x04), Warning(0x02), Error(0x01), Ageout(0x08), BMReq(0x10), FW-Upgrade(0x20), FW-UpgradeErr(0x40), CfgUpdate(0x80), CfgUpdateErr(0x100), Beacon(0x200), BcnTLV(0x400), BcnErr(0x800), APB(0x1000), Tags(0x2000), ZF(0x4000), AMON(0x8000), IOT-GW(0x10000), AT-HTTPS-JSON(0x20000), AT-WEBSOCKET-PROTOBUF(0x40000), DevMgmt(0x80000), Enocean(0x100000), IoTOps(0x200000), Azure-IoTHub(0x400000), Filter(0x800000), None(0x00) }

//
fc:7f:f1:cd:99:04# show ap debug ble-database

BLE APB Information
-------------------
AP Name            AP Group  BLE MAC            Radio Type  BLE Cur. Bank   BLE Opp. Bank   AP Eth MAC         AP IP      Reported at           ConfigID  Status
-------            --------  -------            ----------  -------------   -------------   ----------         -----      -----------           --------  ------
fc:7f:f1:cd:99:04            6c:79:b8:12:2e:a9  Internal    OAD B   1.2-42  OAD A   1.2-42  fc:7f:f1:cd:99:04  127.0.0.1  2023-09-01 22:41:44   20        Current

Total AP BLE devices reported:1
Note:'Status' column indicates whether information received for an AP's
    : BLE radio is 'Current' (message received in the last 10 minutes)
    : or 'OutOfDate' (message received more than last 10 minutes ago and/or AP might be down).

//
fc:7f:f1:cd:99:04# show ap debug ble-relay iot-profile

ConfigID                                : 20

---------------------------Profile[test]---------------------------

Identifier                              : 1693400229
serverURL                               : ws://192.168.40.249:6666/data
serverType                              : Telemetry Websocket
deviceClassFilter                       : iBeacon,Unclassified,sBeacon,Aruba Beacons,Google,Ability Smart Sensors,Aruba Tags,Aruba Sensors,Polestar,Wiliot,MySphera,ZF Tags,Blyott
reportingInterval                       : 5 second
authentication-mode                     : none
accessToken                             : 123456
clientID                                : ble_token
rssiReporting                           : Average
environmentType                         : office
bleDataForwarding                       : TRUE
companyIdentifierFilter                 : 947b
Server Connection State
--------------------------
TransportContext                        : Connection Established
Last Data Update                        : 2023-09-01 22:42:17
Last Send Time                          : 2023-09-01 22:42:17
TransType                               : Websocket

fc:7f:f1:cd:99:04# show ap debug ble-relay report


---------------------------Profile[test]---------------------------

WebSocket Connect Status                : Connection Established
WebSocket Connection Established        : Yes
Location Id                             : Not Configured
Websocket Address                       : ws://192.168.40.249:6666/data
WebSocket Host                          : 192.168.40.249:6666
WebSocket Path                          : data
Vlan Interface                          : Not Configured
Current WebSocket Started at            : 2023-09-01 22:36:26
Previous WebSocket Terminated at        : 2023-09-01 22:35:51
Web Proxy                               : NA
Proxy Username&password                 : NA, NA
Last Send Time                          : 2023-09-01 22:42:25
Websocket Write Stats                   : 3733 (1103455B)
Websocket Write Errors                  : 0
Websocket Write WM                      : 0B (0)
Websocket Read Stats                    : 0 (0B)
Websocket Read Pong Stats               : 2202 (26424B)

//
fc:7f:f1:cd:99:04# show iot radio-profile poc

Name                      :poc
References                :1
Instance                  :internal
Mode                      :ble
BLE Opmode                :scanning beaconing
BLE Console               :dynamic
BLE/Zigbee TxPower (dBm)  :0
Zigbee Mode               :coordinator
Zigbee Channel(s)         :auto
Zone                      :
fc:7f:f1:cd:99:04# show iot transportProfile test

Name                       :test
EndpointURL                :ws://192.168.40.249:6666/data
EndpointType               :telemetry-websocket
PayloadContent             :ibeacon,unclassified,sbeacon,managed-beacons,google,ability-smart-sensor,managed-tags,aruba-sensors,polestar,wiliot,mysphera,zf-tags,blyott
TransportInterval          :5
EndpointToken              :123456
EndpointID                 :ble_token
Username                   :
Password                   :
UUIDFilter                 :
CellSizeFilter             :
MovementFilter             :
AgeFilter                  :
AuthenticationURL          :
Authentication-mode        :none
UIDNamespaceFilter         :
URLFilter                  :
VendorFilter               :
RSSIReporting              :average
EnvironmentType            :office
CustomFadingFactor         :20
AccessID                   :
Client-secret              :
ProxyServer                :
ProxyPort                  :
ProxyUsername              :
ProxyPassword              :
VLAN                       :none
rtlsDestMAC                :
deviceCountOnly            :FALSE
bleDataForwarding          :TRUE
perFrameFiltering          :FALSE
ZSDFilter                  :
DataFilter                 :
Azure DPS id-scope         :
Azure DPS group-key        :
usbSerialDeviceTypeFilter  :
serviceUUIDFilter          :
companyIdentifierFilter    :947b
macOuiFilter               :
localNameFilter            :
zone                       :
fc:7f:f1:cd:99:04# show image version

Primary Partition                 :1
Primary Partition Build Time      :2023-08-20 18:25:47 UTC
Primary Partition Build Version   :8.10.0.8_87765 LSR (Digitally Signed - Production Build)
Backup Partition                  :0
Backup Partition Build Time       :2023-06-6 17:25:03 UTC
Backup Partition Build Version    :8.10.0.7_87023 LSR (Digitally Signed - Production Build)
AP Images Classes
-----------------
Class
-----
Ursa