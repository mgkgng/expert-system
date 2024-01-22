def retrieve_contents(path):
    with open(path, 'r') as f:
        text = f.read()
        lines_raw = text.split('\n')
        contents = []
        for line in lines_raw:
            if len(line) == 0 or line[0] == '#':
                continue
            
            content = line.split('#', 1)[0]
            if content == '':
                continue
            
            content = content.replace(' ', '')
            contents.append(content)
        return contents
