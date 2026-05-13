from Estructura import Deque

class ActionManager:
    """Clase principal que maneja la lógica de deshacer/rehacer y registro absoluto."""
    def __init__(self):
        self.undo_deque = Deque()
        self.redo_deque = Deque()
        self.audit_log = []  # Historial absoluto inmutable

    def add_action(self, action: str):
        if not action or not action.strip():
            raise ValueError("La acción no puede estar vacía o ser solo espacios.")

        self.undo_deque.add_rear(action)
        self.redo_deque = Deque()
        self.audit_log.append(f"➕ Acción agregada: '{action}'")

    def undo(self):
        if self.undo_deque.is_empty():
            raise IndexError("No hay acciones para deshacer.")

        action = self.undo_deque.remove_rear()
        self.redo_deque.add_rear(action)
        self.audit_log.append(f"↩️ Se deshizo: '{action}'")
        return action

    def redo(self):
        if self.redo_deque.is_empty():
            raise IndexError("No hay acciones para rehacer.")

        action = self.redo_deque.remove_rear()
        self.undo_deque.add_rear(action)
        self.audit_log.append(f"↪️ Se rehizo: '{action}'")
        return action

    def get_history(self):
        """Devuelve el historial de acciones activas (para el Undo/Redo)."""
        return self.undo_deque.get_all()

    def get_audit_log(self):
        """Devuelve el registro absoluto de todos los eventos."""
        return self.audit_log

    def get_current_state(self):
        history = self.get_history()
        if not history:
            return "Estado inicial (vacío)"
        return f"Acciones aplicadas: {', '.join(history)}"