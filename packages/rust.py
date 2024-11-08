from utils.handle_install import is_package_installed
from utils.handle_install import serialize_install_packages


def install_rust() -> None:
    package_name: str = "rustc"
    is_rust_installed: bool = is_package_installed(package_name)
    if is_rust_installed:
        return
    curl_query: dict[str, str] = {
        "rustc": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y"
    }
    try:
        serialize_install_packages(curl_query)
    except Exception as error:
        print(f"{error}")
        return
    return
