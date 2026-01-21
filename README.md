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
4. Récupérer le modèle à partir de ce lien, puis l’ajouter au dossier décompressé : [Lien modèle](https://drive.google.com/drive/folders/1KuUZVL8Pmh7N3PR7EHH6l6szzE36-LVe?usp=sharing)
   
## Étape 2 : Installer Python (Version spécifique)
1. Ce projet nécessite "**Python 3.7.12**". Téléchargez-le ici : [Python 3.7.12](https://www.python.org/downloads/release/python-3712/)
2. Lancez l'installation
3. **Important :** Cochez la case **"Add Python 3.7 to PATH"** avant de cliquer sur "**Install Now**"
   
## Étape 3 : Préparer l'environnement
Ouvrez votre terminal (Invite de commandes sur Windows ou Terminal sur macOS/Linux) et déplacez-vous dans le dossier du projet :

1. Installation de Streamlit : 
```pip install streamlit ```


2. Installation des autres bibliothèques requises :
```pip install -r requirements.txt```

## Utilisation
Une fois l'installation terminée, vous pouvez lancer l'application avec la commande suivante tout en restant dans le dossier du projet :
```streamlit run app.py```

---

## Technologies utilisées

Le projet s'appuie sur un écosystème Python moderne pour garantir rapidité et interactivité :

* **Langage :** [Python 3.7.12](https://www.python.org/) 
* **Interface Web :** [Streamlit](https://streamlit.io/) (Framework pour applications Data)
* **Gestion des données :** Pandas & NumPy (Manipulation de tableaux et calculs)
* **Modèles & Détection :** Scikit-Learn / OpenCV (Analyse d'images ou modèles prédictifs)

---

## Structure du projet

L'organisation des fichiers permet une maintenance simplifiée :

```text
📂 Detect
├─ models                  # À récupérer sur le drive
├─ images                  # Dossier avec les images du projet
├── app.py                 # Point d'entrée principal de l'application
├── requirements.txt       # Liste des dépendances à installer
└── README.md              # Documentation du projet
