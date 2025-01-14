import sys
import json
from collections import Counter

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path) as r, open(output_path, "w") as w:
    clusters = [json.loads(line) for line in r]
    clusters = [cluster for cluster in clusters if cluster["annotation_doc"]["pub_time"] > 1649030400]
    clusters.sort(key=lambda x: x["create_time"])
    for cluster in clusters:
        w.write(json.dumps(cluster, ensure_ascii=False).strip() + "\n")
