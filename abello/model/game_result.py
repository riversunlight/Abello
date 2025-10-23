import sqlite3

class GameResultModel():
    DATABASE = 'database.db'

    def game_no_battle(self, player1_id, player2_id):
        player = player1_id if player2_id == '-' else player2_id

        con = sqlite3.connect(self.DATABASE)
        data = con.execute('SELECT * FROM game_result WHERE round = ? AND (win_player_id = ? OR lose_player_id = ?)', [self.round, player, player]).fetchall()
        prev_stone = data[0][3]
        win_lose = "不戦勝" if data[0][1] == player else "不戦敗"
        con.close()
        return win_lose, prev_stone
    
    def person_game_result(self, player_id):
        con = sqlite3.connect(self.DATABASE)
        person_result_data = con.execute('SELECT * FROM game_result WHERE (win_player_id=? OR lose_player_id=?)', [player_id, player_id]).fetchall()
        con.close()
        return person_result_data
    
    def now_games(self, round):
        con = sqlite3.connect(self.DATABASE)
        game_data = con.execute("SELECT * FROM game_result WHERE round = ?", [round]).fetchall()
        con.close()
        return game_data

    def delete_now_games(self, round):
        con = sqlite3.connect(self.DATABASE)
        con.execute('DELETE FROM game_result WHERE round = ?', [round])
        con.commit()
        con.close()

    def add(self, round, win_player_id, lose_player_id, stone_diff):
        con = sqlite3.connect(self.DATABASE)
        con.execute('INSERT INTO game_result VALUES(?, ?, ?, ?)', [round, win_player_id, lose_player_id, stone_diff])
        con.commit()
        con.close()

    def get_game(self, player1_id, player2_id):
        con = sqlite3.connect(self.DATABASE)
        data = con.execute('SELECT * FROM game_result WHERE (win_player_id = ? AND lose_player_id=?) OR (win_player_id = ? AND lose_player_id=?)', [player1_id, player2_id, player2_id, player1_id]).fetchall()
        con.close()
        return data
    
    def get_now_game(self, round, player_id):
        con = sqlite3.connect(self.DATABASE)
        game_data = con.execute('SELECT * FROM game_result WHERE (win_player_id = ? OR lose_player_id = ?) AND round = ?', [player_id, player_id, round]).fetchall()
        con.close()
        return game_data
    
    def delete_game(self, win_player_id, lose_player_id):
        con = sqlite3.connect(self.DATABASE)
        con.execute('DELETE FROM game_result WHERE win_player_id = ? AND lose_player_id=?', [win_player_id, lose_player_id])
        con.commit()
        con.close()
    
    def delete_now_game(self, round, player):
        con = sqlite3.connect(self.DATABASE)
        con.execute('DELETE FROM game_result WHERE round = ? AND (win_player_id = ? OR lose_player_id = ?)', [round, player, player]).fetchall()
        con.commit()
        con.close()

    def reset(self):
        con = sqlite3.connect(self.DATABASE)
        con.execute("DELETE FROM game_result")
        con.commit()
        con.close()
