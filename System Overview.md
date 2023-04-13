# Tổng quan hệ thống
Hoạt động tổng quan của hệ thống như hình duới đây:  
![SO](/images/System_Overview.png)

Hệ thống giao tiếp với cảm biến bằng giao thức SPI, để truy xuất dữ liệu.  
Kiến trúc hệ thống bao gồm các lớp cơ bản trong kiến trúc Android và lớp Non-hlos.  
Non-hlos là một thuật ngữ xác định bởi Qualcomm, tham chiếu đến thành phần Firmware. Trong non-hlos, có nhiều khối xử lý, khối xử lý các tác vụ liên quan đến cảm biến là ADSP.  
ADSP là viết tắt của Application Digital Signal Processor, là một thành phần trong chipset của Qualcomm. ADSP là bộ xử lý chuyên dụng được thiết kế để xử lý dữ liệu số, chẳng hạn như dữ liệu thoại và âm thanh, theo cách tiết kiệm năng lượng và hiệu quả.
