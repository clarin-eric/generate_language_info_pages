#!/bin/bash

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
OUTPUT_DIR="${SCRIPT_DIR}/output"

if [ -e "${OUTPUT_DIR}/tmp"/* ]; then
	echo -n "Previous temporary output found in ${OUTPUT_DIR}/tmp. Remove? (y/n)"
	read YN
	if [ "${YN}" = 'y' ]; then
		rm -r "${OUTPUT_DIR}/tmp"/*
	else
		echo "Aborted"
		exit 1
	fi
fi

if [ -e "${OUTPUT_DIR}/tmp"/* ]; then
	echo "Noise found in ${OUTPUT_DIR}/tmp, please remove manually. Aborted"
	exit 1
fi

mkdir -p "${OUTPUT_DIR}/tmp"

# Build
(cd "${SCRIPT_DIR}" && docker build --tag "generate_language_info_pages:latest" .)


# Run
docker run --rm -v "${OUTPUT_DIR}/tmp":"/tmp" "generate_language_info_pages:latest"

# Check output
if [ -d "${OUTPUT_DIR}/tmp"/* ]; then
  mv "${OUTPUT_DIR}/tmp"/* "${OUTPUT_DIR}"
  echo "Result found in ${OUTPUT_DIR}"
  rmdir "${OUTPUT_DIR}/tmp"
else
  echo "ERROR: No result found in ${OUTPUT_DIR}"
fi
