import os
import git

if __name__ == '__main__':
    string = input('update setup.py?(y/n)')

    if string:
        os.system('D:')
        os.system('cd D:\\program physicsLab\\hub')
        os.system('py setup.py sdist bdist_wheel')
        # os.system('twine upload hub/dist/*')
        # ����python��
        # pip install --upgrade xxx

    string = input('push?(y/n)')
    if string == 'y':
        repo = git.Git("/hub")
        repo.checkout('master')
        repo.merge('dev')
        repo.push('gitee', 'master')
        repo.push('github', 'master')
        repo.checkout('dev')
