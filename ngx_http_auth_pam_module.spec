#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: nginx
# autospec version: v3
# autospec commit: c1050fe
#
Name     : ngx_http_auth_pam_module
Version  : 1.5.5
Release  : 36
URL      : https://github.com/sto/ngx_http_auth_pam_module/archive/v1.5.5/ngx_http_auth_pam_module-1.5.5.tar.gz
Source0  : https://github.com/sto/ngx_http_auth_pam_module/archive/v1.5.5/ngx_http_auth_pam_module-1.5.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: ngx_http_auth_pam_module-lib = %{version}-%{release}
Requires: ngx_http_auth_pam_module-license = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-nginx
BuildRequires : openssl-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# ngx_http_auth_pam_module
## Nginx module to use PAM for simple http authentication

%package lib
Summary: lib components for the ngx_http_auth_pam_module package.
Group: Libraries
Requires: ngx_http_auth_pam_module-license = %{version}-%{release}

%description lib
lib components for the ngx_http_auth_pam_module package.


%package license
Summary: license components for the ngx_http_auth_pam_module package.
Group: Default

%description license
license components for the ngx_http_auth_pam_module package.


%prep
%setup -q -n ngx_http_auth_pam_module-1.5.5
cd %{_builddir}/ngx_http_auth_pam_module-1.5.5
pushd ..
cp -a ngx_http_auth_pam_module-1.5.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nginx-module configure
nginx-module build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/ngx_http_auth_pam_module
cp %{_builddir}/ngx_http_auth_pam_module-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/ngx_http_auth_pam_module/150c254a838b4d8a70938c5bdc955d744d97da01 || :
nginx-module install %{buildroot}

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_http_auth_pam_module.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ngx_http_auth_pam_module/150c254a838b4d8a70938c5bdc955d744d97da01
