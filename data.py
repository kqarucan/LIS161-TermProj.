import sqlite3

db_path = 'bangtan.db'

# This function conencts to the DB and returns a conn and cur objects
def connect_to_db(path):
    conn = sqlite3.connect(path)
    # Converting tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

# This function returns pets by pet_type
def read_mems_by_mem_type(bang_mem):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM membio WHERE line = ?'
    value = bang_mem
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    print(results)
    return results

# This function retrieves 1 pet by pet_id
def read_bangmems_by_bangmem_id(bangmem_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM membio WHERE id = ?'
    value = bangmem_id
    result = cur.execute(query,(value,)).fetchone()
    conn.close()
    return result
#baguhin pa sana yung mem id 
#UPDATE MAY TABLE NA

# This function inserts 1 pet data
def insert_mem(mem_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO membio (fname, sname, bdate, pbirth, position, picurl, line) VALUES (?,?,?,?,?,?,?)'
    values = (mem_data['bang_mem'], mem_data['fname'], mem_data['sname'],
              mem_data['bdate'], mem_data['pbirth'],
              mem_data['position'], mem_data['picurl'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

# This function updates a record
def update_mem(mem_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE membio SET fname=?, sname=?, bdate=?, pbirth=?, position=?, picurl=?, line=? WHERE id=?"
    values = (mem_data['bang_mem'], mem_data['fname'], mem_data['sname'],
              mem_data['bdate'], mem_data['pbirth'],
              mem_data['position'], mem_data['picurl'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_mem(bangmem_id):
    conn, cur = connect_to_db(db_path)
    query = "DELETE FROM membio WHERE id = ?"
    values = (bangmem_id,)
    cur.execute(query, values)
    conn.commit()
    conn.close()

#so far okay na tong data.py shet!!!
