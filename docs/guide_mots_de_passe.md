# Politique de Sécurité des Mots de Passe et Déverrouillage de Compte

Directives pour la gestion des accès et la réinitialisation des comptes d'utilisateurs bloqués sur l'Active Directory de l'entreprise.

## Règles d'Or pour un Mot de Passe Conforme

Pour être accepté par le système, votre nouveau mot de passe doit respecter les critères de complexité obligatoires suivants :
*   Longueur minimale de **12 caractères**.
*   Contenir au moins une lettre **majuscule** et une lettre **minuscule**.
*   Contenir au moins un **chiffre** (0-9).
*   Contenir au moins un **caractère spécial** (ex: `@`, `#`, `$`, `*`).
*   Durée de validité : Le système exige un renouvellement tous les **90 jours**.

## Procédure de Déverrouillage Autonome

Après **3 tentatives infructueuses**, votre compte de session Windows se bloque automatiquement pendant une durée de **15 minutes** par mesure de sécurité contre les attaques.

Si vous avez urgemment besoin d'accéder à votre session :
1. Rendez-vous sur le portail interne : `https://entreprise.dz`.
2. Cliquez sur **Compte Bloqué / Mot de passe oublié**.
3. Entrez votre identifiant et validez l'authentification par le code SMS envoyé sur votre téléphone professionnel.
4. Saisissez votre nouveau mot de passe conforme aux règles de l'entreprise.
