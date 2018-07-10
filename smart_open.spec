#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : smart_open
Version  : 1.6.0
Release  : 29
URL      : https://pypi.debian.net/smart_open/smart_open-1.6.0.tar.gz
Source0  : https://pypi.debian.net/smart_open/smart_open-1.6.0.tar.gz
Summary  : Utils for streaming large files (S3, HDFS, gzip, bz2...)
Group    : Development/Tools
License  : MIT
Requires: smart_open-python3
Requires: smart_open-license
Requires: smart_open-python
Requires: boto
Requires: boto3
Requires: bz2file
Requires: requests
BuildRequires : boto
BuildRequires : boto3
BuildRequires : bz2file
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : requests
BuildRequires : setuptools

%description
smart_open -- utils for streaming large files
        =============================================
        
        |License|_ |Travis|_

%package license
Summary: license components for the smart_open package.
Group: Default

%description license
license components for the smart_open package.


%package python
Summary: python components for the smart_open package.
Group: Default
Requires: smart_open-python3

%description python
python components for the smart_open package.


%package python3
Summary: python3 components for the smart_open package.
Group: Default
Requires: python3-core

%description python3
python3 components for the smart_open package.


%prep
%setup -q -n smart_open-1.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530989825
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/smart_open
cp LICENSE %{buildroot}/usr/share/doc/smart_open/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/smart_open/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
