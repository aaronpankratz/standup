# Standup

Kick off standup meeting in a fun way.

## Getting started

Install and authenticate [spotify-cli](https://pypi.org/project/spotify-cli/)

Setup virtualenv
```
python3 -m venv .venv3
source .venv/bin/activate
```

Install python packages
```
python3 -m pip install -r requirements.txt
```

Create team member data files
```
printf "Aaron\nBob\nAlice" > team_members.txt
touch team_member_history.txt
```

Make sure you have the spotify client running on your device and a playlist called "Meeting music" with good (appropriate) music.

Run the script
```
./kickoff_standup.sh
```

