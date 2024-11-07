from utils.handle_install import is_package_installed
from utils.handle_install import install_package


def install_node() -> None:
    node_exist: bool = is_package_installed("node")
    if node_exist:
        return
    curl_query = {
        "Setup Node.js 18 repository": "curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -",
        "Install Node.js 18": "sudo apt install -y nodejs"
    }
    for name_package, query in curl_query.items():
        try:
            install_package(query, name_package)
            return
        except Exception as error:
            print(f"error: error on install node: {error}")
            return
        return
