# create table reserving set info (stone_color, player_name)
CREATE_PLAYER_NAME_TABLE = '''
CREATE TABLE IF NOT EXISTS player_name_table(
color INTEGER,
username TEXT
)
'''

# delete table for initialization
DELETE_PLAYER_NAME_TABLE = '''
DROP TABLE IF EXISTS player_name_table
'''

# methods to control player_name_table
# white == 1
REGISTER_PLAYER_WHITE_NAME = '''
INSERT INTO player_name_table(color, username)
VALUES(1, ?)
'''

GET_PLAYER_WHITE_NAME = '''
SELECT username FROM player_name_table WHERE color == 1
'''

# black == -1
REGISTER_PLAYER_BLACK_NAME = '''
INSERT INTO player_name_table(color, username)
VALUES(-1, ?)
'''

GET_PLAYER_BLACK_NAME = '''
SELECT username FROM player_name_table WHERE color == -1
'''

# get player's color
GET_PLAYER_COLOR = '''
SELECT color FROM player_name_table LIMIT 1
'''

# create table reserving the newest board information (1, -1, 0, 2)
CREATE_BOARD_INFO_TABLE = '''
CREATE TABLE IF NOT EXISTS board_info_table(
board TEXT,
next_turn INTEGER,
winner INTEGER
)
'''

# delete table for inilialization
DELETE_BOARD_INFO_TABLE = '''
DROP TABLE IF EXISTS board_info_table
'''

# methods to control board_info_table
REGISTER_BOARD_INFO = '''
INSERT INTO board_info_table(board, next_turn)
VALUES(?, ?)
'''

GET_BOARD_INFO = '''
SELECT board FROM board_info_table
'''

UPDATE_BOARD_INFO = '''
UPDATE board_info_table
SET board = ?, next_turn = ?
'''

GET_NEXT_TURN = '''
SELECT next_turn FROM board_info_table
'''

REGISTER_WINNER = '''
INSERT INTO board_info_table(winner)
VALUES(?)
'''

GET_WINNER = '''
SELECT winner FROM board_info_table
'''
