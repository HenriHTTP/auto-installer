from utils.handle_install import is_package_installed
from utils.handle_install import serialize_install_packages


def install_zed() -> None:
    package_name: str = "zed"
    is_zed_installed: bool = is_package_installed(package_name, "~/.local/bin/zed")
    if is_zed_installed:
        return
    curl_query: dict[str, str] = {
        "zed": "curl -f https://zed.dev/install.sh | sh -s -- -y"
    }
    try:
        serialize_install_packages(curl_query)
    except Exception as error:
        print(f"{error}")
        return
    return
