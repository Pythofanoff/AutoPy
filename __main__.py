try:
    import os, time

except ImportError as e:
    print(f"Not enough trace dependencies: {e}")


if __name__ == "__main__":
    sep = '-' * 15

    src_fld = ('src', 'src/tests', 'src/logs', 'src/configs', 'src/functions', 'src/classes', 'src/images', 'src/cashes')
    
    
    start = time.time()
    
    print(sep)
    print('AutoPy start...')
    print(sep)

    try:
        for el in src_fld:
            os.makedirs(el, exist_ok=True)


        with open(".gitignore", "x") as file: pass

        with open("README.md", "x", encoding="UTF-8") as file: pass

        with open("pyproject.toml", "x") as file: pass

        with open("src/main.py", "x") as file: pass

    except FileExistsError as e: print(f"The following files already exist: {e}")

    finally: print(f"{sep} \n[Spent {round(time.time() - start, 3)}]: AutoPy created the project structure successfully \n{sep}")


