# Mickey's Speedway USA

A repository exploring a decompilation of Mickey's Speedway USA.

This is super minimal and likely won't become a full decomp project. It is just being used to explore the Diddy Kong Racing engine as it evolved on the N64.

Grab tools

```sh
git submodule update --init --recursive
```

Install Dependencies
```sh
sudo apt install build-essential pkg-config git python3 wget libcapstone-dev python3-pip binutils-mips-linux-gnu
python3 -m pip install --user colorama watchdog levenshtein cxxfilt
python3 -m pip install --upgrade pycparser
```

Drop in `us` as `baserom.us.z64` (sha1sum: `TODO`)

```sh
make dependencies
make extract
make
```

