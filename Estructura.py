class Deque:
    """Estructura de datos Deque (Double-Ended Queue) personalizada."""
    def __init__(self):
        self._items = []

    def add_front(self, item):
        self._items.insert(0, item)

    def add_rear(self, item):
        self._items.append(item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("El Deque está vacío, no se puede remover del frente.")
        return self._items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("El Deque está vacío, no se puede remover del final.")
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def get_all(self):
        """Método auxiliar de lectura para no romper el encapsulamiento al consultar."""
        return list(self._items)