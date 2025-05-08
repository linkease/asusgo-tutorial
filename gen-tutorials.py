# -*- coding: utf-8 -*-
import os
import json
import codecs

tutorials_dir = 'tutorials'
output_file = 'tutorials.json.js'

result = []

# 遍历 tutorials 目录下的插件文件夹
for plugin_name in os.listdir(tutorials_dir):
    plugin_path = os.path.join(tutorials_dir, plugin_name)
    info_path = os.path.join(plugin_path, 'info.json')

    if os.path.isdir(plugin_path) and os.path.isfile(info_path):
        try:
            with codecs.open(info_path, 'r', 'utf-8') as f:
                tutorials = json.load(f)
                result.append({
                    'plugin_name': plugin_name,
                    'tutorials': tutorials
                })
        except Exception as e:
            print('跳过文件: %s，错误: %s' % (info_path, e))

# 写入结果到 plugin-tutorials.json.js
with codecs.open(output_file, 'w', 'utf-8') as f:
    f.write(json.dumps(result, ensure_ascii=False, indent=2))

print('已生成: %s' % output_file)
