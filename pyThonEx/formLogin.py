import tkinter as tk

def login():
    username = entry_username.get()
    password = entry_password.get()
    # Ở đây bạn sẽ thực hiện kiểm tra thông tin đăng nhập
    # Ví dụ: so sánh với thông tin lưu trữ trong một file hoặc cơ sở dữ liệu
    if username == "admin" and password == "password123":
        label_result["text"] = "Đăng nhập thành công!"
    else:
        label_result["text"] = "Tên đăng nhập hoặc mật khẩu không đúng!"

window = tk.Tk()
window.title("Form đăng nhập")

label_username = tk.Label(window, text="Tên đăng nhập:")
label_username.pack()

entry_username = tk.Entry(window)
entry_username.pack()

label_password = tk.Label(window, text="Mật khẩu:")
label_password.pack()

entry_password = tk.Entry(window, show="*")
entry_password.pack()

button_login = tk.Button(window, text="Đăng nhập", command=login)
button_login.pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()