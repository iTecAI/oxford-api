import ems
import urllib2 as url
def getDefs(word, numdef):
    psr = ems.parser(url.urlopen('https://en.oxforddictionaries.com/definition/' + word).read())
    defspans = psr.getElementsByClass('ind')
    defs = []
    if numdef > len(defspans):
        for i in defspans:
            defs.append(psr.getContent(i))
    else:
        for i in defspans[0:numdef]:
            defs.append(psr.getContent(i))
    return defs

#args:
#word: word to be defined
#numdef: how many definitions you want
    


