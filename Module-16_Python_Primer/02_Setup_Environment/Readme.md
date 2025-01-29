# Setting up the environment for developing apps with Python

To get started, we need below applications:

- Python installer
- IDE (Pycharm/Spyder/IntelliJ)

## 1. Install and Configure Python

- Python supports all the OS platforms:
  - Windows
  - Linux
  - MacOS
- Minimum system requirement for Python installation
  - **Operating System**
    - Windows 8 (or above)
    - Linux RHEL 6/7, 64-bit | Ubuntu
    - Mac OS X 10.11 or higher, 64-bit
  - **Processor**: x86 64-bit CPU (Intel/AMD)
  - **Memory**: 4 GB RAM
  - **Storage**: 20 GB free disk space

### 1.1: Install Python using `Python Installer`

- Official Website - https://www.python.org/
- Download and Install the latest version of Python as per your system's OS:
  - [Windows](https://www.python.org/downloads/windows/)
  - [Linux](https://www.python.org/downloads/source/)
  - [MacOS](https://www.python.org/downloads/macos/)
- To verify the python installation, go to start menu >> Command prompt >> and run command `python --version` and see if returns current installed version of python.
- When you install Python, there are some other programs also which gets installed namely:
  - Python Shell
  - IDLE (Integrated Development and Learning Environment)

### 1.2: (Optional) Install Python using `Anaconda distribution`

- Official website - https://www.anaconda.com/
- The Anaconda distribution comes with Python interpreter, Jupyter notebook and many Python libraries.
- Direct link to download: https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Windows-x86_64.exe

## Step-02: Install IDE (Integrated Development Environment)

- You may install any of the below IDE (editors) for developing python apps:
  - [PyCharm](https://www.jetbrains.com/pycharm/)
    - For jupyter notebook support, install following extensions:
      - Extension Name: Jupyter (Published by Microsoft | ExtensionID: ms-toolsai.jupyter)
  - [Eclipse](https://www.eclipse.org/eclipseide/)
  - [Spyder](https://www.spyder-ide.org/)
  - [Atom](https://atom.en.uptodown.com/windows)
  - [Visual Studio Code](https://code.visualstudio.com/)
- Once you're done with the IDE (PyCharm) installation, you need to configure two things:
  - Base Interpreter (Python 3.x in our case)
  - Enable Reformat code/file settings

## Step-03: Verify all the required utilities on your system

```
# To check python
python --version

# To check pip
pip --version

# To check git
git --version
```
