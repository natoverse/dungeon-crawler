from nicegui import ui
from copy import deepcopy
from nicegui.events import KeyEventArguments
from maps import get_map, is_valid_move
from symbols import E, G, L
from styles import css
from models import Player

# TODO: create a run config object with things like the timer interval
# TODO: basic version with just movement and walls
# TODO: add gold, health, monsters, ladders, holes and multiple levels
# TODO: phase this in so students can add complexity
# TODO: for each variant, list out things to try, such as changing the symbols and maps, adding more monsters, etc
# TODO: 3d version

# explain: object structure, state, avoiding globals by using params
# explain: typical terminology such as models, agents, scenes

# this global object holds all the game state as the player plays
state = {
    'player': Player(),
    'level': 1,
}

# this global object holds all of the page elements we may need to update
page = {
    'header': ui.card(),
    'scene': ui.card()
}


def render_header(player, level, container):
    container.clear()
    with container:
        ui.html(f'''<div class="stats">
            <span>Player: {player.name}</span>
            <span>Gold: {player.gold}</span>
            <span>Health: {player.health}</span>
            </div>
        ''')
        ui.html(f'<div>Level {level}</div>')


# renders the map including current player position
# this is rendered in a game loop, so it represents all collected state
# such as player position, enemy positions, etc. continuously
def render_level(player, level, container):
    map = get_map(level)
    # create a copy of the map so we can write our player and monsters into it
    map_copy = deepcopy(map)
    map_copy[player.position[0]][player.position[1]] = player.symbol
    html_string = '<table>'
    for r in range(len(map_copy)):
        html_string += '<tr>'
        row = map_copy[r]
        for c in range(len(row)):
            cell = row[c]
            html_string += f'<td>{cell}</td>'
        html_string += '<tr>'
    html_string += '</table>'
    container.clear()
    with container:
        ui.html(html_string)


def render():
    player = state['player']
    level = state['level']
    header = page['header']
    scene = page['scene']
    render_header(player, level, header)
    render_level(player, level, scene)


# handle player movement
# this will create a new possible position based on the keyboard input,
# but then only update the actual player position if it's a valid move
# we'll do the same thing for monsters later
def handle_key(e: KeyEventArguments):
    player = state['player']
    map = get_map(state['level'])
    new_position = player.position.copy()
    if e.action.keydown:
        if e.key.arrow_left:
            new_position[1] -= 1
        elif e.key.arrow_right:
            new_position[1] += 1
        elif e.key.arrow_up:
            new_position[0] -= 1
        elif e.key.arrow_down:
            new_position[0] += 1
    if is_valid_move(new_position, map):
        player.position[0] = new_position[0]
        player.position[1] = new_position[1]
        resolve_move(player, map)


def resolve_move(player, map):
    # check to see what's at the map in the player's position
    # if it's gold, add to the player's gold, and replace the gold with a space
    # if it's a monster, subtract from the player's health
    # if it's a ladder, move to the next level
    # if it's a hole, move to the previous level
    symbol = map[player.position[0]][player.position[1]]
    if symbol == G:
        player.gold += 1
        map[player.position[0]][player.position[1]] = E
    elif symbol == L:
        state['level'] += 1
        player.position = [1, 1]


# set up the page with a title and some css
ui.page_title('Dungeon Crawler')
ui.add_css(css)
# wire up a key press handler
ui.keyboard(on_key=handle_key)
# render the map in a game loop
ui.timer(0.5, render)
# trigger the nicegui framework to run the app
ui.run()
