# RAG Chatbot - Support Technique Niveau 1

## 📌 Description
Chatbot conversationnel basé sur une architecture RAG (Retrieval-Augmented Generation) 
pour automatiser le support technique de niveau 1. Le système répond aux 
questions des utilisateurs en se basant sur une base de connaissances interne 
(guides au format Markdown et PDF) via une API LLM performante.

## 🎯 Objectif
- Support instantané 24/7
- Réduction des coûts opérationnels
- Centralisation de la documentation interne (.md et .pdf)
- Réponses précises basées strictement sur la documentation interne

## 🛠️ Stack technique
| Composant       | Technologie              |
|-----------------|---------------------------|
| Langage         | Python 3.11               |
| Orchestration   | LangChain                 |
| Base vectorielle| FAISS                     |
| Embeddings      | Sentence-Transformers (all-MiniLM-L6-v2) |
| Backend LLM     | OpenRouter API (ChatOpenAI)|
| Interface       | Streamlit                 |
| Infrastructure  | Serveur Linux (AlmaLinux) |

## 📁 Structure du projet
```text
rag_project/
├── docs/                   # Documents sources (.md, .pdf)
│   ├── email.md
│   ├── dns.md
│   ├── ssl.md
│   ├── wordpress.md
│   ├── fichiers.md
│   └── bases_de_donnees.md
├── faiss_index/            # Base vectorielle générée (créée automatiquement)
├── ingest.py               # Script d'indexation (à lancer lors du premier démarrage ou mise à jour)
├── app.py                  # Application Streamlit (chatbot)
└── README.md
```

## ⚙️ Installation

### 1. Prérequis
- Python 3.9+ (recommandé : 3.11)
- Une clé d'API OpenRouter

### 2. Configurer la clé API
Ajouter la clé d'API dans les variables d'environnement Linux :
```bash
export OPENROUTER_API_KEY="votre_cle_api_ici"
```

### 3. Installer les dépendances
```bash
python3.11 -m pip install streamlit langchain langchain-community langchain-core \
    langchain-openai langchain-huggingface langchain-text-splitters faiss-cpu \
    pypdf sentence-transformers
```

## 🚀 Utilisation

### Étape 1 : Ajouter des documents
Placer des fichiers `.md` ou `.pdf` dans le dossier `docs/`.

### Étape 2 : Construire l'index (à refaire à chaque ajout de document)
```bash
python3.11 ingest.py
```

### Étape 3 : Lancer l'application
```bash
streamlit run app.py
```

### Étape 4 : Accéder à l'interface
Ouvrir dans le navigateur :
```text
http://localhost:8501
```
(Si accès via serveur distant en SSH, utiliser un tunnel SSH sur le port 8501)

## 🔧 Maintenance

### Ajouter un nouveau guide
1. Ajouter le fichier `.md` ou `.pdf` dans `docs/` (ou l'uploader via la barre latérale Streamlit)
2. Relancer `python3.11 ingest.py` (ou cliquer sur "Reconstruire la base" sur l'interface)
3. Redémarrer l'application Streamlit si nécessaire

### Améliorer la vitesse de réponse
- Choisir un modèle plus rapide sur OpenRouter API
- Réduire le nombre de chunks récupérés (`search_kwargs={"k": 3}`)
- Réduire la taille des chunks (`chunk_size`)

## ⚠️ Points de vigilance
- S'assurer que la variable d'environnement `OPENROUTER_API_KEY` est bien définie avant le lancement.
- Assurer une connexion Internet stable sur le serveur pour communiquer avec l'API OpenRouter.
- Toujours faire une copie de sauvegarde avant de modifier le code source.

## 📊 KPIs à suivre (rapport d'amélioration continue)
- Taux de résolution automatique
- Temps de réponse moyen
- Satisfaction utilisateur

## 👤 Auteur
Stagiaire - Projet encadré par Mehdi