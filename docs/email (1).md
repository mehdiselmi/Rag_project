# Support Email - cPanel

## Comment créer une nouvelle adresse email ?
1. Connectez-vous à cPanel
2. Allez dans la section "Email" puis "Email Accounts"
3. Cliquez sur "Create"
4. Entrez le nom (ex: contact@domaine.com) et un mot de passe
5. Cliquez sur "Create" pour valider

## L'email ne reçoit pas de messages
- Vérifiez que les enregistrements MX sont correctement configurés dans "Zone Editor"
- Vérifiez que la boîte n'a pas atteint son quota maximum
- Consultez "Track Delivery" pour voir où le message a été bloqué

## L'email n'arrive pas à envoyer de messages (Outgoing mail)
- Vérifiez les paramètres SMTP (port 465 ou 587)
- Vérifiez "Email Deliverability" dans cPanel pour voir si SPF et DKIM sont bien configurés
- Si les messages rebondissent, consultez le "Error Log"

## Comment changer le mot de passe d'un email ?
1. Allez dans "Email Accounts"
2. Trouvez le compte, cliquez sur "Manage"
3. Entrez le nouveau mot de passe et cliquez sur "Update Email Settings"

## Comment configurer un email dans Outlook ou Gmail ?
Utilisez les paramètres suivants :
- IMAP : port 993 (SSL)
- SMTP : port 465 (SSL)
- Nom d'utilisateur : l'adresse email complète (ex: contact@domaine.com)

## Peut-on augmenter l'espace de stockage d'un email ?
Oui, depuis "Email Accounts", cliquez sur "Manage" sur le compte concerné, puis modifiez la valeur du "Mailbox Quota".
