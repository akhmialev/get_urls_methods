import json
import urlextract
import requests


def see_json(data):
    datas = json.dumps(data)
    print(datas)


def http_methods(urls, methods):
    data = {}
    if urls:
        for url in urls:
            data[url] = {}
            for method in methods:
                try:
                    r = requests.request(f'{method}', url)
                    if r.status_code != 405:
                        m = str(method).upper()
                        code = r.status_code
                        data[url].update({m: code})
                except:
                    print(f'{url}: not correct url')

    return data



def check_url(urls):
    extractor = urlextract.URLExtract()

    for u in urls:
        url = extractor.find_urls(u)
        if url:
            return url
        else:
            print('String not url')


def main():
    urls = [i for i in str(input()).split(',')]
    methods = ['post', 'get', 'head', 'put', 'option', 'delete', 'connect', 'trace', 'patch']

    see_json(http_methods(check_url(urls), methods))


if __name__ == '__main__':
    main()
