from utils.handle_install import is_package_installed
from utils.handle_install import serialize_install_packages


def install_node() -> None:
    node_exist: bool = is_package_installed("node")
    if node_exist:
        return
    curl_query = {
        "Setup Node.js 18 repository": "curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -",
        "Install Node.js 18": "sudo apt install -y nodejs",
    }
    try:
        serialize_install_packages(curl_query)
    except Exception as error:
        print(f"{error}")
        return
    return
