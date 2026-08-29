# Bases de données - cPanel

## Comment créer une nouvelle base de données (MySQL) ?
1. Connectez-vous à cPanel
2. Allez dans "MySQL Databases"
3. Entrez le nom de la base, cliquez sur "Create Database"
4. Créez un nouvel utilisateur (Add New User) et définissez un mot de passe
5. Associez l'utilisateur à la base (Add User to Database) et donnez-lui tous les privilèges (All Privileges)

## J'ai oublié le mot de passe de la base de données
1. Allez dans "MySQL Databases"
2. Sous "Current Users", trouvez l'utilisateur
3. Cliquez sur "Change Password" et entrez le nouveau mot de passe
4. ⚠️ Pensez à mettre à jour le mot de passe dans le fichier de configuration du site (ex: wp-config.php pour WordPress)

## Comment faire une sauvegarde d'une base de données ?
1. Allez dans "phpMyAdmin"
2. Sélectionnez la base à gauche
3. Cliquez sur l'onglet "Export"
4. Choisissez "Quick" puis cliquez sur "Go" - un fichier .sql sera téléchargé

## Comment importer une base de données depuis un fichier .sql ?
1. Allez dans "phpMyAdmin"
2. Sélectionnez la base de destination
3. Cliquez sur l'onglet "Import"
4. Choisissez le fichier .sql depuis votre ordinateur, cliquez sur "Go"

## Message d'erreur "Error establishing a database connection"
- Vérifiez que les informations dans le fichier de configuration du site sont correctes (nom de la base, utilisateur, mot de passe, hôte)
- Vérifiez que la base n'a pas été supprimée par erreur dans "MySQL Databases"
- Vérifiez que l'utilisateur est bien associé à la base avec les bons privilèges

## La base de données a atteint sa taille maximale
- Supprimez les anciennes tables ou données inutiles
- Ou mettez à jour le plan d'hébergement pour obtenir plus d'espace
