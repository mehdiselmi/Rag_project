# Résolution des Problèmes de Connexion Réseau et VPN

Ce document fournit la procédure de niveau 1 pour diagnostiquer et résoudre une perte d'accès au réseau local ou aux applications internes via le VPN.

## 1. Vérification de la Connectivité Locale (LAN/Wi-Fi)

Avant de contacter le support, effectuez les vérifications matérielles de base :
*   Vérifiez que le câble Ethernet est correctement branché (LED verte clignotante).
*   Si vous utilisez le Wi-Fi, assurez-vous d'être connecté au réseau sécurisé nommé `Entreprise_Corporate`.
*   Ouvrez un terminal et testez la passerelle avec la commande : `ping 192.168.1.1`.

## 2. Connexion au VPN pour le Télétravail

Pour accéder aux outils internes depuis l'extérieur des bureaux, le client VPN FortiClient doit être actif.

*   **Identifiant :** Votre matricule professionnel.
*   **Adresse de la passerelle VPN :** `vpn.entreprise.dz`
*   **Port de communication :** `10443`

## 3. Procédure de Réinitialisation en cas de Panne

Si les pages web internes ne s'ouvrent pas :
1. Déconnectez le VPN, puis reconnectez-le.
2. Videz le cache DNS de votre machine Windows en ouvrant l'invite de commandes (CMD) et en tapant : `ipconfig /flushdns`.
3. Redémarrez votre routeur ou votre box internet locale.
