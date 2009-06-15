Summary:	Ruby's Intelligent Packaging
Name:		ruby-rip
Version:	0.0.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	rip.tar.gz
# Source0-md5:	c50a7da205326d834f23cd8f8630c5e3
Patch0:	%{name}-prefix.patch
URL:		http://hellorip.com/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rip is a next-generation packaging system for Ruby.

%prep
%setup -q -n rip
%patch0 -p1
cp %{_datadir}/setup.rb .
rm -r ext

%build
ruby setup.rb config \
	--prefix=%{_prefix}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rip
%{ruby_sitelibdir}/rip.rb
%{ruby_sitelibdir}/rip
