#!/bin/bash

# target directory and the URL of Scripts repo
TARGET_DIR="scripts"

# check whether the Scripts repo exists or not. If not exist, clone the Scripts repo.
if [ -d "$TARGET_DIR" ]; then
  echo "Directory '$TARGET_DIR' exists. Entering and updating repository..."
  cd "$TARGET_DIR"
  git pull
  cd ..
else
  echo "Directory '$TARGET_DIR' does not exist. Cloning repository..."
  git clone -b new_check_format "$SCRIPTS_REPO"
fi

# Initialize variables
EN_FILES=()
ZH_CN_FILES=()

echo "Changed files: $@"

# Inspect each file passed to the script
for file in "$@"; do
  case "$file" in
    docs/en/*) EN_FILES+=("$file") ;;
    docs/zh_CN/*) ZH_CN_FILES+=("$file") ;;
  esac
done

# Process English files if any
if [ ${#EN_FILES[@]} -gt 0 ]; then
  echo "Start checking the rst format for English file(s): ${EN_FILES[*]}"
  python3 scripts/check_docs_format.py "en" "${EN_FILES[@]}"
fi

# Process Chinese files if any
if [ ${#ZH_CN_FILES[@]} -gt 0 ]; then
  echo "Start checking the rst format for Chinese file(s): ${ZH_CN_FILES[*]}"
  python3 scripts/check_docs_format.py "zh_CN" "${ZH_CN_FILES[@]}"
fi

# Handle case where no files matched
if [ ${#EN_FILES[@]} -eq 0 ] && [ ${#ZH_CN_FILES[@]} -eq 0 ]; then
  echo "No matching files found in 'en/' or 'zh_CN/' folders."
fi
