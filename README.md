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
   
## Step 2: Install Python (Specific Version)
1. This project requires "**Python 3.7.12**". Download it here : [Python 3.7.12](https://www.python.org/downloads/release/python-3712/)
2. Run the installer
3. **Important :** Check the box **"Add Python 3.7 to PATH"** before clicking "**Install Now**"
   
## Step 3: Prepare the Environment
Open your terminal (Command Prompt on Windows or Terminal on macOS/Linux) and navigate to the project folder:

1. Install Streamlit: 
```pip install streamlit ```


2.Install the other required libraries:
```pip install -r requirements.txt```

## Usage
Once the installation is complete, you can launch the application by running the following command while staying in the project directory:
```streamlit run app.py```

---

## Technologies Used

The project relies on a modern Python ecosystem to ensure speed and interactivity:

* **Language :** [Python 3.7.12](https://www.python.org/) 
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
