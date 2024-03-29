# Kaggle-Colab Setup Tool

Effortlessly set up and switch between Kaggle and Google Colab environments from an existing GitHub repository to leverage their GPU-accelerated hardware.

When training neural networks using accelerated hardware like GPUs in Kaggle or Colab environments, several challenges may arise during setup. Firstly, if your project comprises multiple python files in different subfolders, not just a single jupyter notebook, accessing all associated files and folders can be a problem. Copying and pasting everything for each session in Colab is feasible but inefficient, as all files are deleted when the session ends. Secondly, importing your dataset in each session is necessary to run your notebook and train your model. While datasets can be stored in Google Drive and accessed when mounted in Google Colab, transitioning to Kaggle requires repeating the process with different steps. This tool streamlines this process, allowing you to effortlessly switch between local, Google Colab, or Kaggle environments with a simple procedure. Its aim is to set up once and reuse indefinitely.

## How it Works

To set up your environment, add the following cell at the top of your main notebook and configure it according to your requirements.

```python
!pip install kaggle-colab --quiet

from kaggle_colab import setup_environment, GitHubRepo, KaggleDataset
from kaggle_colab.core import get_environment, GOOGLE_COLAB

if get_environment() == GOOGLE_COLAB:
    from google.colab import drive
    drive.mount('/content/drive')

dataset_path = setup_environment(
    github_repo=GitHubRepo(name='yolo-crafting', owner='pgmesa', install_requirements=True),
    dataset=KaggleDataset(name='face-mask-detection', owner='pgmesa', dest='.')
)
```

Import your main notebook from GitHub and grant permissions to Colab and/or Kaggle if you want them to access your private repositories. Run the cell, and the tool will handle the environment setup automatically. The idea is that all your code resides within a GitHub repository, while your dataset is zipped (.zip) and accessible online through a downloadable link or stored in Kaggle. In the latter scenario, it can be in your Kaggle account (whether it's a private or public dataset) or in someone else's public dataset.

## Explanation

Depending on the environment you are in, the tool will perform different steps. However, two main actions will occur in all environments:

1. **Dataset**: The specified dataset will be downloaded from the specified URL. The dataset should be contained in a .zip file. For Kaggle datasets, the Kaggle API needs to be installed (it is by default in Colab and Kaggle) to download the dataset. You will also need to create and locate the API key file in the correct directory. The process is detailed in the next section, as it differs for each environment.

2. **Scripts Associated with the Notebook**: To access the other files in your project, the GitHub repository will be cloned and added to the Python PATH so that imports work as in a local environment. The repository can be public or private, but for private repos, a GitHub token must be created and located in the correct place. By default, if a requirements.txt file is found inside the cloned repo, all the requirements will also be installed automatically inside Google Colab and Kaggle environments. This ensures that any extra dependencies used in your repository's scripts are added as well. If you make any changes to your repository files and push your changes to GitHub, running the cell again will remove the previous cloned repo and download it again with the updated files.

### Detailed Procedure for Each Environment

1. **Local/Unknown Environment**:

    If you are not on Kaggle or Colab, the tool will only download the specified dataset, assuming that you are working inside your project in a local environment, and imports are available as usual.

    To configure Kaggle dataset download in a normal machine:

    - Install the Kaggle API package:
        ```
        pip install kaggle
        ```

    - Obtain your Kaggle API key by creating an API key on your Kaggle account and downloading the kaggle.json file containing it. Place the file in `~/.kaggle/kaggle.json` on your machine (`/home/<user>/.kaggle/kaggle.json` or `C:\Users\<user>\.kaggle\kaggle.json`).

2. **Kaggle**:

    When in Kaggle, the dataset should be manually attached to the notebook. You can add the data manually from the GUI if your dataset is stored in Kaggle (your account or someone else's). If it's from another source, the .zip file should be uploaded (this data in Kaggle will not be removed after restarting the session).

    ![Kaggle Data](/.github/kaggle_data.png)

    To import the rest of the files of the project, create a GitHubRepo object and pass it to the setup_environment function. If your repo is private, you need to create a Kaggle secret called `github-token` and attach it to the notebook. The tool will clone the project to `/kaggle/working` and add it to the PATH so that imports work normally.

    ![Kaggle Secrets](/.github/kaggle_secrets.png)

3. **Google Colab**:

    When in Google Colab, both dataset and repo downloading are performed. The process is similar to the other environments. First, save the Kaggle API key and GitHub token in your Google Drive at `/content/drive/MyDrive/.keys/` with the names `kaggle.json` and `github-token.txt`, respectively. When downloading a Kaggle dataset, the program will move the key to your environment `~/.kaggle/`, which in Colab is located at (`/root/.kaggle/`). Once this is achieved, the Kaggle dataset and GitHub repo will be downloaded at `/content`. If Google Drive mounting is not desired, another option is to change the default path for searching the keys and manually upload them into the base `/content` Colab directory each time a new session is started.

    ```python
    from kaggle_colab.core import gdrive_keys_path
    gdrive_keys_path = "/content/"
    ```

    ![Colab Keys](/.github/colab_keys.png)