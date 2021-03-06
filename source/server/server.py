# coding: utf-8
import logic
import logging
from flask import Flask,url_for,request
app = Flask(__name__)
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def hello_world():
    print "---> Something happened"
    return u'Τι θες ρε μαλακισμένο? Πάρε την ip σου ' + request.remote_addr + '\n'

@app.route('/register/<int:port>/<username>')
def registrate(port,username):
	return logic.register(request.remote_addr,port,username)

@app.route('/list_groups/')
def groups():
	return logic.listgroups()

@app.route('/list_members/<group>')
def groupies(group):
	return logic.listmembers(group)

@app.route('/join_group/<group>/<username>')
def joinare(group,username):
	return logic.joingroup(group,username)

@app.route('/exit_group/<group>/<username>')
def feuga(group,username):
	return logic.exitgroup(group,username)

@app.route('/heartbeat/<int:id>')
def alive(id):
	return logic.heartbeat(id)

@app.route('/quit/<int:id>')
def rage(id):
	return logic.quitchat(id)