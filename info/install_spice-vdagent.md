# spice-vdagent

```info
spice-vdagent


Rôle :
Ce service est spécifique à l’utilisation du protocole SPICE (Simple Protocol for Independent Computing Environments). Il améliore l’expérience utilisateur en :

Optimisant l’affichage : Meilleure gestion de la résolution d’écran et des redimensionnements de fenêtre.
Copier-coller : Permet le partage du presse-papiers entre l’hôte et la VM.
Intégration du bureau : Meilleure synchronisation des périphériques (comme les claviers ou souris).



Cas d’usage typique :
Utilisé avec des VMs qui utilisent SPICE comme protocole d’affichage (souvent dans des environnements comme virt-manager ou oVirt).


outils: spice-vdagent
environnement: spice
fonctionnalités principales: Optimisation d’affichage, presse-papiers
Si vous utilisez SPICE (pour une meilleure expérience graphique), installez les deux : qemu-guest-agent pour la gestion et spice-vdagent pour l’affichage et l’intégration.
```

**Description** : a quoi sert spice-vdagent
**Tags** : install,qemu,kvm,vm,spice,vdagent
