# Sécurité et SSL - cPanel

## Comment installer un certificat SSL gratuit ?
1. Connectez-vous à cPanel
2. Allez dans "SSL/TLS Status" ou "Let's Encrypt SSL"
3. Sélectionnez le domaine
4. Cliquez sur "Run AutoSSL" ou "Issue"
5. Attendez quelques minutes pour l'activation

## Le site affiche "Votre connexion n'est pas privée" / "Not Secure"
- Vérifiez que le certificat SSL est bien installé et actif dans "SSL/TLS Status"
- Vérifiez que le site force bien la redirection HTTPS (voir "Domains" > "Force HTTPS Redirect")
- Videz le cache du navigateur et réessayez

## Comment forcer la redirection HTTP vers HTTPS ?
1. Allez dans "Domains" dans cPanel
2. Trouvez le domaine concerné
3. Activez l'option "Force HTTPS Redirect"

## Mon compte cPanel a été piraté, que faire ?
1. Changez immédiatement le mot de passe cPanel
2. Vérifiez "File Manager" pour des fichiers suspects récemment modifiés
3. Vérifiez les comptes email créés sans votre autorisation
4. Contactez l'hébergeur pour un scan de sécurité complet (souvent via "Imunify360" si disponible)

## Comment activer la protection contre les attaques (Imunify360 / firewall) ?
- Si disponible dans votre cPanel, allez dans "Imunify360" pour voir les tentatives d'intrusion bloquées
- Activez le pare-feu applicatif (WAF) depuis cette interface

## Comment changer le mot de passe cPanel ?
1. Allez dans "Password & Security" dans cPanel
2. Entrez l'ancien mot de passe puis le nouveau
3. Cliquez sur "Change your password now"

## Recommandations générales de sécurité
- Utilisez des mots de passe forts et uniques
- Activez l'authentification à deux facteurs (2FA) si disponible
- Mettez à jour régulièrement WordPress, plugins et thèmes
- Faites des sauvegardes régulières