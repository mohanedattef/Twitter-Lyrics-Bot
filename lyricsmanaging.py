
#open up the full lyrics file, utf8 encoding because the lyrics are in arabic
rlyrics= open('lyrics.txt', encoding='utf-8')
#put them into a list to mange
lyrics=rlyrics.readlines()
#figure the number of lines
lines=len(lyrics)
#open up the empty lyrics file that we're gonna fill, use w for write permessions 
lyrics2=open('lyrics2.txt','w', encoding='utf-8')
#counter
r=0
#iterate over the entire file to get a line and the line after it, strip it from the \n then join them together
#  with a " | "  to help later in the actual lyrics posting
for lyric in lyrics:
    if r<lines:
        x1=lyrics[r]
        x2=lyrics[r+1]
        x1=x1.strip()
        x2=x2.strip()
        if x1=='' or x2=='':
            r=r+1
            continue
        x=''.join(x1+ '|'+x2)
        lyrics2.write(x)
        r=r+2
        lyrics2.write('\n')

#close the file
lyrics2.close()