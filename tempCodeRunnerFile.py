import os
import webview
import sys

def resource_path(relative_path):
    # Caminho correto mesmo dentro do .exe
    if getattr(sys, 'frozen', False):
        # Caminho do exe
        base_path = sys._MEIPASS
    else:
        # Caminho normal do script
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

html_file = resource_path("index.html")
webview.create_window("Meu App", html_file)
webview.start()
