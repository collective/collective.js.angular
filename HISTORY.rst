History
=======

1.2.10.4 (unreleased)
---------------------

- Don't compress ``angular.min.js`` because safe compression of minimized files
  raises javascript errors.
  [saily]


1.2.10.3 (2014-01-27)
---------------------

- still z3c.autoinclude did not not work. Found
  http://romanofskiat.wordpress.com/2012/09/25/z3c-autoinclude-does-not-automatically-include-a-plone-package/
  and yes, the namespace package was not declared correctly. This should fix it. Phew
  [jensens]


1.2.10.2 (2014-01-27)
---------------------

- fix entry-point for z3c.autoinclude
  [jensens]


1.2.10.1 (2014-01-27)
---------------------

- initial work
  [jensens]
