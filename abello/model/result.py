import sqlite3

class ResultModel():
    DATABASE = 'database.db'
    
    def all(self):
        con = sqlite3.connect(self.DATABASE)
        data = con.execute("SELECT * FROM results").fetchall()
        con.close()

        res = []
        for row in data:
            res.append({'player_id': row[0], 'win': row[1], 'lose': row[2], 'stone_diff': row[3]})
        return res
    
    def person_data(self, player_id):
        con = sqlite3.connect(self.DATABASE)
        data = con.execute("SELECT * FROM results WHERE player_id = ?", [player_id]).fetchall()
        con.close()
        if len(data) == 0:
            return None
        data = data[0]

        return {'player_id': data[0], 'win': data[1], 'lose': data[2], 'stone_diff': data[3]}
    
    def update_data(self, player_id, isWin, stone_diff):
        con = sqlite3.connect(self.DATABASE)
        if isWin:
            con.execute('UPDATE results SET win = win + 1 WHERE player_id = ?', [player_id])
            con.execute('UPDATE results SET stone_diff = stone_diff + ? WHERE player_id = ?', [stone_diff, player_id])
        else:
            con.execute('UPDATE results SET lose = lose + 1 WHERE player_id = ?', [player_id])
            con.execute('UPDATE results SET stone_diff = stone_diff - ? WHERE player_id = ?', [stone_diff, player_id])
        con.commit()
        con.close()

    def fix_data(self, player_id, isWin, stone_diff):
        con = sqlite3.connect(self.DATABASE)
        if isWin:
            con.execute('UPDATE results SET win = win - 1 WHERE player_id = ?', [player_id])
            con.execute('UPDATE results SET stone_diff = stone_diff - ? WHERE player_id = ?', [stone_diff, player_id])
        else:
            con.execute('UPDATE results SET lose = lose - 1 WHERE player_id = ?', [player_id])
            con.execute('UPDATE results SET stone_diff = stone_diff + ? WHERE player_id = ?', [stone_diff, player_id])
        con.commit()
        con.close()
    
    def add(self, player_id):
        con = sqlite3.connect(self.DATABASE)
        con.execute('INSERT INTO results VALUES(?, ?, ?, ?)', [player_id, 0, 0, 0])
        con.commit()
        con.close()

    def reset(self):
        con = sqlite3.connect(self.DATABASE)
        con.execute("DELETE FROM results")
        con.commit()
        con.close()