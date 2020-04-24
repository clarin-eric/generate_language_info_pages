set -e

echo "Compress results"
tar -czvf ${LANG_INFO_PAGES_TAR} lang_info_pages/

if [ -e ./${LANG_INFO_PAGES_TAR} ]; then
  echo "Compressed results ${LANG_INFO_PAGES_TAR} finished"
else
  echo "Failed to compress results"
fi
