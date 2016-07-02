Summary: Ulyaoth package repositories
Name: ulyaoth-repos
Version: 20160702
Release: 1%{?dist}
License: GPLv3
Group: System Environment/Base
URL: https://www.ulyaoth.net
Source0: https://repos.ulyaoth.net/RPM-GPG-KEY-ulyaoth
Source1: https://raw.githubusercontent.com/ulyaoth/ulyaothos/master/Packages/u/ulyaoth-repo/SOURCE/ulyaoth.repo
Source2: https://raw.githubusercontent.com/ulyaoth/ulyaothos/master/Packages/u/ulyaoth-repo/SOURCE/COPYING
Provides: ulyaoth-repos
Requires: ulyaoth-release
BuildArch: x86_64

%description
Ulyaoth package repository files for yum and dnf along with gpg public keys

%install
%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/licenses/ulyaoth

%{__install} -m 644 -p %{SOURCE0} \
   $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ulyaoth
%{__install} -m 644 -p %{SOURCE1} \
   $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ulyaoth.repo
%{__install} -m 644 -p %{SOURCE2} \
   $RPM_BUILD_ROOT/usr/share/licenses/ulyaoth/COPYING
   
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir /usr/share/licenses/ulyaoth
%config(noreplace) /etc/yum.repos.d/ulyaoth.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-ulyaoth
/usr/share/licenses/ulyaoth/COPYING

%changelog
* Sat Jul 2 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> - 20160702-1
- Initial Release..