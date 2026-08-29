# Configuration de la Messagerie Professionnelle

Ce guide explique comment configurer l'accès au courrier électronique de l'entreprise sur un client de messagerie (Outlook, Thunderbird, ou mobile).

## Paramètres de Connexion (Serveur Sécurisé)

Pour garantir la sécurité et la confidentialité des échanges, utilisez exclusivement les protocoles sécurisés suivants :

*   **Protocole de Réception (IMAP) :**
    *   Serveur : `mail.entreprise.dz`
    *   Port : `993`
    *   Chiffrement : `SSL/TLS`
*   **Protocole d'Envoi (SMTP) :**
    *   Serveur : `mail.entreprise.dz`
    *   Port : `465`
    *   Chiffrement : `SSL/TLS`
    *   Authentification : `Requise (Identique au serveur de réception)`

## Procédure d'Activation

1. Ouvrez votre client de messagerie et sélectionnez **Ajouter un compte**.
2. Saisissez votre adresse email complète (ex: `nom.prenom@entreprise.dz`).
3. Choisissez une configuration **Manuelle** ou **Avancée**.
4. Introduisez les serveurs et les ports indiqués ci-dessus.
5. Entrez votre mot de passe initial fourni par le service informatique.

## Résolution des Problèmes Récurrents

Si le client de messagerie affiche une erreur de connexion, vérifiez en priorité que le port `465` ou `993` n'est pas bloqué par votre pare-feu local ou le routeur de votre agence.
