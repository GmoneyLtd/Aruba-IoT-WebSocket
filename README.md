### Aruba IoT WebSocket
#### Aruba IoT Telemetry Southbound Websocket interface and northbound Websocket interface
- 重新基于python3环境测试，protoc版本与pip protobuf版本一致，升级其他相关依赖环境，删除未使用依赖
- 升级protobuf版本至ArubaOS 8.10(LSR)
- 更新message中的timestamp格式为日期格式
- IoT的南向接口暂未有实例测试，该仓库不包含南向接口的相关测试及代码