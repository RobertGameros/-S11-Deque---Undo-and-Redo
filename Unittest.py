import unittest

# Corrección aquí:
from ManagerActions import ActionManager
from Estructura import Deque

class TestUndoRedoSystem(unittest.TestCase):
    def setUp(self):
        # Corrección aquí:
        self.manager = ActionManager()

    # ... (el resto de tus tests se quedan exactamente igual) ...

    def test_deque_operations(self):
        d = Deque()
        self.assertTrue(d.is_empty())
        d.add_rear("A")
        d.add_front("B")
        self.assertEqual(d.size(), 2)
        self.assertEqual(d.remove_rear(), "A")
        self.assertEqual(d.remove_front(), "B")

    def test_add_and_undo(self):
        self.manager.add_action("Escribir 'Hola'")
        self.manager.add_action("Escribir 'Mundo'")
        self.assertEqual(self.manager.undo(), "Escribir 'Mundo'")
        self.assertEqual(self.manager.get_history(), ["Escribir 'Hola'"])

    def test_redo(self):
        self.manager.add_action("Acción 1")
        self.manager.undo()
        self.assertEqual(self.manager.redo(), "Acción 1")
        self.assertEqual(self.manager.get_history(), ["Acción 1"])

    def test_clear_redo_on_new_action(self):
        self.manager.add_action("A")
        self.manager.undo()
        self.manager.add_action("B")
        with self.assertRaises(IndexError):
            self.manager.redo()

    def test_empty_action_validation(self):
        with self.assertRaises(ValueError):
            self.manager.add_action("   ")

    def test_undo_empty_validation(self):
        with self.assertRaises(IndexError):
            self.manager.undo()

# Para ejecutar las pruebas de forma independiente:
# if __name__ == '__main__':
#     unittest.main()