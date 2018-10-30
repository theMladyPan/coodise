# Coodise source code

## [forms/](forms/)
used for generating various forms, for tools such as rename, delete, create a file or login form

## [models/](models/)
for now unused

## [static/](static/)
contains static files such as Javascript files, css files and images. these should be served by actual server like apache, nginx and similar

## [templates/](templates/)
contains html templates for renderer. Most visuals will be in here

## [templatetags/](templatetags/)
contains custom filters used by templates, for example `{{ any_variable|tabsToSpaces }}`

## [utils/](utils/)
custom functions and classes used in project

## [views/](views/)
contains renderers of project, the actual backend of Coodise
