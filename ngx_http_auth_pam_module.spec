#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ngx_http_auth_pam_module
Version  : 1.5.2
Release  : 20
URL      : https://github.com/sto/ngx_http_auth_pam_module/archive/v1.5.2/ngx_http_auth_pam_module-1.5.2.tar.gz
Source0  : https://github.com/sto/ngx_http_auth_pam_module/archive/v1.5.2/ngx_http_auth_pam_module-1.5.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: ngx_http_auth_pam_module-lib = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-nginx
BuildRequires : openssl-dev

%description
# ngx_http_auth_pam_module
## Nginx module to use PAM for simple http authentication

%package lib
Summary: lib components for the ngx_http_auth_pam_module package.
Group: Libraries

%description lib
lib components for the ngx_http_auth_pam_module package.


%prep
%setup -q -n ngx_http_auth_pam_module-1.5.2
cd %{_builddir}/ngx_http_auth_pam_module-1.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nginx-module configure
nginx-module build

%install
nginx-module install %{buildroot}


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_http_auth_pam_module.so
