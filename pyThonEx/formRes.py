from curses import window
import tkinter as tk

def register():
    username = entry_username.get() # type: ignore
    password = entry_password.get() # type: ignore
    confirm_password = entry_confirm_password.get()
    email = entry_email.get()

    # Kiểm tra tính hợp lệ của dữ liệu
    if password != confirm_password:
        label_result["text"] = "Mật khẩu không khớp!" # type: ignore
        return

    # Ở đây bạn sẽ thực hiện lưu thông tin đăng ký vào cơ sở dữ liệu
    # Ví dụ: sử dụng thư viện SQLite để tạo một bảng người dùng và lưu thông tin vào đó
    # ... (code kết nối và lưu dữ liệu vào cơ sở dữ liệu)

    label_result["text"] = "Đăng ký thành công!" # type: ignore

# ... (các phần còn lại của code như trong ví dụ trước)

# Thêm các trường mới cho form đăng ký
label_confirm_password = tk.Label(window, text="Xác nhận mật khẩu:")
label_confirm_password.pack()
entry_confirm_password = tk.Entry(window, show="*")
entry_confirm_password.pack()

label_email = tk.Label(window, text="Email:")
label_email.pack()
entry_email = tk.Entry(window)
entry_email.pack()

# Thay đổi nhãn của nút đăng nhập thành "Đăng ký"
button_login.config(text="Đăng ký") # type: ignore