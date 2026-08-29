# Domaines et DNS - cPanel

## Comment pointer mon domaine vers l'hébergement (nameservers) ?
1. Connectez-vous à votre registrar (là où vous avez acheté le domaine)
2. Cherchez la section "Nameservers" ou "DNS"
3. Remplacez-les par les nameservers fournis par votre hébergeur (ex: ns1.hebergeur.com, ns2.hebergeur.com)
4. Attendez la propagation (peut prendre jusqu'à 24-48h)

## Comment ajouter un sous-domaine ?
1. Allez dans cPanel > "Subdomains"
2. Entrez le nom du sous-domaine (ex: `blog` pour blog.domaine.com)
3. Vérifiez le dossier racine proposé (ou changez-le)
4. Cliquez sur "Create"

## Le site ne s'affiche pas après avoir pointé le domaine
- Vérifiez que les nameservers sont corrects chez le registrar
- Attendez la propagation DNS (utilisez un outil comme whatsmydns.net pour vérifier)
- Vérifiez qu'un site par défaut (index.html) existe bien dans `public_html`

## Comment configurer un enregistrement MX pour un email externe (ex: Google Workspace) ?
1. Allez dans cPanel > "Zone Editor" (ou "MX Entry")
2. Supprimez ou modifiez les enregistrements MX existants
3. Ajoutez les nouveaux enregistrements MX fournis par le service externe (ex: Google)
4. Définissez la priorité selon les instructions du fournisseur

## Comment ajouter un enregistrement DNS personnalisé (A, CNAME, TXT) ?
1. Allez dans cPanel > "Zone Editor"
2. Cliquez sur "Manage" pour le domaine concerné
3. Cliquez sur "Add Record"
4. Choisissez le type (A, CNAME, TXT...), entrez les valeurs demandées
5. Cliquez sur "Save"

## Combien de temps prend la propagation DNS ?
Généralement entre quelques minutes et 24-48 heures, selon les fournisseurs et les caches DNS dans le monde.