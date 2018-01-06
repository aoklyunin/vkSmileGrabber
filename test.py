from urllib.request import urlretrieve

for i in range(0,255):
    for j in range(12,15):
        try:
            name = ("D83DD"+format(j, 'x')+format(i, 'x')).upper()
            print(name)
            href = "http://vk.com/images/emoji/"+name+".png"
            urlretrieve(href,"smiles/"+name+".png")
            print(href)
        except:
            print('not found')