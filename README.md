*Web blog PTIT

Ý tưởng tạo web blog cơ bản cho PTITer sử dụng django. Trang web cho người dùng có thể đăng bài(hình ảnh, tiêu đề, bài viết), bình luận các bài viết, đồng thời có thể xóa các bài viết, bình luận của mình, xem thông tin, bài viết của các blogger khác, ngoài ra người dùng có thể thay đổi ảnh đại diện và tổng các bài viết cảu mình. Người quản trị trang web sẽ có các tính năng bổ sung như xóa tất cả các bài viết, bình luận và xóa cả người dùng.

Trang web sử dụng:

Python 3.10.0

django 3.2.9

Pillow 8.4.0

*Chạy web

1. Thiết lập môi trường phát triển Python. Cài framework django bằng câu lệnh

    pip install django
    
sau đó cài Pillow bằng câu lệnh(nếu chưa có)

    pip install pillow


2. Khi đã thiết lập môi trường:


    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser # Co the khong can (admin co san username: Admin1 password:admin1)
    python manage.py runserver

3. Mở trình duyệt tới localhost:8000/admin/ (http://127.0.0.1:8000/admin/) để mở trang web quản trị

4. Tạo một vài đối tượng thử nghiệm của mỗi loại.

5. Mở tab tới localhost:8000 (http://127.0.0.1:8000/admin/ ) để xem trang web chính
