# Gestion des fichiers - cPanel

## Comment envoyer (upload) un fichier sur le serveur ?
1. Connectez-vous à cPanel
2. Allez dans "File Manager"
3. Sélectionnez le dossier (généralement `public_html`)
4. Cliquez sur "Upload", puis choisissez le fichier depuis votre ordinateur

## Peut-on envoyer plusieurs fichiers en une seule fois ?
La meilleure méthode : créez un fichier compressé (ZIP) sur votre ordinateur, envoyez-le, puis utilisez "Extract" dans File Manager pour le décompresser automatiquement sur le serveur.

## J'ai oublié les permissions d'un fichier, que faire ?
- Dossiers : généralement `755`
- Fichiers : généralement `644`
- Pour modifier : clic droit sur le fichier/dossier dans File Manager, choisissez "Change Permissions"

## Peut-on récupérer un fichier supprimé par erreur ?
Oui, si une sauvegarde (Backup) est activée, allez dans "Backup" ou "JetBackup" dans cPanel, et choisissez la date à laquelle revenir.

## L'espace disque de l'hébergement est plein
1. Allez dans "File Manager" ou utilisez "Disk Usage" pour voir où l'espace est utilisé
2. Supprimez les fichiers inutiles (anciens logs, anciennes sauvegardes, fichiers temporaires)
3. Si besoin de plus d'espace, il faudra mettre à jour le plan d'hébergement

## Comment renommer un fichier ou un dossier ?
Clic droit sur le fichier dans File Manager, choisissez "Rename", entrez le nouveau nom.

## Peut-on modifier un fichier directement depuis cPanel sans le télécharger ?
Oui, clic droit sur le fichier, choisissez "Edit" ou "Code Editor", modifiez le contenu et enregistrez.
