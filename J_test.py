"""
演示JSON数据和python字典的相互转换
"""
import json

# 准备列表
List_json = [{"name":"Jack","age":11},{"name":"Lucy","age":11},{"name":"Tom","age":11}]
json_str = json.dumps(List_json,ensure_ascii=False)

#
# json.dumps(dict, indent)：将Python对象转换成json字符串
# json.dump(dict, file_pointer)：将Python对象写入json文件

print(f"json_str的格式为{type(json_str)},json_str的内容为{json_str}")

# 准备字典
dict = {"name":"Jack","age":11}
json_str = json.dumps(List_json,ensure_ascii=False)
print(f"json_str的格式为{type(json_str)},json_str的内容为{json_str}")

# 将json转换为python的数据格式  这里将一个字符串转换成列表
#注意这里要单双引号结合，不然的话就会导致这个引号匹配的问题
s = '[{"name":"Jack","age":11},{"name":"Lucy","age":11},{"name":"Tom","age":11}]'
list_After = json.loads(s)
print(f"json_str的格式为{type(list_After)},json_str的内容为{list_After}")

s = '{"name":"Jack","age":11}'
list_After = json.loads(s)
print(f"json_str的格式为{type(list_After)},json_str的内容为{list_After}")