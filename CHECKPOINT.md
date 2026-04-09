# Story2Video - Snapshot & Checkpoint (V1.2) - Final Professional Release

## 🕒 Thông tin cập nhật (Timestamp)
- **Repo URL mới**: `https://github.com/9dpi/Story2Video`
- **Trạng thái**: Hoàn thiện bộ tính năng chuyên nghiệp và xử lý triệt để các lỗi kỹ thuật từ phía Microsoft Edge TTS.

## 🛠 Những thay đổi cốt lõi (Core Updates)

### 1. Hệ thống Phụ đề Thông minh (Smart Subtitles)
- **[Feature] Max Words Control**: Hỗ trợ giới hạn số từ trên mỗi dòng (mặc định 10 từ). Giúp phụ đề gọn gàng, phù hợp cho video Reels/TikTok.
- **[Fix] Thuật toán Nội suy Thời gian (Temporal Interpolation)**: Do Microsoft không hỗ trợ WordBoundary cho tiếng Việt, mình đã viết code tự động chia nhỏ câu và tính toán mốc thời gian dựa trên độ dài âm thanh. Đảm bảo phụ đề ngắt đúng 10 từ nhưng vẫn khớp với giọng nói.
- **[UI] Positioning & Align**: Tích hợp tùy chọn căn lề (Trái/Giữa/Phải) và thanh điều chỉnh vị trí dọc (V-Position), giúp linh hoạt đặt chữ ở bất kỳ đâu trên khung hình.

### 2. Xử lý Video & Đồ họa
- **[Feature] Transparent Background**: Hỗ trợ xuất video nền trong suốt (không nền). Tự động chuyển đổi sang định dạng **WebM (Codec VP9)** để giữ kênh Alpha (phục vụ dựng phim chuyên nghiệp).
- **[Feature] Green Screen Shortcut**: Nút bấm nhanh để đặt nền xanh chuẩn (#00FF00), giúp tách nền dễ dàng trong CapCut hoặc Premiere.
- **[Feature] Live Preview**: Màn hình xem trước (Canvas) giờ đây tự động cập nhật ngay khi bạn thay đổi Cỡ chữ, Màu sắc, hoặc Vị trí mà không cần tạo lại âm thanh.

### 3. Tối ưu hóa Hệ thống & Sửa lỗi (DevOps)
- **[Fix] Triệt tiêu lỗi 500 (Internal Server Error)**: 
    - Loại bỏ tham số `Pitch="+0Hz"` lúc gửi lên vì gây xung đột với máy chủ Microsoft vùng VN.
    - Ép môi trường chạy sang chuẩn **UTF-8 (PYTHONUTF8=1)** để xử lý chính xác tuyệt đối các ký tự Tiếng Việt có dấu.
    - Sửa lỗi nạp chồng (Overlapping) sự kiện asyncio trên Windows.
- **[Script] Start.bat Nâng cao**: 
    - Tự động dọn dẹp Port 8001 bị treo khi tắt ứng dụng.
    - Tự động kiểm tra và cài đặt thư viện thiếu.

## 🚀 Hướng dấn sử dụng nhanh
1. Chạy **`Start.bat`** để khởi động máy chủ local.
2. Nhập văn bản Tiếng Việt, chọn giọng Hoài My.
3. Chỉnh **Max Words = 10** và **Align = Center**.
4. Bấm **Generate** và thưởng thức!

---
Dự án hiện đã đạt độ ổn định rất cao và có đầy đủ công cụ để sản xuất video content chuyên nghiệp.🎬
