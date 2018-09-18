FILES               = ['data_example.txt']  # Just copy paste the torrents list on a page
TORRENTS_NB         = 15                    # Automatic scanner will be added soon
MIN_TORRENT_SIZE    = 1
MAX_TORRENT_SIZE    = 10                    # In Gb
MIN_SEED            = 10

if not MIN_TORRENT_SIZE: MIN_TORRENT_SIZE = 0
if not MAX_TORRENT_SIZE: MAX_TORRENT_SIZE = 999
if not MIN_SEED: MIN_SEED = 0

print('{} BEST LEECH/SEED RATIOS: '.format(TORRENTS_NB))
print('-'*50)


torrents    = []
attributes  = ['name', 'nfo','comments', 'age', 'size', 'compl', 'seed', 'leech']


def verify_torrent(torrent):
    if MIN_TORRENT_SIZE < torrent['size'] < MAX_TORRENT_SIZE and torrent['seed'] > MIN_SEED and torrent['leech'] > 0:
        return True
    return False


for file in FILES:

    lines = open(file, 'r').readlines()
    for line in lines:
        torrent = {}
        i=0
        splitted = line.split('\t')
        if len(splitted) == len(attributes):
            for value in splitted:
                torrent[attributes[i]] = value
                i+=1

            torrent['size']     = float(torrent['size'][:-2])
            torrent['leech']    = int(torrent['leech'])
            torrent['seed']     = int(torrent['seed'])
            if verify_torrent(torrent):
                torrents.append(torrent)

ratios = []

for torrent in torrents:
    seed = torrent['seed']
    leech = torrent['leech']
    ratio = leech/seed
    ratios.append([torrent, ratio])

ratios.sort(key=lambda x: x[1], reverse=True)

bests = ratios[:TORRENTS_NB]

b=1
for best in bests:
    torrent = best[0]
    name    = torrent['name']
    seed    = torrent['seed']
    leech   = torrent['leech']
    size    = torrent['size']
    ratio   = best[1]

    print('{}. {}\nRatio: {:.3f}\nSeed: {} || Leech: {}\nSize: {}Gb'.format(b, name, ratio, seed, leech, size))
    if b != len(bests):
        print('-'*50)

    b+=1
