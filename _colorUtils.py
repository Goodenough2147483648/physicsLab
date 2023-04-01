_BLACK = '\033[30m'
_RED = '\033[31m'
_GREEN = '\033[32m'
_YELLOW = '\033[33m'
_BLUE = '\033[34m'
_MAGENTA = '\033[35m'
_CYAN = '\033[36m'
_WHITE = '\033[37m'
_DEFAULT = '\033[39m'

# ��ӡwrite_Experiment����Ϣʱ�Ƿ�ʹ�ò�ɫ��
printColor = True

def printf(msg: str) -> None:
    if not isinstance(msg, str):
        raise TypeError
    if printColor:
        print(f"{_GREEN}{msg}{_DEFAULT}")
    else:
        print(msg)
