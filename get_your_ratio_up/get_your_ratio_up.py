FILES       = ['data_example.txt'] # Just copy paste the torrents list on a page
TORRENTS_NB = 5              # Automatic scanner will be added soon

print('{} BEST LEECH/SEED RATIOS: '.format(TORRENTS_NB))
print('-'*50)


torrents    = []
attributes  = ['name', 'nfo','comments', 'age', 'size', 'compl', 'seed', 'leech']

for file in FILES:

    lines = open(file, 'r').readlines()
    for line in lines:
        torrent = {}
        i=0
        for value in line.split('\t'):
            torrent[attributes[i]] = value
            i+=1

        torrent['leech'] = int(torrent['leech'])
        torrent['seed'] = int(torrent['seed'])
        if torrent['leech'] > 0:
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

    print('{}. {}\nRatio: {:.3f}\nSeed: {} || Leech: {}\nSize: {}'.format(b, name, ratio, seed, leech, size))
    if b != len(bests):
        print('-'*50)

    b+=1
