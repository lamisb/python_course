###  Python Virtual Environment (`venv`) Commands

| Command | Description |
|----------|-------------|
| `python3 -m venv myprojectname` | Create a new virtual environment named **myprojectname** |
| `source myprojectname/bin/activate` | Activate the virtual environment (macOS/Linux) |
| `myprojectname\Scripts\activate` | Activate the virtual environment (Windows PowerShell/CMD) |
| `deactivate` | Exit the virtual environment |
| `pip install <package>` | Install a package inside the active virtual environment |
| `pip freeze > requirements.txt` | Save the list of installed packages to a file |
| `pip install -r requirements.txt` | Install packages listed in a requirements file |
| `rm -rf myprojectname` | Delete the virtual environment folder (macOS/Linux) |
| `rmdir /s myprojectname` | Delete the virtual environment folder (Windows) |

💡 **Tip:** It’s common to name your environment folder `.venv` or `venv` and add it to your `.gitignore` so it’s not committed to GitHub.
