import grpc
from concurrent import futures
import time

# Импортируем сгенерированные файлы
import service_pb2 as calculator_pb2
import service_pb2_grpc as calculator_pb2_grpc


class CalculatorService(calculator_pb2_grpc.CalculatorServicer):
    """
    Простой сервис калькулятора, который реализует методы из proto-контракта
    """

    def Add(self, request, context):
        """Сложение двух чисел"""
        print(f" Получен запрос на сложение: {request.number1} + {request.number2}")

        # Вычисляем результат
        result = request.number1 + request.number2

        # Создаем ответ
        response = calculator_pb2.AddResponse(result=result)
        print(f" Отправлен ответ: {result}")
        return response

    def Multiply(self, request, context):
        """Умножение двух чисел"""
        print(f" Получен запрос на умножение: {request.number1} × {request.number2}")

        result = request.number1 * request.number2

        response = calculator_pb2.MultiplyResponse(result=result)
        print(f" Отправлен ответ: {result}")
        return response

    def Greet(self, request, context):
        """Приветствие по имени"""
        print(f" Получен запрос на приветствие для: {request.name}")

        greeting = f"Привет, {request.name}! Добро пожаловать в gRPC калькулятор!"

        response = calculator_pb2.GreetResponse(greeting=greeting)
        print(f" Отправлен ответ: {greeting}")
        return response


def run_server():
    """
    Запускает gRPC сервер
    """
    print(" Запуск gRPC сервера...")

    # Создаем сервер с пулом потоков
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Добавляем наш сервис к серверу
    calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorService(), server
    )

    # Запускаем сервер на порту 50051
    server.add_insecure_port('[::]:50051')
    server.start()
    print(" Сервер запущен на localhost:50051")
    print(" Ожидание запросов...")

    try:
        # Держим сервер активным
        while True:
            time.sleep(60)  # Спим 60 секунд
    except KeyboardInterrupt:
        print("\n Остановка сервера...")
        server.stop(0)


if __name__ == '__main__':
    run_server()