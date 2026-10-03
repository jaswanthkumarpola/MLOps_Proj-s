import os

def get_project_description(project_path):
    readme_path = os.path.join(project_path, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip main headers or empty lines
                if line and not line.startswith('#'):
                    # Truncate if it's too long
                    if len(line) > 100:
                        return line[:97] + "..."
                    return line
    return "No description provided."

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Folders to ignore
    ignore_folders = {'.git', '.vscode', '__pycache__', 'venv', '.idea', 'scratch', 'node_modules'}
    
    projects = []
    
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path) and item not in ignore_folders and not item.startswith('.'):
            projects.append(item)
            
    projects.sort()
    
    readme_content = "# MLOps Projects Repository\n\n"
    readme_content += "Welcome to the MLOps projects repository. This README is automatically generated and updated whenever a new project is added.\n\n"
    readme_content += "## 🚀 Projects\n\n"
    
    if not projects:
        readme_content += "No projects found yet.\n"
    else:
        readme_content += "| Project Name | Description |\n"
        readme_content += "| --- | --- |\n"
        for project in projects:
            desc = get_project_description(os.path.join(root_dir, project))
            # Escape pipes for markdown table
            desc = desc.replace('|', '\\|')
            readme_content += f"| **[{project}](./{project})** | {desc} |\n"
            
    readme_content += "\n## 🤖 Automation\n\n"
    readme_content += "This README is automatically generated using a Git `pre-commit` hook that runs `update_readme.py` before every commit. You just need to commit your new project, and this README will update automatically!\n"

    readme_path = os.path.join(root_dir, 'README.md')
    with open(readme_path, 'w') as f:
        f.write(readme_content)

if __name__ == '__main__':
    main()
