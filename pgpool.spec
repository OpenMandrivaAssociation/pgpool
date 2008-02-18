%define name    pgpool
%define version 3.4.1
%define release %mkrel 2

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Connection pooling/replication server for PostgreSQL
License: BSD
Group: System/Servers
URL: http://pgfoundry.org/projects/pgpool
Source0: http://pgfoundry.org/frs/download.php/1446/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}

%description
Pgpool is a connection pooling/replication 
server for PostgreSQL.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall
mv %{buildroot}/%{_sysconfdir}/pgpool.conf.sample \
    %{buildroot}/%{_sysconfdir}/pgpool.conf
mv %{buildroot}/%{_sysconfdir}/pool_hba.conf.sample \
    %{buildroot}/%{_sysconfdir}/pool_hba.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/pgpool.conf
%config(noreplace) %{_sysconfdir}/pool_hba.conf
%{_bindir}/pgpool
%{_mandir}/man8/pgpool.*
%{_datadir}/pgpool

