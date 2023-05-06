"""from flask import Flask, request, jsonify
import ibm_db

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_hostname = "125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"            # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_port = "30426"                    # e.g. "50000"
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_uid = "hvv26443"                 # e.g. "abc12345"
dsn_pwd = "enOsLa29A2319Otj"                 # e.g. "7dBZ3wWt9XN6$o0J"
dsn_security = "SSL"

app = Flask(__name__)

def get_attendance_data(name):
    # Connect to IBM DB2 database
    dsn = (
        "DRIVER={0};"
        "DATABASE={1};"
        "HOSTNAME={2};"
        "PORT={3};"
        "PROTOCOL={4};"
        "UID={5};"
        "PWD={6};"
        "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,
                                dsn_security)

    conn = ibm_db.connect(dsn, "", "")

    query = "select count(*) from ATTEND where NAME like '{}%' and ATTENDANCE = 'P'".format(name.lower())
    stmt = ibm_db.exec_immediate(conn, query)
    no = ibm_db.fetch_both(stmt)
    ibm_db.close(conn)
    return no[0]

@app.route('/attendance', methods=['GET'])
def get_attendance():
    name = request.args.get('name')
    if not name:
        return "Please provide a 'name' parameter in the query string.", 400
    attendance_data = get_attendance_data(name)
    response_text=str(attendance_data)
    res = {'name': name, 'attendance_days': attendance_data}
    return res, 200


if __name__ == '__main__':
    app.run()"""
    
    
    
    
from flask import Flask, request, jsonify
import ibm_db

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"  # e.g. "BLUDB"
dsn_hostname = "125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"  # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_port = "30426"  # e.g. "50000"
dsn_protocol = "TCPIP"  # i.e. "TCPIP"
dsn_uid = "hvv26443"  # e.g. "abc12345"
dsn_pwd = "enOsLa29A2319Otj"  # e.g. "7dBZ3wWt9XN6$o0J"
dsn_security = "SSL"

app = Flask(__name__)

def get_attendance_data(name):
    # Connect to IBM DB2 database
    dsn = (
        "DRIVER={0};"
        "DATABASE={1};"
        "HOSTNAME={2};"
        "PORT={3};"
        "PROTOCOL={4};"
        "UID={5};"
        "PWD={6};"
        "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,
                                dsn_security)

    conn = ibm_db.connect(dsn, "", "")

    query = "select count(*) from ATTEND where NAME like '{}%' and ATTENDANCE = 'P'".format(name.lower())
    stmt = ibm_db.exec_immediate(conn, query)
    no = ibm_db.fetch_both(stmt)
    ibm_db.close(conn)
    return no[0]

@app.route('/attendance', methods=['GET'])
def get_attendance():
    name = request.args.get('name')
    if not name:
        return "Please provide a 'name' parameter in the query string.", 400
    attendance_data = get_attendance_data(name)
    res = {'name': name, 'attendance_days': attendance_data}
    return jsonify(res)

if __name__ == '__main__':
    app.run()

