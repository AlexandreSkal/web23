import os
import subprocess

def create_project_structure(project_name):
    folders = [
        f'{project_name}',
        f'{project_name}/docs',
        f'{project_name}/tests',
        f'{project_name}/app',
        f'{project_name}/app/models',
        f'{project_name}/app/db',
        f'{project_name}/app/notebooks'
    ]

    files = {
        f"{project_name}/README.md": "#Project Documentation",
        f"{project_name}/app/main.py": "",
        f"{project_name}/.gitignore":         
"""
# Arquivos de ambiente virtual
venv/
.env/

# Cache do Python
__pycache__/
*.py[cod]

# Arquivos de log
*.log

# Arquivos de depuração
*.swp
*.swo
*.bak
*.tmp

# Configurações de IDE
.vscode/
.idea/
*.iml

# Arquivos gerados automaticamente
*.sqlite3
*.db
.DS_Store

# Arquivos de pacotes Python
*.egg
*.egg-info/
dist/
build/

# Arquivos do pytest e cobertura de testes
.pytest_cache/
.coverage
htmlcov/

# Jupyter Notebooks
.ipynb_checkpoints/

# Arquivos temporários de sistemas operacionais
Thumbs.db
"""
    }

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    basic_commands(project_name)
    
    for filepath, content in files.items():
        with open(filepath, "w") as file:
            file.write(content)
            

    print(f'Project {project_name} structure created!')

def basic_commands(project_name):
    #path = f'{project_name}'
    
    venv_command = ["python", "-m", "venv", project_name]
    freeze_command = ["pip", "freeze", ">", "requirements.txt"]
    
    try:
        subprocess.run(venv_command, check=True)
        subprocess.run(freeze_command, check=True)
        print(f'Virtual enviroment and requirements create in: {project_name}')
    except:
        f'Unexpected error'

if __name__ == "__main__":
    project_name = input("Enter the project name:")
    create_project_structure(project_name)