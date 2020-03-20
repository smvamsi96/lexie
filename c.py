import os

origin_path = '/Users/smvamsi/Public/'

destnation_path = '/Users/smvamsi/Code/lexie/grey/static/grey/'

for uploaded_file in os.listdir(origin_path):
    src = origin_path + uploaded_file
    dst = destnation_path + uploaded_file
    os.symlink(src, dst)
    print(f"symlinked - {dst}")
