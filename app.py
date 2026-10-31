from flask import Flask,request,jsonify,send_from_directory
import sqlite3,pathlib
app=Flask(__name__,static_folder='static');DB=pathlib.Path(__file__).with_name('spooler.db')
def db():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
with db() as c:c.execute("CREATE TABLE IF NOT EXISTS jobs(id INTEGER PRIMARY KEY AUTOINCREMENT,filename TEXT,priority INTEGER,status TEXT DEFAULT 'Queued',created_at TEXT DEFAULT CURRENT_TIMESTAMP)")
@app.get('/api/jobs')
def jobs():
 with db() as c:return jsonify([dict(x) for x in c.execute("SELECT * FROM jobs WHERE status!='Cancelled' ORDER BY priority,id")])
@app.post('/api/jobs')
def add():
 x=request.get_json() or {};name=str(x.get('filename','')).strip()
 if not name:return jsonify(error='Filename required'),400
 try:p=max(1,min(5,int(x.get('priority',3))))
 except:p=3
 with db() as c:cur=c.execute('INSERT INTO jobs(filename,priority) VALUES(?,?)',(name[:120],p));return jsonify(id=cur.lastrowid)
@app.post('/api/jobs/<int:i>/<action>')
def act(i,action):
 states={'pause':'Paused','resume':'Queued','print':'Printing (simulated)','cancel':'Cancelled'}
 if action not in states:return jsonify(error='Unknown action'),400
 with db() as c:
  cur=c.execute('UPDATE jobs SET status=? WHERE id=?',(states[action],i))
  if not cur.rowcount:return jsonify(error='Not found'),404
 return jsonify(ok=True)
@app.get('/')
def home():return send_from_directory('static','index.html')
@app.get('/<path:p>')
def files(p):return send_from_directory('static',p)
if __name__=='__main__':app.run(port=5005,debug=True)
