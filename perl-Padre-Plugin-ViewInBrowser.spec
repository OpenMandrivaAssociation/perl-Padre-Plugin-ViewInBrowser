%define upstream_name    Padre-Plugin-ViewInBrowser
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	View selected doc in browser for Padre
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Padre)
BuildRequires:	perl(Path::Class::File)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
Basically it's a shortcut for 
Wx::LaunchDefaultBrowser( $main->current->filename ).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 658871
- rebuild for updated spec-helper

* Mon Jun 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 381788
- update to 0.07
- using %%perl_convert_version
- fix license, summary & description fields

* Tue May 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.06-1mdv2010.0
+ Revision: 372112
- update to new version 0.06

* Mon May 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.04-1mdv2010.0
+ Revision: 371829
- tests broken for this release, skipping them

* Tue Jan 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.04-1mdv2009.1
+ Revision: 328956
- import perl-Padre-Plugin-ViewInBrowser


* Tue Jan 13 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist

