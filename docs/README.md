# software.sandia.gov Documentation

To aid future maintenance of this website, this README
will document details that have the potential to change at
some point in the future.

## Headers and Footers

The headers and footers for all pages are defined in the
[`_includes`](https://github.com/sandialabs/sandialabs.github.io/tree/main/_includes)
directory.

- [head.html](https://github.com/sandialabs/sandialabs.github.io/blob/main/_includes/head.html) contains:
  - Tab icon image
  - Sandia approval information
- [header.html](https://github.com/sandialabs/sandialabs.github.io/blob/main/_includes/header.html) contains:
  - Navigational bar / dropdowns
  - Social media links
- [footer.html](https://github.com/sandialabs/sandialabs.github.io/blob/main/_includes/footer.html) contains:
  - Sandia / NNSA logos
  - Sandia legal/funding statement
  - Copyright statement

## Repository List

The file to control what repositories are queried and cataloged can be found
in [input_lists.json](https://github.com/sandialabs/sandialabs.github.io/blob/main/_explore/input_lists.json).

- `orgs` controls GitHub organizations under which all public repositories will be queried.
  For example, the [`mantevo` organization](https://github.com/mantevo) has 13 public repositories
  (as of the writing of this README). All of these will be included in any query scripts
  for software.sandia.gov.
- `repos` controls individual repositories.

## Categories

The file to control categories that appear on the homepage and the catalog search
can be found in [category_info.json](https://github.com/sandialabs/sandialabs.github.io/blob/main/category/category_info.json).
All categories require a title (as it appears on the homepage), an icon path (with appropriate
alternative text), a description, and the correlated GitHub "topic" (or topics).
For example, for a repository to show up in the `BUILD TOOLS` category on
software.sandia.gov, the repository must have the `snl-build-tools` topic
applied on GitHub. More information on GitHub topics can be found on
their [online documentation](https://help.github.com/articles/about-topics).

## Image Source

Images are stored in the [assets directory](https://github.com/sandialabs/sandialabs.github.io/tree/main/assets/images).
Images from the original LLNL repository are also there for reference.

The icons and banner image were created by Sandia's internal Creative Services
team.

## Automatic Updates

Updates occur nightly via a
[GitHub Actions workflow](https://github.com/sandialabs/sandialabs.github.io/blob/main/.github/workflows/update_data.yml).
This job requires a `TOKEN_USER` and `SECRET_TOKEN` (both secrets on the repository)
in order to run. Information on the `SECRET_TOKEN` requirements can be found
in the [_explore README](https://github.com/sandialabs/sandialabs.github.io/tree/main/_explore).

If the job needs to be run outside of the regular nightly cadence, a user can navigate
to the [Actions page](https://github.com/sandialabs/sandialabs.github.io/actions/workflows/update_data.yml)
and click the "Run workflow" button.

There is a possibility in the future that the nightly query will error due to
GitHub request limits. As of July 2024, GitHub has an hourly limit of 5000 API
requests. If the limit is hit, processing will cease until the available
queries reset.

### Acknowledgements

Sandia National Laboratories is a multimission laboratory managed and operated by National Technology and Engineering
Solutions of Sandia, LLC., a wholly owned subsidiary of Honeywell International, Inc., for the U.S. Department of
Energy’s National Nuclear Security Administration under contract DE-NA-0003525. SAND2024-09661O
