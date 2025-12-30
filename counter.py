import tkinter as tk


class WorkCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("作業回数トラッカー")
        self.root.geometry("320x240")
        self.root.attributes("-topmost", True)

        # 状態管理
        self.count = tk.IntVar(value=0)
        self.status = tk.StringVar(value="待機中")

        self.create_ui()
        self.bind_keys()

    def create_ui(self):
        # タイトル
        tk.Label(
            self.root,
            text="作業回数トラッカー",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        # カウント表示
        tk.Label(
            self.root,
            textvariable=self.count,
            font=("Arial", 36)
        ).pack()

        # ボタンエリア
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="完了 +1",
            width=10,
            command=self.add_count
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="修正 -1",
            width=10,
            command=self.sub_count
        ).pack(side="left", padx=5)

        # リセット
        tk.Button(
            self.root,
            text="新しい作業を開始",
            width=20,
            command=self.reset_count
        ).pack(pady=5)

        # ステータス表示
        tk.Label(
            self.root,
            textvariable=self.status,
            anchor="w"
        ).pack(fill="x", padx=10, pady=5)

    def bind_keys(self):
        # キーボードショートカット
        self.root.bind("<Control-Return>", lambda e: self.add_count())
        self.root.bind("<Control-BackSpace>", lambda e: self.sub_count())
        self.root.bind("<Control-Delete>", lambda e: self.reset_count())

    def add_count(self):
        self.count.set(self.count.get() + 1)
        self.status.set("作業を1件記録しました")

    def sub_count(self):
        if self.count.get() > 0:
            self.count.set(self.count.get() - 1)
            self.status.set("作業を修正しました")
        else:
            self.status.set("これ以上減らせません")

    def reset_count(self):
        self.count.set(0)
        self.status.set("新しい作業セッションを開始しました")


if __name__ == "__main__":
    root = tk.Tk()
    app = WorkCounterApp(root)
    root.mainloop()
