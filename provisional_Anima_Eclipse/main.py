import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
import pygame
import time
import threading

# ============================================================
# CONFIG
# ============================================================

BACKGROUND_PATH = "assets/background.png"
LOGO_PATH = "assets/logo.png"
MUSIC_PATH = "MainMenuTheme.mp3"
LOOP_START_SECONDS = 30   # punto donde empieza el loop

# ============================================================
# AUDIO CONTROL
# ============================================================

def play_music_loop():
    """Reproduce la música una vez y luego la vuelve a reproducir desde LOOP_START."""
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.play()

    # hilo que controla el loop suave
    def loop_checker():
        while True:
            # duración total
            length = pygame.mixer.Sound(MUSIC_PATH).get_length()
            pos = pygame.mixer.music.get_pos() / 1000

            # cuando termine, reinicia desde LOOP_START_SECONDS
            if pos >= length - 0.1:
                pygame.mixer.music.stop()
                pygame.mixer.music.play(start=LOOP_START_SECONDS)

            time.sleep(0.1)

    threading.Thread(target=loop_checker, daemon=True).start()


# ============================================================
# UI PRINCIPAL
# ============================================================

class AnimaEclipseUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Anima Eclipse")
        self.root.geometry("900x600")
        self.root.configure(bg="black")

        # Cargar imágenes
        self.bg = self.load_background(BACKGROUND_PATH)
        self.logo_img = self.load_image(LOGO_PATH, (400, 200))

        # Fondo
        self.bg_label = tk.Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Contenedor principal
        self.main_frame = tk.Frame(self.root, bg="#1a1f2e")
        self.main_frame.pack(expand=True)

        # Logo con fade-in
        self.logo_label = tk.Label(self.main_frame, bg="#1a1f2e")
        self.logo_label.pack(pady=20)
        self.fade_in_logo()

        # Botones
        self.buttons_frame = tk.Frame(self.main_frame, bg="#1a1f2e")
        self.buttons_frame.pack(pady=40)

        self.create_glowing_button("Nueva Partida", lambda: self.transition(self.open_save_menu))
        self.create_glowing_button("Cargar Partida", lambda: self.transition(self.open_save_menu))
        self.create_glowing_button("Opciones", lambda: self.transition(self.open_options))

    # ============================================================
    # CARGA DE IMÁGENES / FONDO
    # ============================================================

    def load_background(self, path):
        img = Image.open(path).convert("RGBA")
        # borde suave + ligero desenfoque
        img = img.filter(ImageFilter.GaussianBlur(3))
        return ImageTk.PhotoImage(img.resize((900, 600)))

    def load_image(self, path, size):
        img = Image.open(path).convert("RGBA")
        img = img.resize(size)
        return img

    # ============================================================
    # LOGO ANIMADO (FADE IN)
    # ============================================================

    def fade_in_logo(self, alpha=0):
        if alpha > 255:
            return

        img = self.logo_img.copy()
        img.putalpha(alpha)

        tk_img = ImageTk.PhotoImage(img)
        self.logo_label.config(image=tk_img)
        self.logo_label.image = tk_img

        self.root.after(10, lambda: self.fade_in_logo(alpha + 5))

    # ============================================================
    # BOTONES GLOW
    # ============================================================

    def create_glowing_button(self, text, cmd):
        btn = tk.Label(
            self.buttons_frame,
            text=text,
            font=("Georgia", 20),
            fg="#dcdcdc",
            bg="#1a1f2e",
            padx=20,
            pady=10,
            borderwidth=0,
            relief="flat"
        )
        btn.pack(pady=10)

        btn.bind("<Enter>", lambda e: btn.config(bg="#273047"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#1a1f2e"))
        btn.bind("<Button-1>", lambda e: cmd())

    # ============================================================
    # TRANSICIÓN FADE-IN / FADE-OUT ENTRE PANTALLAS
    # ============================================================

    def transition(self, next_screen):
        fade = tk.Toplevel(self.root)
        fade.attributes("-fullscreen", True)
        fade.attributes("-alpha", 0.0)
        fade.configure(bg="black")

        # fade-in negro
        for i in range(0, 11):
            fade.attributes("-alpha", i / 10)
            fade.update()
            time.sleep(0.03)

        # ejecutar pantalla siguiente
        next_screen()

        # fade-out negro
        for i in range(10, -1, -1):
            fade.attributes("-alpha", i / 10)
            fade.update()
            time.sleep(0.03)

        fade.destroy()

    # ============================================================
    # MENÚS SECUNDARIOS (BÁSICOS POR AHORA)
    # ============================================================

    def open_save_menu(self):
        print("Abrir menú de guardado (por implementar)")

    def open_options(self):
        print("Abrir opciones (por implementar)")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    play_music_loop()

    ventana = tk.Tk()
    app = AnimaEclipseUI(ventana)
    ventana.mainloop()