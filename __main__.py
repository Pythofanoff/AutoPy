try:
    import os, time

except ImportError as e:
    print(f"Not enough trace dependencies: {e}")


if __name__ == "__main__":
    start = time.time()
    sep = '-' * 15

    print(sep)
    print('AutoPy start...')
    print(sep)

    try:

        os.makedirs("src", exist_ok=True)
        os.makedirs("src/tests", exist_ok=True)
        os.makedirs("src/logs", exist_ok=True)
        os.makedirs("src/configs", exist_ok=True)
        os.makedirs("src/functions", exist_ok=True)
        os.makedirs("src/classes", exist_ok=True)
        os.makedirs("src/images", exist_ok=True)
        os.makedirs("src/cashes", exist_ok=True)


        with open(".gitignore", "x") as file: pass

        with open("README.txt", "x", encoding="UTF-8") as file: pass

        with open("pyproject.toml", "x") as file: pass

        with open("src/main.py", "x") as file: pass

    except FileExistsError as e: print(f"The following files already exist: {e}")

    finally: print(f"{sep} \n[Spent {round(time.time() - start, 3)}]: AutoPy created the project structure successfully \n{sep}")


