from collections import Counter
from app import raspar_g1, raspar_google_noticias, analisar_sentimento

terms = ['guerra', 'brasil', 'tecnologia']

for t in terms:
    try:
        print('\n===', t)
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
        print('total:', len(combined))
        c = Counter([it.get('fonte','') for it in combined])
        print('counts:', dict(c))
        for i, it in enumerate(combined[:8],1):
            print(f"{i}. {it.get('titulo','')[:200]} -> {it.get('orig_link') or it.get('link')}")
    except Exception as e:
        print('ERROR for', t, e)
