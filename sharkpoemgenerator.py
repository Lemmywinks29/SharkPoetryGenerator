import random

subject = ['a', 'the']

questionOpener = ['where', 'how']

question = ['do']

connector = ['and', 'with', 'where']

opener = ['when', 'although', 'while', 'as']

verbs = ['bled', 'faded', 'writhed', 'flowed', 'commiserated', 'ran', 'careened', 'helped', 'prostrated', 'waited', 'contemplated', 'pontificated', 'understood','climbed', 'killed', 'hurt', 'walked', 'stopped', 'ate', 'jumped', 'decided', 'considered', 'planted', 'swung', 'pounced', 'bit', 'began','cried', 'laughed', 'doubled over']

presverbs = ['writhe', 'fade', 'commiserate', 'flow', 'run', 'careen', 'help', 'prostrate', 'wait', 'contemplate', 'pontificate', 'understand', 'climb', 'kill', 'bleed', 'hurt', 'walk', 'stop', 'eat', 'jump', 'decide', 'consider', 'plant', 'swing', 'pounce', 'bite', 'begin', 'cry', 'laugh']

nouns = ['cypress', 'carolina cherry', 'pecan', 'tonight', 'clothespin', 'anchor', 'anaqua', 'carriage', 'tide', 'disease', 'frog', 'moon', 'toad', 'basilisk', 'spectacle', 'eternity', 'marriage', 'rabbit', 'farm', 'cactus', 'palace', 'ember', 'statue', 'hat', 'person', 'human', 'sponge', 'night', 'urchin', 'porch', 'cat', 'dog', 'mouse', 'table', 'plant', 'building', 'star', 'suitor', 'mollusk', 'map', 'sunset', 'daffodil', 'portrait', 'river', 'tree', 'particle' ]

plrnouns = ['people', 'spectacles', 'diseases', 'tides', 'anchors', 'clothespins', 'moons', 'basilisks', 'frogs', 'eternities', 'marriages', 'rabbits', 'farms', 'cacti', 'palaces', 'embers', 'statues', 'hats', 'humans', 'sponges', 'nights', 'porches', 'cats', 'dogs', 'mice', 'tables', 'plants', 'buildings', 'suitors', 'mollusks', 'stars', 'maps', 'sunsets', 'daffodils', 'portraits', 'rivers', 'streams', 'estuaries', 'trees', 'flora', 'fauna']

adjectives = ['tall', 'fading', 'synthetic', 'broken', 'bleeding', 'sinister', 'perishing', 'vile','phosphorescent', 'turqoise', 'diseased', 'aquatic', 'maddening', 'prostrate', 'endless', 'viscous', 'friendly', 'hateful', 'special', 'surely', 'decrepit', 'accidental', 'mournful', 'tricky', 'spiteful', 'beautiful', 'frowning', 'descending', 'decayed', 'sacharine', 'loved', 'rotten', 'vaporous', 'putrid', 'glowing', 'rambunctious', 'hesitant', 'eager', 'shining', 'dull', 'glimmering', 'peaceful', 'profound']



print (random.choice(subject), random.choice(adjectives) ,  random.choice(nouns),  random.choice(verbs), 'the', random.choice(plrnouns))
print (random.choice(opener), random.choice(subject),  random.choice(nouns),  random.choice(verbs), 'and' , random.choice(verbs))
print (random.choice(subject), random.choice(adjectives), random.choice(nouns),  random.choice(verbs))

print (" ")

print (random.choice(opener), random.choice(adjectives) ,  random.choice(nouns),  random.choice(verbs), random.choice(subject), random.choice(nouns))
print (random.choice(plrnouns),  random.choice(verbs), 'and' , random.choice(verbs))
print (random.choice(subject), random.choice(adjectives), random.choice(nouns),  random.choice(verbs), 'into' , random.choice(subject), random.choice(nouns))

print (" ")

print (random.choice(questionOpener), random.choice(question), random.choice(adjectives), random.choice(plrnouns), random.choice(presverbs) + '?')
print (random.choice(opener), random.choice(adjectives), random.choice(plrnouns), random.choice(presverbs))
print (random.choice(questionOpener), random.choice(question), random.choice(adjectives), random.choice(plrnouns), random.choice(presverbs))
print (random.choice(opener), random.choice(adjectives), random.choice(plrnouns), random.choice(presverbs) + '?')

"""the glimmering tide killed the anchors
when a clothespin decided and ate
a sinister mouse pounced

while eager frog understood the mollusk
nights cried and bit
the decayed portrait helped into the spectacle

where do vaporous plants run?
while prostrate tides flow
how do eager flora help
when dull tides jump?"""
