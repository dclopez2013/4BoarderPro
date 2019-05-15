from __future__ import print_function

import basc_py4chan as p4
import downloader as ft

board = None
boardInput=""
prompt = "Enter board you wish to visit. IE: 'a' for anime and manga \n ,'c' for anime cute,\n 'w' animeand " \
         "wallpapers,\n 'm' for mecha,\n 'cgl' for cosplay,\n 'cm' for cute male,\n'f' for flash ,\n 'n' for " \
         "transportation,\n 'jp' for otaku culture,\n 'vp' for pokemon,\n 'v' for videogames,\n 'vg' for video game " \
         "generals,\n 'vr' retro games,\n 'co' comics and cartoons,\n'g' for technology,\n 'tv' television and films," \
         "\n 'k' weapons,\n 'o' auto,\n 'an' animals,\n 'tg' traditional games,\n 'qst' quests,\n 'sp' sports," \
         "\n 'asp' alternative sports,\n'sci' science and math,\n 'int' international,\n 'out' outdoors,\n 'toy' for " \
         "toys,\n 'biz' business and finance,\n 'i' Oekaki,\n 'po' papercraft and origami,\n 'p' photography\n," \
         "'ck' food and cooking,\n 'ic' Artwork critique,\n 'wg' Wallpapers general,\n 'mu' music,\n 'fa' fashion," \
         "\n '3' 3dcg,\n 'gd' graphic design,\n 'diy' do it yourself,\n 'wsg' worksafe gif\n,'s' beautiful women," \
         "\n 'hc' hardcore,\n 'hm' handsome men,\n 'h' hentain,\n 'e' ecchi,\n 'u' Yurri,\n 'd' Hentai Alternatives," \
         "\n 'y' Yaoi,\n 't' Torrents,\n 'hr' high resolution,\n'g' gif,\n 'trv' travel,\n 'fit' fitness," \
         "\n 'x' paranomal,\n 'lit' literature,\n 'adv' advice,\n 'lgbt' LGBT,\n 'mlp' my little pony," \
         "\n'b' **Random**,\n 'r' requests,\n 'r9k' robot9001,\n 'pol' poltically incorrect,\n 'soc' cams and " \
         "meetups,\n 's4s' shit 4chan says\n Enter your Choice Below: "

print(prompt)
boardInput = input()

board = p4.Board(str(boardInput))

if board:
    print("Board found")

else:
    print("Board: ", boardInput, " not found!")

ft.downloadEmAll(board)