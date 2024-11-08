from utils.handle_install import is_package_installed
from utils.handle_install import serialize_install_packages


def install_docker() -> None:
    if is_package_installed("docker"):
        return
    curl_query: dict[str, str] = {
        "Update packages": "sudo apt update -y",
        "pre-requisite packages": "sudo apt install -y apt-transport-https ca-certificates curl software-properties-common",
        "Docker GPG Key": (
            "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | "
            "sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg"
        ),
        "Docker Repository": (
            "echo 'deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] "
            "https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable' | "
            "sudo tee /etc/apt/sources.list.d/docker.list > /dev/null"
        ),
        "Docker": "sudo apt install -y docker-ce",
    }
    try:
        serialize_install_packages(curl_query)
    except Exception as error:
        print(f"{error}")
        return
    return
