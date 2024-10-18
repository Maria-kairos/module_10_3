import random
import time
from threading import Thread, Lock
from random import randint
from time import sleep
import threading

class Bank:
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            x = random.randint(50, 100)
            self.balance += x
            time.sleep(0.001)
            print(f'Пополнение: {x}. Баланс: {self.balance}.')

    def take(self):
        for i in range(100):
            x = random.randint(50, 100)
            print(f'Запрос на {x}')
            if self.balance >= x:
                self.balance -= x
                time.sleep(0.001)
                print(f'Снятие: {x}. Баланс: {self.balance}.')
            else:
                time.sleep(0.001)
                print(f'Запрос отклонен, недостаточно средств.')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')