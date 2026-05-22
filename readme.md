# Multi-Agent Local System with CrewAI

Ce projet implémente une architecture modulaire multi-agents utilisant le framework **CrewAI**. Le système est conçu pour fonctionner 100% en local en utilisant une instance de **llama.cpp** (ou tout autre serveur compatible OpenAI API).

## 🚀 Architecture du Projet

```text
/mon_projet_agents
  ├── .env                   # Variables d'environnement (URL API, Clé)
  ├── requirements.txt       # Dépendances Python
  ├── document_test.txt      # Fichier texte de test (généré automatiquement)
  ├── main.py                # Point d'entrée du script
  └── /src
      ├── config.py          # Configuration du LLM
      ├── /agents
          └── agents_factory.py # Définition des agents (Analyste, Planificateur)
      ├── /tasks
          └── tasks_factory.py  # Définition des tâches
      └── /tools
          └── file_tools.py     # Outil de lecture de fichier local
```

## 🛠 Stack Technique

- **Langage** : Python 3.10+
- **Framework** : CrewAI
- **LLM Engine** : llama.cpp (émulation API OpenAI)
- **Library LLM** : LiteLLM (via CrewAI)

## 📋 Prérequis

1.  **Serveur LLM Local** : Avoir une instance de `llama.cpp` qui tourne en mode serveur.
    -   Exemple : `./server -m models/gemma-4.gguf --port 8080`
2.  **Python** : Version 3.10 ou supérieure installée.

## ⚙️ Installation

1.  Clonez ce dépôt ou copiez les fichiers.
2.  Créez un environnement virtuel (optionnel mais recommandé) :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Linux/Mac
    # ou
    venv\Scripts\activate     # Sur Windows
    ```
3.  Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## 🔧 Configuration

Le fichier `.env` contient les paramètres de connexion au serveur local :

```env
OPENAI_API_BASE=http://localhost:8080/v1
OPENAI_API_KEY=sk-no-key-required
MODEL_NAME=gemma-4
```

## 🏃 Lancement

Lancez le script principal :

```bash
python main.py
```

Le script vous demandera une instruction. Vous pouvez tester deux modes :

1.  **Analyse de fichier** : Tapez "Analyse le fichier document_test.txt". L'agent utilisera son outil pour lire le fichier.
2.  **Analyse directe** : Fournissez directement du texte (ex: "Voici mon projet : Budget 10k, fin en décembre, équipe de 2 personnes. Fais un plan."). L'agent analysera le texte sans utiliser l'outil.

## 🤖 Agents & Tâches

-   **Data Analyst** : Responsable de l'extraction des informations clés. Il possède l'outil `read_local_file`.
-   **Strategic Planner** : Responsable de la création d'un plan stratégique en 3 étapes basé sur l'analyse.

*Note : Bien que le code et les rôles soient définis en anglais, les agents sont configurés pour réfléchir et répondre exclusivement en **français**.*
