import tkinter as tk

from ..config import ConfigManager
from .frames.login_frame import LoginFrame
from .frames.register_frame import RegisterFrame
from .frames.report_frame import ReportFrame


class MainWindow(tk.Frame):
    def __init__(self, parent, config: ConfigManager):
        super().__init__(parent)
        self.controller = parent  # App
        self.config = config
        self.theme = config.get_theme()
        self.cliente_actual = None  # se llena al guardar

        self.pack(fill=tk.BOTH, expand=True)
        self.configure(bg=self.theme["bg"])

        # Contenedor donde se apilan los frames
        container = tk.Frame(self, bg=self.theme["bg"])
        container.pack(fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginFrame, RegisterFrame, ReportFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginFrame)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.on_enter()
        frame.tkraise()
