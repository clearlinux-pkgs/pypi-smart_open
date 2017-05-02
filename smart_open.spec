#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : smart_open
Version  : 1.5.2
Release  : 7
URL      : https://pypi.debian.net/smart_open/smart_open-1.5.2.tar.gz
Source0  : https://pypi.debian.net/smart_open/smart_open-1.5.2.tar.gz
Summary  : Utils for streaming large files (S3, HDFS, gzip, bz2...)
Group    : Development/Tools
License  : MIT
Requires: smart_open-python
Requires: boto
Requires: bz2file
Requires: requests
BuildRequires : boto
BuildRequires : bz2file
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : requests
BuildRequires : setuptools

%description
=============================================
smart_open -- utils for streaming large files
=============================================

%package python
Summary: python components for the smart_open package.
Group: Default

%description python
python components for the smart_open package.


%prep
%setup -q -n smart_open-1.5.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492372257
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1492372257
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
