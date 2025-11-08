# liste de commandes Apache

```bash
# Vérifier le statut d'Apache
sudo systemctl status apache2
# Redémarrer Apache
sudo systemctl restart apache2
# Recharger Apache
sudo systemctl reload apache2
# Activer Apache au démarrage
sudo systemctl enable apache2
# Tester la configuration Apache
sudo apachectl configtest
# Activer un site Apache
sudo a2ensite /chemindossier/fichier.conf
# Désactiver un site Apache
sudo a2dissite /chemindossier/fichier.conf
# Activer un module Apache
sudo a2enmod /chemindossier/fichier.conf
# Activer une configuration Apache
sudo a2enconf /chemindossier/fichier.conf
# Désactiver une configuration Apache
sudo a2disconf /chemindossier/fichier.conf
```

**Description** : liste de commandes les plus courantes d'Apache
**Tags** : apache,status,restart,site,web,http
