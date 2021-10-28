import random
import requests

with open("team_members.txt") as team_members_file, open("team_member_history.txt") as team_member_history_file, open("fonts.txt") as fonts_file:
    # load static fonts
    fonts = [l.rstrip() for l in fonts_file.readlines()]
    # load static team members
    team_members = [l.rstrip() for l in team_members_file.readlines()]
    # load history of choices
    team_member_history = [l.rstrip() for l in team_member_history_file.readlines()]
    team_member_choices = [tm for tm in team_members if tm not in team_member_history]

    team_member_history_file_write_buffer = ["\n"]
    
    # when we've chosen everyone, start over
    if len(team_member_choices) == 0 or len(team_member_history) == 0:
        team_member_choices = team_members
        # delete history
        open("team_member_history.txt", "w").close()
        team_member_history_file_write_buffer.pop()
    
    # pick a team member
    team_member = random.choice(team_member_choices)
    team_member_history_file_write_buffer.append(team_member)

    with open("team_member_history.txt", "a+") as team_member_history_file:
        # record the choice
        for contents in team_member_history_file_write_buffer:
            team_member_history_file.write(contents)

    # pick a font
    font = random.choice(fonts)
    
    print(f"and the winner is....\n")
    r = requests.get(f'https://artii.herokuapp.com/make?text={team_member}&font={font}')
    print(r.text)
    print(f"\na.k.a {team_member} (in {font} font)")
