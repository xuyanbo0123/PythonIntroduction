zoo = ['lion', "elephant", 'monkey']

if __name__ == "main":
    f = open("output.txt", 'a')

    for i in zoo:
        f.writelines(i)

    f.close()