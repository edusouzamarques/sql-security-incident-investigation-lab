import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../database/organization.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS log_in_attempts (
        event_id INTEGER PRIMARY KEY,
        username VARCHAR(16) NOT NULL,
        login_date DATE NOT NULL,
        login_time TIME NOT NULL,
        country VARCHAR(32) NOT NULL,
        ip_address VARCHAR(32) NOT NULL,
        success INTEGER NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        device_id VARCHAR(16),
        username VARCHAR(16) NOT NULL,
        department VARCHAR(32) NOT NULL,
        office VARCHAR(32) NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS machines (
        device_id VARCHAR(16) PRIMARY KEY,
        operating_system VARCHAR(16) NOT NULL,
        email_client VARCHAR(16) NOT NULL,
        OS_patch_date DATE NOT NULL,
        employee_id INTEGER
    );
    """)

    # Populate log_in_attempts based on real lab dataset
    login_data = [
        (1, 'jrafael', '2022-05-09', '04:56:27', 'CAN', '192.168.243.140', 1),
        (2, 'apatel', '2022-05-10', '20:27:27', 'CAN', '192.168.205.12', 0),
        (3, 'dkot', '2022-05-09', '06:47:41', 'USA', '192.168.151.162', 1),
        (4, 'dkot', '2022-05-08', '02:00:39', 'USA', '192.168.178.71', 0),
        (8, 'bisles', '2022-05-08', '01:30:17', 'US', '192.168.119.173', 0),
        (12, 'dkot', '2022-05-08', '09:11:34', 'USA', '192.168.100.158', 1),
        (18, 'pwashing', '2022-05-11', '19:28:50', 'US', '192.168.66.142', 0),
        (20, 'tshah', '2022-05-12', '18:56:36', 'MEXICO', '192.168.109.50', 0),
        (24, 'arusso', '2022-05-09', '06:49:39', 'MEXICO', '192.168.171.192', 1),
        (28, 'aestrada', '2022-05-09', '19:28:12', 'MEXICO', '192.168.27.57', 0),
        (30, 'yappiah', '2022-05-09', '03:22:22', 'MEX', '192.168.124.48', 1),
        (34, 'drosas', '2022-05-11', '21:02:04', 'US', '192.168.45.93', 0),
        (42, 'cgriffin', '2022-05-09', '23:04:05', 'US', '192.168.4.157', 0),
        (52, 'cjackson', '2022-05-10', '22:07:07', 'CAN', '192.168.58.57', 0),
        (69, 'wjaffrey', '2022-05-11', '19:55:15', 'USA', '192.168.100.17', 0),
        (82, 'abernard', '2022-05-12', '23:38:46', 'MEX', '192.168.234.49', 0),
        (87, 'apatel', '2022-05-08', '22:38:31', 'CANADA', '192.168.132.153', 0),
        (96, 'ivelasco', '2022-05-09', '22:36:36', 'CAN', '192.168.84.194', 0),
        (104, 'asundara', '2022-05-11', '18:38:07', 'US', '192.168.96.200', 0),
        (107, 'bisles', '2022-05-12', '20:25:57', 'USA', '192.168.116.187', 0),
        (111, 'aestrada', '2022-05-10', '22:00:26', 'MEXICO', '192.168.76.27', 0),
        (127, 'abellmas', '2022-05-09', '21:20:51', 'CANADA', '192.168.70.122', 0),
        (131, 'bisles', '2022-05-09', '20:03:55', 'US', '192.168.113.171', 0),
        (155, 'cgriffin', '2022-05-12', '22:18:42', 'USA', '192.168.236.176', 0),
        (160, 'jclark', '2022-05-10', '20:49:00', 'CANADA', '192.168.214.49', 0),
        (199, 'yappiah', '2022-05-11', '19:34:48', 'MEXICO', '192.168.44.232', 0)
    ]

    cursor.executemany("INSERT OR IGNORE INTO log_in_attempts VALUES (?, ?, ?, ?, ?, ?, ?);", login_data)

    # Populate employees dataset
    employee_data = [
        (1000, 'a320b137c219', 'elarson', 'Marketing', 'East-170'),
        (1001, 'b239c825d303', 'bmoreno', 'Marketing', 'Central-276'),
        (1002, 'c116d593e558', 'tshah', 'Human Resources', 'North-434'),
        (1003, 'd394e816f943', 'sgilmore', 'Finance', 'South-153'),
        (1004, 'e218f877g788', 'eraab', 'Human Resources', 'South-127'),
        (1005, 'f551g340h864', 'gesparza', 'Human Resources', 'South-366'),
        (1007, 'h174i497j413', 'wjaffrey', 'Finance', 'North-406'),
        (1008, 'i858j583k571', 'abernard', 'Finance', 'South-170'),
        (1009, None, 'lrodriqu', 'Sales', 'South-134'),
        (1010, 'k242l212m542', 'jlansky', 'Finance', 'South-109'),
        (1011, 'l748m120n401', 'drosas', 'Sales', 'South-292'),
        (1015, 'p611q262r945', 'jsoto', 'Finance', 'North-271'),
        (1016, 'q793r736s288', 'sbaelish', 'Human Resources', 'North-229'),
        (1017, 'r550s824t230', 'jclark', 'Finance', 'North-188'),
        (1018, 's310t540u653', 'abellmas', 'Finance', 'North-403'),
        (1020, 'u899v381w363', 'arutley', 'Marketing', 'South-351'),
        (1022, 'w237x430y567', 'arusso', 'Finance', 'West-465'),
        (1024, 'y976z753a267', 'iuduike', 'Sales', 'South-215'),
        (1025, 'z381a365b233', 'jhill', 'Sales', 'North-115'),
        (1052, 'a192b174c940', 'jdarosa', 'Marketing', 'East-195'),
        (1075, 'x573y883z772', 'fbautist', 'Marketing', 'East-267'),
        (1088, 'k865l965m233', 'rgosh', 'Marketing', 'East-157'),
        (1103, None, 'randerss', 'Marketing', 'East-460'),
        (1156, 'a184b775c707', 'dellery', 'Marketing', 'East-417'),
        (1163, 'h679i515j339', 'cwilliam', 'Marketing', 'East-216'),
        (1201, 'm991n882o111', 'adm_tech', 'Information Technology', 'North-501')
    ]

    cursor.executemany("INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?, ?);", employee_data)

    conn.commit()
    conn.close()
    print("[+] Database successfully initialized at:", DB_PATH)

if __name__ == "__main__":
    init_db()
