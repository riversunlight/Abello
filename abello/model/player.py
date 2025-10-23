import sqlite3

class PlayerModel():
    DATABASE = 'database.db'

    def add(self, name, short, block, grade):
        con = sqlite3.connect(self.DATABASE)
        con.execute('INSERT INTO players(name, short, block, grade, status) VALUES(?, ?, ?, ?, ?)', [name, short, block, grade, "参加"])
        con.commit()
        con.close()

    def delete(self, player_id):
        con = sqlite3.connect(self.DATABASE)
        con.execute('DELETE FROM players WHERE player_id = ?', [player_id])
        con.execute('DELETE FROM results WHERE player_id = ?', [player_id])
        con.commit()
        con.close()

    def get_player_data(self, player_id):
        con = sqlite3.connect(self.DATABASE)
        data = con.execute('SELECT * FROM players WHERE player_id = ?', [player_id]).fetchall()
        con.close()
        return {'player_id': data[0][0], 'name': data[0][1], 'short': data[0][2], 'block': data[0][3], 'grade': data[0][4], 'status': data[0][5]}

    def all(self):
        con = sqlite3.connect(self.DATABASE)
        data = con.execute("SELECT * FROM players").fetchall()
        con.close()

        res = []
        for row in data:
            res.append({'player_id': row[0], 'name': row[1], 'short': row[2], 'block': row[3], 'grade': row[4], 'status': row[5]})
        return res
    
    def change_status(self, player_id, status):
        con = sqlite3.connect(self.DATABASE)
        con.execute('UPDATE players SET status = ? WHERE player_id = ?', [status, player_id])
        con.commit()
        con.close()
    
    def reset(self):
        con = sqlite3.connect(self.DATABASE)
        con.execute("DELETE FROM players")
        con.commit()
        con.close()
