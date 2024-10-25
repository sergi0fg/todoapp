class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {status}"
