import os, shutil
os.chdir('C:/Python')
modules = os.listdir('module')
print(modules) 
for dir in os.listdir():
    # if dir == 'module':
    #     continue
    if os.path.isdir(dir):
        if not os.path.isdir(dir+'/module'):
            os.makedirs(dir+'/module')
        for file in modules:
            if file == 'test.py':
                continue
            if os.path.isfile(f'module/{file}') and '.py' in file:
                shutil.copyfile(f'module/{file}', f'{dir}/module/{file}')
            if not os.path.isdir(f'{dir}/image'):
                os.makedirs(f'{dir}/image')