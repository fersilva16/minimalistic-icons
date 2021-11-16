<div align="center">
    <img src="examples/beer.png" alt="Beer" width="256" height="256">
    <img src="examples/boom.png" alt="Boom" width="256" height="256">
    <img src="examples/majhong.png" alt="Majhong" width="256" height="256">
</div>

# Minimalistic Icons [![MIT License][license-shield]][license-url] [![Twitter][twitter-shield]][twitter-url]
`minimalistic-icons` is a simple Command Line Interface for creating icons using [Twitter emojis](https://twemoji.twitter.com) and colored backgrounds, written using Python, [PIL](https://pillow.readthedocs.io) and [click](https://click.palletsprojects.com)!

# How to install
To clone and run, you'll need [Git](https://git-scm.com), [Python v3.8](https://www.python.org) and [PIP](https://pip.pypa.io).

```console
# Clone the repository
$ git clone https://github.com/fersilva16/minimalistic-icons

# Go into the repository
$ cd minimalistic-icons

# Install the dependencies
$ pip install -r requirements.txt

# Run the CLI
$ python3 minimalistic-icons/main.py
```

# Usage
```console
# Show usage
$ python3 minimalistic-icons/main.py --help

# Create an icon, it will create an image called `image.png`
$ python3 minimalistic-icons/main.py "#33d690" 👽

# Create an icon with custom size, you can use the alias `-s` or `-w`/`--width` and `-h`/`--height`
$ python3 minimalistic-icons/main.py "#9833d6" 🦴 --size 1024

# Create an icon with custom filename, you can use the alias `-o`
$ python3 minimalistic-icons/main.py "#d65e3a" 🐾 --output dog.png
```

# Roadmap
- [x] Add CLI with help message.
- [x] Add solid image creation and color parameter.
- [x] Add twemoji support and emoji parameter.
- [x] Create a README!
- [x] Add circle cropping.
- [x] Add custom image sizes.
- [ ] Add anti-aliasing.
- [ ] Add better installation, using PIP with Github url.
- [ ] Add text support.
- [x] Add an example icon in the README.
- [ ] Add typings using [mypy](http://mypy-lang.org).
- [ ] Add [setuptools](https://setuptools.pypa.io).
- [x] Get emoji as SVG for better resolution.
- [ ] Add custom emoji sizes.
- [ ] Add border radius option.

# Contribution
Contributions are welcome, feel free to create a [Issue][new-issue-url] or a [Pull Request][new-pr-url]. Don't forget to give the project a star! Thanks!

1. Fork the repository
2. Create a new branch
```console
$ git checkout -b BRANCH_NAME
```
3. Commit your changes
```console
$ git commit -m "add something"
```
4. Push to the branch
```console
$ git push origin BRANCH_NAME
```
5. [Open the Pull Request][new-pr-url]

# License
Distributed under the MIT License. See `LICENSE` for more information.


<!-- Links and images -->
[license-shield]: https://img.shields.io/github/license/fersilva16/minimalistic-icons?style=flat-square
[license-url]: https://github.com/fersilva16/minimalistic-icons/blob/master/LICENSE
[twitter-shield]: https://img.shields.io/badge/-fersilvaa16-black.svg?style=flat-square&logo=twitter&logoColor=white&colorB=49a2f2
[twitter-url]: https://twitter.com/fersilvaa16
[new-issue-url]: https://github.com/fersilva16/minimalistic-icons/issues/new
[new-pr-url]: https://github.com/fersilva16/minimalistic-icons/pulls/new
