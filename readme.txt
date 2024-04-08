Mô tả:
    1. Đồ án yêu cầu các thư viện sau:
        easyocr
        streamlit
        ipython
        Pillow
        pandas
        mathplotlib
        scikit-learn
    2. Trong thư mục scripts, file streamlit_app.py là phần hiển thị ứng dụng web với home_page.py là trang home 
    và dataframe.py là trang database, file Extraction.py chứa hàm extract_data nhằm mục đích trích xuất thông tin 
    và phân loại trường thông tin từ ảnh được upload trên homepage
    3. File data.json được sử dụng để lưu các thông tin đã lưu sau khi trích xuất
    4. Thư mục sample_cards chứa các mẫu business card với format phù hợp nhất với đồ án
Hướng dẫn thực thi:
    1. Tại terminal thư mục "Scripts", dùng lệnh "streamlit run streamlit_app.py" 
    hoặc thực thi file "streamlit_app.py" để có một lệnh khởi chạy của streamlit (streamlit run part\to\folder\Scripts\streamlit_app.py)
    sử dụng lệnh như ví dụ trên để chạy trên terminal
    2. Các bước thực hiện như upload hình, trích xuất, lưu trữ sé là các lựa chọn trên app tại homepage
    3. Ở database page:
        Thao tác xem được thực hiện bằng nút "Press"
        Thao tác xóa được thực hiện bằng cách chọn số trong bảng chọn, sau đó bấm nút "Delete"
