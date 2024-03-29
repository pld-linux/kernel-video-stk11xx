#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_with	verbose		# verbose build (V=1)
#
%define		_modname	stk11xx
%define		_rel	1
%define		snap	20110613
Summary:	Syntek camera driver for Linux
Summary(pl.UTF-8):	Sterownik do kamer firmy Syntek dla Linuksa
Name:		kernel%{_alt_kernel}-video-%{_modname}
Version:	2.2.0
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
#Source0:	http://dl.sourceforge.net/syntekdriver/%{_modname}-%{version}.tar.gz
Source0:	%{_modname}-%{snap}.tar.gz
# Source0-md5:	1f9f33033c893bdb215e5085d57bf831
URL:		http://syntekdriver.sourceforge.net/
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.34}
BuildRequires:	rpmbuild(macros) >= 1.379
Requires(post,postun):	/sbin/depmod
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Syntek USB 2.0 video camera driver (developement version) for
DC-1125 ans STK-1135. This driver can do damages. Use this driver only
if you know what you are doing.

%description -l pl.UTF-8
Wersja rozwojowa sterownika dla kamer USB DC-1125 i STK-1135 firmy
Syntek. Sterownik ten może uszkodzić sprzęt, należy używać go tylko
wtedy, gdy się wie, co się robi.

%prep
%setup -q -n %{_modname}-%{version}

%build
%build_kernel_modules -m %{_modname}

%install
rm -rf $RPM_BUILD_ROOT

%install_kernel_modules -m %{_modname} -d kernel/drivers/video 

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n kernel%{_alt_kernel}-video-%{_modname}
%depmod %{_kernel_ver}

%postun   -n kernel%{_alt_kernel}-video-%{_modname}
%depmod %{_kernel_ver}

%files
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/kernel/drivers/video/%{_modname}.ko*
