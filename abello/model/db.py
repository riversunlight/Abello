import sqlite3

DATABASE = 'database.db'

def create_players_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS players (player_id INTEGER PRIMARY KEY AUTOINCREMENT , name, short, block, grade, status)")
    con.close()

def create_results_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS results (player_id, win int, lose int, stone_diff int)")
    con.close()

def create_new_matches_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS now_matches (player1_id, player2_id, winner)")
    con.close()

def create_new_game_result_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS game_result (round int, win_player_id, lose_player_id, stone_diff int)")
    con.close()
    