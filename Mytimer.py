import time as t
class Mytimer():
    def __init__(self):
        self.unit = ['年','月','日','小时','分钟','秒']
        self.prompt="未开始计时!"
        self.lasted = []
        self.begin = 0
        self.end =0
    def __str__(self):
        return self.prompt
    def __repr__(self):
        return self.prompt
    #开始计时
    def start(self):
        self.begin = t.localtime()
        print("计时开始...")
    #停止计时
    def stop(self):
        self.end = t.localtime()
        print("计时结束!")
        self.calc()
    #计算运行时间
    def calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin [index])
            if self.lasted[index]:
             self.prompt +=str(self.lasted[index]) + self.unit[index]
        print(self.prompt)

t1 = Mytimer()
t1.start()
from time import sleep
sleep(2)
t1.stop()
