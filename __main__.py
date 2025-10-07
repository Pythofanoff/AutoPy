import os


if __name__ == '__main__':

    with open('.gitignore', 'w') as file: file.write('')

    with open('README.txt', 'w', encoding='UTF-8') as file: file.write('')

    with open('pyproject.toml', 'w') as file: file.write('')

    os.makedirs("src", exist_ok=True)

    with open('src/main.py', 'w') as file: file.write('')

    os.makedirs("src/tests", exist_ok=True)
    os.makedirs("src/logs", exist_ok=True)
    os.makedirs("src/configs", exist_ok=True)
    os.makedirs("src/functions", exist_ok=True)
    os.makedirs("src/classes", exist_ok=True)
    os.makedirs("src/images", exist_ok=True)
    os.makedirs("src/cashes", exist_ok=True)

