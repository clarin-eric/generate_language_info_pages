#!/bin/bash
set -e

echo "Generating language info pages"
bash ./docker-run.sh ./lang_info_pages
