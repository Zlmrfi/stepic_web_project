def app(environ,start_response):
    s=''
    s=environ["QUERY_STRING"]
    otto=[]
    if s:
        ot="200 OK"
        s=s[s.find('?')+1:]
        while s:
            ore=s.find('&')
            if ore==-1:
                ore=len(s)
            #otto.append(bytes(s[:ore]+'\n',encoding='utf8')) python3
            otto.append(bytes(s[:ore]+'\n'))
            s=s[ore+1:]
    start_response('200 OK', [("Content-Type", "text/plain")])
    return otto
