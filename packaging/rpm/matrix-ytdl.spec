%global ghurl   https://github.com/felfert/%{name}

Name:           matrix-ytdl
Version:        0.1
Release:        1%{?dist}
Summary:        A matrix bot for downloading YouTube videos

License:        MIT
BuildArch:      noarch

Buildrequires:  python3
Source:         %{ghurl}/archive/refs/tags/%{version}.tar.gz?fn=%{name}-%{version}.tar.gz
URL:            %{ghurl}

Requires: python3-matrix-nio
Requires: yt-dlp
Requires: libolm-python3
Requires: systemd
%{?sysusers_requires_compat}

%description
This package provides a matrix bot for downloading YouTube videos

%prep
%setup -q

%build
echo RPMBUILD

%install
install -D -m 0644 %{name}.sysusers %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m 0644 %{name}.tmpfiles %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -m 0644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}%{_var}/cache/%{name}

%files
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf
%dir %attr(0750, %{name}, %{name}) %{_sysconfdir}/%{name}
%dir %attr(0750, %{name}, %{name}) %{_var}/cache/%{name}

%pre
%sysusers_create_compat %{name}.sysusers

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%changelog
* Sun Apr 03 2022 Fritz Elfert <fritz@fritz-elfert.de> - 0.1-1
- Initial package.
