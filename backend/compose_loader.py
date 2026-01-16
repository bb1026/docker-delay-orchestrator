import yaml
import os

def load_compose(root="/vol1/docker"):
    projects = {}
    for base, _, files in os.walk(root):
        for f in files:
            if "compose" in f and f.endswith((".yml", ".yaml")):
                path = os.path.join(base, f)
                with open(path) as fh:
                    data = yaml.safe_load(fh)
                    services = {}
                    for name, cfg in data.get("services", {}).items():
                        services[name] = {
                            "depends_on": cfg.get("depends_on", [])
                        }
                    projects[os.path.basename(base)] = services
    return projects