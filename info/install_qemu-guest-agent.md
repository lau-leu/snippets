# qemu-guest-agent

```info
Les outils qemu-guest-agent et spice-vdagent sont principalement utilisés dans des environnements de virtualisation, notamment avec QEMU/KVM et SPICE, pour améliorer l’interaction entre la machine virtuelle (VM) et l’hôte. Voici leurs rôles respectifs :
qemu-guest-agent


Rôle :
Ce service s’exécute à l’intérieur de la machine virtuelle et permet une communication bidirectionnelle entre l’hôte et la VM. Il facilite des fonctionnalités avancées comme :

Gestion de l’état de la VM : Arrêt propre, redémarrage, suspension, etc.
Échanges de fichiers : Copier/coller ou glisser-déposer entre l’hôte et la VM.
Informations système : Récupérer des données sur le système invité (comme l’utilisation du CPU, la mémoire, etc.).
Synchronisation de l’heure : Garder l’heure de la VM synchronisée avec celle de l’hôte.



Cas d’usage typique :
Utilisé avec QEMU/KVM pour automatiser des tâches ou améliorer l’intégration de la VM.
outils: qemu-guest-agent
environnement: QEMU/KVM
fonctionnalités principales: Gestion de la VM, synchronisation, échanges
```

**Description** : a quoi sert qemu-guest-agent
**Tags** : install,qemu,guest,agent,vm,kvm
