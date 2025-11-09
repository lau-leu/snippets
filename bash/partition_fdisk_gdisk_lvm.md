# création de partion

```bash
#1. Type de partition requis

# Type : Linux LVM (code 8e dans fdisk/gdisk).
# Utilité : Ce type indique au système que la partition sera utilisée par LVM pour créer des volumes physiques (PV).

#2. Comment créer une partition de type "Linux LVM"

# Avec fdisk (pour les disques < 2 To ou en mode DOS)
# Lancez fdisk pour chaque disque :
## bash ##

sudo fdisk /dev/sdb

## ##
# (Répétez pour /dev/sdc et /dev/sdd.)
#Dans fdisk :
# - Tapez n pour créer une nouvelle partition.
# - Choisissez p (primaire) et acceptez les valeurs par défaut pour utiliser tout le disque.
# - Tapez t pour modifier le type de partition.
# - Sélectionnez la partition (généralement 1).
# - Entrez 8e pour définir le type Linux LVM.
# - Tapez w pour sauvegarder les changements.

#Avec gdisk (pour les disques > 2 To ou en mode GPT)
#Lancez gdisk :
## bash ##

sudo gdisk /dev/sdb

## ##
#Dans gdisk :
# - Tapez n pour créer une nouvelle partition.
# - Acceptez les valeurs par défaut pour utiliser tout le disque.
# - Tapez t pour modifier le type de partition.
# - Entrez 8e00 pour définir le type Linux LVM.
# - Tapez w pour sauvegarder.

#laurent@jarvis-kde:~$ sudo gdisk /dev/sda
#GPT fdisk (gdisk) version 1.0.10

#Partition table scan:
#  MBR: protective
#  BSD: not present
#  APM: not present
#  GPT: present

#Found valid GPT with protective MBR; using GPT.

#Command (? for help): n
#Partition number (1-128, default 1):
#First sector (2048-7814037134, default = 2048) or {+-}size{KMGTP}:
#First sector (2048-7814037134, default = 2048) or {+-}size{KMGTP}:
#Last sector (2048-7814037134, default = 7814035455) or {+-}size{KMGTP}:
#Current type is 8300 (Linux filesystem)
#Hex code or GUID (L to show codes, Enter = 8300): 8e00
#Changed type of partition to 'Linux LVM'

#Command (? for help): w

#Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING PARTITIONS!!

#Do you want to proceed? (Y/N): y
#OK; writing new GUID partition table (GPT) to /dev/sda.
#The operation has completed successfully.

#3. Vérification

# Après avoir créé les partitions, vérifiez leur type avec :
## bash ##

lsblk -f

# ou

sudo blkid

## ##
# Vous devriez voir quelque chose comme : /dev/sdb1: UUID="..." TYPE="LVM2_member"

#4. Pourquoi ce type est-il important ?

# Compatibilité : LVM ne reconnaîtra que les partitions de type Linux LVM (8e) comme éligibles pour devenir des volumes physiques (PV).
# Évite les erreurs : Si le type est incorrect (par exemple, Linux filesystem), LVM refusera de créer un PV sur cette partition.

#5. Cas particulier : Disques entiers sans partition
# Si vous souhaitez utiliser tout le disque (sans partition), vous pouvez directement créer un PV sur le disque entier (par exemple, /dev/sdb au lieu de /dev/sdb1). Cependant, cette méthode est moins flexible et non recommandée pour les environnements de production.

# Résumé des étapes clés
# - Créez une partition sur chaque disque.
# - Définissez le type de partition sur Linux LVM (8e).
# - Sauvegardez les changements.
# - Vérifiez avec lsblk -f ou blkid.
```

**Description** : création de partition primaire ou logique LVM
**Tags** : lvm,LVM,hdd,sata,gdisk,lsblk,fdisk,blkid
