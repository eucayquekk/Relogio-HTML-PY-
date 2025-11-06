import os
import sys
import tkinter as tk
from tkinter import PhotoImage
import webview

# ---------------------------
# Função compatível com .exe
# ---------------------------
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------------------------
# Tela de splash (intro animada)
# ---------------------------
def show_splash():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.geometry("420x260+700+350")
    splash.configure(bg="#0e0e0e")
    splash.attributes("-alpha", 0.0)  # começa invisível

    # logo
    logo_path = resource_path("app.png")
    if os.path.exists(logo_path):
        logo_img = PhotoImage(file=logo_path)
        logo_img = logo_img.subsample(3, 3)  # reduz imagem
        logo_label = tk.Label(splash, image=logo_img, bg="#0e0e0e")
        logo_label.image = logo_img
        logo_label.pack(pady=30)

    # texto
    label = tk.Label(
        splash,
        text="Carregando Relógio App...",
        fg="white",
        bg="#0e0e0e",
        font=("Segoe UI", 12, "bold")
    )
    label.pack(pady=20)

    # animação fade-in
    def fade_in(alpha=0.0):
        if alpha < 1.0:
            splash.attributes("-alpha", alpha)
            splash.after(50, fade_in, alpha + 0.05)
        else:
            # depois de 2,5s, inicia fade-out
            splash.after(2500, fade_out, 1.0)

    # animação fade-out
    def fade_out(alpha):
        if alpha > 0:
            splash.attributes("-alpha", alpha)
            splash.after(50, fade_out, alpha - 0.05)
        else:
            splash.destroy()

    fade_in()  # inicia a animação
    splash.mainloop()

# ---------------------------
# Início do App
# ---------------------------
if __name__ == "__main__":
    show_splash()  # mostra a intro
    html_file = resource_path("index.html")
    webview.create_window("Relógio App", html_file)
    webview.start()
