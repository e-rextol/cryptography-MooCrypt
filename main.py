
# MooCrypt - Blue & White Cow Themed GUI (ttkbootstrap)
# main.py
# -------------------------------------------------------------
# Requires:
#   pip install ttkbootstrap
#   Place alongside:
#     Decryption.py  (split_index, len_text, Return_value_int, put_space, mixtext)
#     Encrption.py or Encryption.py (put_keyword_and_cut_value, put_slash_and_high, random_text, fusion)
# Run:
#   python main.py
# -------------------------------------------------------------
import importlib
import sys
import traceback
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
try:
    from ttkbootstrap.toast import ToastNotification
except Exception:
    ToastNotification = None

APP_NAME = "MooCrypt 🐮"
# Palette (blue/white)
THEME_BG = "#eaf4ff"
THEME_WHITE = "#ffffff"
THEME_SKY = "#70a6ff"
THEME_SKY_DK = "#3b7dff"

# ------------------------------
# Dynamic imports & pipelines
# ------------------------------
class CryptoPipes:
    def __init__(self):
        self.dec_mod = None
        self.enc_mod = None
        self._import_modules()

    def _import_modules(self):
        try:
            self.dec_mod = importlib.import_module("Decryption")
        except Exception as e:
            raise ImportError("Decryption.py file not found or error importing\n" + str(e))

        errors = []
        for name in ["Encrption", "Encryption"]:
            try:
                self.enc_mod = importlib.import_module(name)
                break
            except Exception as e:
                errors.append(f"{name}: {e}")
        if not self.enc_mod:
            raise ImportError("Encrption.py/Encryption.py file not found or error importing\n" + "\n".join(errors))

        for fn in ["split_index", "len_text", "Return_value_int", "put_space", "mixtext"]:
            if not hasattr(self.dec_mod, fn):
                raise AttributeError(f"Decryption.py missing function: {fn}")
        for fn in ["put_keyword_and_cut_value", "put_slash_and_high", "random_text", "fusion"]:
            if not hasattr(self.enc_mod, fn):
                raise AttributeError(f"{self.enc_mod.__name__}.py missing function: {fn}")

    def encrypt(self, a: str) -> str:
        try:
            step1 = self.enc_mod.put_keyword_and_cut_value(a)
            step2 = self.enc_mod.put_slash_and_high(step1)
            step3 = self.enc_mod.random_text(step2)
            result = self.enc_mod.fusion(step3)
            return str(result)
        except Exception as e:
            raise RuntimeError(f"Error during Encrypt: {e}\n{traceback.format_exc()}")

    def decrypt(self, a: str) -> str:
        try:
            step1 = self.dec_mod.split_index(a)
            step2 = self.dec_mod.len_text(step1)
            step3 = self.dec_mod.Return_value_int(step2)
            step4 = self.dec_mod.put_space(step3)
            result = self.dec_mod.mixtext(step4)
            return str(result)
        except Exception as e:
            raise RuntimeError(f"Error during Decrypt: {e}\n{traceback.format_exc()}")

# ------------------------------
# GUI
# ------------------------------
class MooCryptApp(tb.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10, bootstyle="light")
        self.master.title(APP_NAME)
        self.master.minsize(860, 540)

        # ----- top-level grid weights for responsive expansion
        self.master.rowconfigure(0, weight=0)   # header
        self.master.rowconfigure(1, weight=1)   # content
        self.master.rowconfigure(2, weight=0)   # footer doodle
        self.master.columnconfigure(0, weight=1)

        self.grid(row=1, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Header (uses primary color, set to blue)
        header = tb.Frame(self.master, padding=(16, 14), bootstyle="primary")
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(1, weight=1)
        tb.Label(header, text="🐮", font=("Segoe UI Emoji", 28), bootstyle="inverse-primary").grid(row=0, column=0, padx=(0, 12))
        tb.Label(header, text="MooCrypt", font=("Segoe UI Semibold", 20), bootstyle="inverse-primary").grid(row=0, column=1, sticky="w")
        tb.Label(header, text="Encrypt / Decrypt playground", font=("Segoe UI", 10),
                 bootstyle="inverse-primary").grid(row=1, column=1, sticky="w", pady=(2, 0))

        # Content area: two equal columns (input | output)
        content = tb.Frame(self, padding=8)
        content.grid(row=0, column=0, sticky="nsew")
        content.rowconfigure(1, weight=1)  # row with text widgets grows
        # Enforce equal column widths via 'uniform'
        content.columnconfigure(0, weight=1, uniform="cols")
        content.columnconfigure(1, weight=1, uniform="cols")

        # --- Input card
        input_card = tb.Labelframe(content, text="Input", padding=8, bootstyle="secondary")
        input_card.grid(row=1, column=0, sticky="nsew", padx=(0, 6))
        input_card.rowconfigure(0, weight=1)
        input_card.columnconfigure(0, weight=1)

        self.input_text = tk.Text(input_card, wrap="word", borderwidth=0, font=("Consolas", 11))
        self.input_text.grid(row=0, column=0, sticky="nsew")
        in_scroll = tb.Scrollbar(input_card, command=self.input_text.yview, bootstyle="round")
        in_scroll.grid(row=0, column=1, sticky="ns")
        self.input_text.configure(yscrollcommand=in_scroll.set)

        # --- Output card
        output_card = tb.Labelframe(content, text="Output", padding=8, bootstyle="secondary")
        output_card.grid(row=1, column=1, sticky="nsew", padx=(6, 0))
        output_card.rowconfigure(0, weight=1)
        output_card.columnconfigure(0, weight=1)

        self.output_text = tk.Text(output_card, wrap="word", borderwidth=0, font=("Consolas", 11))
        self.output_text.grid(row=0, column=0, sticky="nsew")
        out_scroll = tb.Scrollbar(output_card, command=self.output_text.yview, bootstyle="round")
        out_scroll.grid(row=0, column=1, sticky="ns")
        self.output_text.configure(yscrollcommand=out_scroll.set)

        # --- Controls row (buttons in center, placed between input and output)
        ctrl_row = tb.Frame(content)
        ctrl_row.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(6, 12))
        ctrl_row.columnconfigure(0, weight=1)
        ctrl_row.columnconfigure(1, weight=0)
        ctrl_row.columnconfigure(2, weight=0)

        self.btn_encrypt = tb.Button(ctrl_row, text="Encrypt 🔐", bootstyle=PRIMARY, command=self.on_encrypt)
        self.btn_decrypt = tb.Button(ctrl_row, text="Decrypt 🔓", bootstyle=INFO, command=self.on_decrypt)
        self.btn_copy   = tb.Button(ctrl_row, text="Copy Output 📋", bootstyle=SECONDARY, command=self.on_copy)
        self.btn_encrypt.grid(row=0, column=1, padx=(0, 8), sticky="e")
        self.btn_decrypt.grid(row=0, column=2, padx=(0, 8), sticky="e")
        self.btn_copy.grid(row=0, column=3, sticky="e")

        # Keyboard shortcuts
        self.master.bind("<Return>", lambda e: self.on_encrypt())
        self.master.bind("<Control-Return>", lambda e: self.on_decrypt())
        self.master.bind("<Control-c>", lambda e: self.on_copy())

        # Footer cow doodle (fixed minimal height but non-intrusive)
        self._cow_footer()

        # Crypto init
        try:
            self.crypto = CryptoPipes()
        except Exception as e:
            messagebox.showerror("Import Error", str(e))
            self.disable_actions(True)

    def disable_actions(self, state: bool):
        new_state = tk.DISABLED if state else tk.NORMAL
        for w in (self.btn_encrypt, self.btn_decrypt, self.btn_copy):
            w.configure(state=new_state)

    def get_input(self) -> str:
        return self.input_text.get("1.0", "end-1c")

    def set_output(self, text: str):
        # keep editable for user to select/copy; no disabled state
        self.output_text.delete("1.0", "end")
        if text is not None:
            self.output_text.insert("1.0", text)

    def on_encrypt(self):
        a = self.get_input().strip()
        if not a:
            self.set_output("")
            return
        try:
            out = self.crypto.encrypt(a)
            self.set_output(out)
        except Exception as e:
            self.set_output(str(e))

    def on_decrypt(self):
        a = self.get_input().strip()
        if not a:
            self.set_output("")
            return
        try:
            out = self.crypto.decrypt(a)
            self.set_output(out)
        except Exception as e:
            self.set_output(str(e))

    def on_copy(self):
        text = self.output_text.get("1.0", "end-1c")
        if not text:
            self._notify("Nothing to copy", "Output is still empty.")
            return
        try:
            self.master.clipboard_clear()
            self.master.clipboard_append(text)
            self.master.update()  # keep clipboard after app closes
            self._notify("Copied", "Output has been copied.")
        except Exception as e:
            messagebox.showerror("Clipboard Error", str(e))

    def _notify(self, title, message):
        # Prefer toast if available
        if ToastNotification is not None:
            try:
                toast = ToastNotification(title=title, message=message, duration=2000, position=(None, 64, "ne"))
                toast.show_toast()
                return
            except Exception:
                pass
        messagebox.showinfo(title, message)

    def _cow_footer(self):
        # keep footer minimal height; avoid hogging space
        footer = tb.Frame(self.master, padding=(0, 6))
        footer.grid(row=2, column=0, sticky="ew")
        canvas = tk.Canvas(footer, height=90, bg=self.master.cget("background"), highlightthickness=0)
        canvas.pack(fill="x", expand=False)
        w = 900
        canvas.config(width=w)

        # ground
        canvas.create_rectangle(0, 70, w, 90, fill="#d7ebff", outline="")

        # cow head
        cx, cy = 60, 45
        canvas.create_oval(cx-35, cy-28, cx+35, cy+28, fill=THEME_WHITE, outline="#b0c4ff", width=2)
        canvas.create_oval(cx-52, cy-8, cx-32, cy+8, fill=THEME_WHITE, outline="#b0c4ff", width=2)
        canvas.create_oval(cx+32, cy-8, cx+52, cy+8, fill=THEME_WHITE, outline="#b0c4ff", width=2)
        canvas.create_oval(cx-22, cy-12, cx-6, cy+4, fill=THEME_SKY, outline="")
        canvas.create_oval(cx+4, cy-4, cx+18, cy+8, fill=THEME_SKY, outline="")
        canvas.create_oval(cx-16, cy-2, cx-10, cy+4, fill="#0b2545", outline="")
        canvas.create_oval(cx+12, cy-2, cx+18, cy+4, fill="#0b2545", outline="")
        canvas.create_oval(cx-16, cy+10, cx+16, cy+24, fill="#f1f5ff", outline="#b0c4ff", width=2)
        canvas.create_oval(cx-8, cy+14, cx-2, cy+20, fill="#0b2545", outline="")
        canvas.create_oval(cx+2, cy+14, cx+8, cy+20, fill="#0b2545", outline="")
        canvas.create_text(150, 36, text="MooCrypt", anchor="w", font=("Segoe UI Semibold", 16), fill=THEME_SKY_DK)
        canvas.create_text(150, 58, text="By e-rextol", anchor="w", font=("Segoe UI", 10), fill="#3c5a99")

def main():
    # ttkbootstrap themed window
    app = tb.Window(themename="flatly")  # blue/white vibe
    # Stretchable background
    app.configure(padx=0, pady=0)
    # Fill window with our frame
    MooCryptApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()
