try: 
    import os, time, venv 
    from APySC.PATHS import PATH_FLD, PATH_FLE, CNST_TXT
     
except ImportError as e: 
    print(f"Not enough trace dependencies: {e}")
   
 
if __name__ == "__main__":
    
    def enum_paths(target:tuple):
        for el in target:
            if target == PATH_FLD: os.makedirs(el, exist_ok=True) 
            elif el == '.gitignore' and os.path.exists('./venv'): open('.gitignore', "w", encoding="UTF-8").write(CNST_TXT) 
            else: open(el, "x", encoding="UTF-8")
        
            print(f'[Spent: {round(time.time() - start, 3)}]: Create {el}')
     
    sep = '-' * 15 
 
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
 
    try:
        venv.create('venv') 
    except: print("There is no following dependency: venv") 
    
    try: 
        enum_paths(PATH_FLD)
        enum_paths(PATH_FLE)
         
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