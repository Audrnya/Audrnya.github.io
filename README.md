## Audrnya's personal website

This is just a personal website to display my projects, information about me, etc.

It is a static site generated by Jekyll and implements [Mr. Green's Jekyll Theme](https://github.com/MrGreensWorkshop/MrGreen-JekyllTheme) (Special thanks!) with some personal modifications.

## How to run locally

1. [Install Jekyll](https://jekyllrb.com/docs/installation/) and its prerequisites to your OS.
1. Clone or download this repo, in command prompt go to the folder run `bundle install` command.
1. Build the site using the command in `test.ps1`. (if not using powershell, change the file extension name)
   - with `--safe` parameter you can make sure no 3rd party plugin added. (for GitHub pages development)
   - with `--incremental` to update only individual files that were just changed instead of the whole site.
1. The page will be up and running at the `localhost:4000/` address.

### Documentation

Check out [Mr. Green theme tutorials playlist](https://www.youtube.com/playlist?list=PLAymxPbYHgl-fFy5can7uZBMJtFWVcphD) on YouTube.
