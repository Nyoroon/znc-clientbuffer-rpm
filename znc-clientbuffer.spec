%global commit fe0f368e1fcab2b89d5c94209822d9b616cea840
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global modname clientbuffer

%global znc_version %((znc -v 2>/dev/null || echo 'a 0') | head -1 | awk '{print $2}')

Name:           znc-%{modname}
Version:        0
Release:        0.9git%{shortcommit}%{?dist}
Summary:        ZNC module for client specific buffers

License:        ASL 2.0
URL:            https://github.com/jpnurmi/znc-clientbuffer
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  znc-devel
Requires:       znc%{?_isa} = %znc_version

%description
The client buffer module maintains client specific buffers for identified
clients.

%prep
%autosetup -n %{name}-%{commit}

%build
CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" znc-buildmod %{modname}.cpp

%install
install -Dpm0755 %{modname}.so %{buildroot}%{_libdir}/znc/%{modname}.so

%files
%{_libdir}/znc/%{modname}.so

%changelog
* Tue Jul 31 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.9gitfe0f368
- Require specific version of znc, to avoid unexpected breakage when znc
  updates.  (Broken deps are better than a broken server.)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0-0.7gitfe0f368
- Rebuild for ICU 62

* Fri Jun 01 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.6gitfe0f368
- Rebuild for new znc.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.1gitfe0f368
- Initial package
