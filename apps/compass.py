from utils.handle_install import serialize_install_packages
from utils.handle_install import is_package_installed


def install_mongodb_compass() -> None:
    if is_package_installed("mongodb-compass"):
        return
    curl_query: dict[str, str] = {
        "Download MongoDB Compass": "wget https://downloads.mongodb.com/compass/mongodb-compass_1.35.0_amd64.deb",
        "Install MongoDB Compass package": "sudo dpkg -i mongodb-compass_1.35.0_amd64.deb",
        "Fix dependencies (if needed)": "sudo apt-get install -f -y",
        "Remove .deb file after installation": "rm mongodb-compass_1.35.0_amd64.deb",
    }
    try:
        serialize_install_packages(curl_query)
    except Exception as error:
        print(f"{error}")
        return
    return
