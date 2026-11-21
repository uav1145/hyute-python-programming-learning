# QA REPORT — HYUTE PYTHON KỸ THUẬT (v1.0)

**Ngày biên tập:** 20/11/2026. **Đối tượng:** sinh viên kỹ thuật, ưu tiên Điện lạnh & ĐHKK và Công nghệ ô tô. **Nguồn:** 15 tài liệu người dùng cung cấp và tài liệu API chính thức.

## Phạm vi nghiệm thu tự động

- 5 mô-đun, **20 bài** theo đúng đề xuất v0.1; 24 trang HTML (gồm trang chủ, thuật ngữ, hướng dẫn và nguồn).
- Mỗi bài có mục tiêu đo được, bài toán kỹ thuật, I/O–đơn vị, giả thiết, lý thuyết, **mã giả và SVG lưu đồ riêng**, code Python, công cụ tương tác, ≥4 ca kiểm thử, hai bài vận dụng chuyên ngành, trắc nghiệm 3×4 đáp án kèm giải thích và rubric.
- Hai bộ dữ liệu CSV **tự tạo**; mã nguồn Python .py tải được. Không sao chép tài liệu nguồn trong gói ZIP.
- Mọi script Python được thực thi trên Python **3.13.5**, các package cài trong môi trường thử nghiệm: **numpy 2.3.5, pandas 2.2.3, matplotlib 3.10.8, scipy 1.17.0**.

## Double check theo bài

**Lượt 1:** `ast.parse` và `compile` → chạy tệp bằng Python thật → kiểm tra đầu ra với giá trị kỳ vọng độc lập trước khi chuyển sang bài tiếp theo.

**Lượt 2:** kiểm tra bất biến/tính toán độc lập 20/20; DOM/Chromium 20/20 với 3/3 trắc nghiệm, thao tác mã giả, mô hình JS, nút ghi chép và tiến độ, hiển thị SVG; kiểm tra cú pháp JS và đường dẫn nội bộ.

| Bài | Kiểm tra Python + đầu ra | Kiểm tra toán độc lập | Tương tác Chromium | Kết quả chương trình mẫu |
|---:|---|---|---|---|
| 01 | PASS | PASS | PASS | Điện năng: 4.50 kWh |
| 02 | PASS | PASS | PASS | P = 60 W; E = 120 Wh = 0.120 kWh |
| 03 | PASS | PASS | PASS | CANH BAO |
| 04 | PASS | PASS | PASS | TB = 27.875 °C; Max = 31.0 °C; vuot = 1 |
| 05 | PASS | PASS | PASS | E = 4.50 kWh |
| 06 | PASS | PASS | PASS | 2026-11-20T08:00:00 25.6 °C OK |
| 07 | PASS | PASS | PASS | Vi tri vuot: [1, 3]; Cau hinh: (20.0, 30.0) |
| 08 | PASS | PASS | PASS | So cam bien: 2; So canh bao: 1; S3: CHUA CO |
| 09 | PASS | PASS | PASS | {'so_hop_le': 7, 'so_loi': 1} |
| 10 | PASS | PASS | PASS | S1 True; S2 False |
| 11 | PASS | PASS | PASS | K: [293.15, 298.15, 303.15]; x: [2.0, 1.0]; //Ax-b// = 0.00e+00 |
| 12 | PASS | PASS | PASS | Goc=8, hop le=7, loai=1; hour; 2026-11-20 08:00:00    27.00; 2026-11-20 09:00:00    28.73 |
| 13 | PASS | PASS | PASS | So diem: 7 / Da luu: bai13_do_thi.png |
| 14 | PASS | PASS | PASS | q* = 20.000 (don vi quy uoc); Phan du = 0.000e+00 Pa |
| 15 | PASS | PASS | PASS | a=99.80 °C/V, b=-49.76 °C; MAE=0.225 °C |
| 16 | PASS | PASS | PASS | E = 3.500 kWh; T(2 h) Euler = 23.164 °C |
| 17 | PASS | PASS | PASS | Sai lech lon nhat = 0.1892 °C |
| 18 | PASS | PASS | PASS | Luu: 2 / Loi: 1 |
| 19 | PASS | PASS | PASS | Dien lanh: n=7, Tmax=31.2 °C; O to: n=6, Umin=12.21 V |
| 20 | PASS | PASS | PASS | {'so_hop_le': 7, 'so_loi': 1, 'tb_c': 27.743, 'so_vuot_30_c': 1} |

## Kiểm tra tệp và tính nhất quán

- 24 HTML: không phát hiện liên kết tệp nội bộ bị thiếu hoặc ID trùng trong phép rà soát.
- 20 lưu đồ SVG và 20 tệp DOT nguồn; cú pháp hợp lệ, SVG hiển thị trong Chromium (nạp từ dữ liệu kiểm thử).
- `app.js`: đạt `node --check`; mỗi bài đạt kiểm tra phản hồi trắc nghiệm bằng bộ đáp án đã cấu hình.
- Đồ thị đầu ra `output/bai13_do_thi.png` và `output/bai17_mo_phong.png` đã được tạo bằng chương trình mẫu.
- Dữ liệu có chú thích là **mô phỏng**; giá trị các ngưỡng/trường hợp đại diện không phải ngưỡng bảo vệ thiết bị thật.

## Giới hạn và bước kiểm định còn thiếu

1. Môi trường hiện tại **chặn Chromium điều hướng tới HTTP nội bộ và `file://`**. Kiểm thử tương tác được tiến hành bằng cách nạp trực tiếp DOM/HTML/CSS/JS vào Chromium, giả lập localStorage và nạp SVG dạng data URI; không chứng minh luồng truy cập GitHub Pages đã chạy end-to-end. Liên kết nội bộ được kiểm chứng độc lập bằng đường dẫn tệp.
2. Chưa thử nghiệm trên toàn bộ môi trường Windows 11/Colab của sinh viên, chưa đánh giá tải nhận thức và mức độ đạt CLO trên lớp thật.
3. Thời lượng và CLO trong khóa học là **đề xuất**, chưa đối chiếu với đề cương học phần Lập trình Python kỹ thuật chính thức vì tài liệu đó chưa được cung cấp.
4. Dữ liệu mô phỏng, mô hình nhiệt và các ngưỡng được dùng để giảng dạy thuật toán; không dùng trực tiếp cho thiết kế kỹ thuật, chẩn đoán hay vận hành an toàn.
5. Website tĩnh **không thực thi Python trong trình duyệt**, **không lưu điểm sinh viên tập trung**; các hoạt động JS chỉ hỗ trợ hình thành và kiểm tra trực giác.
6. Phương thức cài dependencies theo `requirements.txt` chỉ được kiểm tra trong môi trường hiện tại; các phiên bản khác cần kiểm thử tương thích theo cấu hình của phòng máy.

**Trạng thái phát hành:** Ứng viên nghiệm thu học liệu (release candidate). Có thể triển khai thử nghiệm có kiểm soát; chưa chứng nhận READY FOR PUBLICATION khi chưa có nghiệm thu sư phạm và đối chiếu đề cương chính thức.
