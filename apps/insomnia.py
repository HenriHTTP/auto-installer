from utils.handle_install import serialize_install_packages
from utils.handle_install import is_package_installed


def install_insomnia() -> None:
    if is_package_installed("insomnia"):
        return
    curl_query: dict[str, str] = {
        "Download insomnia": "wget https://github.com/Kong/insomnia/releases/download/core%4010.1.1/Insomnia.Core-10.1.1.deb -O insomnia.deb",
        "Install MongoDB Compass package": "sudo dpkg -i insomnia.deb",
        "Remove .deb file after installation": "rm insomnia.deb",
    }
    try:
        serialize_install_packages(curl_query)
    except Exception as error:
        print(f"{error}")
        return
    return
