try:
    import os, time, venv

except ImportError as e:
    print(f"Not enough trace dependencies: {e}")

if __name__ == "__main__":
    sep = '-' * 15

    src_fld = ('src', 'src/tests', 'src/logs', 'src/configs', 'src/functions', 'src/classes', 'src/images', 'src/caсhes')
    src_fle = ('.gitignore', 'README.md', 'pyproject.toml', 'src/main.py')

    start = time.time()

    print('''

░█████╗░██████╗░██╗░░░██╗░██████╗░█████╗░
██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
███████║██████╔╝░╚████╔╝░╚█████╗░██║░░╚═╝
██╔══██║██╔═══╝░░░╚██╔╝░░░╚═══██╗██║░░██╗
██║░░██║██║░░░░░░░░██║░░░██████╔╝╚█████╔╝
╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░

░██████╗████████╗░█████╗░██████╗░████████╗░░░░░░░░░
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝░░░░░░░░░
╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░░░░░░░░░░
░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░░░░░░░░░░
██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░██╗██╗██╗
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝╚═╝''')

    # ДОБАВИТЬ ПРОВЕРКУ НА НАЛИЧИЕ СУЩ. БИБЛИОТЕКИ.
    venv.create('venv')
    
    try:
        for el in src_fld:
            print(f'[Spent: {round(time.time() - start, 3)}]: Create {el}')

            os.makedirs(el, exist_ok=True)
            

        for el in src_fle:
            print(f'[Spent: {round(time.time() - start, 3)}]: Create {el}')

            if el == '.gitignore' and os.path.exists('./venv'): open('.gitignore', "w", encoding="UTF-8").write('venv')
            else: open(el, "x", encoding="UTF-8")


    except FileExistsError as e: print(f"The following files already exist: {e}")

    finally: 
        print('''
░█████╗░██████╗░██╗░░░██╗░██████╗░█████╗░
██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
███████║██████╔╝░╚████╔╝░╚█████╗░██║░░╚═╝
██╔══██║██╔═══╝░░░╚██╔╝░░░╚═══██╗██║░░██╗
██║░░██║██║░░░░░░░░██║░░░██████╔╝╚█████╔╝
╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░

███████╗██╗███╗░░██╗██╗░██████╗██╗░░██╗██╗
██╔════╝██║████╗░██║██║██╔════╝██║░░██║██║
█████╗░░██║██╔██╗██║██║╚█████╗░███████║██║
██╔══╝░░██║██║╚████║██║░╚═══██╗██╔══██║╚═╝
██║░░░░░██║██║░╚███║██║██████╔╝██║░░██║██╗
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝''')

        print(f"{sep} \n[Spent {round(time.time() - start, 3)}]: AutoPy created the project structure successfully \n{sep}")




