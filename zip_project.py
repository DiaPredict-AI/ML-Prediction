import os
import zipfile

def zip_folder(folder_path, output_path):
    # Exclude directories
    exclude_dirs = {'.git', 'venv', '.venv', '__pycache__', '.ipynb_checkpoints', '.vscode'}
    # Exclude files
    exclude_files = {
        'ML_Project.zip', 
        'zip_project.py', 
        '.DS_Store', 
        'Thumbs.db'
    }
    
    print(f"Starting to zip the project folder: {folder_path}")
    print(f"Excluding directories: {list(exclude_dirs)}")
    print(f"Excluding files: {list(exclude_files)}")
    
    count = 0
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            # Prune excluded directories in-place so os.walk doesn't descend into them
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if file in exclude_files:
                    continue
                # Skip any existing .zip files
                if file.endswith('.zip'):
                    continue
                
                full_path = os.path.join(root, file)
                # Compute relative path for storing in zip
                rel_path = os.path.relpath(full_path, folder_path)
                
                # Exclude temporary or lock files
                if file.startswith('.~') or file.startswith('~$'):
                    continue
                
                print(f"  Adding: {rel_path}")
                zipf.write(full_path, rel_path)
                count += 1
                
    print(f"\n[SUCCESS] Clean zip file created successfully at: {output_path}")
    print(f"Total files zipped: {count}")
    print(f"Size of new zip file: {os.path.getsize(output_path) / 1024:.2f} KB")

if __name__ == '__main__':
    project_dir = os.path.dirname(os.path.abspath(__file__))
    zip_path = os.path.join(project_dir, 'ML_Project.zip')
    zip_folder(project_dir, zip_path)
