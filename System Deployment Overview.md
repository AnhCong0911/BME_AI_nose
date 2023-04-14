# Tổng quan quá trình triển khai hệ thống
Hệ thống cần thiết kế có chức năng phân biệt khí Gas và không khí trong điều kiện phòng.
## Cài đặt
1. Cài và chạy docker file
2. Build Android source
3. Build HL_NONHL source

Sau khi cài đặt, có đầy đủ mã nguồn để triển khai hệ thống.
## Kiến trúc hệ thống
Kiến trúc tổng quan của hệ thống như hình duới đây:  
![SO](/images/System_Overview.png)  
Hệ thống giao tiếp với cảm biến bằng giao thức SPI, để truy xuất dữ liệu.  
Kiến trúc hệ thống bao gồm các lớp cơ bản trong kiến trúc Android và lớp Non-hlos.  
Non-hlos là một thuật ngữ xác định bởi Qualcomm, tham chiếu đến thành phần Firmware. Trong non-hlos, có nhiều khối xử lý, khối xử lý các tác vụ liên quan đến cảm biến là ADSP.  
ADSP là viết tắt của Application Digital Signal Processor, là một thành phần trong chipset của Qualcomm. ADSP là bộ xử lý chuyên dụng được thiết kế để xử lý dữ liệu số, chẳng hạn như dữ liệu thoại và âm thanh, theo cách tiết kiệm năng lượng và hiệu quả.
## Triển khai
### 1. Truy xuất dữ liệu từ cảm biến
### 2. Xây dựng mô hình tự dự liệu
### 3. Xử lý du liệu, đưa và mô hình
### 4. Phá triển Ứng dung giao diện
