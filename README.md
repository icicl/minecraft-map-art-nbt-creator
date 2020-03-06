# minecraft-map-art-nbt-creator
autogenerate the map_[##].dat nbt files for minecraft map art.


## how to use
### set the path to minecraft
the values of the variables on the first two lines in `mc map nbt.py` need to be changed to the minecraft path (which varies by system and is easy to look up), and the world name. this only needs to be done once
### set the parameters for that specific image
set `image` to the image path, `mapswide` and `mapstall` to the dimensions of the display, and `map_id` to the first map id # to be used.

## screenshots 
![Output](https://github.com/icicl/minecraft-map-art-nbt-creator/raw/master/screenshots/eagle_maps.png)<br />
![Input](https://github.com/icicl/minecraft-map-art-nbt-creator/raw/master/screenshots/eagle.jpeg)<br />

###### how it works
it resizes the given image so its pixel ratio is 1:1 to the right size grid of maps (128x128 'pixels' each). Then it determines which of the 204 allowable map colors is closest to each pixel and writes these to a gz'd nbt file. If the `locked` tag is set (it is by default), the map will not change even when close enough to its coords that it normally would.
