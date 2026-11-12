import re, json
from collections import Counter
txt = open('guide.txt', encoding='utf-8').read()
pages = txt.split('\f')
DEPT_MAP = {"english/language arts":"English Language Arts","english language arts":"English Language Arts","language arts":"English Language Arts",
 "social studies":"Social Studies","mathematics":"Mathematics","science":"Science","physical education & health":"Physical Education & Health",
 "physical education":"Physical Education & Health","health":"Physical Education & Health","art":"Art","avid":"AVID",
 "business and computer science":"Business & Computer Science","business & computer science":"Business & Computer Science",
 "career & internship experiences":"Career & Internship Experiences","career and internship experiences":"Career & Internship Experiences",
 "english learners (el) program":"English Learners","english learners":"English Learners",
 "family and consumer sciences":"Family & Consumer Sciences","family & consumer sciences":"Family & Consumer Sciences",
 "music":"Music","non-departmental":"Non-departmental","technology education":"Technology Education","world languages":"World Languages","world language":"World Languages"}
hdr = re.compile(r'^\s*(\d{4}(?:\s*,\s*\d{4})*)\s*[–—-]\s*(.+?)\s*$')
metare = re.compile(r'^\s*(Full[ -]year|Semester|Year[- ]?long|Quarter|Trimester|[\d½.]+\s*credits?)', re.I)
def PAGE_DEPT(p, cur):
    rng=[(34,38,'English Language Arts'),(39,43,'Social Studies'),(44,44,'Social Studies'),(45,50,'Mathematics'),(51,55,'Science'),(56,59,'Physical Education & Health'),(60,63,'Art'),(64,65,'AVID'),(66,67,'Business & Computer Science'),(68,75,'Career & Internship Experiences'),(76,77,'English Learners'),(78,80,'Family & Consumer Sciences'),(81,85,'Music'),(86,87,'Non-departmental'),(88,89,'Technology Education'),(90,90,'Art'),(91,95,'World Languages')]
    for a,b,d in rng:
        if a<=p<=b: return d
    return cur
dept=None; courses=[]; pending=[]; cur_group=None
def start_group():
    global cur_group
    cur_group = dict(entries=pending[:], body=[], meta=[])
    courses.append(cur_group)
for pno, pg in enumerate(pages, 1):
    if pno < 34 or pno > 95: continue
    dept = PAGE_DEPT(pno, dept)
    lines = pg.split('\n')
    for i, ln in enumerate(lines):
        s = ln.strip()
        if not s:
            if cur_group is not None and cur_group['body'] and cur_group['body'][-1] != '': cur_group['body'].append('')
            continue
        base = re.sub(r'\s*[-–]\s*Continued$', '', s, flags=re.I).strip().lower()
        if base in DEPT_MAP and len(s) < 70:
            continue
        m = hdr.match(ln)
        if m and not s.lower().startswith('prereq'):
            # header if some line in next 3 looks like meta, or next line is another header
            nxt = [l.strip() for l in lines[i+1:i+9] if l.strip() and l.strip().lower() not in ('mathematics','departments','science','art','music','avid','careers & internships','course descriptions') and not re.fullmatch(r'\d{1,3}',l.strip()) and not re.match(r'^(Mathematics|Science|Music|Art|World Languages?|Physical Education|English/Language Arts|Social Studies)( - Continued)?$',l.strip(),re.I)]
            if nxt and (metare.match(nxt[0]) or hdr.match(nxt[0]) or re.search(r'credit', nxt[0], re.I)):
                if cur_group is not None and not pending_open if False else False: pass
                if not pending or not cur_group is None and cur_group.get('closed', True) is False:
                    pass
                # new header: if previous group already has meta, start fresh pending
                if cur_group is not None and cur_group['meta']:
                    pending.clear(); cur_group = None
                pending.append(dict(codes=[c.strip() for c in m.group(1).split(',')], title=m.group(2), dept=dept, page=pno))
                continue
        if pending and cur_group is None:
            if metare.match(s) or re.search(r'credit', s, re.I):
                start_group(); cur_group['meta'].append(s); continue
        if cur_group is not None:
            if not cur_group['meta'] or len(cur_group['meta']) < 3 and re.match(r'^(Grades?\b|Prereq)', s, re.I) is None and False: pass
            if len(cur_group['meta']) < 2 and re.match(r'^(Grades?\b|[-–])', s, re.I) and not cur_group['body']:
                cur_group['meta'].append(s); continue
            if re.fullmatch(r'\d{1,3}', s): continue
            cur_group['body'].append(s)
out=[]
for g in courses:
    mm = ' '.join(g['meta'])
    b = '\n'.join(g['body'])
    term = 'Full Year' if re.search(r'full[ -]year|year-?long', mm, re.I) else ('Semester' if re.search('semester', mm, re.I) else ('Quarter' if re.search('quarter',mm,re.I) else ''))
    cr = re.search(r'([\d.]*\d?\s*½|[\d]*\.?\d+(?:\s*/\s*\d)?)\s*credits?', mm, re.I)
    credits = ''
    if cr: credits = cr.group(1).replace(' ','').replace('½','.5') if cr.group(1)!='½' else '.5'; credits = '0.5' if credits in ('.5','0.5') else credits
    gr = re.search(r'Grades?\s*([0-9s].*?)(?:\s*$)', mm, re.I)
    if not gr: gr = re.search(r'Grades?\s*([0-9s][0-9s\s,/&–-]*)', b[:200], re.I)
    pre = re.search(r'Prerequisites?s?\s*[:\-]?\s*(.+?)(?=\n\s*\n|\Z)', b, re.S)
    gl = re.search(r'(Guideline[^\n]*(?:\n(?!\s*\n)[^\n]*)?)', b)
    hw = re.search(r'Homework Guide\s*=\s*([0-9.\-–]+)', b)
    mult = re.search(r'Weighted Grade,?\s*([\d.]+)\s*Multiplier', b)
    for e in g['entries']:
        out.append(dict(codes=e['codes'], title=e['title'], department=e['dept'], pdf_page=e['page'],
            term=term, credits=credits, grades=(re.sub(r'\s*(l|\|)\s*Prereq.*$','',re.sub(r'\s+',' ',gr.group(1)).strip()) if gr else ''),
            prerequisite=(re.sub(r'\s+',' ',pre.group(1)).strip()[:400] if pre else ''), guideline=(re.sub(r'\s+',' ',gl.group(1)).strip()[:200] if gl else ''),
            homework_guide=hw.group(1) if hw else '', weighted_multiplier=mult.group(1) if mult else '',
            college_credit=bool(re.search(r'college credit|PSEO|concurrent enrollment|\(CE\)|\bCE\b|\bCIS\b|AP', b+' '+e['title'])),
            raw_meta=mm, description=re.sub(r'\n{3,}','\n\n',re.sub(r'[ \t]+',' ',b)).strip()))
json.dump(out, open('build/courses_raw2.json','w'), indent=1, ensure_ascii=False)
print(len(out)); print(Counter(o['department'] for o in out))
for k in ['credits','grades','term','homework_guide']:
    print('missing',k,[o['title'] for o in out if not o[k]])
