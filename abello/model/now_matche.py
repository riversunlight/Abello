import sqlite3

class NowMatchModel():
    DATABASE = 'database.db'
    
    def all(self):
        con = sqlite3.connect(self.DATABASE)
        res = con.execute('SELECT * FROM now_matches').fetchall()
        con.close()
        return res

    def add(self, player1_id, player2_id, winner):
        con = sqlite3.connect(self.DATABASE)
        con.execute('INSERT INTO now_matches VALUES(?, ?, ?)', [player1_id, player2_id, winner])
        con.commit()
        con.close()
    
    def during_game(self):
        con = sqlite3.connect(self.DATABASE)
        during_game = con.execute('SELECT * FROM now_matches WHERE winner = ?', ['PLAYING']).fetchall()
        con.close()
        return len(during_game)
    
    def delete(self, player):
        con = sqlite3.connect(self.DATABASE)
        con.execute('DELETE FROM now_matches WHERE player1_id = ? OR player2_id = ?', [player, player])
        con.close()
    
    def reset(self):
        con = sqlite3.connect(self.DATABASE)
        con.execute('DELETE FROM now_matches')
        con.commit()
        con.close()

    def reset_winner(self, player1_id, player2_id):
        con = sqlite3.connect(self.DATABASE)
        con.execute('UPDATE now_matches SET winner = ? WHERE (player1_id=? AND player2_id = ?) OR (player1_id=? AND player2_id = ?)', ["PLAYING", player1_id, player2_id, player2_id, player1_id])
        con.commit()
        con.close()
    
    def now_match(self, player_ids):
        con = sqlite3.connect(self.DATABASE)
        now_match = con.execute('SELECT * FROM now_matches WHERE (player1_id = ? AND player2_id = ?) OR (player1_id = ? AND player2_id = ?)', [player_ids[0], player_ids[1], player_ids[1], player_ids[0]]).fetchall()
        con.close()
        return now_match 
        
    def swap_matches(self, player_ids):
        oppos = ["_", "__"]
        con = sqlite3.connect(self.DATABASE)
        for i in range(0, 2):
            mch = con.execute("SELECT * FROM now_matches WHERE player1_id = ? OR player2_id = ?", [player_ids[i], player_ids[i]]).fetchall()
            oppos[i] = mch[0][0] if mch[0][0] != player_ids[i] else mch[0][1]

        for i in range(0, 2):
            con.execute("DELETE FROM now_matches WHERE (player1_id = ? AND player2_id = ?) OR (player1_id = ? AND player2_id = ?)", [player_ids[i], oppos[i], oppos[i], player_ids[i]])
    
        con.execute("INSERT INTO now_matches VALUES(?, ?, ?)", [player_ids[0], player_ids[1], "PLAYING"])
        con.execute("INSERT INTO now_matches VALUES(?, ?, ?)", [oppos[0], oppos[1], "PLAYING"])
    
        con.commit()
        con.close()

    def reset_match(self, player1_id, player2_id):
        con = sqlite3.connect(self.DATABASE)
        con.execute('UPDATE now_matches SET winner = ? WHERE (player1_id=? AND player2_id = ?) OR (player1_id=? AND player2_id = ?)', ["PLAYING", player1_id, player2_id, player2_id, player1_id])
        con.commit()
        con.close()

    def set_winner(self, win_player_id):
        con = sqlite3.connect(self.DATABASE)
        con.execute('UPDATE now_matches SET winner=? WHERE player1_id=? OR player2_id=?', [win_player_id, win_player_id, win_player_id])
        con.commit()
        con.close()

    def get_data(self, player_id):
        print("now_matches", player_id)
        con = sqlite3.connect(self.DATABASE)
        game_data = con.execute('SELECT * FROM now_matches WHERE player1_id=? OR player2_id=?', [player_id, player_id]).fetchall()
        con.close()
        return game_data
    
    def reset(self):
        con = sqlite3.connect(self.DATABASE)
        con.execute("DELETE FROM now_matches")
        con.commit()
        con.close()
        