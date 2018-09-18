
FILES = ['data_example.txt'] # Just copy paste the torrents list on a page, automatic scanner will be added soon
TORRENTS_NB = 5              # Numbers of bests ratios to display

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
    name = torrent['name']
    seed = torrent['seed']
    leech = torrent['leech']
    ratio = best[1]

    print('{}. {}\nRatio: {}\nSeed: {} || Leech: {}'.format(b, name, ratio, seed, leech))
    print('-'*50)

    b+=1
