# Synchroniser et modifier les permissions pour incollab

```bash
sudo rsync -av \/smbd-drive/03-Data/www/Projet site/incollab\ /var/www/ && sudo chmod 755 /var/www/incollab -R && clear
```

**Description** : Synchronise le dossier incollab vers /var/www/ et modifie les permissions.
**Tags** : linux,rsync,permissions,incollab
