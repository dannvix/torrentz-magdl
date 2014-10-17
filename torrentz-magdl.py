#!/usr/bin/env python
# encoding: utf-8
# torrentz-dl.py - command-line downloader for Torrentz resources

import re
import sys
import urllib
import webbrowser
from HTMLParser import HTMLParser

# pip install requests
import requests
try:
    # pip install blessings
    from blessings import Terminal
except ImportError, e:
    class Terminal:
        def __getattr__(self, name):
            def _missing(*args, **kwargs):
                return ''.join(args) or None
            return _missing


# globals
h = HTMLParser()
t = Terminal()


def query(keyword, num=10):
    url = 'https://torrentz.eu/search'
    params = dict(f=keyword)
    response = requests.get(url, params=params)
    if response.status_code == requests.codes.ok:
        html = response.text
        items = [m.groupdict() for m in re.finditer(r'<dl><dt><a href="/(?P<sha1>[0-9a-f]+)">(?P<title>.*)</a>', html)]
        dates = re.findall(r'<span class="a"><span title="[^"]+">(.*)</span></span>', html)
        metas = re.findall(r'<span class="[sud]+">([^<]*)</span>', html) # [size, seeds, peers]
        results = []
        for idx, item in enumerate(items[:num]):
            title = h.unescape(re.sub(r'</?b>', '', item['title']))
            results.append(dict(
                sha1=item['sha1'],
                title=title,
                date=dates[idx],
                size=metas[idx*3],
                seed=metas[idx*3+1],
                peer=metas[idx*3+2]))
        return results
    else:
        raise Exception('HTTP status_code=%s' % response.status_code)
    return []


def ask(choices):
    for idx, item in enumerate(choices):
        num = t.red(str(idx+1).rjust(2))
        title = t.white(item['title'].ljust(70))
        date = t.yellow(item['date'].rjust(10))
        seed = t.blue(item['seed'].rjust(6))
        peer = t.green(item['peer'].rjust(6))
        print '%s. %s %s %s %s' % (num, title, date, seed, peer)
    answers = raw_input('What items do you want? (seperated by commas) [1] ')
    if answers: return map(lambda x: int(x)-1, answers.split(r','))
    else: return[0]


def download(items):
    # FIXME: random.choice(torrent host) to grab magnet links with tracker urls
    for item in items:
        dn = urllib.urlencode({'dn': item['title']})
        uri = 'magnet:?xt=urn:btih:%s&%s' % (item['sha1'], dn)
        webbrowser.open(uri)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: %s <keyword>' % sys.argv[0]
        print "Example: %s 'The Big Bang Theory S07E01'" % sys.argv[0]
        sys.exit(1)
    keyword = sys.argv[1]
    choices = query(keyword)
    chosen_ids = ask(choices)
    chosens = map(lambda idx: choices[idx], chosen_ids)
    download(chosens)
