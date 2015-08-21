#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from pathlib import Path


def process_language(resource, endangered_languages_http_connection_pool, output_dir_path: Path, template):
    from logging import info
    from requests.status_codes import codes

    identifiers = {identifier['type']: identifier['identifier'] for identifier in resource['identifiers']}
    if 'iso639-3' in identifiers:
        identifiers['iso639'] = identifiers.pop('iso639-3')
        identifiers['glottolog'] = resource['id']
        identifiers['name'] = resource['name']
        if 'WALS' not in identifiers:
            identifiers['WALS'] = ''

        endangered_languages_http_request_response = endangered_languages_http_connection_pool.head(
            'http://www.endangeredlanguages.com/lang/' + identifiers['iso639'])

        language_info_page_file_path = output_dir_path.joinpath(identifiers['iso639'] + '.html')

        with language_info_page_file_path.open(mode='wt', encoding='utf-8') as language_info_page_file:
            info('Written language info page {language_info_page_file_path}'.format(
                language_info_page_file_path=language_info_page_file_path))
            language_info_page_file.write(
                template.render(iso639=identifiers['iso639'],
                                glottolog=identifiers['glottolog'],
                                name=identifiers['name'],
                                wals=identifiers['WALS'],
                                is_on_endangered_languages=endangered_languages_http_request_response.status_code ==
                                                           codes['OK']))


def main():
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from json import loads
    from logging import error, warning
    from mako.template import Template
    from pathlib import Path
    from requests import get, Session
    from requests.adapters import HTTPAdapter
    from sys import stdout
    from tempfile import mkdtemp

    glottlog_response = get('http://glottolog.org/resourcemap.json?rsc=language')
    glottolog_mapping = loads(glottlog_response.text)

    template = Template(filename='data/language_info.template.html',
                        input_encoding='utf-8')

    output_dir_path = Path(mkdtemp(prefix='langinfo_'))

    warning("Creating language info pages in '{output_dir_path}'.".format(output_dir_path=output_dir_path))

    with Session() as HTTP_connection_pool:
        adapter = HTTPAdapter(pool_connections=25, pool_maxsize=25)
        HTTP_connection_pool.mount('http://www.endangeredlanguages.com/lang/', adapter)
        number_of_languages = len(glottolog_mapping['resources'])

        with ThreadPoolExecutor(max_workers=4) as executor:
            future_to_response = dict((executor.submit(process_language,
                                                       language,
                                                       HTTP_connection_pool,
                                                       output_dir_path,
                                                       template),
                                       language)
                                      for language in glottolog_mapping['resources'])
            resource_index = 0
            for future in as_completed(future_to_response):
                resource_index += 1
                if future.exception() is not None:
                    error('Thread generated an exception: {0}'.format(future.exception()))
                else:
                    progress = resource_index / number_of_languages
                    block = int(round(80 * progress))
                    text = "\rProgress: [{0:s}] {1:0.3f} %".format("#" * block + "-" * (80 - block), progress * 100)
                    stdout.write(text)
                    stdout.flush()


if __name__ == '__main__':
    from logging import getLogger, WARNING

    getLogger().setLevel(WARNING)
    main()
