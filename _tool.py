from typing import Union

# ��������physicsLab�е�����
def roundData(num: Union[int, float]):
    if isinstance(num, int):
        return float(num)
    return round(num, 4)

# ��������ַ���
def randString() -> str:
    from string import ascii_letters as _ascii_letters, digits as _digits
    from random import choice as _choice
    return ''.join(_choice(_ascii_letters + _digits) for _ in range(34))
