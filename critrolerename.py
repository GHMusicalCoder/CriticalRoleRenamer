import os
import re
import shutil
import collections

Episode = collections.namedtuple('Episode',
                                 'series, season, ep_num, title, format')

EpTest = 36

def main():
    path = os.path.join('/home', 'chris', 'Work')
    os.chdir(path)
    load_header()
    option = load_menu()
    critrole_re = re.compile('([\w\s&\.,!]+)\s-*\s[\w\s]+Episode\s(\d+)')
    season_re = re.compile('([\w\s]+)\s-\sS(\d+)E(\d+)\s-\s([\w\s&\.,!]+)\.(\w+)')
    for file in os.listdir(path):
        if option == 1:
            rename_episode(critrole_re, file)
        elif option == 2:
            renumber_season(season_re, file)


def load_header():
    print('---------------------------------------------')
    print('            My Rename Utility')
    print('---------------------------------------------')
    print()


def load_menu():
    print('[1] for Critical Role File rename')
    print('[2] for Season Renumber')
    print()
    value = input('Your Selection: ')
    return int(value)


def rename_episode(regex, file):
    match = regex.search(file)
    if match is not None:
        season = 2 if int(match.group(2)) > EpTest else 1
        print('Critical Role - S{:0>2}E{:0>2} - {}.mp3'.
              format(season, match.group(2), match.group(1).title()))
        # shutil.move(file, 'Critical Role - S{:0>2}E{:0>2} - {}.mp3'.
        #             format(season, match.group(2), match.group(1).title()))


def renumber_season(regex, file):
    match = regex.search(file)
    if match is not None:
        episode = Episode(series=match.group(1),
                          season=int(match.group(2)),
                          ep_num=int(match.group(3)),
                          title=match.group(4),
                          format=match.group(5))
        if episode.ep_num > EpTest and episode.season == 1:
            season = episode.season + 1
            # print('{} - S{:0>2}E{:0>2} - {}.{}'.
            #       format(episode.series, season, episode.ep_num, episode.title, episode.format))
            shutil.move(file, '{} - S{:0>2}E{:0>2} - {}.{}'.
                        format(episode.series, season, episode.ep_num, episode.title, episode.format))


if __name__ == '__main__':
    main()