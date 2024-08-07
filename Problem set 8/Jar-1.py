class Jar:
    def __init__(self, cookies=0, capacity=12):
        if capacity < 0:
            raise ValueError
        self.cookies = cookies

    def __str__(self):
        string = ""
        for i in range(self.cookies):
            string + "🍪"
        return string

    def deposit(self, n):
        self.cookies += n

    def withdraw(self, n):
        if self.cookies >= n:
            self.cookies -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.cookies

if __name__  == '__main__':
    jar=Jar()
    jar.deposit(10)
    print(jar)
