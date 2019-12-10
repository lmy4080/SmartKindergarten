# SmartKindergarten

<div>
  <img width="644" hspace="20" src="https://user-images.githubusercontent.com/42701193/70548212-80abe180-1bb5-11ea-8159-c9f8ed0f8438.JPG">
  <img width="300" height="300" hspace="20" src="https://user-images.githubusercontent.com/42701193/70548213-81447800-1bb5-11ea-8eeb-aea646084c26.JPG">
  <img width="300" height="300" hspace="20" src="https://user-images.githubusercontent.com/42701193/70548215-81447800-1bb5-11ea-8929-d89ddafd66fc.JPG">
  <img width="300" height="300" hspace="20" src="https://user-images.githubusercontent.com/42701193/70548216-81447800-1bb5-11ea-9a2c-f4469b91b390.JPG">
  <img width="300" height="300" hspace="20" src="https://user-images.githubusercontent.com/42701193/70548217-81dd0e80-1bb5-11ea-89cd-481b1984d4a8.JPG">
</div>

#### 프로젝트 설명(Project Description)

- 유치원 내부에 부착된 IoT 센서들을 사용자 모바일 어플리케이션을 통해 원격으로 제어 및 관리하는 시스템

#### 프로젝트 구성(Project Composition)

- Android app(Smart Kindergarten Controller), Lollipop v22
- Raspberry Pi(Smart Kindergarten/IoT Sensors), v2 B+ Model
  [link](https://github.com/lmy4080/SmartKindergarten)
- Cloud Mqtt Server [link](mqtt.eclipse.org)

#### 프로젝트 구성도(Project Architecture)

<div>
  <img width="600" src="https://user-images.githubusercontent.com/42701193/70446386-5b996f00-1ae0-11ea-81a2-cb266a171ce4.JPG">
</div>

#### SmartKindergarten 기능(SmartKindergarten Features)

 - 온도 센서를 사용한 유치원 내부 온도 데이터 저장 및 MQTT Broker Server로 전달
 - 습도 센서를 사용한 유치원 내부 습도 데이터 저장 및 MQTT Broker Server로 전달
 - 원격 컨트롤러 앱(SmartKindergartenController App) 명령에 따라 유치원 내부 전등을 점등 및 소등
 - 원격 컨트롤러 앱(SmartKindergartenController App) 명령에 따라 유치원 내부 커튼을 열기 및 닫기
 - 유치원 내부를 Live-Streaming으로 서버에 전송 / MQTT Broker Server로 Live-Streaming 서버 주소 전달
 - 거리/초음파 센서를 사용한 유치원 외부 주차장 상태 데이터를 MQTT Broker Server로 전달
 
#### SmartKindergarten IoT 구성(SmartKindergarten IoT Composition)

 - iot_device_1
   - LED Sensor, 3mm (2pcs)
   - Servo Motor sg90 (1pc)
 - iot_device_2
   - Temperature/Humidity Sensor (1pc)
   - Ultrasonic Sensor/HC-SR04 (1pc)
   - Raspberry Pi Camera Module 5MP (1pc)
   
#### SmartKindergarten IoT 개발 환경 (SmartKindergarten IoT Development Environment)

 - Hardware
   - Raspberry Pi B+ Model (2pcs)
 - OS
   - Raspbian, NOOBS v2.8.2
 
#### SmartKindergarten 활용 기술 스택(SmartKindergarten Used-Technical Stack Features)

 - Paho Mqtt Library(IoT Communication Protocol)
