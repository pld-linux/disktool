Summary:	Linux DiskTool - file manager for text terminal
Summary(pl):	Linux DiskTool - zarz�dca plik�w dla terminala tekstowego
Name:		disktool
Version:	1.5.5
Release:	1
License:	Freeware
Group:		Applications/Shells	
Source0:	http://www.freewebs.com/mlsoft/dt-%{version}-1.i386.tar.gz
# Source0-md5:	df92838462332d5dea7b8811bca32bd3
URL:		http://www.freewebs.com/mlsoft/
ExclusiveArch:	%{ix86}
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

%description -l pl
DiskTool to ma�y, w pe�ni funkcjonalny zarz�dca plik�w dla konsoli
linuksowej albo terminala typu xterm. Ma kopiowanie, przenoszenie i
zmian� nazw, zaznaczanie plik�w do wykonywania tej samej akcji (takiej
jak kopiowanie czy usuwanie) na wszystkich zaznaczonych plikach, pe�n�
obs�ug� katalog�w (przenoszenie, zmian� nazw, usuwanie), obs�ug�
uprawnie� i w�asno�ci (chmod/chown), edycj� i tworzenie plik�w,
zarz�dc� RPM do instalowania i przegl�dania plik�w .rpm, centrum
archiwizacji obs�uguj�ce pliki .tar, .gz, .tar.gz i .zip oraz w pe�ni
konfigurowalne kolory i wyb�r edytor�w. Wszystkie funkcje s� dost�pne
pod pojedynczymi skr�tami klawiaturowymi i wymagaj� bardzo ma�ej
znajomo�ci Linuksa. DiskTool zosta� napisany w Pascalu, a nie C. Kod
�r�d�owy jest dost�pny na ��danie poczt� elektroniczn�, ale do
kompilacji modu��w potrzebny jest kompilator FPC.

%prep
%setup -q -n dt-install

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

install -D dt $RPM_BUILD_ROOT%{_bindir}/dt
install -D ale $RPM_BUILD_ROOT%{_bindir}/ale

gzip -dc dt.1.gz >$RPM_BUILD_ROOT%{_mandir}/man1/dt.1
gzip -dc ale.1.gz >$RPM_BUILD_ROOT%{_mandir}/man1/ale.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ale.doc dt.doc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
