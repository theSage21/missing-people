import os
from tqdm import tqdm
import pandas as pd


files = [os.path.join('csvs', i) for i in sorted(os.listdir('csvs'))]
parts = []
for path in tqdm(files):
    part = pd.read_csv(path, header=None)
    if len(part) > 0:
        vals = (part.values)
        parts.extend(list(vals))
    else:
        print(path)
df = pd.DataFrame(parts)
df = df.drop_duplicates()
df.columns = ['slno', 'A', 'B', 'C', 'D', 'E']
df = df.loc[df.E != 'Photograph']
df = df.fillna('')


def proc(x):
    return x.strip().replace('\r', ' ').replace('  ', ' ')


for col in df.columns[1:]:
    df[col] = df[col].apply(proc)
df = df.drop('E', axis=1)
raw = df.copy()
df = pd.DataFrame()


# ------------- reformat to columns
def get_name(x):
    n = x.split(',')[0]
    n = n if n not in ['Male', 'Female'] else None
    return n


def get_gender(x):
    g = None
    if 'Male' in x:
        g = 'Male'
    elif 'Female' in x:
        g = 'Female'
    return g


def get_relative(x):
    n = x.split(',')
    if n[0] in ['Male', 'Female']:
        n = n[1]
    else:
        try:
            n = n[2]
        except IndexError:
            n = None
    n = n if n not in ['Male', 'Female'] else None
    return n


def get_address(x):
    n1 = get_name(x)
    n2 = get_relative(x)
    if 'Male' in x:
        x = x.replace('Male', '')
    if 'Female' in x:
        x = x.replace('Female', '')
    if n1 is not None:
        x = x.replace(n1, '')
    if n2 is not None:
        x = x.replace(n2, '')
    x = x.replace(',,', ',')
    return x


def get_age_start(x):
    x = x.replace(' - ', '-')
    x = x.split(' ')
    if '-' in x[0]:
        return int(x[0].split('-')[0])


def get_age_end(x):
    x = x.replace(' - ', '-')
    x = x.split(' ')
    if '-' in x[0]:
        return int(x[0].split('-')[1])


def get_height_start(x):
    x = x.replace(' - ', '-')
    x = x.split(' ')
    if '-' in x[1]:
        return float(x[1].split('-')[0])


def get_height_end(x):
    x = x.replace(' - ', '-')
    x = x.split(' ')
    if '-' in x[1]:
        return float(x[1].split('-')[1])


def get_built(x):
    x = x.split('-')[-1]
    x = x.strip().split(' ')[1:]
    return ''.join(x)


def get_missing_date(x):
    parts = list(reversed(x.split(' ')))
    date = ''
    for p in parts:
        nd = date + p
        if nd.count('/') == 2:
            return date
    return None


def get_ps(x):
    return x.split('/')[0]


def get_district(x):
    diststate = x.split('#')[0]
    dist = '/'.join(diststate.split('/')[:-1])
    return dist


def get_state(x):
    diststate = x.split('#')[0]
    state = diststate.split('/')[-1][:-2].strip()
    return state


df['Name'] = raw.A.apply(get_name)
df['Gender'] = raw.A.apply(get_gender)
df['Relative'] = raw.A.apply(get_relative)
df['Address'] = raw.A.apply(get_address)
df['AgeStart'] = raw.B.apply(get_age_start)
df['AgeEnd'] = raw.B.apply(get_age_end)
df['HeightStart'] = raw.B.apply(get_height_start)
df['HeightEnd'] = raw.B.apply(get_height_end)
df['Built'] = raw.B.apply(get_built)
df['Date'] = raw.C.apply(get_missing_date)
df['Dist'] = raw.D.apply(get_district)
df['State'] = raw.D.apply(get_state)


print(raw.D)

# -------------
df.to_csv('data.csv', index=False)
print(df.info())
