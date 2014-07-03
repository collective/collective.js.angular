AngularJS JavaScript Library Packaged for Plone
===============================================

This package provides the `AngularJS <http://angularjs.org//>`_ libray for use in Plone.

**Superheroic JavaScript MVW Framework** (cite of the original website title)

The whole ZIP file distribution is provided. So far only the main angular library is registered in ``portal_javascripts`` (read section Installion).

Anyway: all other angular standard distribution js-libs are available under ``++resources++collective.js.angular/NAME.js`` with name one out of:

- angular-animate.js/ angular-animate.min.js
- angular-cookies.js/ angular-cookies.min.js
- angular-csp.css
- angular-loader.js/ angular-loader.min.js
- angular-resource.js angular-resource.min.js
- angular-route.js/ angular-route.min.js
- angular-sanitize.js/ angular-sanitize.min.js
- angular-touch.js/ angular-touch.min.js


Installation
============

Just depend in your buildout on the egg ``collective.js.angular``.

Install ``AngularJS Javascript Library`` as an addon in Plone control-panel or in portal_setup.

Minified
  GenericSetup dependency string for ``metadata.xml`` is
  ``profile-collective.js.angular:default``.

Uncompressed
  GenericSetup dependency string for ``metadata.xml`` is
  ``profile-collective.js.angular:uncompressed``.

CDN (via Google, minified)
  GenericSetup dependency string for ``metadata.xml`` is
  ``profile-collective.js.angular:cdn``.

At the moment theres no uninstall profile configured.

This package is tested with for Plone 4.3 (should work with the 4-series)

Source Code and Contributions
=============================

If you want to help with the development (improvement, update, bug-fixing, ...)
of ``collective.js.angular`` this is a great idea!

The code is located in the
`github collective <https://github.com/collective/collective.js.angular>`_.

You can clone it or `get access to the github-collective
<http://collective.github.com/>`_ and work directly on the project.

Maintainer is Jens Klein and the BlueDynamics Alliance developer team. We
appreciate any contribution and if a release is needed to be done on pypi,
please just contact one of us
`dev@bluedynamics dot com <mailto:dev@bluedynamics.com>`_


Contributors
============

- Jens W. Klein <jens@bluedynamics.com>
- Daniel Widerin <daniel@widerin.net>

License Python Package is **GPL 2**

License external libray AngularJS is **MIT License**

