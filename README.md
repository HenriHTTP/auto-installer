# AutoInstaller

This project is a Python tool for automating the installation of popular packages and tools, such as **Postman**, **MongoDB Compass**, **Docker**, **Git**, **Rust**, **Zed**, **Node.js**, and **Insomnia**. The script checks if each package is already installed, and if not, it handles the download and installation.

## Installation

1. Clone the repository:
    ```bash
    git clone hhttps://github.com/HenriHTTP/auto-installer.git
    cd auto-installer
    ```

2. Create and activate a Python virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install any project dependencies (if required):
    ```bash
    pip install -r requirements.txt
    ```

## Requirements
- Python 3.7 or higher
- Sudo permissions for package installations
- Internet connection for downloading packages

## Usage

1. Run the main script to install all listed packages:
    ```bash
    python main.py
    ```

2. The script will check if each package is installed. If not, it will handle the download and installation automatically.

## Packages Installed

This script includes the following packages:

- **Zed**: Lightweight code editor
- **Rust**: Programming language and toolchain
- **Node.js**: JavaScript runtime environment
- **Docker**: Platform for creating and managing containers
- **Git**: Version control system
- **MongoDB Compass**: GUI for MongoDB
- **Insomnia**: REST and GraphQL API testing client
