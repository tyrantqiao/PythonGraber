# This Python file uses the following encoding: utf-8

import requests
import re

t = """1111111111</div><div class="lemma-summary" label-module="lemmaSummary">
<div class="para" label-module="para">Python<sup>[1]</sup><a class="sup-anchor" name="ref_[1]_21087">&nbsp;</a>
（英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/）, 是一种面向对象的解释型<a target=_blank href="/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80">计算机程序设计语言</a>，由荷兰人<a target=_blank href="/item/Guido%20van%20Rossum">Guido van Rossum</a>于1989年发明，第一个公开发行版发行于1991年。</div><div class="para" label-module="para">Python是纯粹的<a target=_blank href="/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6">自由软件</a>， <a target=_blank href="/item/%E6%BA%90%E4%BB%A3%E7%A0%81/3969" data-lemmaid="3969">源代码</a>和<a target=_blank href="/item/%E8%A7%A3%E9%87%8A%E5%99%A8">解释器</a>CPython遵循 <a target=_blank href="/item/GPL">GPL</a>(<a target=_blank href="/item/GNU">GNU</a> General Public License)协议<sup>[2]</sup><a class="sup-anchor" name="ref_[2]_21087">&nbsp;</a>
。Python语法简洁清晰，特色之一是强制用空白符(white space)作为语句缩进。</div><div class="para" label-module="para">Python具有丰富和强大的库。它常被昵称为<a target=_blank href="/item/%E8%83%B6%E6%B0%B4%E8%AF%AD%E8%A8%80">胶水语言</a>，能够把用其他语言制作的各种模块（尤其是<a target=_blank href="/item/C/7252092" data-lemmaid="7252092">C</a>/<a target=_blank href="/item/C%2B%2B">C++</a>）很轻松地联结在一起。常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），然后对其中<sup>[3]</sup><a class="sup-anchor" name="ref_[3]_21087">&nbsp;</a>
有特别要求的部分，用更合适的语言改写，比如<a target=_blank href="/item/3D%E6%B8%B8%E6%88%8F">3D游戏</a>中的图形渲染模块，性能要求特别高，就可以用C/C++重写，而后封装为Python可以调用的扩展类库。需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供<a target=_blank href="/item/%E8%B7%A8%E5%B9%B3%E5%8F%B0">跨平台</a>的实现。</div><div class="para" label-module="para">7月20日，IEEE发布2017年编程语言排行榜：Python高居首位<sup>[4]</sup><a class="sup-anchor" name="ref_[4]_21087">&nbsp;</a>
。</div>
</div>
<div class="configModuleBanner">
"""
# t.strip().encode('utf-8')
# <[/ad].*?>([^<\n]*)<[/sad].*?> 0.1

# <[/ad].*?>([^\s<\n]*?)<[/sad].*?> 0.2
# final edition >\s*?([^\&\b\n\[\]]*?)< 1.0
# update edition (?=lemma-summary")(.*?)(?<=config)
#TODO use regex less is more, changing to use tool
t.strip()
a = re.findall('''(?=lemma-summary")(.*?)(?<=config)''',
               t, flags=re.VERBOSE | re.MULTILINE | re.DOTALL)
m = re.findall('>\s*?([^\&\b\n\[\]]*?)<', t, flags=re.VERBOSE)
# print("".join(m))
print(a)
