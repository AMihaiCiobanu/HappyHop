#!/bin/sh
# Construieste folderul `dist/` cu exact fisierele care trebuie urcate pe server.
# Exclude fotografiile originale (_source-photos/) si generatorul (_tools/).
set -e
cd "$(dirname "$0")"
rm -rf dist
mkdir -p dist
cp *.html robots.txt sitemap.xml dist/
cp -R css js assets dist/
echo "dist/ gata — $(du -sh dist | cut -f1)"
