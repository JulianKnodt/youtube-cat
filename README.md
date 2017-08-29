# Youtube Cat

_Please clone repo for usage._

## Purpose

The intended purpose of this project was to create personal playlists
from youtube videos, and combine them into one mp3.

It was intended to use a highly readable format, which anyone could use.


## Usage
```
$ python cat.py <*.csv>
```

### Creating a CSV
``` csv
comment, This is a sample file
c, the first number is the hh:mm:ss start time
c, the second number is the duration in seconds
c, the third element is the url of the youtube video being added.

c, Electric Light Orchestra Telephone Line
10,74,https://www.youtube.com/watch?v=77R1Wp6Y_5Y

c, Gorillaz Andromeda Purple Disco Mac. Remix,
1:03,33,https://www.youtube.com/watch?v=tW3J9XnBbqk

c, Savant Starscream Forever
36.5,62,https://www.youtube.com/watch?v=QHjGGQI3iU0

c, Silence
4,,-
```
