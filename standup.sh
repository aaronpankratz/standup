#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
PURPLE='\033[0;35m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

play_music() {
    printf "\n${CYAN}Finding some music to play...${NC}\n\n"
    spotify volume to 40
    printf "\n"
    spotify play --playlist Meeting music -q -s on
    spotify status -vv
}

pick_team_member() {
    printf "\n${PURPLE}Picking someone to kick off standup...${NC}\n\n"
    python3 random_team_member.py
}

standup() {
    printf "${GREEN}Welcome to standup!${NC}\n\n"
    echo Just so you know, right now it\'s $(date)
    play_music
    pick_team_member
}

standup
