
class Array:
    # 初始化
    def __init__(self, capacity=10):
        self.__size = 0
        self.__capacity = capacity
        self.__data = []
        for i in range(capacity):
            self.__data.append(0)

    # 返回容量
    def get_capacity(self):
        return self.__capacity

    # 返回实际大小
    def get_size(self):
        return self.__size

    # 判断是否为空
    def is_empty(self):
        if self.__size == 0:
            return True
        else:
            return False

    # 向所有元素后添加一个新元素
    def add_last(self, val):
        self.add(val, self.__size)

    # 在指定位置添加一个元素
    def add(self, val, index):
        # try:
        #     self.__data[index] = val
        # except IndexError as i:
        #     print("%s:索引有误" % (i,))
        if self.__size == self.__capacity:
            print("数组已满")
        elif index > self.__size or index < 0:
            print("索引异常")
        else:
            for i in range(self.__size, index, -1):
                print(i)
                self.__data[i] = self.__data[i-1]
            print(index)
            self.__data[index] = val
            self.__size += 1

    def get_data(self):
        return self.__data


if __name__=="__main__":
    demo = Array(10)
    demo.add_last(10)
    print(demo.get_data())

