import execjs  

# # jsscript = "function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('c[1]="0/b/d/e/i.a";c[2]="0/b/d/e/l.a";c[3]="0/b/d/e/n.a";c[4]="0/b/d/e/k.a";c[5]="0/b/d/e/o.a";c[6]="0/b/d/e/j.a";c[7]="0/b/d/e/g.a";c[8]="0/b/d/e/f.a";c[9]="0/b/d/e/h.a";c[p]="0/b/d/e/m.a";c[r]="0/b/d/e/z.a";c[x]="0/b/d/e/y.a";c[v]="0/b/d/e/w.a";c[q]="0/b/d/e/s.a";c[t]="0/b/d/e/u.a";',36,36,'2017||||||||||jpg|07|photosr|18|00|01c211a18b|0151461a87|01b09fd1af|01c5125870|01095e4743|01f814f86a|0187484cb5|013bf7c8fc|01766ba5a1|015585b042|10|14|11|01ea784573|15|015dd8d6ed|13|01997959e8|12|01cc37f8ea|012536f709'.split('|'),0,{})"
# jsscript = "eval(function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('c[1]="0/b/d/e/i.a";c[2]="0/b/d/e/l.a";c[3]="0/b/d/e/n.a";c[4]="0/b/d/e/k.a";c[5]="0/b/d/e/o.a";c[6]="0/b/d/e/j.a";c[7]="0/b/d/e/g.a";c[8]="0/b/d/e/f.a";c[9]="0/b/d/e/h.a";c[p]="0/b/d/e/m.a";c[r]="0/b/d/e/z.a";c[x]="0/b/d/e/y.a";c[v]="0/b/d/e/w.a";c[q]="0/b/d/e/s.a";c[t]="0/b/d/e/u.a";',36,36,'2017||||||||||jpg|07|photosr|18|00|01c211a18b|0151461a87|01b09fd1af|01c5125870|01095e4743|01f814f86a|0187484cb5|013bf7c8fc|01766ba5a1|015585b042|10|14|11|01ea784573|15|015dd8d6ed|13|01997959e8|12|01cc37f8ea|012536f709'.split('|'),0,{}))"
# jsn = execjs.eval(jsscript)
# print(jsn)

def getImageUrls(encodeStr):
    content = open('/Users/yif/Documents/code/python/crawler/evaltest.js', 'r').read()
    ctx = execjs.compile(content)  
    # base64code = 'ZXZhbChmdW5jdGlvbihwLGEsYyxrLGUsZCl7ZT1mdW5jdGlvbihjKXtyZXR1cm4gYy50b1N0cmluZygzNil9O2lmKCEnJy5yZXBsYWNlKC9eLyxTdHJpbmcpKXt3aGlsZShjLS0pe2RbZShjKV09a1tjXXx8ZShjKX1rPVtmdW5jdGlvbihlKXtyZXR1cm4gZFtlXX1dO2U9ZnVuY3Rpb24oKXtyZXR1cm4nXFx3Kyd9O2M9MX07d2hpbGUoYy0tKXtpZihrW2NdKXtwPXAucmVwbGFjZShuZXcgUmVnRXhwKCdcXGInK2UoYykrJ1xcYicsJ2cnKSxrW2NdKX19cmV0dXJuIHB9KCdjWzFdPSIwL2IvZC9lL2kuYSI7Y1syXT0iMC9iL2QvZS9sLmEiO2NbM109IjAvYi9kL2Uvbi5hIjtjWzRdPSIwL2IvZC9lL2suYSI7Y1s1XT0iMC9iL2QvZS9vLmEiO2NbNl09IjAvYi9kL2Uvai5hIjtjWzddPSIwL2IvZC9lL2cuYSI7Y1s4XT0iMC9iL2QvZS9mLmEiO2NbOV09IjAvYi9kL2UvaC5hIjtjW3BdPSIwL2IvZC9lL20uYSI7Y1tyXT0iMC9iL2QvZS96LmEiO2NbeF09IjAvYi9kL2UveS5hIjtjW3ZdPSIwL2IvZC9lL3cuYSI7Y1txXT0iMC9iL2QvZS9zLmEiO2NbdF09IjAvYi9kL2UvdS5hIjsnLDM2LDM2LCcyMDE3fHx8fHx8fHx8fGpwZ3wwN3xwaG90b3NyfDE4fDAwfDAxYzIxMWExOGJ8MDE1MTQ2MWE4N3wwMWIwOWZkMWFmfDAxYzUxMjU4NzB8MDEwOTVlNDc0M3wwMWY4MTRmODZhfDAxODc0ODRjYjV8MDEzYmY3YzhmY3wwMTc2NmJhNWExfDAxNTU4NWIwNDJ8MTB8MTR8MTF8MDFlYTc4NDU3M3wxNXwwMTVkZDhkNmVkfDEzfDAxOTk3OTU5ZTh8MTJ8MDFjYzM3ZjhlYXwwMTI1MzZmNzA5Jy5zcGxpdCgnfCcpLDAse30pKQo='
    a = ctx.call('GetSource', encodeStr)
    return a