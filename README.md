# 🔍 Detect - Application d'Analyse avec Streamlit

[![Python](https://img.shields.io/badge/Python-3.7.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3712/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)

Une application web interactive et intuitive développée avec **Python** et **Streamlit**. Ce projet permet de traiter des données et de visualiser des résultats directement dans votre navigateur.

<p align="center">
  <img src="images/preview.png" alt="Aperçu de l'application" width="600"/>
</p>

---

## 📌 Introduction

Ce projet a été réalisé dans un cadre académique/personnel pour répondre à un besoin de détection et d'analyse de données. L'interface utilisateur repose sur Streamlit, ce qui permet une manipulation simple sans nécessiter de connaissances approfondies en programmation.

---

## 🚀 Installation (Guide pas à pas)

Suivez ces étapes pour faire fonctionner l'application sur votre machine locale.

### Étape 1️⃣ : Récupérer le projet
1. Cliquez sur le bouton vert **Code** en haut de cette page.
2. Sélectionnez **Download ZIP**.
3. Décompressez le dossier `.zip` à l'emplacement de votre choix.

## Étape 2️⃣ : Installer Python (Version spécifique)
1. Ce projet nécessite **Python 3.7.12**. Téléchargez-le ici : [Python 3.7.12](https://www.python.org/downloads/release/python-3712/)
2. Lancez l'installateur.
3. **Important :** Cochez la case **"Add Python 3.7 to PATH"** avant de cliquer sur *Install Now*.
   
### Étape 3️⃣ : Préparer l'environnement
Ouvrez votre terminal (Invite de commandes sur Windows ou Terminal sur macOS/Linux) et déplacez-vous dans le dossier du projet :

Installation de Streamlit : 
```pip install streamlit ```


Installation des autres bibliothèques requises :
```pip install -r requirements.txt```

# 💻 Utilisation
Une fois l'installation terminée, vous pouvez lancer l'application avec la commande suivante :
```streamlit run app.py```

---

## 🛠️ Technologies utilisées

Le projet s'appuie sur un écosystème Python moderne pour garantir rapidité et interactivité :

* **Langage :** [Python 3.7.12](https://www.python.org/) 🐍
* **Interface Web :** [Streamlit](https://streamlit.io/) (Framework pour applications Data)
* **Gestion des données :** Pandas & NumPy (Manipulation de tableaux et calculs)
* **Modèles & Détection :** Scikit-Learn / OpenCV (Analyse d'images ou modèles prédictifs)

---

## 📁 Structure du projet

L'organisation des fichiers permet une maintenance simplifiée :

```text
📂 Detect
├─ models                  #contenant le model de segmentation
├─ images                  #dossier avec les images du projet
├── app.py                 # Point d'entrée principal de l'application
├── requirements.txt       # Liste des dépendances à installer
└── README.md              # Documentation du projet
