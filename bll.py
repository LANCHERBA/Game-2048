"""
    游戏核心逻辑控制器
"""
import random

from model import LocationModel


class GameCoreController:
    def __init__(self):
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_merge = None
        self.__list_empty_location = []

    @property
    def list_merge(self):
        return self.__list_merge

    @property
    def map(self):
        return self.__map

    # 1. 定义函数，将list_merge中的零元素移动到末尾。
    def __zeroToEnd(self):
        """
            零元素移动到末尾
            思路：从后向前以此判断，如果是零元素，则删除后追加零。
        """
        for num in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[num] == 0:
                del self.__list_merge[num]
                self.__list_merge.append(0)

    # 2. 定义函数，将list_merge中的元素进行合并（相邻且相同）
    def __merge(self):
        """
            合并
            思路：
                将零元素后移
                判断如果相邻且相同则合并。
        :param list_merge:
        """
        self.__zeroToEnd()
        for num in range(len(self.__list_merge) - 1):
            if self.__list_merge[num] == self.__list_merge[num + 1] and self.__list_merge[num] != 0:
                self.__list_merge[num] = self.__list_merge[num] * 2
                self.__list_merge[num + 1] = 0
                self.__zeroToEnd()

    # 3. 定义函数，将二维列表ｍａｐ中的元素向左移动。
    def moveLeft(self):
        """
            向左移动
            思路：将每行（一维列表）赋值给全局变量list_merge
                　在通过ｍｅｒｇｅ函数操作数据。
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    # 4.定义函数，将二维列表ｍａｐ中的元素向右移动
    def moveRight(self):
        """
        向右移动
            思路：将每行（反向切片）赋值给全局变量list_merge
                　在通过ｍｅｒｇｅ函数操作数据。
                再对list_merge(反向切片)
        """
        for line in self.__map:
            # 因为切片，所以创建了新列表
            self.__list_merge = line[::-1]
            self.__merge()  # 操作的是新列表
            line[::-1] = self.__list_merge

    # 反转矩阵
    def __Tmatrix(self):
        for c in range(len(self.__map) - 1):
            for r in range(c + 1, len(self.__map)):
                self.__map[r][c], self.__map[c][r] = self.__map[c][r], self.__map[r][c]

    # 5. 定义函数,将二维列表ｍａｐ中的元素向上移动
    def moveUp(self):
        """
            向上移动
            思想：方阵转置
                调用向左移动
                方针转置
        """
        self.__Tmatrix()
        self.moveLeft()
        self.__Tmatrix()

    # 6. 定义函数,将二维列表ｍａｐ中的元素向下移动
    def moveDown(self):
        """
            思想：方阵转置
                调用向右移动
                方针转置
        """
        self.__Tmatrix()
        self.moveRight()
        self.__Tmatrix()

    # 7. 定义函数，产生新数字
    def generateNewNum(self):
        # ranNum = random.randint(1,10)
        # if ranNum != 4:
        #     ranNum = 2
        self.__list_empty_location.clear()
        for item in self.__getZero():
            self.__list_empty_location.append(item)
        if len(self.__list_empty_location) == 0:
            return
        ranPos = random.choice(self.__list_empty_location)
        self.__map[ranPos.r][ranPos.c] = self.__select_random_number()

    def __select_random_number(self):
        return 4 if random.randint(1, 10) == 1 else 2

    # 　获得游戏中中空位的位置
    def __getZero(self):
        for i in range(len(self.__map)):
            for c in range(len(self.__map[i])):
                if self.__map[i][c] == 0:
                    yield LocationModel(i, c)

    def is_game_over(self):
        if len(self.__list_empty_location) > 0:
            return False
        for r in range(len(self.map)):
            for c in range(len(self.map[r])-1):
                if self.map[r][c] == self.map[r][c+1] or self.map[c][r] == self.map[c+1][r]:
                    return False
        return True


# Test for Controller
# if __name__ == "__main__":
#     controller = GameCoreController()
#     controller.moveUp()
#     print(controller.map)
#     controller.generateNewNum()
#     print(controller.map)
