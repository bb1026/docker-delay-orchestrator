from flask import Flask, jsonify, request
from docker_api import list_containers, start_container
from compose_loader import load_compose
from dependency import topo_sort
import time, json, os

app = Flask(__name__)
STATE = "state.json"

def load_state():
    if not os.path.exists(STATE):
        return {}
    return json.load(open(STATE))

def save_state(s):
    json.dump(s, open(STATE, "w"), indent=2)

@app.route("/api/containers")
def containers():
    return jsonify(list_containers())

@app.route("/api/compose")
def compose():
    return jsonify(load_compose())

@app.route("/api/state", methods=["GET","POST"])
def state():
    if request.method == "POST":
        save_state(request.json)
        return {"ok": True}
    return jsonify(load_state())

@app.route("/api/start", methods=["POST"])
def start():
    cfg = load_state()
    deps = {k:v["depends"] for k,v in cfg.items() if v["enabled"]}
    order = topo_sort(deps)
    logs = []
    for name in order:
        logs.append(f"启动 {name}")
        start_container(name)
        time.sleep(cfg[name]["delay"])
    return jsonify(logs)

app.run(host="0.0.0.0", port=8080)