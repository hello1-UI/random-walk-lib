# random_walk_lib/random_walk.py
import random
from typing import List, Optional


class RandomWalk:
    """
    随机游走类，实现二维平面上的随机方向移动

    Attributes:
        rn (list): 当前位置坐标 [x, y]
        all_positions (list): 记录所有走过的位置，格式为 [[x1,y1], [x2,y2], ...]
    """

    def __init__(self, start_position: List[int] = None):
        """
        初始化随机游走对象

        Args:
            start_position: 起始位置，默认 [0, 0]
        """
        self.rn = start_position if start_position is not None else [0, 0]
        self.CHOICES = ['up', 'down', 'left', 'right']
        self.UD = ['up', 'down']
        self.LR = ['left', 'right']
        self.all_positions = [self.rn.copy()]  # 初始化位置记录

    def _choice_walk(self) -> List[int]:
        """私有方法：执行单次随机移动，更新位置"""
        choice = random.choice(self.CHOICES)
        if choice in self.UD:
            self.rn[0] += 1 if choice == 'up' else -1
        else:
            self.rn[1] += 1 if choice == 'right' else -1
        self.all_positions.append(self.rn.copy())
        return self.rn

    def walk(self, steps: int, verbose: bool = True) -> List[List[int]]:
        """
        执行指定步数的随机游走

        Args:
            steps: 移动步数
            verbose: 是否打印每步位置，默认 True

        Returns:
            所有走过的位置列表
        """
        for step in range(1, steps + 1):
            self._choice_walk()
            if verbose:
                print(f"Step {step}: x={self.rn[0]}, y={self.rn[1]}")
        return self.all_positions

    def plot_walk(self, figsize: tuple = (8, 6)) -> None:
        """
        可视化随机游走路径（需安装matplotlib）

        Args:
            figsize: 图表尺寸，默认 (8,6)
        """
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            raise ImportError("请先安装matplotlib: pip install matplotlib")

        x_coords = [pos[0] for pos in self.all_positions]
        y_coords = [pos[1] for pos in self.all_positions]

        plt.figure(figsize=figsize)
        plt.plot(x_coords, y_coords, marker='o', markersize=4, linestyle='-', color='blue')
        plt.scatter(x_coords[0], y_coords[0], color='green', s=100, label='Start')
        plt.scatter(x_coords[-1], y_coords[-1], color='red', s=100, label='End')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.title('Random Walk Path')
        plt.legend()
        plt.grid(True)
        plt.show()

    @property
    def current_position(self) -> str:
        """返回当前位置的可读字符串"""
        return f"x position: {self.rn[0]}, y position: {self.rn[1]}"
