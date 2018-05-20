## Globals ##


import os
import pystache
import sys
import subprocess


## Helpers ##


def generate_project(project_name):
    """
    Generates template files for a specific project (written by @jimfleming).

    @param project_name:
    @param install_dependencies:
    @return:
    """

    project_config = {"project_name": project_name}

    # Copy template to current directory
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "template"))
    project_dir = os.getcwd()

    if not os.path.exists(template_dir):
        sys.stdout.write(' '.join([template_dir, "containing template files does not exist"]))
        exit(1)

    # Recurse files and directories, replacing their filename with the
    # template string and the file contents with the template strings
    for root, dirs, files in os.walk(template_dir):
        rel_root = os.path.relpath(root, start=template_dir)
        for dirname in dirs:
            dest_dir = os.path.normpath(os.path.join(project_dir, rel_root, dirname))
            dest_dir = pystache.render(dest_dir, project_config)

            if os.path.exists(dest_dir):
                sys.stdout.write(' '.join([dest_dir, "already exists, skipping..."]))
                continue

            os.mkdir(dest_dir)

        for filename in files:
            _, extension = os.path.splitext(filename)
            if extension == ".pyc":
                continue

            src_path = os.path.join(root, filename)

            dest_path = os.path.normpath(os.path.join(project_dir, rel_root, filename))
            dest_path = pystache.render(dest_path, project_config)

            if os.path.exists(dest_path):
                sys.stdout.write(' '.join([dest_path, "already exists, skipping..."]))
                continue

            with open(src_path) as f:
                file_str = f.read()

            file_str = pystache.render(file_str, project_config)

            with open(dest_path, 'w') as f:
                f.write(file_str)

    sys.stdout.write(' '.join(["Project created:", project_dir, '\n']))


## Main ##


def main():
    if (len(sys.argv) < 2):
        sys.stdout.write("Error: You need to include a project name")
        sys.exit(1)
    else:
        generate_project(sys.argv[1])

        # BUG: These need to be run in the user's project directory, not PyReserve's directory
        setup = subprocess.Popen(["python3", "setup.py", "sdist"], stdout=subprocess.PIPE)
        subprocess.Popen(["twine", "register", "dist/*"])
        subprocess.Popen(["twine", "upload", "dist/*"])
