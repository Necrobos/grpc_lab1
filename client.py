import grpc

# Импортируем сгенерированные файлы
import service_pb2 as calculator_pb2
import service_pb2_grpc as calculator_pb2_grpc


class CalculatorClient:
    """
    Простой клиент для взаимодействия с gRPC сервером калькулятора
    """

    def __init__(self, host='localhost', port=50051):
        # Создаем канал связи с сервером
        self.channel = grpc.insecure_channel(f'{host}:{port}')

        # Создаем stub (заглушку) для вызова методов
        self.stub = calculator_pb2_grpc.CalculatorStub(self.channel)
        print(f"Подключен к серверу {host}:{port}")

    def add_numbers(self, a, b):
        """Вызывает метод сложения на сервере"""
        print(f"\nЗапрос на сложение: {a} + {b}")

        # Создаем запрос
        request = calculator_pb2.AddRequest(number1=a, number2=b)

        # Вызываем удаленный метод
        response = self.stub.Add(request)

        print(f"Результат: {response.result}")
        return response.result

    def multiply_numbers(self, a, b):
        """Вызывает метод умножения на сервере"""
        print(f"\nЗапрос на умножение: {a} × {b}")

        request = calculator_pb2.MultiplyRequest(number1=a, number2=b)
        response = self.stub.Multiply(request)

        print(f"Результат: {response.result}")
        return response.result

    def greet(self, name):
        """Вызывает метод приветствия на сервере"""
        print(f"\nЗапрос на приветствие для: {name}")

        request = calculator_pb2.GreetRequest(name=name)
        response = self.stub.Greet(request)

        print(f"Ответ сервера: {response.greeting}")
        return response.greeting


def run_client():
    """
    Демонстрирует работу клиента
    """
    print("Инициализация клиента...")
    client = CalculatorClient()

    # Тестируем различные методы
    print("\n" + "=" * 50)
    print("Начинаем тестирование gRPC вызовов")
    print("=" * 50)

    # Тест 1: Сложение
    client.add_numbers(10, 5)

    # Тест 2: Умножение
    client.multiply_numbers(7, 8)

    # Тест 3: Приветствие
    client.greet("Михаил")

    # Тест 4: Дробные числа
    client.add_numbers(3.14, 2.71)

    # Тест 5: Еще одно умножение
    client.multiply_numbers(12, 15)

    print("\n" + "=" * 50)
    print("Все тесты завершены!")
    print("=" * 50)


if __name__ == '__main__':
    run_client()