from pathlib import Path

def parse_folder(path):
  

    files = []
    folders = []
    for item in path.iterdir():
        if item.is_file():
            files.append(item.name)
        elif item.is_dir():
            folders.append(item.name)
        
            
        
            
    return files, folders


print("result",parse_folder(Path('/Users/grejule/Documents/GitHub-home/Python/Python-practice')))