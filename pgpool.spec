%define name    pgpool
%define version 3.1.1
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Pgpool is a connection pooling/replication server for PostgreSQL
License: BSD
Group: System/Servers
URL: http://pgfoundry.org/projects/pgpool
Source0: %{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-root

%description
Pgpool is a connection pooling/replication 
server for PostgreSQL.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/pgpool.conf.sample
%{_bindir}/pgpool
%{_mandir}/man8/pgpool.*


