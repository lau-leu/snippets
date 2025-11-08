# réaliser un connexion ssh depuis android

```info
Pour établir une connexion SSH depuis un appareil Android, voici les étapes à suivre :

1. Installer une application cliente SSH
Android ne dispose pas nativement d’un client SSH. Il faut installer une application dédiée depuis le Google Play Store. Voici quelques options populaires :

Termux : Un émulateur de terminal avancé qui permet d’installer des outils comme SSH.
JuiceSSH : Une application conviviale spécialement conçue pour les connexions SSH.
ConnectBot : Un client SSH open source, simple et efficace.


2. Configurer la connexion SSH
Une fois l’application installée, voici comment configurer une connexion SSH (exemple avec JuiceSSH) :


Ouvrir l’application et appuyer sur le bouton pour ajouter une nouvelle connexion.


Remplir les informations suivantes :

Nom de la connexion : Un nom pour identifier la connexion (ex: "Mon Serveur").
Type : SSH.
Adresse IP ou nom d’hôte : L’adresse IP ou le nom de domaine du serveur auquel vous voulez vous connecter.
Port : Par défaut, le port SSH est le 22.
Nom d’utilisateur : Votre identifiant sur le serveur.
Mot de passe : Votre mot de passe (ou utilisez une clé SSH si configurée).



Enregistrer la configuration.



3. Se connecter au serveur

Sélectionnez la connexion que vous venez de créer.
L’application va établir la connexion SSH. Si tout est correctement configuré, vous serez connecté au serveur et verrez l’invite de commande du terminal distant.


4. Utiliser des clés SSH (optionnel)
Pour une sécurité renforcée, vous pouvez utiliser une paire de clés SSH au lieu d’un mot de passe. Voici comment faire :

Générer une clé SSH sur votre appareil Android (avec Termux, par exemple).
Copier la clé publique sur le serveur distant (dans le fichier ~/.ssh/authorized_keys).
Configurer l’application SSH pour utiliser la clé privée.


5. Résoudre les problèmes courants

Connexion refusée : Vérifiez l’adresse IP, le port, le nom d’utilisateur et le mot de passe.
Problème de réseau : Assurez-vous que votre appareil est connecté à Internet et que le serveur est accessible.
Port bloqué : Si vous êtes sur un réseau public (Wi-Fi d’hôtel, entreprise), le port 22 peut être bloqué. Essayez d’utiliser un autre port ou un VPN.


Exemple avec Termux
Si vous utilisez Termux, voici les commandes de base :
pkg update && pkg upgrade
pkg install openssh
ssh utilisateur@adresse_ip -p 22
```

**Description** : réaliser un connexion ssh depuis android
**Tags** : connexion,ssh,android
