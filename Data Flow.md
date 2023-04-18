# Luồng dữ liệu
Trình bày luồng đẩy dữ liệu từ cảm biến vật lý lên lớp Ứng dụng trên thiết bị.

## Sơ đồ luồng dữ liệu
Phần này trình bày cái nhìn tổng quan để hiểu luồng dữ liệu.
![DF](/images/Push_Data_Flow.png)

### 1. Các thành phần:
- BME68x: Thiết bị cảm biến vật lý, thuộc khối Sensor hub. Đây là cảm biến môi trường thực hiện thu thập và lưu trữ dữ liệu vào bộ nhớ.
- Sensor Instance: Đối tượng biểu diễn cho cảm biến hoạt động ở cấu hình cụ thể, được thể hiện trong trình điều khiển cảm biến. Sensor Driver: Trình điều khiển là phần mềm, có nhiệm vụ quản lý cảm biến trên thiết bị và cung cấp giao diện chuẩn cho các phần mềm bậc cao để truy xuất dữ liệu từ cảm biến. Nó truyền thông với cảm biến bằng các chuẩn giao tiếp phần cứng như SPI, I2C.
- SEE: Sensors Execution Environment, là một phần mềm quản lý cảm biến của Qualcomm, thuộc SSC framework. Nó cung cấp các khung hướng sự kiện, các giao diện, API đơn giản, để thao tác với cảm biến.
- Sensor/Client API: Các API được định nghĩa bởi nhà sản xuất cảm biến, Qualcomm.
- Android HAL: Lớp cung cấp giao diện cho các lớp trên, để thực hiện quản lý và điều khiển cảm biến.
- Android App: Các ứng dụng sử dụng các thông số của cảm biến để hiện thị lên giao diện người dùng.
- HAL: Hardware Abstraction Layer, lớp trừu tượng phần cứng. Một lớp quan trọng trong kiến trúc của hệ điều hành Android. HAL cung cấp giao diện tiêu chuẩn cho lớp trên, để thực hiện các chức năng của phần cứng cụ thể.
- App: Application Layer, lớp ứng dụng. Các ứng dụng thể hiện các thông số của cảm biến lên giao diện người dùng.
### 2. Tương tác
Sensor Instance truy xuất dữ liệu từ bộ nhớ cảm biến BME68x bằng chuẩn giao tiếp phần cứng SPI; thực hiện hiệu chỉnh, xử lý dữ liệu thô; đẩy dữ liệu lên theo loại tương ứng.  
Có 4 loại dữ liệu được xác định bởi nhà sản xuất, bao gồm:
- BME68x_TEMPERATURE (Temp_path)
- BME68x_HUMIDITY (Humi_path)
- BME68x_PRESSURE (Press_path)
- BME68x_GAS (Gas_path)

SEE chứa một tập các framework để thao tác với cảm biến. Hàm ```notify_event()``` được gọi để thông báo cho SEE rằng có sự thay đổi dữ liệu trên cảm biến, và SEE nhận dữ liệu mới.  
Dữ liệu trên SEE được gửi đến các lớp trên thông qua client API. Trong hệ thống thiết kế, lớp trên của SEE là HAL trong hệ điều hành Android. Lớp trên truy xuất dữ liệu trong SEE thông qua giao diện gói tin của client API.

Từ HAL, các ứng dụng trong hệ điều hành Android có thể lấy dữ liệu cảm biến thông qua SensorManager cung cấp bởi framework API (API hệ thống). 


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
