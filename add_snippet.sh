#!/bin/bash

# Chemin relatif au dossier courant
SNIPPETS_DIR="."

# Demander les informations
read -p "Langage (python/sql/postgres/bash/virsh/mariadb/git/docker/nginx/apache) : " lang
read -p "Nom du snippet (sans extension) : " name
read -p "Description : " description
read -p "Tags (séparés par des virgules) : " tags
echo "Code (appuyez sur Ctrl+D pour terminer) :"
code=$(cat)

# Créer le fichier Markdown
file_path="$SNIPPETS_DIR/$lang/${name}.md"
mkdir -p "$SNIPPETS_DIR/$lang"

cat > "$file_path" <<EOL
# $name

\`\`\`$lang
$code
\`\`\`

**Description** : $description
**Tags** : $tags
EOL

# Ajouter et commiter avec Git
git add .
git commit -m "Ajout du snippet $name ($lang)"

echo "Snippet ajouté : $file_path"
