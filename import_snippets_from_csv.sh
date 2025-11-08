#!/bin/bash

# Chemin absolu vers le dossier snippets
SNIPPETS_DIR="$HOME/snippets"
CSV_FILE="$1"

# Vérifier que le fichier CSV est fourni
if [ -z "$CSV_FILE" ]; then
    echo "Usage: $0 <fichier.csv>"
    exit 1
fi

# Vérifier que le fichier CSV existe
if [ ! -f "$CSV_FILE" ]; then
    echo "Erreur : Le fichier $CSV_FILE n'existe pas."
    exit 1
fi

# Lire le fichier CSV et créer les snippets
tail -n +2 "$CSV_FILE" | while IFS=, read -r langage nom titre code description tags; do
    # Supprimer les guillemets des champs
    titre=$(echo "$titre" | tr -d '"')
    code=$(echo "$code" | tr -d '"')
    description=$(echo "$description" | tr -d '"')
    tags=$(echo "$tags" | tr -d '"')

    # Créer le chemin du fichier
    mkdir -p "$SNIPPETS_DIR/$langage"
    file_path="$SNIPPETS_DIR/$langage/${nom}.md"

    # Vérifier si le fichier existe déjà
    if [ -f "$file_path" ]; then
        read -p "Le fichier $file_path existe déjà. Voulez-vous l'écraser ? (o/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Oo]$ ]]; then
            echo "Le fichier $file_path n'a pas été écrasé."
            continue
        fi
    fi

    # Créer le fichier Markdown
    cat > "$file_path" <<EOL
# $titre

\`\`\`$langage
$code
\`\`\`

**Description** : $description
**Tags** : $tags
EOL

    echo "Snippet ajouté : $file_path"
done

# Ajouter et commiter avec Git
cd "$SNIPPETS_DIR" || exit
git add .
git commit -m "Ajout des snippets depuis le fichier CSV"
