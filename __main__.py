try:
    import os, time

except ImportError as e:
    print(f"Not enough trace dependencies: {e}")


if __name__ == "__main__":
    sep = '-' * 15

    src_fld = ('src', 'src/tests', 'src/logs', 'src/configs', 'src/functions', 'src/classes', 'src/images', 'src/cashes')
    
    src_fle = ('.gitignore', 'README.md', 'pyproject.toml', 'src/main.py')

    start = time.time()
    
    print(sep)
    print('AutoPy start...')
    print(sep)

    try:
        for el in src_fld:
            os.makedirs(el, exist_ok=True)

        for el in src_fle:
           with open(el, "x", encoding="UTF-8") as file: pass

    except FileExistsError as e: print(f"The following files already exist: {e}")

    finally: print(f"{sep} \n[Spent {round(time.time() - start, 3)}]: AutoPy created the project structure successfully \n{sep}")


