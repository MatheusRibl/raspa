import json
from collections import Counter
from app import raspar_g1, raspar_google_noticias, analisar_sentimento

terms = ['guerra','brasil','tecnologia']
out = {}

for t in terms:
    try:
        g1 = raspar_g1(t) or []
        ggoogle = raspar_google_noticias(t) or []
        combined = []
        seen = set()
        for r in (g1 + ggoogle):
            link = r.get('link') or r.get('orig_link')
            if not link or link in seen:
                continue
            seen.add(link)
            r['sentimento'] = analisar_sentimento(r.get('titulo',''))
            combined.append(r)
        out[t] = {
            'total': len(combined),
            'counts': dict(Counter([it.get('fonte','') for it in combined])),
            'examples': [{'titulo': it.get('titulo',''), 'link': it.get('orig_link') or it.get('link',''), 'sentimento': it.get('sentimento','')} for it in combined[:12]]
        }
    except Exception as e:
        out[t] = {'error': str(e)}

with open('scripts/latest_results.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print('WROTE scripts/latest_results.json')
