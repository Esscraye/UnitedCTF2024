#!/bin/bash

# Vérifiez si le fichier .jar est fourni
if [ -z "$1" ]; then
  echo "Usage: $0 <path_to_jar_file>"
  exit 1
fi

# Chemin vers le fichier .jar
JAR_FILE=$1

# Répertoire de sortie pour le code source décompilé
OUTPUT_DIR="decompiled_source"

# Téléchargez CFR si nécessaire
if [ ! -f "cfr.jar" ]; then
  echo "Téléchargement de CFR..."
  wget https://www.benf.org/other/cfr/cfr-0.151.jar -O cfr.jar
fi

# Décompilez le fichier .jar
echo "Décompilation de $JAR_FILE..."
java -jar cfr.jar "$JAR_FILE" --outputdir "$OUTPUT_DIR"

echo "Décompilation terminée. Le code source est dans le répertoire $OUTPUT_DIR"