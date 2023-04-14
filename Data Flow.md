# Luồng dữ liệu
Trình bày cách đẩy dữ liệu từ tầng Non-hlos lên tầng Ứng dụng.  
<img src="/images/Data_Flow.png" alt="Data_Flow" width="300" height="300" align="center">


Sử dụng các đường dữ liệu. Có 4 loại đường dữ liệu được xác định bởi nhà sản xuất, bao gồm:
- BME68x_TEMPERATURE (Temp_path)
- BME68x_HUMIDITY (Humi_path)
- BME68x_PRESSURE (Press_path)
- BME68x_GAS (Gas_path)
## Hiện tại
Dữ liệu được đẩy lên và nhận trên GinnoAir bao gồm:
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
