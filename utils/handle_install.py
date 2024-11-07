import os
import shutil
import subprocess


def is_package_installed(package_name: str, default_path: str = "") -> bool:
    package_exist: str | None = shutil.which(package_name)
    default_path_exist: bool = (
        os.path.exists(os.path.expanduser(default_path)) 
        if default_path 
        else False
    )
    if package_exist or default_path_exist:
        print(f"package {package_name} is installed")
        return True
    return False


def install_package(query: str, name_package: str) -> None:
    try:
        subprocess.run(query, shell=True, check=True)
        print(f"{name_package} has been installed successfully.")
        return
    except subprocess.CalledProcessError as error:
        print(f"error: error on install: {error}")
        return
