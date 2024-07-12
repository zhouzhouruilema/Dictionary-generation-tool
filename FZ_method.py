# coding=utf-8
import exrex
# import requests

url = "http://image.abc.music.lwz.com"      # image.abc.music.lwz.com


"""
get_url
传入一个参数之后，获取url里面有用的内容
"""
def get_url(url):
    # 通过split切割出来是一个列表
    url_list = url.split(".")

    # 通过拿到url_list的列表长度
    # if len(url_list)
    len(url_list)

    # 永远都切第一位，因为第一位不纯粹有  http://内容
    # 第一位内容：
    new_url_list = [url_list[0].split("://")[-1]]

    for value in url_list:
        if value == url_list[0] or value == url_list[-1]:
            continue
        new_url_list.append(value)

    # 这个是我们处理之后的信息   列表
    return new_url_list


"""
get_txt_contents
传入文件名
返回值是一个列表list
"""
def get_txt_contents(file_name="muben.txt"):
    with open(f"{file_name}", "r") as f:
        # 去除\n换行方法
        dict_list = f.read().splitlines()
    return dict_list

"""
put_txt_contents
dict_list是我们原始文件的内容。
new_url_list是我们的url处理之后的值。
"""
def put_txt_contents(new_url_list, dict_list, filename="dict"):
    # image.abc.music.lwz
    with open(f"new_{filename}.txt", "a", newline="") as f:
        for value in dict_list:
            # 第一个参数值用range来改变  第二个就是不用刚刚用了个range的值的其他range值
            for i in range(0, len(new_url_list)):
                for j in range(0, len(new_url_list)):
                    # if i == j:
                    #     continue
                    a = new_url_list[i]
                    b = new_url_list[j]
                    dicts = list(exrex.generate(rf"{a}{value}{b}"))
                    f.write(dicts[0]+"\n")

if __name__ == '__main__':
    url = input("请输入url：")
    put_txt_contents(get_url(url), get_txt_contents())
