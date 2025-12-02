from locust import HttpUser, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def fibonacci_task(self):
        # Aquí se puede llamar a la función de Fibonacci o simular una solicitud
        # Por ejemplo, si tu aplicación tiene un endpoint que calcula Fibonacci:
        self.client.get("/fibonacci?n=10")  # Cambia la URL según tu aplicación

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000  # Tiempo mínimo de espera entre tareas
    max_wait = 3000  # Tiempo máximo de espera entre tareas