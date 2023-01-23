import json
import os

stats = {}
main_dir = r""
for root, _, _ in os.walk(main_dir):
    if os.path.exists(os.path.join(root, 'annotations.json')):
        file = os.path.join(root, 'annotations.json')
        with open(file, 'r', encoding='utf-8') as f:
            info = json.load(f)
        for k, v in info.items():
            if k == '___sa_version___':
                continue
            else:
                if root.split('\\')[7] == '1' or root.split('\\')[7] == '2':
                    path = '/'.join(root.split('\\')[5:8])
                else:
                    path = '/'.join(root.split('\\')[5:7])
                box_count = len(v['instances'])
                if path in stats:
                    stats[path] += box_count
                else:
                    stats[path] = box_count

with open("result.txt", 'w', encoding='utf-8') as f:
    for k, v in stats.items():
        f.write(f"{k}: {v}\n")



