# WAXIE SOLSTA

## When does the site update?
Anytime a change is made

## How
It uses GitHub Actions to run [Render Engine]

## How to Edit Items

- In Code Select the Content Folder and Look for the _Corresponding Item Number_
- Select the Pencil Icon to edit the text
- When changes are complete add a Commit Message at the bottom and Commit to `master`

[Render Engine] uses a split system of metadata and [markdown](https://daringfireball.net/projects/markdown/).

To edit an image, product description, item number, or category data, you will edit **the metadata**. To edit the long description, update the settings

## How to Edit the Site Template

This site uses the [Jinja2](https://jinja.palletsprojects.com), this is similar to the HTML markup of Hubspot's HUBL language.

:warning: Please use caution when updating the files as it can cause the build to error if there is a validation error. The website will default to the last stable build.

[Render Engine]: https://render-engine.readthedocs.org
