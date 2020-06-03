#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Output
Version  : 1.031
Release  : 34
URL      : http://search.cpan.org/CPAN/authors/id/B/BD/BDFOY/Test-Output-1.031.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/B/BD/BDFOY/Test-Output-1.031.tar.gz
Summary  : 'Utilities to test STDOUT and STDERR messages.'
Group    : Development/Tools
License  : Artistic-1.0-Perl Artistic-2.0
Requires: perl-Test-Output-license = %{version}-%{release}
Requires: perl-Test-Output-perl = %{version}-%{release}
Requires: perl(Capture::Tiny)
Requires: perl(Test::Builder)
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)

%description
=pod
=encoding utf8
=head1 The Test::Output module
looking at this because you don't know where else to find what you're
looking for. Read this once and you might never have to read one again
for any Perl module.

%package dev
Summary: dev components for the perl-Test-Output package.
Group: Development
Provides: perl-Test-Output-devel = %{version}-%{release}
Requires: perl-Test-Output = %{version}-%{release}

%description dev
dev components for the perl-Test-Output package.


%package license
Summary: license components for the perl-Test-Output package.
Group: Default

%description license
license components for the perl-Test-Output package.


%package perl
Summary: perl components for the perl-Test-Output package.
Group: Default
Requires: perl-Test-Output = %{version}-%{release}

%description perl
perl components for the perl-Test-Output package.


%prep
%setup -q -n Test-Output-1.031
cd %{_builddir}/Test-Output-1.031

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Output
cp %{_builddir}/Test-Output-1.031/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Output/46ff8d6b70f1daa7d3b90d4d9f497b4c0bca0b67
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Output.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Output/46ff8d6b70f1daa7d3b90d4d9f497b4c0bca0b67

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Test/Output.pm
