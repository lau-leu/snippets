#!/bin/bash

# Chemin absolu vers le dossier snippets
SNIPPETS_DIR="$HOME/snippets"

# Vérifier que le dossier snippets existe
if [ ! -d "$SNIPPETS_DIR" ]; then
    echo "Erreur : Le dossier $SNIPPETS_DIR n'existe pas."
    exit 1
fi

# Menu interactif
echo "Choisissez une option :"
echo "1. Rechercher par mot-clé"
echo "2. Rechercher par tag"
read -p "Option (1 ou 2) : " option

if [ "$option" = "1" ]; then
    read -p "Mot-clé à rechercher : " keyword
    rg --color=always -l --glob="*.md" "$keyword" "$SNIPPETS_DIR/" | sed -r "s/\x1B\[[0-9;]*[mGK]//g" | while IFS= read -r file; do
        echo "---"
        echo "Fichier : $file"
        echo "---"
        batcat --language=markdown "$file"
        echo
    done
elif [ "$option" = "2" ]; then
    read -p "Tag à rechercher : " tag
    rg --color=always -l --glob="*.md" "Tags.*$tag" "$SNIPPETS_DIR/" | sed -r "s/\x1B\[[0-9;]*[mGK]//g" | while IFS= read -r file; do
        echo "---"
        echo "Fichier : $file"
        echo "---"
        batcat --language=markdown "$file"
        echo
    done
else
    echo "Option invalide."
fi
