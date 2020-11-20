# Sandia Software Catalog

Author: Wade Burgess <pwburge@sandia.gov> and Miranda Mundt <mmundt@sandia.gov> (forked from LLNL. Author Ian Lee: <lee1001@llnl.gov>)

Welcome to the Sandia National Laboratories software portal! The purpose of this software portal is to serve as a hub for open source software that is produced by Sandia National Labs.

## Prerequisites

Before you begin, make sure you have working installs of Git, Ruby, and Bundler <https://bundler.io/> You will need these tools for development.

## Getting Started

To work locally, first clone into the repository:

```
git clone https://github.com/sandialabs/sandialabs.github.io.git
```

Make sure you are in the directory you just created by running `cd sandialabs.github.io` Then you can use `bundler` to install the Ruby dependencies (see the [Jekyll installation docs](https://jekyllrb.com/docs/installation/) for step-by-step guides to setting this up):

```
bundle install
```

Running this will install everything in your Gemfile (including Jekyll). Finally, run the development web server with:

```
bundle exec jekyll serve
```

Followed by opening <http://localhost:4000> in a web browser.

### Tips

The gems in your sourcefile get updated frequently. It is a good idea to occasionally run `bundle update` from within your project's root directory to make sure the software on your computer is up to date.

## Contact

If you have any questions, please don't hesitate to contact [Wade Burgess](mailto:pwburge@sandia.gov).

You can also contact us via our mailing list: <wg-1424-ops@sandia.gov>

# Release

The code of this site is released under the MIT License. For more details see the
[LICENSE](LICENSE) File.

LLNL-CODE-705597
LLNL-WEB-680594
