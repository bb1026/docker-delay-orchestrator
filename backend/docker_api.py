import docker

client = docker.from_env()

def list_containers():
    result = []
    for c in client.containers.list(all=True):
        result.append({
            "id": c.id,
            "name": c.name,
            "status": c.status,
            "restart": c.attrs["HostConfig"]["RestartPolicy"]["Name"]
        })
    return result

def start_container(name):
    c = client.containers.get(name)
    c.start()