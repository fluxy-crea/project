#!/usr/bin/env python3
import unittest

from task import (
    Task,  # Assurez-vous d'importer correctement la classe Task depuis votre module
)


class TestTaskSerialization(unittest.TestCase):
    def test_serialization(self):
        # Instancier une première tâche
        a = Task(identifier="task123")

        # Sérialiser la tâche et instancier une deuxième tâche à partir de la sérialisation
        txt = a.to_json()
        b = Task.from_json(txt)

        # Vérifier que a == b
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
