# Luồng dữ liệu
Luồng đẩy dữ liệu từ cảm biến vật lý lên lớp Ứng dụng trên thiết bị dựa trên [kiến trúc hệ thống](System Deployment Overview.md) đã trình bày.

## Sơ đồ luồng dữ liệu
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
Có 4 loại dữ liệu được xác định bởi nhà sản xuất, bao gồm:
- BME68x_TEMPERATURE
- BME68x_HUMIDITY
- BME68x_PRESSURE
- BME68x_GAS
#### Sensor Instance và SEE
SEE chứa một tập các framework để thao tác với cảm biến. Hàm ```notify_event()``` được gọi để thông báo cho SEE rằng có sự thay đổi dữ liệu trên cảm biến, và SEE nhận dữ liệu mới.
#### SEE và HAL  
Dữ liệu trên SEE được gửi đến client thông qua client API. Trong hệ thống thiết kế, client là HAL. HAL truy xuất dữ liệu từ SEE thông qua giao diện gói tin của client API.
#### HAL và App
Từ HAL, các ứng dụng có thể lấy dữ liệu cảm biến thông qua SensorManager cung cấp bởi framework API (API hệ thống). 


Cảm biến BME68x thu thập thông số môi trường, lưu dữ liệu vào bộ nhớ. Sensor Driver đọc bộ nhớ của cảm biến, tiền xử lý dữ liệu và đẩy lên thông qua Sensor API. SEE nhận và xử lý dữ liệu, sau đó đẩy dữ liệu lên cho HAL. Lớp ứng dụng lấy dữ liệu từ HAL để hiện thị lên giao diện.


## Hiện tại
Dữ liệu được đẩy lên và nhận trên ứng dụng thông qua **Sensor Manager** bao gồm:
- Temp - Nhiệt độ (Temp_path)
- Humi - Độ ẩm (Humi_path)
- IAQ average- Chất lượng không khí trung bình (Press_path)
- IAQ - Chất lượng không khí (Gas_path)
### Đối với IAQ
Thông số IAQ được lưu vào file dạng JSON, có đường dẫn "/mnt/vendor/persist/sensors/iaqdata.json" trong điện thoại.

Cách đọc file như sau:
1. Kết nối máy tính với điện thoại thông qua dây USB
2. Mở Terminal trên máy tính. 
Gõ lệnh:
```C
adb shell
cat /mnt/vendor/persist/sensors/iaqdata.json
```
### Đối với Temp, Humi và IAQ average
Các thông số này được đẩy trực tiếp lên từ tầng Non-hlos thông qua các đường dữ liệu tương ứng như trên.
## Hướng đề xuất
Dữ liệu mong muốn thu được bao gồm:
- Temp - Nhiệt độ
- Humi - Độ ẩm
- Press - Áp suất
- Gas_res - Trở kháng khí <br/>

Các dữ liệu được lưu vào file và có thể được truy xuất bởi mô hình AI để thực hiện chức năng phân biệt mùi.
