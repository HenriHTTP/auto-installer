from utils.handle_install import serialize_install_packages
from utils.handle_install import is_package_installed


def install_git() -> None:
    git_exist: bool = is_package_installed("git")
    if git_exist:
        return
    curl_query: dict[str, str] = {"git": "sudo apt install -y git"}
    try:
        serialize_install_packages(curl_query)
    except Exception as error:
        print(f"{error}")
        return
    return
