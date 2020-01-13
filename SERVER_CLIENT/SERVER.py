#!/usr/bin/env python3
import sqlite3
import os
import socket

HOST = ''
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        real = data.decode('utf-8')
        print("Database wordt geopend")
        sqlite_file="/home/bart/database.db"
        sconn = sqlite3.connect(sqlite_file)
        sc = sconn.cursor()
        # Probeer database te maken (in het geval deze nog niet bestaat
        try:
           sc.execute("""
           create table resources('host' text, 'cpu' real, 'ram' real, 'disk' real)
            """)
        except:
            pass
        # Ontvanged data in database zetten
        data_string = real.split(',')
        # Fresh
        sc.execute('''DELETE FROM resources''')
        sc.execute('''INSERT INTO resources (host, ram, cpu, disk) VALUES (?, ?, ?, ?)''', (data_string[0], data_string[1], data_string[2], data_string[3]))
        sconn.commit()
        print("Database geopend en data weggeschreven")
        conn.sendall(data)
    
