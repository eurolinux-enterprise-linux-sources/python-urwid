%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:          python-urwid
Version:       1.1.1
Release:       1%{?dist}
Summary:       Console user interface library

Group:         Development/Libraries
License:       LGPLv2+
URL:           http://excess.org/urwid/
Source0:       http://excess.org/urwid/urwid-%{version}.tar.gz

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
BuildRequires: python2-devel
BuildRequires: python-setuptools-devel
BuildRequires: python-twisted-core
BuildRequires: pygobject2
BuildRequires: python-test
# needed by selftest suite for test.support

%description
Urwid is a Python library for making text console applications.  It has
many features including fluid interface resizing, support for UTF-8 and
CJK encodings, standard and custom text layout modes, simple markup for
setting text attributes, and a powerful, dynamic list box that handles a
mix of widget types.  It is flexible, modular, and leaves the developer in
control.

%prep
%setup -q -n urwid-%{version}
find urwid -type f -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
find urwid -type f -name "*.py" -exec chmod 644 {} \;

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}

%{__python} setup.py install --skip-build --no-compile --root %{buildroot}

%check
python setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG examples docs
%{python_sitearch}/urwid
%{python_sitearch}/urwid-%{version}*.egg-info

%changelog
* Wed Jun 05 2013 Mike Burns <mburns@redhat.com> - 1.1.1-1
- Rebase on upstream 1.1.1 release

* Mon Aug 22 2011 Andy Grover <agrover@redhat.com> - 0.9.9.1-4
- Fix license in specfile to LGPLv2+ from LGPLv2.1+

* Wed Aug 17 2011 Andy Grover <agrover@redhat.com> - 0.9.9.1-3
* Add fix-none-leak.patch

* Mon Aug 15 2011 Andy Grover <agrover@redhat.com> - 0.9.9.1-2
- Add -fno-strict-aliasing to CFLAGS to fix warnings

* Wed May 19 2010 David Cantrell <dcantrell@redhat.com> - 0.9.9.1-1
- Initial package

