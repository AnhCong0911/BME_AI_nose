# Tổng quan quá trình triển khai hệ thống
Hệ thống cần thiết kế có chức năng phân biệt khí Gas và không khí trong điều kiện phòng.
## Đối tượng, thiết bị
Điện thoại sử dụng hệ điều hành Android có tích hợp cảm biến BME68x.
## Cài đặt
1. Cài và chạy docker
2. Cài đặt mã nguồn Android
3. Cài đặt mã nguồn Non_hlos

Non-hlos là một thuật ngữ xác định bởi Qualcomm, tham chiếu đến thành phần Firmware.
Sau khi cài đặt, có đầy đủ mã nguồn để triển khai hệ thống.
## Kiến trúc hệ thống
Kiến trúc dưới đây bao gồm các thành phần phần cứng và phần mềm, có liên quan đến quá trình thiết kế hệ thống.  
![SO](/images/Architecture.png)  

- Sensor và Sensor hub  
Sensor thể hiện cho các cảm biến vật lý có trong thiết bị. Với hệ thống cần thiết kế, cảm biến được sử dụng là BME68x. Có hai phiên bản BME680 và BME688.  
Sensor hub là khối phần cứng quản lý các cảm biến và xử lý dữ liệu từ chúng.
- ADSP  
ADSP (Application Digital Signal Processor) là bộ xử lý chuyên dụng, thực hiện các tác vụ thời gian thực liên quan đến cảm biến và xử lý tín hiệu số, được tối ưu cho tiêu thụ công suất thấp.
- SSC  
SSC (Snapdragon Sensors Core) là một framework phần mềm do Qualcomm phát triển, để quản lý dữ liệu cảm biến trên nền tảng di động Snapdragon.
- Sensor driver và sensor instance  
Sensor Driver: Trình điều khiển là phần mềm, có nhiệm vụ quản lý cảm biến trên thiết bị và cung cấp giao diện chuẩn cho các phần mềm bậc cao để truy xuất dữ liệu từ cảm biến. Nó truyền thông với cảm biến bằng các chuẩn giao tiếp phần cứng như SPI, I2C.
Sensor instance: Đối tượng đại diện cho trạng thái của cảm biến khi hoạt động ở một cấu hình cụ thể. Được xác định trong trình điều khiển cảm biến.
- SEE  
SEE (Sensors Execution Environment) là một phần mềm quản lý cảm biến được phát triển bởi Qualcomm, thuộc SSC framework.
- Application Processor  
Bộ xử lý đa năng chính của thiết bị, có nhiệm vụ điều khiển hệ điều hành, khởi chạy ứng dụng và quản lý tài nguyên hệ thống.
- Android OS  
Android là hệ điều hành chạy trên thiết bị. HAL (Hardware Abstraction Layer) và Application là hai lớp quan trọng trong kiến trúc Android.  
Lớp HAL cung cấp các giao diện tiêu chuẩn giúp cho các phần mềm cấp cao hơn thao tác với phần cứng thiết bị.  
Lớp Application triển khai các ứng dụng giao diện tương tác với người dùng.

## Triển khai
### 1. Truy xuất dữ liệu từ cảm biến
### 2. Xây dựng mô hình tự dữ liệu
### 3. Xử lý dữ liệu, đưa vào mô hình
### 4. Phát triển ng dụng giao diện
