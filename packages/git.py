from utils.handle_install import install_package
from utils.handle_install import is_package_installed

def install_git() -> None:
    git_exist: bool = is_package_installed("git")
    if git_exist:
        return
    try:
        curl_query: str = "sudo apt install -y git"
        install_package(curl_query, "Git")
        return
    except Exception as error:
        print(f"Error: Failed to install Git: {error}")
        return
