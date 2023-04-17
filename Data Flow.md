# Luồng dữ liệu
Trình bày luồng đẩy dữ liệu từ cảm biến vật lý lên lớp Ứng dụng trên thiết bị.
## Tổng quan
Sơ đồ khối tổng quan như sau:  
![Block_diagram](/images/Data_Flow_Block_diagram_Bottom_to_Top.png)

Các thành phần chính bao gồm:
- Physical Sensor: Thiết bị cảm biến vật lý. Ở đây, là BME68x, cảm biến môi trường.
- Sensor Driver: Trình điều khiển là phần mềm, có nhiệm vụ quản lý cảm biến trên thiết bị và cung cấp giao diện chuẩn cho các phần mềm bậc cao để truy xuất dữ liệu từ cảm biến. Nó truyền thông với cảm biến bằng các chuẩn giao tiếp phần cứng như SPI, I2C.
- SEE: Viết tắt của Sensors Execution Environment. Là một phần mềm quản lý cảm biến của Qualcomm. Nó cung cấp các framework hướng sự kiện, các giao diện, API đơn giản, để thao tác với cảm biến.
- Sensor/Client API: Các API được định nghĩa bởi nhà sản xuất cảm biến, Qualcomm.
- HAL: Hardware Abstraction Layer, lớp trừu tượng phần cứng. Một lớp quan trọng trong kiến trúc của hệ điều hành Android. HAL cung cấp giao diện tiêu chuẩn cho lớp trên, để thực hiện các chức năng của phần cứng cụ thể.
- App: Application Layer, lớp ứng dụng. Các ứng dụng thể hiện các thông số của cảm biến lên giao diện người dùng.

Cảm biến BME68x thu thập thông số môi trường, lưu dữ liệu vào bộ nhớ. Sensor Driver đọc bộ nhớ của cảm biến, tiền xử lý dữ liệu và đẩy lên thông qua Sensor API. SEE nhận và xử lý dữ liệu, sau đó đẩy dữ liệu lên cho HAL. Lớp ứng dụng lấy dữ liệu từ HAL để hiện thị lên giao diện.

Tầng Non-hlos thực hiện truy xuất và xử lý dữ liệu từ cảm biến. Tầng Ứng dụng thực hiện hiển thị dữ liệu lên giao diện. Có 4 loại đường dữ liệu được xác định bởi nhà sản xuất, bao gồm:
- BME68x_TEMPERATURE (Temp_path)
- BME68x_HUMIDITY (Humi_path)
- BME68x_PRESSURE (Press_path)
- BME68x_GAS (Gas_path)
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
## Mong muốn triển khai
Dữ liệu mong muốn thu được bao gồm:
- Temp - Nhiệt độ
- Humi - Độ ẩm
- Press - Áp suất
- Gas_res - Trở kháng khí <br/>

Các dữ liệu được lưu vào file và có thể được truy xuất bởi mô hình AI để thực hiện chức năng phân biệt mùi.
