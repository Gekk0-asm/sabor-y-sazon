import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from .base_frame import BaseFrame
from ...models import GestionClientes


class RegisterFrame(BaseFrame):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.apply_bg()
        self._build()

    def _build(self):
        # --- Centrado global ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = tk.Frame(self, bg=self.theme["bg"])
        container.grid(row=0, column=0)

        # --- Anchos fijos de columnas ---
        container.grid_columnconfigure(0, minsize=170)  # labels
        container.grid_columnconfigure(1, minsize=300)  # inputs

        # --- Encabezado ---
        tk.Label(
            container,
            text="Registro de Cliente",
            font=("Segoe UI", 18, "bold"),
            bg=self.theme["bg"],
            fg=self.theme["accent"],
        ).grid(row=0, column=0, columnspan=2, pady=(0, 25))

        lbl_opts = dict(
            bg=self.theme["bg"], fg=self.theme["fg"], font=("Segoe UI", 10), anchor="e"
        )
        lbl_grid = dict(sticky="e", padx=(0, 12), pady=6)

        in_grid = dict(sticky="ew", pady=6)

        # --- Identificación ---
        tk.Label(container, text="Identificación:", **lbl_opts).grid(
            row=1, column=0, **lbl_grid
        )
        self.id_var = tk.StringVar()
        tk.Entry(container, textvariable=self.id_var).grid(row=1, column=1, **in_grid)

        # --- Nombre ---
        tk.Label(container, text="Nombre completo:", **lbl_opts).grid(
            row=2, column=0, **lbl_grid
        )
        self.nombre_var = tk.StringVar()
        tk.Entry(container, textvariable=self.nombre_var).grid(
            row=2, column=1, **in_grid
        )

        # --- Género ---
        tk.Label(container, text="Género:", **lbl_opts).grid(
            row=3, column=0, **lbl_grid
        )
        self.genero_var = tk.StringVar(value="Masculino")
        frame_gen = tk.Frame(container, bg=self.theme["bg"])
        frame_gen.grid(row=3, column=1, sticky="ew", pady=6)
        frame_gen.grid_columnconfigure(0, weight=1)
        frame_gen.grid_columnconfigure(1, weight=1)

        radio_opts = dict(
            variable=self.genero_var,
            bg=self.theme["bg"],
            fg=self.theme["fg"],
            selectcolor=self.theme["secondary"],
            activebackground=self.theme["bg"],
            activeforeground=self.theme["fg"],
            anchor="w",
            bd=0,
            highlightthickness=0,
        )
        tk.Radiobutton(
            frame_gen, text="Masculino", value="Masculino", **radio_opts
        ).grid(row=0, column=0, sticky="w")
        tk.Radiobutton(frame_gen, text="Femenino", value="Femenino", **radio_opts).grid(
            row=0, column=1, sticky="w"
        )

        # --- Tipo de menú ---
        tk.Label(container, text="Tipo de menú:", **lbl_opts).grid(
            row=4, column=0, **lbl_grid
        )
        self.menu_var = tk.StringVar()
        self.cmb_menu = ttk.Combobox(
            container,
            textvariable=self.menu_var,
            state="readonly",
            values=list(GestionClientes.COSTOS_MENU.keys()),
        )
        self.cmb_menu.grid(row=4, column=1, **in_grid)
        self.cmb_menu.bind("<<ComboboxSelected>>", self._on_menu_change)

        # --- Costo por sesión ---
        tk.Label(container, text="Costo por sesión:", **lbl_opts).grid(
            row=5, column=0, **lbl_grid
        )
        self.costo_var = tk.StringVar()
        tk.Entry(
            container,
            textvariable=self.costo_var,
            state="disabled",
            disabledforeground=self.theme["comment"],
        ).grid(row=5, column=1, **in_grid)

        # --- Número de sesiones ---
        tk.Label(container, text="Número de sesiones:", **lbl_opts).grid(
            row=6, column=0, **lbl_grid
        )
        self.sesiones_var = tk.StringVar()
        tk.Entry(container, textvariable=self.sesiones_var).grid(
            row=6, column=1, **in_grid
        )

        # --- Fecha ---
        tk.Label(container, text="Fecha de registro:", **lbl_opts).grid(
            row=7, column=0, **lbl_grid
        )
        self.fecha_var = tk.StringVar(
            value=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        tk.Entry(
            container,
            textvariable=self.fecha_var,
            state="disabled",
            disabledforeground=self.theme["comment"],
        ).grid(row=7, column=1, **in_grid)

        # --- Botones ---
        btn_frame = tk.Frame(container, bg=self.theme["bg"])
        btn_frame.grid(row=8, column=0, columnspan=2, pady=(30, 0))

        tk.Button(
            btn_frame,
            text="Guardar Registro",
            bg=self.theme["green"],
            fg=self.theme["bg"],
            activebackground=self.theme["primary"],
            activeforeground=self.theme["bg"],
            font=("Segoe UI", 10, "bold"),
            width=18,
            command=self._guardar,
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            btn_frame,
            text="Calcular / Mostrar Reporte",
            bg=self.theme["accent"],
            fg=self.theme["bg"],
            activebackground=self.theme["primary"],
            activeforeground=self.theme["bg"],
            font=("Segoe UI", 10, "bold"),
            width=22,
            command=self._mostrar_reporte,
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            btn_frame,
            text="Salir",
            bg=self.theme["red"],
            fg=self.theme["bg"],
            activebackground=self.theme["primary"],
            activeforeground=self.theme["bg"],
            font=("Segoe UI", 10, "bold"),
            width=12,
            command=self._salir,
        ).pack(side=tk.LEFT, padx=5)

    # ---------- Eventos ----------
    def _on_menu_change(self, _event=None):
        costo = GestionClientes.costo_por_menu(self.menu_var.get())
        self.costo_var.set(f"$ {costo:,}".replace(",", "."))

    def _leer_formulario(self):
        if not self.id_var.get().strip():
            messagebox.showwarning("Validación", "Debe ingresar la identificación")
            return None
        if not self.nombre_var.get().strip():
            messagebox.showwarning("Validación", "Debe ingresar el nombre")
            return None
        if not self.menu_var.get():
            messagebox.showwarning("Validación", "Debe seleccionar un menú")
            return None
        try:
            sesiones = int(self.sesiones_var.get())
            if sesiones <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Validación", "Número de sesiones inválido")
            return None

        return GestionClientes(
            identificacion=self.id_var.get().strip(),
            nombre=self.nombre_var.get().strip(),
            genero=self.genero_var.get(),
            tipo_menu=self.menu_var.get(),
            numero_sesiones=sesiones,
            fecha_registro=self.fecha_var.get(),
        )

    def _guardar(self):
        cliente = self._leer_formulario()
        if cliente is None:
            return
        self.controller.cliente_actual = cliente
        messagebox.showinfo(
            "Registro", f"Cliente '{cliente.nombre}' guardado con éxito."
        )

    def _mostrar_reporte(self):
        cliente = self._leer_formulario()
        if cliente is None:
            return
        self.controller.cliente_actual = cliente
        from ..window import ReportFrame

        self.controller.show_frame(ReportFrame)

    def _salir(self):
        if messagebox.askyesno("Salir", "¿Realmente desea salir de la aplicación?"):
            self.controller.controller.destroy()

    def on_enter(self):
        self.app.title("Sabor y Sazón - Registro")
        self.fecha_var.set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
