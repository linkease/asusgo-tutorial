import os
import json

tutorials_dir = 'tutorials'
output_file = 'tutorials.json.js'

result = []

# 遍历 tutorials 下的每个子目录
for plugin_name in os.listdir(tutorials_dir):
    plugin_path = os.path.join(tutorials_dir, plugin_name)
    info_path = os.path.join(plugin_path, 'info.json')

    if os.path.isdir(plugin_path) and os.path.isfile(info_path):
        with open(info_path, 'r', encoding='utf-8') as f:
            try:
                tutorials = json.load(f)
                result.append({
                    'plugin_name': plugin_name,
                    'tutorials': tutorials
                })
            except json.JSONDecodeError as e:
                print(f"跳过无效 JSON 文件: {info_path}，错误：{e}")

# 写入输出文件
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"已生成：{output_file}")
