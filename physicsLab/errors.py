# ���ڴ���Զ��������
# ������ʱ��package����Ҫ�쳣�����ʲ�Ϊ�ļ�˽�б���
import physicsLab._colorUtils as _colorUtils

def warning(msg: str) -> None:
    _colorUtils.printf("Warning: " + msg, _colorUtils.YELLOW)

# ��ʵ���쳣
class openExperimentError(Exception):
    def __str__(self):
        return "open a experiment but find nothing."

class wireColorError(Exception):
    def __str__(self):
        return "illegal wire color."

class wireNotFoundError(Exception):
    def __str__(self):
        return "Unable to delete a nonexistent wire"

class bitLengthError(Exception):
    def __str__(self):
        return "illegal bitLength number"

# ����ʵ���Ѵ���
class experimentExistError(Exception):
    def __str__(self):
        return 'Duplicate name archives are forbidden'

# �򿪵�ʵ������õ�Ԫ������
class experimentTypeError(Exception):
    def __str__(self):
        return "The type of experiment does not match the element"