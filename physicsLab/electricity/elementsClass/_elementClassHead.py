# coding=utf-8
import physicsLab._tools as _tools
from typing import Callable as _Callable
import physicsLab._fileGlobals as _fileGlobals
import physicsLab.electricity.elementPin as _elementPin
import physicsLab.electricity.elementXYZ as _elementXYZ

# 是否为big_Element
is_big_Element: bool = False

# 所有元件的父类
class elementBase:
    # 设置原件的角度
    def set_Rotation(self, xRotation: _tools.numType = 0, yRotation: _tools.numType = 0,
                     zRotation: _tools.numType = 180):
        if not (
                isinstance(xRotation, (int, float)) and
                isinstance(yRotation, (int, float)) and
                isinstance(zRotation, (int, float))
        ):
            raise RuntimeError('illegal argument')

        self._arguments["Rotation"] = \
            f"{_tools.roundData(xRotation)},{_tools.roundData(zRotation)},{_tools.roundData(yRotation)}"
        return self

    # 重新设置元件的坐标
    def set_Position(self, x: _tools.numType, y: _tools.numType, z: _tools.numType):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
            raise RuntimeError('illegal argument')
        x, y, z = _tools.roundData(x), _tools.roundData(y), _tools.roundData(z)
        del _fileGlobals.elements_Position[self._position]
        self._position = (x, y, z)
        self._arguments['Position'] = f"{x},{z},{y}"
        _fileGlobals.elements_Position[self._position] = self
        return self

    # 格式化坐标参数，主要避免浮点误差
    def format_Position(self) -> tuple:
        if not isinstance(self._position, tuple) or self._position.__len__() != 3:
            raise RuntimeError("Position must be a tuple of length three but gets some other value")
        self._position = (_tools.roundData(self._position[0]), _tools.roundData(self._position[1]),
                          _tools.roundData(self._position[2]))
        return self._position

    # 获取原件的坐标
    def get_Position(self) -> tuple:
        return self._position

    # 获取父类的类型
    def father_type(self) -> str:
        return 'element'

    # 获取元件的index（每创建一个元件，index就加1）
    def get_Index(self) -> int:
        return self._index

    # 获取子类的类型（也就是ModelID）
    def type(self) -> str:
        return self._arguments['ModelID']

    # 打印参数
    def print_arguments(self) -> None:
        print(self._arguments)


# __init__ 装饰器
_index = 1


def element_Init_HEAD(func: _Callable) -> _Callable:
    def result(
            self,
            x: _tools.numType = 0,
            y: _tools.numType = 0,
            z: _tools.numType = 0,
            elementXYZ: bool = None
    ) -> None:
        if not (
                isinstance(x, (float, int)) and
                isinstance(y, (float, int)) and
                isinstance(z, (float, int))
        ):
            raise TypeError('illegal argument')
        # 初始化全局变量
        global is_big_Element
        is_big_Element = False

        x, y, z = _tools.roundData(x, y, z)
        self._position = (x, y, z)
        # 元件坐标系
        if elementXYZ == True or (_elementXYZ.is_elementXYZ() == True and elementXYZ is None):
            x, y, z = _elementXYZ.xyzTranslate(x, y, z)
        func(self, x, y, z)
        # 若是big_Element，则修正坐标
        if is_big_Element:
            x, y, z = _elementXYZ.amend_big_Element(x, y, z)

        self._arguments["Identifier"] = _tools.randString(32)
        # x, z, y 物实采用欧拉坐标系
        self._arguments["Position"] = f"{x},{z},{y}"
        _fileGlobals.Elements.append(self._arguments)

        # 该坐标是否已存在，则存入列表
        if self._position in _fileGlobals.elements_Position.keys():
            _fileGlobals.elements_Position[self._position]['self'].append(self)
        else:
            elementDict: dict = {
                'self': [self],
                'elementXYZ': _elementXYZ.is_elementXYZ,  # 是否为元件坐标系
                'originPosition': tuple(_elementXYZ.get_OriginPosition())  # 坐标原点
            }
            _fileGlobals.elements_Position[self._position] = elementDict
        self.set_Rotation()
        # 通过元件生成顺序来索引元件
        global _index
        self._index = _index
        _fileGlobals.elements_Index.append(self)
        # 元件index索引加1
        _index += 1
    return result


# 双引脚模拟电路原件的引脚
def two_pin_ArtificialCircuit_Pin(cls):
    @property
    def red(self):
        return _elementPin.element_Pin(self, 0)

    cls.red, cls.l = red, red

    @property
    def black(self):
        return _elementPin.element_Pin(self, 1)

    cls.black, cls.r = black, black

    return cls
