# ShuffleMusicForProfit
Shuffles list of songs based on streaming costs

This program is intended to read a given list of music (CSV file) and shuffle it.
However, each time a song is played, the streaming service has to pay royalties/fees to the artists.

Depending on how cheap/expensive the song is per play, the shuffle algorithm should provide the cheap songs first and then the more expensive ones, so the streaming service can avoid paying for the expensive songs as much as possible, by simply suppressing the expensive songs to the end of this forced "shuffled" list

Example:
List of songs: (musics UUU and XXX are more expensive, so we will only present these songs at the end of this "custom shuffle" list produced.

Music / Price per play
1. Music AAA  - $0.001
2. Music TTT  - $0.002
3. Music YYY  - $0.001
4. Music UUU  - $0.08 - expensive to play (must go to the bottom of the shuffle list)
5. Music XXX  - $0.09 - expensive to play (must go to the bottom of the shuffle list)
6. Music EEE  - $0.002
7. Music PPP  - $0.001

Sample result of custom shuffling:
Music YYY
Music PPP
Music AAA
Music EEE
Music TTT
Music XXX
Music UUU
