# liste de commande apache

```bash
# Vérifier le statut d'Apache
   5   │ sudo systemctl status apache2
   6   │ # Redémarrer Apache
   7   │ sudo systemctl restart apache2
   8   │ # Recharger Apache
   9   │ sudo systemctl reload apache2
  10   │ # Activer Apache au démarrage
  11   │ sudo systemctl enable apache2
  12   │ # Tester la configuration Apache
  13   │ sudo apachectl configtest
  14   │ # Activer un site Apache
  15   │ sudo a2ensite /chemindossier/fichier.conf
  16   │ # Désactiver un site Apache
  17   │ sudo a2dissite /chemindossier/fichier.conf
  18   │ # Activer un module Apache
  19   │ sudo a2enmod /chemindossier/fichier.conf
  20   │ # Activer une configuration Apache
  21   │ sudo a2enconf /chemindossier/fichier.conf
  22   │ # Désactiver une configuration Apache
  23   │ sudo a2disconf /chemindossier/fichier.conf
```

**Description** : liste de commande les plus courante d'apache
**Tags** : apache,status,restart,site,web,http
