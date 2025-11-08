# Synchroniser et modifier les permissions pour teamup

```bash
sudo rsync -av /smbd-drive/03-Data/www/teamup /var/www/ && sudo chmod 755 /var/www/teamup -R && clear
```

**Description** : Synchronise le dossier teamup vers /var/www/ et modifie les permissions pour permettre l'accès.
**Tags** : linux,rsync,permissions,teamup
