# Tổng quan quá trình triển khai hệ thống
Hệ thống cần thiết kế có chức năng phân biệt khí Gas và không khí trong điều kiện phòng.
## Đối tượng, thiết bị
Điện thoại sử dụng hệ điều hành Android có tích hợp cảm biến BME68x.
## Cài đặt
1. Cài và chạy docker file
2. Build Android source
3. Build HL_NONHL source

Sau khi cài đặt, có đầy đủ mã nguồn để triển khai hệ thống.
## Kiến trúc hệ thống
Kiến trúc dưới đây bao gồm các thành phần phần cứng và phần mềm, có liên quan đến quá trình thiết kế hệ thống.  
![SO](/images/Architecture.png)  

### 1. Sensor và Sensor hub
Sensor thể hiện cho các cảm biến vật lý có trong thiết bị. Với hệ thống cần thiết kế, cảm biến được sử dụng là BME68x. Có hai phiên bản BME680 và BME688.  
Sensor hub là khối quản lý các cảm biến và xử lý dữ liệu từ chúng.
### 2. ADSP 
ADSP (Application Digital Signal Processor) là bộ xử lý chuyên dụng, thực hiện các tách vụ thời gian thực liên quan đến cảm biến và xử lý tín hiệu số, được tối ưu cho tiêu thụ công suất thấp.
### 3. SSC
SSC (Snapdragon Sensors Core) là một framework phần mềm do Qualcomm phát triển, để quản lý dữ liệu cảm biến trên nền tảng di động Snapdragon.
### 4. Sensor driver và sensor instance
Sensor driver là trình điều khiển có nhiệm vụ quản lý các cảm biến trên thiết bị và cung cấp giao diện cho phần mềm cấp cao hơn để truy cập dữ liệu từ cảm biến.
Sensor instance: Thể hiện cho trạng thái của cảm biến khi hoạt động ở một cấu hình cụ thể.
### 5. SEE
SEE (Sensors Execution Environment) là một phần mềm quản lý cảm biến được phát triển bởi Qualcomm.
### 6. Application Processor
Bộ xử lý đa năng chính của thiết bị, có nhiệm vụ điều khiển hệ điều hành, khởi chạy ứng dụng và quản lý tài nguyên hệ thống.
### 7. Android OS
Android là hệ điều hành chạy trên thiết bị. Trong kiến trúc Android, HAL (Hardware Abstraction Layer) và Application là hai lớp quan trọng. 

Hệ thống giao tiếp với cảm biến bằng giao thức SPI, để truy xuất dữ liệu.  
Kiến trúc hệ thống bao gồm các lớp cơ bản trong kiến trúc Android và lớp Non-hlos.  
Non-hlos là một thuật ngữ xác định bởi Qualcomm, tham chiếu đến thành phần Firmware. Trong non-hlos, có nhiều khối xử lý, khối xử lý các tác vụ liên quan đến cảm biến là ADSP.  
ADSP là viết tắt của Application Digital Signal Processor, là một thành phần trong chipset của Qualcomm. ADSP là bộ xử lý chuyên dụng được thiết kế để xử lý dữ liệu số, chẳng hạn như dữ liệu thoại và âm thanh, theo cách tiết kiệm năng lượng và hiệu quả.
## Triển khai
### 1. Truy xuất dữ liệu từ cảm biến
### 2. Xây dựng mô hình tự dự liệu
### 3. Xử lý du liệu, đưa và mô hình
### 4. Phá triển Ứng dung giao diện
