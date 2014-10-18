# torrentz-magdl
Command-line downloader (via magnet link) for the holy _Torrentz_.


## Screenshot
![torrentz-magdl screenshot](https://raw.github.com/dannvix/torrentz-magdl/master/screenshot.png)


## One-click Downloader
* Given keywords, and search for _Torrentz_ resources
* Retrieve Magnet links, and open for download
* Multiple downlaods


## Dependency
* Python 2.x
* BitTorrent client with Magnet support
    - We use `webbrowser.open('magnet:...')`


## Usage
* Install to somewhere like `/usr/local/bin`
* Run `torrentz-magdl <keyword>`


## Get Your Hands Dirty
It'd be fun to integrate `download()` with other projects like:

* [torrent-mount](https://github.com/mafintosh/torrent-mount) -- mount magnet link as a filesystem via FUSE
* [peerflix](https://github.com/mafintosh/peerflix) -- stream torrent content to VLC

Thanks to [@clkao](https://github.com/clkao) for the brilliant ideas!


## MIT License
Copyright (c) 2014 Shao-Chung Chen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
