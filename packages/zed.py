from utils.handle_install import is_package_installed
from utils.handle_install import install_package


def install_zed() -> None:
    package_name: str = "zed"
    is_zed_installed: bool = is_package_installed(package_name, "~/.local/bin/zed")
    if is_zed_installed:
        return
    try:
        query: str = "curl -f https://zed.dev/install.sh | sh -s -- -y"
        install_package(query, package_name)
        return
    except Exception as error:
        print(f"error: error on install zed: {error}")
        return
