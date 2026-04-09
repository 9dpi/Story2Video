# Story2Video - Snapshot & Checkpoint (V1.1)

## 🕒 Thông tin cập nhật (Timestamp)
- **Repo URL gốc**: `https://github.com/dvchd/story2video`
- **Repo URL mới**: `https://github.com/9dpi/Story2Video`
- **Trạng thái**: Hoàn thiện phiên bản Offline (Local) & xử lý dứt điểm các lỗi giao thức của Server Edge-TTS.

## 🛠 Những thay đổi cốt lõi (Core Updates)

### 1. Khắc phục triệt để lỗi Back-end (`main.py`)
- **[Fix] Microsoft Edge TTS SSML Parser Bug**: Đã vá lỗ hổng đánh sập websocket (`NoAudioReceived`, trả về HTTP 500) khi người dùng truyền văn bản chứa mã lập trình hoặc ký tự toán học (`<`, `>`, `&`). Giải pháp: nhúng `xml.sax.saxutils.escape()` để cô lập (sanitize) nội dung an toàn trước khi đóng gói gửi sang máy chủ SSML của Microsoft.
- **[Optimize] Cơ chế Smart Retry (Vượt rào Rate-Limit)**: Edge-TTS thường xuyên bị rớt mạng ngẫu nhiên đối với một số lớp mạng khu vực. Thiết lập thêm vòng lặp try-catch 3 lớp (có chờ Delay) giúp hệ thống tự động gõ cửa lại nếu bị ngắt kết nối giữa chừng.
- **[Debug] Tracker Truy vết linh hoạt**: Cấu hình khối lệnh bắt Exception toàn cục, đổ chi tiết Traceback trực tiếp qua API lên Error Modal của ứng dụng trình duyệt giúp dễ dàng nắm bắt lỗi.

### 2. Tiện ích vận hành Local (Start.bat)
- **Tạo hệ thống `Start.bat` độc quyền cho môi trường Windows**:
  - Không cần tương tác dòng lệnh thủ công.
  - Tích hợp kiểm tra phiên bản Python 3.11+.
  - Tự động bắt diện các gói thư viện chưa cài (`pip install FastAPI/uvicorn...` ngầm).
  - Tự động kích hoạt Localhost tại 8001 và điều hướng trình duyệt sau 2 giây.
  - Xóa dọn tiền trình an toàn: Triệt tiêu rác PID cổng 8001 và các process python.exe bị treo sau khi thoát CMD. (Có bổ sung cấu hình mã hóa chuẩn Ascii để tránh lỗi Unicode Parser của CMD cũ).

### 3. Độc lập hoá phân hệ GitHub Pages
- **Cấu hình Repo nhánh cho Cloud UI**: Chiết xuất giao diện front-end nguyên nguyên bản ra thành trang `index.html` độc lập cho https://9dpi.github.io/Story2Video/. 
- Qua đó, kho lưu trữ Github chứa 2 phần mềm biệt lập:
   1. Trang Client-side Renderer UI (thuần tuý hoạt động trên mọi host tĩnh).
   2. Máy chủ uvicorn Python hỗ trợ sinh Audio.

## 🚀 Hướng đi tiếp theo (Roadmap)
1. **Đưa Python Server lên mây**: Nếu muốn Github Pages phát huy tác dụng thực tiễn, phân vùng Server File (`main.py`) cần được cấu hình Dockerized và Deploy lên các dịch vụ Platform-as-a-Service (Render.com, Hugging Face Spaces, Railway, v.v.).
2. **Tuỳ biến Giao diện (Theming)**: Tuỳ chỉnh phong cách Dark/Light hoặc mở rộng bố cục Bootstrap.
3. **Mở rộng API Endpoint**: Bổ sung kho giọng đọc từ bên thứ ba (Google Cloud / OpenAI) bên cạnh TTS miễn phí của Microsoft Edge.
