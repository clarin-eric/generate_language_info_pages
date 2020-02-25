#!/bin/sh

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
OUTPUT_DIR="${SCRIPT_DIR}/output"

# Build
(cd "${SCRIPT_DIR}" && docker build --tag "generate_language_info_pages:latest" .)


# Run
docker run --rm -v "${OUTPUT_DIR}":"/tmp" "generate_language_info_pages:latest"

# Check output
if [ -d "${OUTPUT_DIR}"/langinfo* ]; then
  echo "Result found in $(echo "${OUTPUT_DIR}"/langinfo*)"
else
  echo "ERROR: No result found in ${OUTPUT_DIR}"
fi

