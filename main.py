import tkinter as tk
from tkinter import messagebox


# Hàm tính BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100

        if weight <= 0 or height <= 0:
            raise ValueError("Cân nặng và chiều cao phải là số dương.")

        bmi = weight / (height ** 2)
        result_label.config(text=f"Chỉ số BMI của bạn: {bmi:.2f}")

        if bmi < 18.5:
            category = "Gầy"
        elif 18.5 <= bmi < 24.9:
            category = "Bình thường"
        elif 25 <= bmi < 29.9:
            category = "Thừa cân"
        else:
            category = "Béo phì"

        category_label.config(text=f"Phân loại: {category}")
    except ValueError as e:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho cân nặng và chiều cao")


# Tạo cửa sổ ứng dụng
window = tk.Tk()
window.title("Ứng Dụng Tính BMI")

# Thêm các widget
label_weight = tk.Label(window, text="Cân nặng (kg):")
label_weight.grid(row=0, column=0, padx=10, pady=10)

entry_weight = tk.Entry(window)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

label_height = tk.Label(window, text="Chiều cao (cm):")
label_height.grid(row=1, column=0, padx=10, pady=10)

entry_height = tk.Entry(window)
entry_height.grid(row=1, column=1, padx=10, pady=10)

# Nút tính BMI
calculate_button = tk.Button(window, text="Tính BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Nhãn hiển thị kết quả BMI và phân loại
result_label = tk.Label(window, text="Chỉ số BMI của bạn: ", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=2, pady=5)

category_label = tk.Label(window, text="Phân loại: ", font=("Arial", 12))
category_label.grid(row=4, column=0, columnspan=2, pady=5)

# Chạy ứng dụng
window.mainloop()
