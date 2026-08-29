# RAG Chatbot - Support Technique Niveau 1

## 📌 Description
Chatbot conversationnel basé sur une architecture RAG (Retrieval-Augmented Generation)
locale, pour automatiser le support technique de niveau 1. Le système répond aux
questions des utilisateurs en se basant sur une base de connaissances interne
(guides au format Markdown), sans envoyer aucune donnée vers des services externes.

## 🎯 Objectif
- Support instantané 24/7
- Réduction des coûts opérationnels
- Centralisation de la documentation interne
- Souveraineté totale des données (rien n'est envoyé à des tiers)

## 🛠️ Stack technique
| Composant       | Technologie              |
|-----------------|---------------------------|
| Langage         | Python 3.11               |
| Orchestration   | LangChain                 |
| Base vectorielle| FAISS                     |
| Embeddings      | Sentence-Transformers (all-MiniLM-L6-v2) |
| LLM local       | Ollama (llama3.2)         |
| Interface       | Streamlit                 |
| Infrastructure  | Serveur Linux (AlmaLinux) |

## 📁 Structure du projet
```
rag_project/
├── docs/                   # Documents sources (.md, .pdf)
│   ├── email.md
│   ├── fichiers.md
│   └── bases_de_donnees.md
├── faiss_index/            # Base vectorielle générée (créée automatiquement)
├── ingest.py          # Script d'indexation (à lancer une seule fois)
├── app.py                  # Application Streamlit (chatbot)
└── README.md
```

## ⚙️ Installation

### 1. Prérequis
- Python 3.9+ (recommandé : 3.11)
- Ollama installé (https://ollama.com)

### 2. Installer les dépendances
```bash
python3.11 -m pip install streamlit langchain langchain-community langchain-core \
    langchain-text-splitters faiss-cpu sentence-transformers ollama
```

### 3. Télécharger un modèle Ollama
```bash
ollama pull llama3.2
# ou une version plus légère et rapide :
ollama pull llama3.2:1b
```

## 🚀 Utilisation

### Étape 1 : Ajouter des documents
Placer des fichiers `.md` ou `.pdf` dans le dossier `docs/`.

### Étape 2 : Construire l'index (à refaire à chaque ajout de document)
```bash
python3.11 build_index.py
```

### Étape 3 : Lancer l'application
```bash
streamlit run app.py
```

### Étape 4 : Accéder à l'interface
Ouvrir dans le navigateur :
```
http://localhost:8501
```
(Si accès via serveur distant en SSH, utiliser un tunnel SSH sur le port 8501)

## 🔧 Maintenance

### Ajouter un nouveau guide
1. Ajouter le fichier `.md` dans `docs/`
2. Relancer `python3.11 build_index.py`
3. Redémarrer l'application Streamlit

### Améliorer la vitesse de réponse
- Utiliser un modèle Ollama plus léger (`llama3.2:1b`)
- Réduire le nombre de chunks récupérés (`search_kwargs={"k": 3}`)
- Réduire la taille des chunks (`chunk_size`)

## ⚠️ Points de vigilance
- Ne jamais utiliser de service externe (OpenAI, etc.) — l'objectif du projet
  est la souveraineté totale des données (tout doit rester local via Ollama).
- Toujours faire une copie de sauvegarde avant de modifier le code source.

## 📊 KPIs à suivre (rapport d'amélioration continue)
- Taux de résolution automatique
- Temps de réponse moyen
- Satisfaction utilisateur

## 👤 Auteur
Stagiaire - Projet encadré par Mehdi