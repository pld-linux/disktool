Summary:	Linux DiskTool
Name:		disktool
Version:	1.5.2
Release:	1
License:	GPL v2
Group:		Applications/Shells	
Source0:	http://freshmeat.net/redir/disktool/39170/url_tgz/dt-%{version}-1.i386.tar.gz
# Source0-md5:	5963e29f5072bea72fe23e096bc33574
URL:		http://www.freewebs.com/mlsoft
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DiskTool is a small, full-featured file manager for the Linux console
or an xterm-style terminal. It features file copying, moving, and
renaming, file marking for performing the same action on all marked
files (such as copy or delete), full directory support such as moving,
renaming, and deleting directories, permission and owner support (like
chmod and chown), file editing and creation, an RPM manager for
installing and inspecting .rpm files, an archive center supporting
.tar, .gz, .tar.gz, and .zip files, and fully configurable colors and
editor choices. All features are available with single keystroke
commands and require very little understanding of Linux. DiskTool is
written in Pascal and not in C. The source code is available upon
email request, but you will need to install the FPC compiler to
compile the modules.

%prep
%setup -q -n dt-install

%install
rm -rf $RPM_BUILD_ROOT

install -D dt $RPM_BUILD_ROOT%{_bindir}/dt
install -D ale $RPM_BUILD_ROOT%{_bindir}/ale

install -D dt.1.gz $RPM_BUILD_ROOT%{_mandir}/dt.1.gz
install -D ale.1.gz $RPM_BUILD_ROOT%{_mandir}/ale.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ale.doc dt.doc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*
