import csv

PLAYER_LETTER = '''
    Dear {Guardian Name(s)},
    Your child {Name} has been added into the {team} team. 
    The first training will be on {training_info}. We hope to see you there!

    Kind regards,
    Soccer league organisation.
'''

TRAINING_INFO = {
    'Sharks': 'March 17 at 3PM',
    'Dragons': 'March 18 at 1PM',
    'Raptors': 'March 17 at 1PM'
}

def build_league():
    """
    Create soccer league, divide players, create `teams.txt` and create letter files
    """
    ### Read the csv file
    with open('soccer_players.csv') as players_file:
        players_reader = csv.DictReader(players_file)
        players = list(players_reader)

    ### Create empty team lists
    sharks = []
    dragons = []
    raptors = []

    ### Create list of all teams
    all_teams = {'Sharks': sharks, 'Dragons': dragons, 'Raptors': raptors}
    team_names = ['Sharks', 'Dragons', 'Raptors']

    ### Create emty lists for experienced and not experienced players
    experienced = []
    not_experienced = []

    ### Divide players on experience
    for player in players:
        if player['Soccer Experience'] == 'YES':
            experienced.append(player)
        else:
            not_experienced.append(player)

    ### Divide players over teams based on experience
    for index, player in enumerate(experienced):
        all_teams[team_names[index / 3]].append(player)
    for index, player in enumerate(not_experienced):
        all_teams[team_names[index / 3]].append(player)

    ### Create teams.txt file
    with open('teams.txt', 'a') as teamsFile:
        for name, team in all_teams.items():
            teamsFile.write(name + '\n=====\n')
            teamsFile.write(createPlayerListFromTeam(team))
    
    ### Create letters for each player
    for name, team in all_teams.items():
        for player in team:
            createLetterForPlayer(player, name, TRAINING_INFO[name])

def createPlayerListFromTeam(team):
    """Creates newline seperated list of players with some information"""
    playerStrings = []
    for player in team:
        playerStrings.append('{}, {}, {}'.format(player['Name'], player['Soccer Experience'], player['Guardian Name(s)']))
    return '\n'.join(playerStrings) + '\n\n'

def createLetterForPlayer(player, team, training_info):
    """Creates formatted letter in textfile for player with specified info"""
    filename = player['Name'].lower().replace(' ', '_')
    with open(filename + '.txt', 'w') as playerFile:
        playerFile.write(PLAYER_LETTER.format(team=team, training_info=training_info, **player))
   
if __name__ == '__main__':
    build_league()