# Ԫ������ϵ
# һ�����ŵĳ�Ϊ0.15����Ϊ0.075
# һ�����ŵĳ�����ΪԪ������ϵ��x, y�ĵ�λ����
# z��ĵ�λ������ԭ����ϵ��0.1
#
# ���λ�˷�������Ԫ����λ�ñ��뾭����������ʹԪ����������
# x, z�᲻������
# y�������Ϊ +0.045

import elementsClass as ecls

# װ����
def xyz(elementSelf: ecls.elementObject):
    if elementSelf.isElementPosition == True:
        return 