# Thị giác máy tính - Nhận diện cảm xúc khuôn mặt sử dụng CNN 
Đây là bài tập lớn môn Thị Giác Máy Tính

Đề tài yêu cầu Xây dựng ứng dụng nhận dạng cảm xúc của con người sử dụng mạng nơ-ron tích chập CNN

Mô hình nhận dạng sẽ sử dụng bộ dữ liệu FER-2013, bộ dữ liệu này cung cấp 7 nhãn là 7 cảm xúc trên khuôn mặt con người. Tuy nhiên, với đề tài này, mình đã thay đổi dataset chỉ sử dụng 5 nhãn là (angry, happy, neutral, sad, surprise). Lý do là bởi :
  + disgust có lượng dữ liệu quá ít so với các tập khác
  + fear dễ nhầm lẫn với angry ngay cả khi là người bình thường tự đánh giá
Do vậy nên mình đã quyết định không sử dụng 2 nhãn này

Dataset ban đầu chứa 32.398 ảnh, trong đó có 28.709 cho bộ train và 3.589 cho bộ test. Sau khi xóa 2 nhãn không dùng đến, dataset còn 30.219 ảnh ( 24.176 train + 6043 test). Mình xây dựng mô hình CNN với 8 lớp conv, tuy nhiên tỷ lệ chính xác sau khi đào tạo với 100 epoch chỉ khoảng 74-75%, đặc biệt các cảm xúc angry - happy, neutral - sad hay bị nhận dạng nhầm. 

Sau khi xem xét kỹ lại ảnh trong dataset, mình phát hiện ra có rất nhiều ảnh bị đánh nhãn sai và nhiều ảnh lỗi đen không hiển thị được. Do đó mình đã tiến hành loại bỏ 1 phần ảnh nhiễu và bổ sung thêm các tự thu thập từ internet. Ảnh tự thu thập sẽ cần xử lý chuyển sang ảnh xám, rezise thành 48x48 để phù hợp với dataset. 

Đào tạo mô hình với epoch=200, sử dụng Early_Stopping với cài đặt là nếu giá trị val_accuracy không tăng sau 20 epoch liên tục thì dừng huấn luyện. Quá trình huấn luyện đã dừng lại tại Epoch 75 và khôi phục lại trọng số của Epoch 55. 

Ứng dụng được viết bằng ngôn ngữ python sử dụng phương pháp Haar-Cascade của OpenCV để phát hiện khuôn mặt người, load file .h5(chứa trọng số mô hình) và file .json(chứa kiến trúc mô hình) vào chương trình. Hệ thống có thể nhận dạng thành công 5 cảm xúc đề ra.
# Demo

# Technology

# Reference
