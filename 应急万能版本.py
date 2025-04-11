import tkinter as tk
from tkinter import font, messagebox
import random
import datetime

class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("智能抽号系统")
        # 基础尺寸
        self.base_width = 600
        self.base_height = 400
        self.root.geometry(f"{self.base_width}x{self.base_height}")
        self.root.minsize(self.base_width, self.base_height)
        # 状态变量
        self.blinking = False
        self.numbers_to_show = []
        self.current_number_index = 0
        # 界面字体
        self.base_size = 16
        self.result_base_size = 120
        self.base_font = font.Font(family="黑体", size=self.base_size)
        self.result_font = font.Font(family="黑体", size=self.result_base_size)
        # 创建界面组件
        self.create_widgets()
        # 初始状态设置
        self.max_num_entry.insert(0, "50")
        self.quantity_entry.insert(0, "1")
        self.btn.config(state=tk.DISABLED)
        self.update_button_state()

    def create_widgets(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        # 控制区
        control_frame = tk.Frame(main_frame)
        tk.Label(control_frame, text="最大号码：", font=self.base_font).grid(row=0, column=0, padx=5)
        self.max_num_entry = tk.Entry(control_frame, font=self.base_font, width=8)
        self.max_num_entry.grid(row=0, column=1, padx=5)
        tk.Label(control_frame, text="抽号数量：", font=self.base_font).grid(row=0, column=2, padx=5)
        self.quantity_entry = tk.Entry(control_frame, font=self.base_font, width=5)
        self.quantity_entry.grid(row=0, column=3, padx=5)
        control_frame.pack(side=tk.TOP, pady=10)
        # 抽号按钮
        self.btn = tk.Button(main_frame, text="开始抽号", command=self.start_lottery,
                             font=self.base_font, width=18, height=2)
        self.btn.pack(pady=15)
        # 结果显示
        result_frame = tk.Frame(main_frame)
        self.result = tk.Label(result_frame, text="", font=self.result_font,
                               anchor="center", justify="center", relief="ridge", borderwidth=3)
        self.result.pack(expand=True, fill=tk.BOTH)
        result_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

    def update_button_state(self):
        """更新按钮状态"""
        try:
            max_num = self.max_num_entry.get().isdigit() and int(self.max_num_entry.get()) > 0
            quantity = self.quantity_entry.get().isdigit() and int(self.quantity_entry.get()) > 0
            ready = all([
                max_num,
                quantity,
                not self.blinking
            ])
            self.btn.config(state=tk.NORMAL if ready else tk.DISABLED)
        except:
            self.btn.config(state=tk.DISABLED)

    def start_lottery(self):
        try:
            max_num = int(self.max_num_entry.get())
            quantity = int(self.quantity_entry.get())
            if max_num <= 0 or quantity <= 0:
                messagebox.showwarning("错误", "请输入有效的正整数！")
                return
        except:
            messagebox.showwarning("错误", "请输入有效的正整数！")
            return
        # 计算可用号码
        available = set(range(1, max_num + 1))
        if len(available) < quantity:
            messagebox.showwarning("错误", "可用号码不足，请调整参数！")
            return
        # 抽号
        self.numbers_to_show = random.sample(list(available), quantity)
        # 后续动画逻辑
        self.current_number_index = 0
        self.btn.config(state=tk.DISABLED)
        if quantity == 1:
            self.run_single_animation(max_num)
        else:
            self.run_multi_animation()

    def run_single_animation(self, max_num):
        """单次抽号动画"""
        self.blinking = True
        self.animation_start_time = datetime.datetime.now()  # 记录动画开始时间
        self.animate_number(max_num)

    def animate_number(self, max_num):
        """动画效果"""
        if self.blinking:
            elapsed_time = (datetime.datetime.now() - self.animation_start_time).total_seconds()
            if elapsed_time < 1.2:  # 动画持续 1.2 秒
                self.result.config(text=str(random.randint(1, max_num)))
                self.root.after(100, lambda: self.animate_number(max_num))
            else:
                # 动画结束，显示最终结果
                self.blinking = False
                self.result.config(text=str(self.numbers_to_show[0]))
                self.btn.config(state=tk.NORMAL)

    def run_multi_animation(self):
        """多次抽号动画"""
        self.blinking = True
        self.show_next_number()

    def show_next_number(self):
        """依次显示每个号码"""
        if self.current_number_index < len(self.numbers_to_show):
            num = self.numbers_to_show[self.current_number_index]
            self.result.config(text=str(num))
            self.current_number_index += 1
            self.root.after(1000, self.show_next_number)
        else:
            self.blinking = False
            self.btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = LotteryApp(root)
        root.mainloop()
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("程序崩溃，按回车键退出...")