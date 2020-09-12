"""
    游戏界面逻辑模块
"""
import os

from bll import GameCoreController


class GameConsoleView:
    """
        控制台界面类
    """
    def __init__(self):
        self.__controller = GameCoreController()
        self.__move_direction = ""

    def __start(self):
        for i in range(2):
            self.__controller.generateNewNum()
        self.__draw_map()

    def __update(self):
        print("W,S,A,D键控制方向,输入exit退出游戏。")
        while True:
            self.__move_map_for_input()
            self.__controller.generateNewNum()
            if self.__controller.is_game_over():
                print("失败了！")
                break
            self.__draw_map()
            if self.__move_direction == "exit":
                if input("您确定要结束游戏吗? 请输入Yes/No　") == "Yes":
                    break

    def __move_map_for_input(self):
        self.__move_direction = input("请输入移动方向：　")
        if self.__move_direction == "w":
            self.__controller.moveUp()

        elif self.__move_direction == "s":
            self.__controller.moveDown()

        elif self.__move_direction == "a":
            self.__controller.moveLeft()

        elif self.__move_direction == "d":
            self.__controller.moveRight()

    def __draw_map(self):
        # os.system("clear")
        for line in self.__controller.map:
            for item in line:
                print(item , end = "\t")
            print()

    def main(self):
        self.__start()
        self.__update()
