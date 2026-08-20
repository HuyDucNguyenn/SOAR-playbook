import sqlite3
from typing import Dict, Any
import json
DB_PATH = "incident_storage.db"
class DatabaseManager:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        with self.get_connection as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS incidents
                            incident_id TEXT PRIMARY KEY
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                            alert_id TEXT 
                            host_name TEXT
                            user_name TEXT
                            process_name TEXT
                            parent_process TEXT
                            file_hash TEXT
                            file_path TEXT
                            command_line TEXT
                            destination_ip TEXT
                            severity TEXT
                            detection_name TEXT
                            risk_score INTEGER
                            action_taken TEXT
                            raw_enrichment TEXT
                            mitre_technique TEXT
            """)
            cur.commit()
    def save_incident(self, incident_data: Dict[str,Any]):
        with self.get_connection as conn:
            cur = conn.cursor()
            cur.execute(""" INSERT INTO incidents(
                                incident_id,
                                timestamp,
                                alert_id,
                                host_name,
                                user_name,
                                process_name,
                                parent_process,
                                file_hash,
                                file_path,
                                command_line,
                                destination_ip,
                                severity,
                                detection_name,
                                risk_score,
                                action_taken,
                                raw_enrichment,
                                mitre_technique) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,(
                    incident_data["incident_id"],
                    incident_data["timestamp"],
                    incident_data["alert_id"],
                    incident_data["host_name"],
                    incident_data["user_name"],
                    incident_data["process_name"],
                    incident_data["parent_process"],
                    incident_data["file_hash"],
                    incident_data["file_path"],
                    incident_data["command_line"],
                    incident_data["destination_ip"],
                    incident_data["severity"],
                    incident_data["detection_name"],
                    incident_data["risk_score"],
                    incident_data["action_taken"],
                    incident_data["raw_enrichment"],
                    incident_data["mitre_technique"]
                ))
        cur.commit()

    
    

