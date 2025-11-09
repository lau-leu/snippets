# Copier un fichier via SCP

```bash
scp -P 12345 chemin/origine/fichier user@192.168.1.x:chemin/de/réception
# autre methode NE PAS OUBLIER LE \ AVANT LES ESPACES DANS LA CHAINE DE CARACTERE
scp -r -O -P 60 laurent@192.168.1.51:'/volume1/homes/Romane/Documents/Etudes/Scolarité/BUT\ MMI/MMI\ 2/S3/Portfolio' ~/Downloads
sudo scp -r -O -P 60 win11.qcow2 laurent@192.168.1.51:'/volume1/Whitehome_sauv/Modif/Culture\ informatique/Virtual\ Machine/img'
```

**Description** : Copie un fichier vers une machine distante via SCP.
**Tags** : linux,scp,copy,file
