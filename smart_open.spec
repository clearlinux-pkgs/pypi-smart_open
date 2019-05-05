#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : smart_open
Version  : 1.8.3
Release  : 34
URL      : https://files.pythonhosted.org/packages/bf/ba/7eaf3c0dbe601c43d88e449dcd7b61d385fe07c0167163f63f58ece7c1b5/smart_open-1.8.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/bf/ba/7eaf3c0dbe601c43d88e449dcd7b61d385fe07c0167163f63f58ece7c1b5/smart_open-1.8.3.tar.gz
Summary  : Utils for streaming large files (S3, HDFS, gzip, bz2...)
Group    : Development/Tools
License  : MIT
Requires: smart_open-license = %{version}-%{release}
Requires: smart_open-python = %{version}-%{release}
Requires: smart_open-python3 = %{version}-%{release}
Requires: boto
Requires: boto3
Requires: requests
BuildRequires : boto
BuildRequires : boto3
BuildRequires : buildreq-distutils3
BuildRequires : bz2file
BuildRequires : requests

%description
======================================================
smart_open â utils for streaming large files in Python
======================================================

%package license
Summary: license components for the smart_open package.
Group: Default

%description license
license components for the smart_open package.


%package python
Summary: python components for the smart_open package.
Group: Default
Requires: smart_open-python3 = %{version}-%{release}

%description python
python components for the smart_open package.


%package python3
Summary: python3 components for the smart_open package.
Group: Default
Requires: python3-core

%description python3
python3 components for the smart_open package.


%prep
%setup -q -n smart_open-1.8.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557021884
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/smart_open
cp LICENSE %{buildroot}/usr/share/package-licenses/smart_open/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/smart_open/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
