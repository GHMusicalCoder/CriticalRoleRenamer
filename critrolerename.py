import os
import re
import shutil

def main():
    path = os.path.join('/home', 'chris', 'Work')
    os.chdir(path)
    regex = re.compile('([\w\s&\.,]+)\s-\s[\w\s]+Episode\s(\d+)')
    for file in os.listdir(path):
        match = regex.search(file)
        if match is not None:
            #shutil.move(file, 'Critical Role - S01E{:0>2} - {}.mp3'.format(match.group(2), match.group(1).title()))
            print('Critical Role - S01E{:0>2} - {}.mp3'.format(match.group(2), match.group(1).title()))



if __name__ == '__main__':
    main()