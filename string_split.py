import re
w = 'AbcDefgHijkL'
ws= '    .nalf!!213knlsc'
wd ='   ca++ and mbbs '

loc ='mumbai dombivli'
r = re.findall('([A-Z])', w)
print(r)

r = re.findall('([A-Z][a-z]+)', w)
print(r)



r = re.findall('([a-z,A-Z,+]+)',wd)
print(r)

print(' '.join(r))

loc.find('mumcai')

join_locations = {
    'ncr': ['delhi', 'faridabad', 'gurgaon', 'noida', 'ncr'],
    'bangluru': ['banglore', 'bangluru'],
    'pune': ['pune'],
    'hydrabad': ['hydrabad']

}


def cluster_location(location):
    for key,value in join_locations.items():
        print(key , value)
        for item in value:
            print(item)


cluster_location('my name is mumbai pune is new')
