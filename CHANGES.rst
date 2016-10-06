History
=======

1.5.5.0 (2016-10-06)
--------------------

- Upgrade to ``angular.js`` 1.5.5
  [jensens]


1.3.15.0 (2015-04-07)
---------------------

- Upgrade to ``angular.js`` 1.3.15
  [jensens]


1.3.0.0 (2014-10-14)
--------------------

- Upgrade to ``angular.js`` 1.3.0. Branched away 1.2.x series from here on.
  [jensens]


1.2.23.2 (2014-09-05)
---------------------

- fix mixed content problems with cdn, see
  https://stackoverflow.com/questions/18251128/why-am-i-suddenly-getting-a-blocked-loading-mixed-active-content-issue-in-fire
  [jensens]

1.2.32.1 (2014-09-05)
---------------------

- Fix typo in CDN profile
  [jensens]

- Upgrade to ``angular.js`` 1.2.23.
  [jensens]

1.2.19.1 (2014-07-03)
---------------------

- Add profile using the Google CDN
  [jensens]

1.2.19.0 (2014-07-03)
---------------------

- Upgrade to ``angular.js`` 1.2.19.
  [jensens]

1.2.16.1 (2014-06-05)
---------------------

- provide the full AngularJS release contents (ZIP release) as resources.
  [jensens]

1.2.16.0 (2014-06-05)
---------------------

- Upgrade to ``angular.js`` 1.2.16.
  [jensens]


1.2.14.1 (2014-03-03)
---------------------

- Fix GS import step, default is now minimized.
  [saily]

1.2.14.0 (2014-03-03)
---------------------

- Upgrade to ``angular.js`` 1.2.14.
  [jensens]


1.2.13.1 (2014-02-24)
---------------------

- Add uncompressed version of Angular. This targets on developer with need to
  debug into AngularJS Code.
  [jensens]

- Upgrade to ``angular.js`` 1.2.13.
  [jensens]


1.2.11.1 (2014-02-06)
---------------------

- Upgrade to ``angular.js`` 1.2.11.
  [saily]

- Fix wong value for compression attribute in generic setup.
  [saily]


1.2.10.4 (2014-02-06)
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
