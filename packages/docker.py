from utils.handle_install import install_package
from utils.handle_install import is_package_installed


def install_docker() -> None:
    if is_package_installed("docker"):
        print("Docker já está instalado.")
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
    for package_name, query in curl_query.items():
        try:
            install_package(package_name, query)
        except Exception as error:
            print(f"Error: Failed to execute '{package_name}': {error}")
            return
    return
