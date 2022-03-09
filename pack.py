import os
import re
import shutil


def delete_all(delete_path):
    if not os.listdir(delete_path):
        pass
    else:
        for i in os.listdir(delete_path):
            path_file = os.path.join(delete_path, i)
            if os.path.isfile(path_file):
                os.remove(path_file)
            else:
                delete_all(path_file)
                shutil.rmtree(path_file)


with open('./setup.py', 'r+') as setup:
    setup.seek(0, 0)
    read = setup.read()
    find = re.findall('version=(.+?),', read)
    v_id = float(eval(find[0].replace('.', '')))
    setup.seek(0, 0)
    num = str(v_id + 1)
    writing = read.replace(find[0], "'" + num[0] + '.' + num[1] + '.' + num[2] + "'")
    setup.write(writing[:-1])
os.system('python3 setup.py sdist bdist_wheel')
os.system('twine upload dist/* --u CleverCreator --p Bitjop-byfbeg-3sazry')
delete_all('./dist')

                