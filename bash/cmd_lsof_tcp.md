# Afficher les ports TCP à l'écoute

```bash
sudo lsof -nP -iTCP -sTCP:LISTEN
```

**Description** : Affiche tous les ports TCP à l'écoute.
**Tags** : linux,lsof,tcp,listen
