#!/bin/bash

# Chemin absolu vers le dossier snippets
SNIPPETS_DIR="$HOME/snippets"

# Demander le tag à rechercher
read -p "Tag à rechercher : " tag

# Vérifier que le dossier snippets existe
if [ ! -d "$SNIPPETS_DIR" ]; then
    echo "Erreur : Le dossier $SNIPPETS_DIR n'existe pas."
    exit 1
fi

# Rechercher les fichiers contenant le tag
rg --color=always -l --glob="*.md" "Tags.*$tag" "$SNIPPETS_DIR/" | sed -r "s/\x1B\[[0-9;]*[mGK]//g" | while IFS= read -r file; do
    echo "---"
    echo "Fichier : $file"
    echo "---"
    batcat --language=markdown "$file"
    echo
done
