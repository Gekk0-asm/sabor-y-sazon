import tkinter as tk
from tkinter import messagebox

from .base_frame import BaseFrame


class LoginFrame(BaseFrame):

    PASSWORD = "1793"  # Esto podria guardarlo en sqlite

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.apply_bg()
        self._build()

    def _build(self):
        # Icono y nombre
        tk.Label(
            self,
            text="🍽 Sabor & Sazón",
            font=("Segoe UI", 22, "bold"),
            bg=self.theme["bg"],
            fg=self.theme["accent"],
        ).pack(pady=(60, 35))

        tk.Label(
            self,
            text="Ingrese la contraseña de acceso:",
            font=("Segoe UI", 11),
            bg=self.theme["bg"],
            fg=self.theme["fg"],
        ).pack()

        self.pwd_var = tk.StringVar()
        self.pwd_entry = tk.Entry(
            self,
            textvariable=self.pwd_var,
            show="*",  # enmascarada
            font=("Segoe UI", 12),
            width=20,
            justify="center",
        )
        self.pwd_entry.pack(pady=10)
        self.pwd_entry.focus_set()
        self.pwd_entry.bind("<Return>", lambda e: self._validar())

        tk.Button(
            self,
            text="Ingresar",
            bg=self.theme["primary"],
            fg="white",
            activebackground=self.theme["secondary"],
            font=("Segoe UI", 11, "bold"),
            width=15,
            command=self._validar,
        ).pack(pady=(20, 200))

        tk.Label(
            self,
            text=f"Autor: {self.config.get("app.author")}",
            font=("Segoe UI", 10),
            bg=self.theme["bg"],
            fg=self.theme["fg"],
        ).pack(pady=(0, 0))

        tk.Label(
            self,
            text=f"Versión: {self.config.get("app.version")}",
            font=("Segoe UI", 10),
            bg=self.theme["bg"],
            fg=self.theme["fg"],
        ).pack(pady=(0, 0))

    def _validar(self):
        if self.pwd_var.get() == self.PASSWORD:
            from ..window import RegisterFrame

            self.controller.show_frame(RegisterFrame)
        else:
            messagebox.showerror("Acceso denegado", "Contraseña incorrecta")
            self.pwd_var.set("")
            self.pwd_entry.focus_set()

    def on_enter(self):
        self.app.title("Sabor y Sazón - Acceso")

        self.pwd_var.set("")
        self.pwd_entry.focus_set()
