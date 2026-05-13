import tkinter as tk
from tkinter import messagebox
from ManagerActions import ActionManager

class UndoRedoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Gestor de Acciones (Con Auditoría y Atajos)")
        self.root.geometry("850x600") # Ventana más ancha para dos columnas

        # Paleta de colores Dark Mode
        self.bg_color = "#1E1E1E"
        self.fg_color = "#D4D4D4"
        self.accent_color = "#0E639C"
        self.btn_active = "#1177BB"
        self.entry_bg = "#3C3C3C"

        self.root.configure(bg=self.bg_color)
        self.manager = ActionManager()
        self.font_main = ("Segoe UI", 11)
        self.font_title = ("Segoe UI", 12, "bold")

        self._build_ui()
        self._bind_shortcuts()
        self.update_ui()

    def _build_ui(self):
        # 1. Frame de Entrada
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=(20, 10), fill=tk.X, padx=30)

        tk.Label(input_frame, text="Nueva Acción (Presiona Enter para agregar):", bg=self.bg_color, fg=self.fg_color, font=self.font_title).pack(anchor="w")

        self.action_entry = tk.Entry(
            input_frame, font=self.font_main, bg=self.entry_bg,
            fg="white", insertbackground="white", relief="flat"
        )
        self.action_entry.pack(fill=tk.X, pady=(5, 10), ipady=6)

        # 2. Botones Principales
        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack(pady=5)

        self._create_button(btn_frame, "➕ Agregar", self.add_action).grid(row=0, column=0, padx=5)
        self._create_button(btn_frame, "↩️ Deshacer (Ctrl+Z)", self.undo_action).grid(row=0, column=1, padx=5)
        self._create_button(btn_frame, "↪️ Rehacer (Ctrl+Y)", self.redo_action).grid(row=0, column=2, padx=5)

        # 3. Contenedor de Listas (Dos columnas)
        lists_frame = tk.Frame(self.root, bg=self.bg_color)
        lists_frame.pack(pady=(20, 10), fill=tk.BOTH, expand=True, padx=30)

        lists_frame.columnconfigure(0, weight=1)
        lists_frame.columnconfigure(1, weight=1)

        # 3.1 Columna Izquierda: Historial Activo
        left_frame = tk.Frame(lists_frame, bg=self.bg_color)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        tk.Label(left_frame, text="Historial Activo (Pila):", bg=self.bg_color, fg=self.fg_color, font=self.font_title).pack(anchor="w")
        self.history_listbox = self._create_listbox(left_frame)

        # 3.2 Columna Derecha: Registro de Auditoría
        right_frame = tk.Frame(lists_frame, bg=self.bg_color)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        tk.Label(right_frame, text="Registro Absoluto (Auditoría):", bg=self.bg_color, fg="#C586C0", font=self.font_title).pack(anchor="w")
        self.audit_listbox = self._create_listbox(right_frame)

        # 4. Estado Inferior
        self.state_label = tk.Label(self.root, text="", bg=self.bg_color, fg="#4EC9B0", font=self.font_main, wraplength=800)
        self.state_label.pack(pady=(10, 20))

    def _create_listbox(self, parent):
        container = tk.Frame(parent)
        container.pack(fill=tk.BOTH, expand=True, pady=5)
        scrollbar = tk.Scrollbar(container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox = tk.Listbox(
            container, font=self.font_main, bg=self.entry_bg, fg="white",
            relief="flat", highlightthickness=1, highlightcolor=self.accent_color,
            yscrollcommand=scrollbar.set
        )
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)
        return listbox

    def _create_button(self, parent, text, command):
        return tk.Button(
            parent, text=text, font=self.font_main, bg=self.accent_color, fg="white",
            activebackground=self.btn_active, activeforeground="white",
            relief="flat", cursor="hand2", padx=15, pady=6, command=command
        )

    def _bind_shortcuts(self):
        # Atajos de teclado globales
        self.root.bind('<Return>', lambda e: self.add_action())
        self.root.bind('<Control-z>', lambda e: self.undo_action())
        self.root.bind('<Control-y>', lambda e: self.redo_action())

    def add_action(self):
        action_text = self.action_entry.get()
        try:
            self.manager.add_action(action_text)
            self.action_entry.delete(0, tk.END)
            self.update_ui()
        except ValueError as e:
            messagebox.showwarning("Acción Inválida", str(e))

    def undo_action(self):
        try:
            self.manager.undo()
            self.update_ui()
        except IndexError as e:
            messagebox.showinfo("Deshacer", str(e))

    def redo_action(self):
        try:
            self.manager.redo()
            self.update_ui()
        except IndexError as e:
            messagebox.showinfo("Rehacer", str(e))

    def update_ui(self):
        # 1. Actualizar Historial Activo
        self.history_listbox.delete(0, tk.END)
        history = self.manager.get_history()
        for i, act in enumerate(history, 1):
            self.history_listbox.insert(tk.END, f"  {i}. {act}")
        if history:
            self.history_listbox.see(tk.END)

        # 2. Actualizar Registro de Auditoría
        self.audit_listbox.delete(0, tk.END)
        audit_log = self.manager.get_audit_log()
        for log in audit_log:
            self.audit_listbox.insert(tk.END, f"  {log}")
        if audit_log:
            self.audit_listbox.see(tk.END)

        # 3. Actualizar Label de Estado
        self.state_label.config(text=self.manager.get_current_state())

if __name__ == "__main__":
    root = tk.Tk()
    app = UndoRedoApp(root)
    root.mainloop()