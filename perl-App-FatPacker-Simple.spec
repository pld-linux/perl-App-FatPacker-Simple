#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	App
%define		pnam	FatPacker-Simple
Summary:	App::FatPacker::Simple - only fatpack a script
Name:		perl-App-FatPacker-Simple
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/App/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b92ea47141efaf42a236ea7e32d949cf
URL:		http://search.cpan.org/dist/App-FatPacker-Simple/
BuildRequires:	perl-Module-Build >= 0.4210
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-App-FatPacker
BuildRequires:	perl-Capture-Tiny
BuildRequires:	perl-Distribution-Metadata
BuildRequires:	perl-File-pushd
BuildRequires:	perl-Perl-Strip
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
App::FatPacker::Simple or its frontend fatpack-simple helps you
fatpack a script when YOU understand the whole dependencies of it.

For tutorial, please look at App::FatPacker::Simple::Tutorial.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/fatpack-simple
%{perl_vendorlib}/App/FatPacker/*.pm
%{perl_vendorlib}/App/FatPacker/Simple
%{_mandir}/man1/fatpack-simple.1p*
%{_mandir}/man3/App::FatPacker::Simple.3pm*
%{_mandir}/man3/App::FatPacker::Simple::Tutorial.3pm*
%{_examplesdir}/%{name}-%{version}
