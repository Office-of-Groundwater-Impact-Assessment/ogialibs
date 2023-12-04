# OGIA Python Libraries

Some commonly used python libraries.

---

## Local Development Environment Setup

Here are the steps to set up a workstation for running the code and working on this project

### 1. Clone this repository to obtain a copy of the files

- If you are using command line, follow GitHub's official tutorial [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

- Microsoft VsCode [documentation](https://docs.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette#clone-repository)

- Atlassian SourceTree [documentation](https://confluence.atlassian.com/get-started-with-sourcetree/clone-a-remote-repository-847359098.html)

### 2. Create a Conda environment with dependencies

- Copy the path to the **freeze.yml** file from the root folder of this project
- Open a Command Line (Start > Run > "cmd.exe")
- Navigate to the Scripts path of your local Anaconda installation

```msdos
Microsoft Windows [Version 10.0.19044.1766]
(c) Microsoft Corporation. All rights reserved.

H:\>c:

C:\>cd Anaconda\Scripts
```

- Run `conda env create -f` command with the full path to the freeze.yml file you copied earlier.

    The `freeze.yml` file includes a list of all python dependencies and the fixed Python version for this project.

```msdos
C:\Anaconda\Scripts>conda env create -f c:\path\to\template_project\freeze.yml

Collecting package metadata (repodata.json): done
Solving environment: done


...


#
# To activate this environment, use
#
#     $ conda activate templateproj
#
# To deactivate an active environment, use
#
#     $ conda deactivate


C:\Anaconda\Scripts>

```

Please note that in some workstations, Anaconda Navigator has a bug that prevents running this command with an error message such as;

```msdos
CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/current_repodata.json>
```

The workaround is to copy two files from `C:\Anaconda\Library\bin` to `C:\Anaconda\DLLs`

- `libcrypto-1_1-x64.*`
- `libssl-1_1-x64.*`

### 3. Activating the environment and running the code

At this stage you should have a new Conda environment called `templateproj` with all Python packages installed.

New environment should be available for selection from **Anaconda Navigator** or **Visual Studio Code** immediately after creation. For other code editors, the new environment can be referenced in `C:\Anaconda\envs\templateproj` directory of the workstation.

Activating the environment for Jupyter Notebooks Web UI;

```msdos
C:\Anaconda\Scripts>conda.bat activate templateproj

(templateproj) C:\Anaconda\Scripts>

(templateproj) C:\Anaconda\Scripts>jupyter-notebook "c:\path\to\template_project\Analytics.ipynb"
```

The last command in the example above should load a web browser with the `Analytics.ipynb` file loaded.

### 4. Running Unit Tests

Template project comes with a minimal set of unit tests as a proof of concept. Successful execution will provide insight on whether all of the requirements are installed correctly and the code behaves as expected.

Some popular IDEs like VsCode or PyCharm can run Python unit tests out of the box. For Spyder, the [module](https://github.com/spyder-ide/spyder-unittest) `spyder-ide/spyder-unittest` is recommended.

To run the test from the Windows command line, first open a terminal while `templateproj` environment is activated and navigate to the root folder of this project. The following command will then execute the tests and provide a brief report;

```msdos
python -m unittest discover tests
```

Example;

```msdos
(templateproj) C:\path\to\template_project>python -m unittest discover tests
..
----------------------------------------------------------------------
Ran 2 tests in 0.256s

OK

(templateproj) C:\path\to\template_project>
```

---

## Using this template for new projects

### Deciding what to copy

This project consist of a very basic structure of an IPython notebook project. Some of the files under the `libraries` or `tests` folders may not immediately apply to your work at early stages. The Python files in those folders can be skipped. However, preserving the naming of the folder structure across the projects is a recommended practice.

### Creating new files

Preferred location for notebook files are the root folder of the project where this Readme file is located. Dummy test data can be included to the project under `data` folder for testing and debugging the functionality of the code.

For unit testing your methods in the future, Python has a builtin `unittest` library which will look for certain filenames (starting with `test_*`) for running tests automatically. When used in most IDEs, the default behaviour for `unittest` library is to look under `tests` folder.

### Publishing the updated freeze file

Projects should be published with their own specific list of dependencies in order to ensure consistency across different development environments. The best practice is to start a new conda environment for each project with a minimum set of dependencies and keeping the versions up to date.

A freeze file is a list of specific library versions that is used by a Conda environment. Publishing a specific list of these libraries ensures the project will work across multiple workstations regardless of what versions other projects and environments use on any given workstation.

In order to generate a freeze file for the active environment you can simply open a command shell (`cmd.exe`) and type the following;

```msdos
conda env export --from-history -f freeze.yml
```

This will generate a `freeze.yml` file with the current state of your active environment. This file can be included to a project to automate the Conda environment setup. Please see the instructions at the beginning of this file for how to use the freeze file to replicate an environment.

Make sure you edit the freeze file to reflect the new environment name of your project. Two sections to be updated are the `name` at the beginning of the file, and the `prefix` at the end which can be removed. This way, multiple environments can be associated to the projects without naming conflicts.

### Initializing a new Git repository

When you are ready to create a new Git repository from the copy of this template, make sure to remove the old `.git` folder for preventing possible conflicts as it includes configurations like project name and remote host.

Most online git providers like Guthub and Gitlab provide a graphical process for creating repositories. This generates an empty repository for your files to be uploaded to.

Please include a modified version of this README file and provide documentation on how to run your project.

### Git Ignore File

Git [Ignore](https://git-scm.com/docs/gitignore) file is a list for Git utilities to exclude files from processing by checking the filename patterns. A `.gitignore` file is already included in this template project, but you may like to make further changes in the future depending on your project's specific needs.

Some recommended exclusions are;

- `.ipynb_checkpoints` (This should be already in the existing file)
- Workstation specific IDE configuration files (i.e `.vscode`, `.idea`)
- Data artifacts, outputted files of your code

### Automation Configuration

[![.github/workflows/tests.yml](https://github.com/Office-of-Groundwater-Impact-Assessment/template_project/actions/workflows/tests.yml/badge.svg)](https://github.com/Office-of-Groundwater-Impact-Assessment/template_project/actions/workflows/tests.yml)

This project comes with some Github specific workflows to be triggered every time a *push* is being made. These are;

- Static code analysis using [Pylint](https://pypi.org/project/pylint/)
- Unit tests

This automation creates a virtual machine with a Conda environment and can be configured in the `.github/workflows/tests.yml` file. 

For code analysis, `.pylintrc` file is used for customisation of some rules.

Please feel free to copy this structure to your new project or use as a guideline to buid a similar workflow.
