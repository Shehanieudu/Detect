# D3TECT - The power of AI at the service of your cerebral organoids.

[![Python](https://img.shields.io/badge/Python-3.7.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3712/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)

<p align="center">
  <img src="images/Logo_Projet5D3TECT.png" alt="Aperçu de l'application" width="300"/>
</p>

---

## Our solution

D3TECT is an intelligent web application designed to streamline the growth tracking of cerebral organoids. Thanks to its fast and reliable automated segmentation, it enables the analysis of large datasets while maintaining exceptional precision.

Our solution simplifies visual and quantitative analysis over time, providing an efficient, consistent, and reproducible workflow to accelerate research and allow you to focus on innovation.

---

## Installation de D3TECT 

Follow these steps to run the webapp on your computer :

## Step 1: Retrieve the Project
1. Click the green "Code" button at the top of this page
2. Select "**Download ZIP**"
3. Extract the `.zip` folder to the location of your choice
4. Download the model from the following link and add it to the extracted folder : [Lien modèle](https://drive.google.com/drive/folders/1KuUZVL8Pmh7N3PR7EHH6l6szzE36-LVe?usp=sharing)
   
## Step 2: Create the Environment (via Anaconda)

We use **Anaconda Navigator** to easily create a secure space for the project.

1.  Install Anaconda: If you haven't already, download and install [Anaconda](https://www.anaconda.com/download)
2.  Open Anaconda Navigator from your applications menu.
3.  Click on the "Environments" tab on the left sidebar.
4.  Click the Create button (at the bottom).
5.  **Configure the popup window:**
    * Name: project_env
    * Packages: Check "Python" and select version **3.7** from the dropdown list.
6.  Click **"Create"** and wait for the process to finish.

## Step 3: Configure Visual Studio Code

Now, we need to tell VS Code to use the environment you just created.

1.  **Open the Project:**
    Launch VS Code and open the folder you extracted in Step 1 (**File > Open Folder...**).

2.  **Select the Interpreter:**
    * Open the Command Palette: Press Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (macOS).
    * Type and select: Python: Select Interpreter.
    * In the list, find and click on project_env (it should be labeled as 'Conda').

3.  **Open the Terminal:**
    * Go to **Terminal > New Terminal** in the top menu.
    * **Check:** You should see (project_env) appear at the beginning of the command line in the terminal panel below.

> **Note:** If the terminal doesn't show the environment name, try clicking the trash icon to kill the terminal and open a new one after selecting the interpreter.

   
## Step 4: Prepare the Environment
Open your terminal (Command Prompt on Windows or Terminal on macOS/Linux) and navigate to the project folder:

1. Install Streamlit: 
```pip install streamlit ```

2. Install the other required libraries:
```pip install -r requirements.txt```

## Usage
Once the installation is complete, you can launch the application by running the following command while staying in the project directory:
```streamlit run app.py```

---

## Technologies Used

The project relies on a modern Python ecosystem to ensure speed and interactivity:

* **Language :** [Python 3.7.16] 
* **Web Interface :** [Streamlit](https://streamlit.io/) (Data application framework)
* **Data Handling :** Pandas & NumPy (Array manipulation and computations)
* **Models & Detection :** Scikit-Learn / OpenCV (Image analysis or predictive models)

---

## Project Structure

The file organization allows for simplified maintenance:

```text
📂 Detect
├─ models                  # To be retrieved from the drive
├─ images                  # Folder containing project images
├── app.py                 # Main entry point of the application
├── requirements.txt       # List of dependencies to install
└── README.md              # Project documentation
