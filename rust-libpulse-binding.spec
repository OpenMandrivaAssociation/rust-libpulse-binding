# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate libpulse-binding

Name:           rust-%{crate}
Version:        2.15.0
Release:        2%{?dist}
Summary:        Rust language binding for the PulseAudio libpulse library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/libpulse-binding
Source:         %{crates_source}
# Initial patched metadata
# * No Windows deps
Patch0:         libpulse-binding-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust language binding for the PulseAudio libpulse library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dox-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dox-devel %{_description}

This package contains library source intended for building other packages
which use "dox" feature of "%{crate}" crate.

%files       -n %{name}+dox-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+latest_pa_common_compatibility-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+latest_pa_common_compatibility-devel %{_description}

This package contains library source intended for building other packages
which use "latest_pa_common_compatibility" feature of "%{crate}" crate.

%files       -n %{name}+latest_pa_common_compatibility-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+latest_pa_compatibility-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+latest_pa_compatibility-devel %{_description}

This package contains library source intended for building other packages
which use "latest_pa_compatibility" feature of "%{crate}" crate.

%files       -n %{name}+latest_pa_compatibility-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pa_latest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pa_latest-devel %{_description}

This package contains library source intended for building other packages
which use "pa_latest" feature of "%{crate}" crate.

%files       -n %{name}+pa_latest-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pa_latest_common-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pa_latest_common-devel %{_description}

This package contains library source intended for building other packages
which use "pa_latest_common" feature of "%{crate}" crate.

%files       -n %{name}+pa_latest_common-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pa_v12-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pa_v12-devel %{_description}

This package contains library source intended for building other packages
which use "pa_v12" feature of "%{crate}" crate.

%files       -n %{name}+pa_v12-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pa_v12_compatibility-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pa_v12_compatibility-devel %{_description}

This package contains library source intended for building other packages
which use "pa_v12_compatibility" feature of "%{crate}" crate.

%files       -n %{name}+pa_v12_compatibility-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pa_v13-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pa_v13-devel %{_description}

This package contains library source intended for building other packages
which use "pa_v13" feature of "%{crate}" crate.

%files       -n %{name}+pa_v13-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pa_v5-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pa_v5-devel %{_description}

This package contains library source intended for building other packages
which use "pa_v5" feature of "%{crate}" crate.

%files       -n %{name}+pa_v5-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pa_v6-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pa_v6-devel %{_description}

This package contains library source intended for building other packages
which use "pa_v6" feature of "%{crate}" crate.

%files       -n %{name}+pa_v6-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pa_v8-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pa_v8-devel %{_description}

This package contains library source intended for building other packages
which use "pa_v8" feature of "%{crate}" crate.

%files       -n %{name}+pa_v8-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# Doc-tests depend on running pulseaudio
%cargo_test -- --lib
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 08:02:31 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.15.0-1
- Update to 2.15.0

* Wed Dec 11 09:16:32 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.14.0-2
- Enable tests

* Tue Nov 05 23:04:59 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.14.0-1
- Initial package
