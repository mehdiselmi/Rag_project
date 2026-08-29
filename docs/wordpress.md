# Support WordPress - cPanel

## Comment installer WordPress ?
1. Connectez-vous à cPanel
2. Allez dans "Softaculous Apps Installer" (ou "WordPress Installer")
3. Cliquez sur "Install"
4. Choisissez le domaine, entrez le nom du site, votre email et mot de passe admin
5. Cliquez sur "Install" et attendez la fin de l'installation

## J'ai oublié le mot de passe administrateur de WordPress
1. Allez dans "phpMyAdmin"
2. Ouvrez la table `wp_users`
3. Trouvez votre utilisateur, cliquez sur "Edit"
4. Dans le champ `user_pass`, entrez un nouveau mot de passe et sélectionnez la fonction "MD5" dans le menu déroulant
5. Cliquez sur "Go" pour enregistrer

## Le site WordPress affiche "Erreur de connexion à la base de données"
- Vérifiez le fichier `wp-config.php` : nom de la base, utilisateur, mot de passe, host doivent être corrects
- Vérifiez que la base de données existe toujours dans "MySQL Databases"
- Contactez le support si le problème persiste après vérification

## Le site WordPress est très lent
- Installez un plugin de cache (ex: WP Super Cache, W3 Total Cache)
- Optimisez les images (compressez-les avant de les uploader)
- Désactivez les plugins inutilisés
- Vérifiez l'utilisation des ressources dans "cPanel > Resource Usage"

## Comment faire une sauvegarde complète du site WordPress ?
1. Utilisez un plugin comme "UpdraftPlus" ou "All-in-One WP Migration"
2. Ou depuis cPanel, utilisez "JetBackup" pour sauvegarder les fichiers et la base de données ensemble

## Page blanche après une mise à jour de plugin/thème
- Activez le mode debug en ajoutant dans `wp-config.php` :
  `define('WP_DEBUG', true);`
- Renommez le dossier du plugin problématique via File Manager (dans `wp-content/plugins/`) pour le désactiver temporairement