![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)


### Installation Guide:

```bash
git clone "https://github.com/ChrisRosales/ProjectAutomation.git"
cd ProjectInitializationAutomation
pip install -r requirements.txt
MAKE SURE to enter in username, password, and the path of your projects folder in the module named 'config.py'
Also be sure to change Github username in HTML path in both 'removeRep.py' and 'terminate.py' to your own.
```

### Usage:

We have a few options here...

```bash 'create.py <name of your folder/project>' ``` -> Creates a Repository for your Project as well as a folder in your path selected
```bash 'removeRep.py <name of your folder/project>' ``` -> Removes the repository by browser automation
```bash 'delete.py <name of your folder/project>' ``` - Deletes folder from os from path selected
```bash 'terminate.py <name of your folder/project>' ``` - Terminates BOTH Respository and Project (Basically 'removeRep.py' and 'delete.py' together)
