# Usage instructions
#
# - `docker build --tag generate_language_info_pages:latest .`
# - `docker run --rm -v $(pwd)/output:/tmp generate_language_info_pages:latest`
# - Find results in $(pwd)/output

FROM python:3.7.17-alpine3.18

COPY . /generate_language_info_pages

WORKDIR /generate_language_info_pages

RUN python setup.py install --user

CMD ["ash", "-c", "cd /generate_language_info_pages && python -m 'generate_language_info_pages'"]
