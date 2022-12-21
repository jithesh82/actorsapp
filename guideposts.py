# guideposts for actors
guidep = {
        'relationship':'',
        'what I want; what am I fighting for':'',
        'moment before':'',
        'humour':'',
        'opposites':'',
        'discoveries':'',
        'communication & competition':'',
        'importance':'',
        'find the events':'',
        'place':'',
        'game playing & role playing':'',
        'mistery and secrets':'',
        'mischief':'',
        'vulnerability':'',
        'architechture':''
        }
f = open(input('filename: ') + '.txt', 'w')
for item in guidep:
    value = input(item + ': ')
    f.write(item + ': ' + value + '\n')
f.close()
