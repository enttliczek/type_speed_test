import tkinter as tk
import time
import random


class TypingSpeedApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")

        self.text_options = [
            "The quick brown fox jumps over the lazy dog.",
            "Two roads diverged in a wood, and I took the one less traveled by, And that has made all the difference.",
            "In the beginning God created the heavens and the earth.",
            "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...",
        ]

        self.text_to_type = random.choice(self.text_options)

        self.instructions_label = tk.Label(self.master, text="Type the following text: ")
        self.instructions_label.pack()

        self.text_display = tk.Label(self.master, text=self.text_to_type, wraplength=400, justify="left")
        self.text_display.pack()

        self.user_text = tk.Text(self.master, height=5, width=50)
        self.user_text.pack()

        self.start_button = tk.Button(self.master, text="Start typing test", command=self.start_typing_test)
        self.start_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()



    def start_typing_test(self):
        self.user_text.delete("1.0", tk.END) # Clear the user input widget
        self.result_label.config(text="") # Clear the result label
        self.start_time = time.time()  # Record the start time
        self.user_text.bind("<Key>", self.check_typing)  # Bind a callback function to track user input



    def check_typing(self, event):
        typed_text = self.user_text.get("1.0", tk.END).strip()
        typed_length = len(typed_text)
        expected_length = len(self.text_to_type)

        if typed_text == self.text_to_type:
            elapsed_time = time.time() - self.start_time
            typing_speed = (typed_length / elapsed_time) * 60
            self.result_label.config(text=f"Correct!, Typing speed: {typing_speed:.2f} characters per minute")
        elif typed_length > expected_length:
            self.result_label.config(text="Text incorrect you've typed too many characters")
        elif typed_text != self.text_to_type[:typed_length]:
            self.result_label.config(text="Text incorrect, check for mistakes")
        else:
            self.result_label.config(text="Keep trying...")


def main():
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
