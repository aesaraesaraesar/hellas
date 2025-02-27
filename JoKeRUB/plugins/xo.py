from JoKeRUB import l313l
import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="black")

        self.window_size = "300x350"
        self.root.geometry(self.window_size)
        self.root.resizable(False, False)

        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.x_wins = 0
        self.o_wins = 0

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="black")
        frame.place(relx=0.5, rely=0.4, anchor="center")

        self.buttons = [[tk.Button(frame, width=6, height=3, bd=3, bg="black", fg="white", font=("Arial", 14, "bold"),
                                   command=lambda row=i, col=j: self.make_move(row, col))
                         for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.x_points_label = tk.Label(self.root, text="X: 0", font=("Arial", 12), fg="red", bg="black")
        self.x_points_label.place(relx=0.2, rely=0.92, anchor="center")

        self.o_points_label = tk.Label(self.root, text="O: 0", font=("Arial", 12), fg="blue", bg="black")
        self.o_points_label.place(relx=0.8, rely=0.92, anchor="center")

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.update_ui()

            if self.check_winner():
                messagebox.showinfo("نتيجة", f"مبروك! اللاعب {self.current_player} فاز 🎉")
                if self.current_player == 'X':
                    self.x_wins += 1
                else:
                    self.o_wins += 1
                self.update_points()
                self.disable_buttons()
            elif all(cell != ' ' for row in self.board for cell in row):
                messagebox.showinfo("نتيجة", "تعادل! حاول مرة أخرى.")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.update_ui()

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

    def update_ui(self):
        for i in range(3):
            for j in range(3):
                button = self.buttons[i][j]
                button.config(text=self.board[i][j], state=tk.DISABLED if self.board[i][j] != ' ' else tk.NORMAL,
                              bg="red" if self.board[i][j] == 'X' else "blue" if self.board[i][j] == 'O' else "black")

    def check_winner(self):
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)):  # صفوف
                return True
            if all(self.board[j][i] == self.current_player for j in range(3)):  # أعمدة
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)):  # قطر رئيسي
            return True
        if all(self.board[i][2 - i] == self.current_player for i in range(3)):  # قطر ثانوي
            return True

        return False

    def update_points(self):
        self.x_points_label.config(text=f"X: {self.x_wins}")
        self.o_points_label.config(text=f"O: {self.o_wins}")

# قائمة تخزين النوافذ المفتوحة لتتم إعادة تشغيلها أو إيقافها
active_games = {}

def start_xo(chat_id):
    if chat_id in active_games:
        active_games[chat_id].root.destroy()  # إغلاق النافذة القديمة إذا كانت مفتوحة

    root = tk.Tk()
    app = TicTacToeApp(root)
    active_games[chat_id] = app  # حفظ النافذة الجديدة
    l313l.run(root)  # تشغيل التطبيق داخل JoKeRUB

def stop_xo(chat_id):
    if chat_id in active_games:
        active_games[chat_id].root.destroy()
        del active_games[chat_id]
        return True
    return False

@l313l.on_cmd(".العب xo")
def play_xo(event):
    chat_id = event.chat_id
    event.reply("🎮 **تم تشغيل لعبة XO!** ✅\nانتظر لحظة حتى تظهر اللعبة...")
    start_xo(chat_id)

@l313l.on_cmd(".عيد xo")
def restart_xo(event):
    chat_id = event.chat_id
    event.reply("🔄 **تمت إعادة تشغيل اللعبة!** ♻️\nانتظر لحظة...")
    start_xo(chat_id)

@l313l.on_cmd(".ايقاف xo")
def stop_xo_cmd(event):
    chat_id = event.chat_id
    if stop_xo(chat_id):
        event.reply("⛔ **تم إيقاف اللعبة بنجاح!** ❌")
    else:
        event.reply("⚠️ **لا توجد لعبة نشطة للإيقاف!** 🚫")
