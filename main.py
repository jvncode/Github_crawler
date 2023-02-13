# -*- coding: utf-8 -*-
import requests
import json
from random import randint
from bs4 import BeautifulSoup
import chardet


class Crawler:

    def __init__(self, data):
        self.data = json.loads(data)

        # Support for Unicode characters
        for ix, key in enumerate(self.data['keywords']):
            if chardet.detect(str.encode(key))['encoding'] in \
                    ['utf-8', 'ISO-8859-9']:
                self.data['keywords'][ix].encode('ascii', 'ignore')

        self.keywords = "+".join(self.data['keywords'])
        self.proxies_list = self.data['proxies']
        self.data_type = self.data['type']
        self.dict_types = {
                    'Repositories': '',
                    'Isuues': '/issues',
                    'Wikis': '/wikis'
                    }
        self.url_base = f'https://github.com/search?q=\
                    {self.keywords}&type={self.dict_types[self.data_type]}'

        # Random choice of proxy
        self.proxy = {
            'http': self.proxies_list[randint(0, len(self.proxies_list)-1)]
            }
        # Connection to the Git search url
        self.html = requests.get(self.url_base, proxies=self.proxy)

    def parser(self):
        result_global = []
        result = {
            'url': '',
            'extra':
                {
                    'owner': '',
                    'language_stats':
                    {
                    }
                }
            }

        # Getting HTML code from search results
        soup = BeautifulSoup(self.html.text, features='html.parser')
        urls_repos = []
        for block in soup.find_all(class_='f4 text-normal'):
            temp = json.loads(block.a.get('data-hydro-click'))
            urls_repos.append(temp['payload']['result']['url'])

        # If results exist, HTML is fetched from each link for further parsing.
        if urls_repos != []:
            for url in urls_repos:
                repo_html = requests.get(url, proxies=self.proxy)
                soup_repo = BeautifulSoup(
                            repo_html.text,
                            features='html.parser')
                result['url'] = url
                result['extra']['owner'] = url.split('/')[3]
                for p in soup_repo.find_all(
                        'span',
                        class_="Progress-item color-bg-success-emphasis"):
                    result['extra']['language_stats'][p['aria-label']
                    .split(' ')[0]] = p['aria-label'].split(' ')[1]
                result_global.append(result)
                result = {
                    'url': '',
                    'extra':
                        {
                            'owner': '',
                            'language_stats':
                            {
                            }
                        }
                    }

            # Returns results in JSON format
            return json.dumps(result_global)
        return json.dumps({})


# Reading _input.json file and using the data for the instance
try: 
    input_data = open('_input.json', 'r')
    s = Crawler(input_data.read())
    input_data.close()
except Exception as e:
    print(f"Reading error: {e}")

#  Writing the result of the execution to the file _output.json
try:
    output_data = open('_output.json', 'w')
    output_data.write(s.parser())
    output_data.close()
except Exception as e:
    print(f"Typing error: {e}")
