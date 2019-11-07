## AutoCompletions for [frappe bench](https://github.com/frappe/bench)

Currently we are working only on `zsh` completions. Mostly because it helps vastly during development. Hopefully we'll have `bash` too, soon.


### Installation

1. Get the script: git or wget


```sh
git clone https://github.com/gavindsouza/bench-autocomplete && cd bench-auto-complete
```

alternativey,

```sh
wget https://raw.githubusercontent.com/gavindsouza/bench-autocomplete/master/zsh/_bench.old
```


Add the following line to the end of your `.zshrc`

```sh
rm -f ~/.zcompdump; compinit
```

Copy the `_bench.old` to `zsh/site-functions` as `/usr/local/share/zsh/site-functions/_bench` (on macOS)
Quite frankly, I'd like to symlink it but had some issues with that on macOS. arch did just fine though.
