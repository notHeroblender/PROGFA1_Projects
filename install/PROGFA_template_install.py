import os
import shutil
import sys


def get_pycharm_config_paths():
    """
    Gets all PyCharm configuration paths based on the operating system (supports Windows, macOS, Linux).
    """
    paths = []
    if os.name == 'nt':  # Windows
        base_path = os.path.join(os.getenv('APPDATA'), 'JetBrains')
        if os.path.exists(base_path):
            for item in os.listdir(base_path):
                if item.startswith('PyCharm'):
                    paths.append(os.path.join(base_path, item))
    elif os.name == 'posix':  # (macOS and Linux)
        home = os.path.expanduser('~')
        if 'darwin' in os.sys.platform:  # macOS
            base_path = os.path.join(home, 'Library', 'Application Support', 'JetBrains')
        else:  # Linux
            base_path = os.path.join(home, '.config', 'JetBrains')

        if os.path.exists(base_path):
            for item in os.listdir(base_path):
                if item.startswith('PyCharm'):
                    paths.append(os.path.join(base_path, item))

    return paths


def setup_template():
    """
    Sets up the PROGFA template to use in all PyCharm installations found.
    """
    pycharm_paths = get_pycharm_config_paths()
    if not pycharm_paths:
        print("Could not find any PyCharm config paths. Are you sure you properly installed PyCharm? "
              "Check 00b_install_pycharm.pdf for instructions.")
        return

    template_source_path = 'PROGFA_template.py'
    if not os.path.isfile(template_source_path):
        print(f"Template file '{template_source_path}' does not exist. Make sure this file is in the same folder.")
        sys.exit(1)

    for pycharm_path in pycharm_paths:
        template_dir = os.path.join(pycharm_path, 'fileTemplates')
        os.makedirs(template_dir, exist_ok=True)

        destination_path = os.path.join(template_dir, 'PROGFA engine file.py')
        shutil.copyfile(template_source_path, destination_path)
        print(f"-> Template installed in:\n{destination_path}")

    print("=> PROGFA template setup is complete for all detected PyCharm installations.")


if __name__ == "__main__":
    setup_template()
