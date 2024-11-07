import subprocess
from utils.handle_install import is_package_installed
from utils.handle_install import install_package


def install_rust() -> None:
    package_name: str = "rustc"
    is_rust_installed: bool = is_package_installed(package_name)
    if is_rust_installed:
        return
    try:
        query: str = (
            "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y"
        )
        install_package(query, package_name)
        print("rust has been installed successfully.")
        return
    except subprocess.CalledProcessError as error:
        print(f"error: error on install rust: {error}")
    return
