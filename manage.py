import os, shelve, string, uuid

pwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(pwd)

def createNation():
    thisId = uuid.uuid4()
    thisName = raw_input('Nation name? ')
    f = shelve.open('./nation/'+thisName)
    f['id'] = thisId
    f['name'] = thisName
    f['leagues'] = []
    f.close()
    print 'done'
    restart()
    
def getNations():
    nations = os.listdir('./nation')
    if (len(nations) == 0):
        return 0
    else:
        if (nations[0] == '.DS_Store'):
            nations = nations[1:]
        return nations
        
def selectNation():
    nationList = getNations()
    if (nationList == 0):
        print 'No nations in the database, pls create one first...'
        return ''
    else:
        for each in nationList:
            print str(nationList.index(each) + 1) + ': '+ each
            
        selectN = string.atoi(raw_input('Please select one nation by its number: '))
        return nationList[selectN - 1]
        
def chooseNation(natName):
    f = shelve.open('./nation/'+natName)
    return f
    
def createLeague():
    thisId = uuid.uuid4()
    thisName = raw_input('League name? ')
    
    n = selectNation()
    nationF = shelve.open('./nation/'+n)
    thisNation = nationF['name']
    thisLevel = string.atoi(raw_input('League level? '))
    thisRounds = string.atoi(raw_input('League rounds? '))
    
    print ''
    print 'Name: ' + thisName
    print 'Nation: ' + thisNation
    print 'level: ' + str(thisLevel)
    print 'rounds: ' + str(thisRounds)
    print ''
    
    confirmation = raw_input('Is it OK? Y for yes, N for No: ')
    
    if (confirmation == 'Y'):
        temp = nationF['leagues']
        temp.append(str(thisId))
        nationF['leagues'] = temp
        nationF.close()
        lF = shelve.open('./league/' + str(thisId))
        lF['id'] = thisId
        lF['name'] = thisName
        lF['nation'] = thisNation
        lF['level'] = thisLevel
        lF['rounds'] = thisRounds
        lF['teams'] = []
        lF['promoteTo'] = ''
        lF['promoteTeams'] = 0
        lF['promotePlayoffNumber'] = 0
        lF['promotePlayoffSelection'] = 0
        lF['relegateTo'] = []
        lF['relegateTeams'] = 0
        lF['relegatePlayoffNumber'] = 0
        lF['relegatePlayoffSelection'] = 0
        
        print 'done'
        restart()

    else:
        print 'Cancelled, please restart ...'
        restart()
        
    
def chooseLeague(leaId):
    f = shelve.open('./league/'+leaId)
    return f
    
def listLeague(nationName):
    nF = chooseNation(nationName)
    leagList = nF.leagues
    nF.close()
    
    leagNames = []
    for each in leagList:
        lF = chooseLeague(each)
        leagNames.append(lF['name'])
        lF.close()   
        
def exitMe():
    print 'exit, byebye'
    return 0
    
def start():
    print 'Welcome to footy calculator manager!'
    print 'Programmed by ronfe'
    
    print ''
    print '1. Nation'
    print '2. League'
    print '3. Club'
    print '4. Round Match'
    print 'e, exit system'
    
    selection = raw_input('What do you want to create: ')
    
    options = {'1': createNation, '2': createLeague, 'e': exitMe}
    
    options[selection]()
    

def restart():
    print ''
    print '1. Nation'
    print '2. League'
    print '3. Club'
    print '4. Round Match'
    print 'e, exit system'
    
    selection = raw_input('What do you want to create: ')
    
    options = {'1': createNation, '2': createLeague, 'e': exitMe}
    
    options[selection]()
    
start()