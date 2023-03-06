def spilit_part(res_redirect):
    for res in res_redirect:
        set_cookie = res.headers.get('Set-Cookie')
        split1 = set_cookie.split(",")
        split2 = split1[1].split(";")
        split3 = split2[0].split("=")
        print(split3[1])