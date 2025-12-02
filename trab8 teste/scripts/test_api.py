import requests
from collections import Counter

terms=['guerra','brasil','tecnologia']
url='http://127.0.0.1:5000/api/search'

for t in terms:
    try:
        r=requests.get(url, params={'termo':t,'per_page':50}, timeout=15)
        r.raise_for_status()
        data=r.json()
        results=data.get('results', [])
        print('\n===', t, '=> total', data.get('total', len(results)), 'pages', data.get('total_pages'))
        c=Counter([it.get('fonte','') for it in results])
        print('counts:', dict(c))
        for i, it in enumerate(results[:8],1):
            titulo = (it.get('titulo') or it.get('title') or '')
            link = it.get('orig_link') or it.get('link') or ''
            print(f"{i}. {titulo[:200]} -> {link}")
    except Exception as e:
        print('ERROR for', t, e)
