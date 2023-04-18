# Luồng dữ liệu
Luồng đẩy dữ liệu từ cảm biến vật lý lên lớp Ứng dụng trên thiết bị dựa trên [kiến trúc hệ thống](System Deployment Overview.md) đã trình bày.

## I. Sơ đồ luồng dữ liệu
Góc nhìn tổng quan của luồng dữ liệu như sau.
![DF](/images/Push_Data_Flow.png)

### 1. Các thành phần
- BME68x: Thiết bị cảm biến vật lý, thuộc Sensor hub. Thực hiện thu thập các thông số trạng thái của môi trường, tạo thành các mẫu dữ liệu, và lưu trữ trong bộ nhớ.
- Sensor Instance: Đại diện cho cảm biến BME68x khi hoạt động ở chế độ cấu hình cụ thể, được cài đặt bởi người sử dụng.
- SEE: Cung cấp các khung hướng sự kiện, các giao diện, API đơn giản, để thao tác với cảm biến.
- Sensor API: Các API cho phép SEE thao tác với cảm biến và Sensor Instance để cài đặt và truy xuất dữ liệu.
- Client API: Các API cho phép client truy xuất dữ liệu từ SEE.
- HAL: Quản lý sự kiện và các cảm biến khả dụng trên thiết bị. Cho phép các ứng dụng lớp trên thao tác với phần cứng khả dụng thông giao diện chuẩn.
- App: Các ứng dụng sử dụng dữ liệu của cảm biến để hiện thị lên giao diện người dùng và thực hiện các tác vụ xử lý tính toán khác.
### 2. Tương tác
#### BME68x và Sensor Instance
Sensor Instance truy xuất dữ liệu từ bộ nhớ cảm biến BME68x bằng chuẩn giao tiếp phần cứng SPI; thực hiện hiệu chỉnh, xử lý dữ liệu thô; đẩy dữ liệu lên theo loại tương ứng.  
Có 4 loại dữ liệu được định nghĩa bởi nhà sản xuất, bao gồm:
- BME68x_TEMPERATURE
- BME68x_HUMIDITY
- BME68x_PRESSURE
- BME68x_GAS

Các loại dữ liệu này dùng để xác định kiểu cảm biến trong **Sensor Manager**.
#### Sensor Instance và SEE
SEE chứa một tập các framework để thao tác với cảm biến. Hàm ```notify_event()``` được gọi để thông báo cho SEE rằng có sự thay đổi dữ liệu trên cảm biến, và SEE nhận dữ liệu mới.
#### SEE và HAL  
Dữ liệu trên SEE được gửi đến client thông qua client API. Trong hệ thống thiết kế, client là HAL. HAL truy xuất dữ liệu từ SEE thông qua giao diện gói tin của client API.
#### HAL và App
Từ HAL, các ứng dụng có thể lấy dữ liệu cảm biến thông qua **Sensor Manager** cung cấp bởi framework API (API hệ thống).
## II. Hiện tại
Dữ liệu được hiệu chỉnh bởi Sensor Instance trong trình điều khiển, và nhận trên ứng dụng thông qua **Sensor Manager** ,bao gồm:
- Temp - Nhiệt độ
- Humi - Độ ẩm
- IAQ average- Chất lượng không khí trung bình hiện tại
- IAQ - Chất lượng không khí
### Đối với IAQ average
Ngoài việc đẩy lên theo luồng dữ liệu, thông số IAQ average được trình điều khiển cảm biến lưu vào một vùng nhớ dữ liệu cố định, tồn tại qua các lần khởi động lại. Thể hiện dưới dạng file JSON, có đường dẫn ```/mnt/vendor/persist/sensors/iaqdata.json``` trong điện thoại.

Cách đọc file như sau:
1. Kết nối máy tính với điện thoại thông qua dây USB
2. Mở Terminal trên máy tính. 
Gõ lệnh:
```C
adb shell
cat /mnt/vendor/persist/sensors/iaqdata.json
```
### Đối với Temp, Humi và IAQ
Các thông số này được đẩy lên theo luồng dữ liệu được trình bày như trên.
## III. Hướng đề xuất
Dữ liệu mong muốn thu được bao gồm:
- Temp - Nhiệt độ
- Humi - Độ ẩm
- Press - Áp suất
- Gas_res - Trở kháng khí <br/>

Các dữ liệu được lưu vào file và có thể được truy xuất bởi mô hình AI để thực hiện chức năng phân biệt mùi.
