#! coding: utf-8
import sys,os

if __name__ == "__main__":
    f = open(sys.argv[1])
    line = f.readline()
    while line:
        item = line.split("\t")
        name = item[0]
        cate = item[1]
        platform = item[2]
        url = item[3]
        out_file = open("{}/{}.txt".format(cate, name), "w")
        tag = cate
        if len(item[4]) > 0:
            tag = item[4]
        is_free=True
        if len(item) >= 6:
            if "付费" in item[5]:
                is_free = False
        add_wukong=False
        if len(item) >= 6:
            if "悟空" in item[6]:
                add_wukong = True
        out_file.write("{}\n".format(tag))

        if not add_wukong:
            format_line = "<p><a href=\"{}\" target=\"_self\">链接：{}网盘（点我跳转）</a></p>".format(url, platform)
        else:
            format_line = "<p><strong>安卓用户专享</strong></p>"
            format_line += "<p><a href=\"https://v.wkbrowser.com/s/iJTRD3tr/\" target=\"_self\">链接：在线高清（点我跳转）</a></p>"
            format_line += "<p><strong>所有用户可享</strong></p>"
            format_line += "<p><a href=\"{}\" target=\"_self\">链接：{}网盘（点我跳转）</a></p>".format(url, platform)

        if not is_free:
            format_line = "完整高清{}资源链接".format(platform)
            format_line = format_line + "<br>"
            format_line += "[Xhide]<p><a href=\"{}\" target=\"_self\">链接：{}网盘（点我跳转）</a></p>[/Xhide]".format(url, platform)
        out_file.write(format_line)
        out_file.close()
        line = f.readline()
