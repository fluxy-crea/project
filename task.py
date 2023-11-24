import json
import time
import unittest

import numpy as np


class Task:
    def __init__(self, identifier):
        self.identifier = identifier
        self.size = np.random.randint(300, 3_000)
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def to_json(self) -> str:
        task_dict = {
            "identifier": self.identifier,
            "size": self.size,
            "a": self.a.tolist(),
            "b": self.b.tolist(),
            "x": self.x.tolist(),
            "time": self.time,
        }
        json_str = json.dumps(task_dict)
        return repr(json_str)

    @classmethod
    def from_json(cls, json_str: str) -> "Task":
        json_str = eval(json_str)  # Convertir la représentation ASCII en str
        task_dict = json.loads(json_str)
        task = cls(task_dict["identifier"])
        task.size = task_dict["size"]
        task.a = np.array(task_dict["a"])
        task.b = np.array(task_dict["b"])
        task.x = np.array(task_dict["x"])
        task.time = task_dict["time"]
        return task

    # Commenting out the second __eq__ method
    # def __eq__(self, other: "Task") -> bool:
    #     # Comparer tous les attributs pour déterminer l'égalité
    #     if self.identifier != other.identifier:
    #         print(f"Identifier mismatch: {self.identifier} != {other.identifier}")
    #         return False
    #
    #     if not np.array_equal(self.a, other.a):
    #         print(f"Array 'a' mismatch: {self.a} != {other.a}")
    #         return False
    #
    #     if not np.array_equal(self.b, other.b):
    #         print(f"Array 'b' mismatch: {self.b} != {other.b}")
    #         return False
    #
    #     if not np.array_equal(self.x, other.x):
    #         print(f"Array 'x' mismatch: {self.x} != {other.x}")
    #         return False
    #
    #     if self.size != other.size:
    #         print(f"Size mismatch: {self.size} != {other.size}")
    #         return False
    #
    #     if self.time != other.time:
    #         print(f"Time mismatch: {self.time} != {other.time}")
    #         return False
    #
    #
    #     return True


class TestTaskSerialization(unittest.TestCase):
    def test_serialization(self):
        # Instancier une première tâche
        a = Task(identifier="task123")

        # Sérialiser la tâche et instancier une deuxième tâche à partir de la sérialisation
        txt = a.to_json()
        b = Task.from_json(txt)

        # Vérifier que a == b
        are_equal = a == b
        self.assertEqual(a, b)

        print("ASCII de a:", a.to_json())
        print("ASCII de b:", b.to_json())
        print("Les tâches sont-elles égales?", are_equal)


if __name__ == "__main__":
    unittest.main()
