import tkinter as tk
import threading


HANDLE_SIZE = 10  # tamanho da alça de redimensionar (canto inferior direito)


class Overlay:
    def __init__(self):
        self._ready = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()
        self._ready.wait()

    def _run(self):
        self._root = tk.Tk()
        self._root.overrideredirect(True)
        self._root.attributes("-topmost", True)
        self._root.attributes("-alpha", 0.88)
        self._root.configure(bg="#111111")
        self._root.withdraw()

        # Tamanho e posição iniciais
        sw = self._root.winfo_screenwidth()
        sh = self._root.winfo_screenheight()
        self._w, self._h = 700, 110
        self._x = (sw - self._w) // 2
        self._y = sh - 160
        self._root.geometry(f"{self._w}x{self._h}+{self._x}+{self._y}")

        # Frame principal
        self._frame = tk.Frame(self._root, bg="#111111", cursor="fleur")
        self._frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Texto
        self._label = tk.Label(
            self._frame, text="", bg="#111111", fg="#ffffff",
            font=("Segoe UI", 16, "bold"),
            wraplength=self._w - 20,
            justify="center",
        )
        self._label.place(relx=0.5, rely=0.5, anchor="center")

        # Barra de título mínima (arraste)
        self._bar = tk.Frame(self._frame, bg="#e94560", height=6, cursor="fleur")
        self._bar.place(relx=0, rely=0, relwidth=1, height=6)

        # Alça de redimensionar (canto inferior direito)
        self._handle = tk.Frame(self._root, bg="#e94560",
                                 width=HANDLE_SIZE, height=HANDLE_SIZE,
                                 cursor="size_nw_se")
        self._handle.place(relx=1.0, rely=1.0, anchor="se",
                           x=-0, y=-0)

        # Botão fechar
        self._btn_close = tk.Label(self._bar, text="✕", bg="#e94560", fg="white",
                                    font=("Segoe UI", 8, "bold"), cursor="hand2")
        self._btn_close.place(relx=1.0, rely=0, anchor="ne", x=-4)
        self._btn_close.bind("<Button-1>", lambda e: self._do_hide())

        # Bind arraste da janela
        for w in (self._frame, self._bar, self._label):
            w.bind("<ButtonPress-1>", self._drag_start)
            w.bind("<B1-Motion>", self._drag_motion)

        # Bind redimensionar
        self._handle.bind("<ButtonPress-1>", self._resize_start)
        self._handle.bind("<B1-Motion>", self._resize_motion)

        self._drag_ox = self._drag_oy = 0
        self._resize_ox = self._resize_oy = 0
        self._hide_job = None
        self._visible = False

        self._ready.set()
        self._root.mainloop()

    # ── Arraste ──────────────────────────────────────────────
    def _drag_start(self, e):
        self._drag_ox = e.x_root - self._x
        self._drag_oy = e.y_root - self._y

    def _drag_motion(self, e):
        self._x = e.x_root - self._drag_ox
        self._y = e.y_root - self._drag_oy
        self._root.geometry(f"{self._w}x{self._h}+{self._x}+{self._y}")

    # ── Redimensionar ────────────────────────────────────────
    def _resize_start(self, e):
        self._resize_ox = e.x_root
        self._resize_oy = e.y_root
        self._resize_w0 = self._w
        self._resize_h0 = self._h

    def _resize_motion(self, e):
        self._w = max(200, self._resize_w0 + (e.x_root - self._resize_ox))
        self._h = max(50,  self._resize_h0 + (e.y_root - self._resize_oy))
        self._label.config(wraplength=self._w - 20)
        self._root.geometry(f"{self._w}x{self._h}+{self._x}+{self._y}")

    # ── Exibir / esconder ────────────────────────────────────
    def show(self, text: str):
        if not text:
            return
        self._root.after(0, self._do_show, text)

    def _do_show(self, text: str):
        self._label.config(text=text)
        if not self._visible:
            self._root.deiconify()
            self._visible = True

    def _do_hide(self):
        self._root.withdraw()
        self._visible = False

    def hide(self):
        if self._root:
            self._root.after(0, self._do_hide)
