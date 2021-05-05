# sha.ws

A personal website built with [Pelican](https://github.com/getpelican/pelican) and the [pelican-bootstrap3 theme](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3).

## Content License

[![CC BY 4.0][cc-by-shield]][cc-by]

Site content licensed under a [Creative Commons Attribution 4.0 International
License][cc-by], except where indicated otherwise.

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

## GitHub Actions

The site is automatically built and deployed via GitHub Actions.

### Testing

The GitHub Actions workflow can be tested locally using [act](https://github.com/nektos/act).

To supply secret values for testing you must export them as environment variables - The required variables are shown (as secrets) in `.actrc`.
