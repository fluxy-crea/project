import queue

from manager import QueueClient
from task import Task


class Boss(QueueClient):
    def initialize(self):
        super().initialize()  # Initialize the QueueClient connection

    def submit_tasks(self, num_tasks):
        for i in range(num_tasks):
            task = Task(identifier=i)
            self.tasks.put(task)
            print(f"Submitted task {task.identifier} to the task queue")

    def collect_results(self, num_tasks):
        results = []
        for i in range(num_tasks):
            try:
                result = self.results.get()
                print(f"Received result for task {result.identifier}")
                results.append(result)
            except queue.Empty:
                print("Results queue is empty, end of collection.")
                break
        return results


if __name__ == "__main__":
    boss = Boss()
    num_tasks = 4

    boss.submit_tasks(num_tasks)
    print("Tasks submitted, collecting results...")

    collected_results = boss.collect_results(num_tasks)
    print(f"Collected {len(collected_results)} results.")
