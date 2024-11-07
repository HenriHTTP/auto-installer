from apps.compass import install_mongodb_compass
from apps.insomnia import install_insomnia
from packages.docker import install_docker
from packages.git import install_git
from packages.rust import install_rust
from packages.zed import install_zed
from packages.node import install_node
from typing import Callable


def install_packages():
    packages: list[Callable[[], None]] = [
        install_zed,
        install_rust,
        install_node,
        install_docker,
        install_git,
        install_mongodb_compass,
        install_insomnia,
    ]
    for install in packages:
        try:
            install()
        except Exception as error:
            print(f"Error during {install.__name__}: {error}")


if __name__ == "__main__":
    install_packages()
