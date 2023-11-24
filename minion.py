import os
import queue

from manager import QueueClient


class Minion(QueueClient):
    def __init__(self):
        super().__init__()  # Initialize the QueueClient connection
        self.connection = None  # Add the connection attribute

    def connect(self):
        try:
            # Connect to the manager process using the shared connection infrastructure
            self.connection = QueueClient.connect()  # Implement the connect() method
            print(f"Minion {os.getpid()} connected to manager process")
        except Exception as e:
            print(f"Failed to connect to the manager process: {e}")

    def run(self):
        try:
            while True:
                task = self.tasks.get()
                print(f"Minion {os.getpid()} got task {task.identifier}")

                # Call the work method of Task
                task.work()

                # Send the task's result back to the result queue
                self.results.put(task)
                print(f"Minion {os.getpid()} put result for task {task.identifier}")

        except queue.Empty:
            print("Queue empty, Minion stops.")
            return

    def terminate(self):
        if self.connection:
            self.connection.close()  # Close the connection to the manager process


if __name__ == "__main__":
    minion = Minion()
    minion.run()
