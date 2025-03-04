%global need_bootstrap_set 0
%{!?need_bootstrap: %global need_bootstrap %{need_bootstrap_set}}
%bcond_with doc
%ifarch %{arm} %{ix86} x86_64 ppc %{power64}
%global __with_hipe 1
%endif
%global __with_emacs 1
%global __with_xemacs 0
%global __with_examples 1
%global __with_java 1
%global __with_wxwidgets 1
Name:                erlang
Version:             21.3.3
Release:             3
Summary:             General-purpose programming language and runtime environment
License:             ASL 2.0
URL:                 https://www.erlang.org
VCS:                 scm:git:https://github.com/erlang/otp
Source0:             https://github.com/erlang/otp/archive/OTP-%{version}/otp-OTP-%{version}.tar.gz
Source1:             epmd.service
Source2:             epmd.socket
Source3:             epmd@.service
Source4:             epmd@.socket
Patch1:              otp-0001-Do-not-format-man-pages-and-do-not-install-miscellan.patch
Patch2:              otp-0002-Remove-rpath.patch
Patch3:              otp-0003-Do-not-install-C-sources.patch
Patch4:              otp-0004-Do-not-install-Java-sources.patch
Patch5:              otp-0005-Do-not-install-nteventlog-and-related-doc-files-on-n.patch
Patch6:              otp-0006-Do-not-install-erlang-sources.patch
Patch7:              otp-0007-Add-extra-search-directory.patch
Patch8:              otp-0008-Avoid-forking-sed-to-get-basename.patch
Patch9:              otp-0009-Load-man-pages-from-system-wide-directory.patch
Patch10:             otp-0010-Improve-nodes-querying.patch
Patch11:             extern-ei-default-socket-callbacks.patch
BuildRequires:       gcc gcc-c++ flex
%if %{with doc}
%if 0%{?need_bootstrap} < 1
BuildRequires:       erlang
%endif
%endif
BuildRequires:       systemd-devel systemd
%{?systemd_requires}
Requires:            systemd
BuildRequires:       autoconf automake
Requires:            %{name}-asn1%{?_isa} = %{version}-%{release}
%if %{__with_wxwidgets}
Requires:            %{name}-common_test%{?_isa} = %{version}-%{release}
%endif %{__with_wxwidgets}
Requires:            %{name}-compiler%{?_isa} = %{version}-%{release}
Requires:            %{name}-crypto%{?_isa} = %{version}-%{release}
%if %{__with_wxwidgets}
Requires:            %{name}-debugger%{?_isa} = %{version}-%{release}
%endif %{__with_wxwidgets}
%if %{__with_wxwidgets}
Requires:            %{name}-dialyzer%{?_isa} = %{version}-%{release}
%endif %{__with_wxwidgets}
Requires:            %{name}-diameter%{?_isa} = %{version}-%{release}
Requires:            %{name}-edoc%{?_isa} = %{version}-%{release}
Requires:            %{name}-eldap%{?_isa} = %{version}-%{release}
Requires:            %{name}-erl_docgen%{?_isa} = %{version}-%{release}
Requires:            %{name}-erl_interface%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
%if %{__with_wxwidgets}
Requires:            %{name}-et%{?_isa} = %{version}-%{release}
%endif %{__with_wxwidgets}
Requires:            %{name}-eunit%{?_isa} = %{version}-%{release}
Requires:            %{name}-ftp%{?_isa} = %{version}-%{release}
Requires:            %{name}-hipe%{?_isa} = %{version}-%{release}
Requires:            %{name}-inets%{?_isa} = %{version}-%{release}
%if %{__with_java}
Requires:            %{name}-jinterface%{?_isa} = %{version}-%{release}
%endif %{__with_java}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
%if %{__with_wxwidgets}
Requires:            %{name}-megaco%{?_isa} = %{version}-%{release}
%endif %{__with_wxwidgets}
Requires:            %{name}-mnesia%{?_isa} = %{version}-%{release}
%if %{__with_wxwidgets}
Requires:            %{name}-observer%{?_isa} = %{version}-%{release}
%endif %{__with_wxwidgets}
Requires:            %{name}-odbc%{?_isa} = %{version}-%{release}
Requires:            %{name}-os_mon%{?_isa} = %{version}-%{release}
Requires:            %{name}-otp_mibs%{?_isa} = %{version}-%{release}
Requires:            %{name}-parsetools%{?_isa} = %{version}-%{release}
Requires:            %{name}-public_key%{?_isa} = %{version}-%{release}
%if %{__with_wxwidgets}
Requires:            %{name}-reltool%{?_isa} = %{version}-%{release}
%endif %{__with_wxwidgets}
Requires:            %{name}-runtime_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-sasl%{?_isa} = %{version}-%{release}
Requires:            %{name}-snmp%{?_isa} = %{version}-%{release}
Requires:            %{name}-ssh%{?_isa} = %{version}-%{release}
Requires:            %{name}-ssl%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-syntax_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-tftp%{?_isa} = %{version}-%{release}
Requires:            %{name}-tools%{?_isa} = %{version}-%{release}
%if %{__with_wxwidgets}
Requires:            %{name}-wx%{?_isa} = %{version}-%{release}
%endif %{__with_wxwidgets}
Requires:            %{name}-xmerl%{?_isa} = %{version}-%{release}
%description
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.

%package asn1
Summary:             Provides support for Abstract Syntax Notation One
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description asn1
Provides support for Abstract Syntax Notation One.
%if %{__with_wxwidgets}

%package common_test
Summary:             A portable framework for automatic testing
Requires:            %{name}-compiler%{?_isa} = %{version}-%{release}
Requires:            %{name}-crypto%{?_isa} = %{version}-%{release}
Requires:            %{name}-debugger%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-inets%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-observer%{?_isa} = %{version}-%{release}
Requires:            %{name}-runtime_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-sasl%{?_isa} = %{version}-%{release}
Requires:            %{name}-snmp%{?_isa} = %{version}-%{release}
Requires:            %{name}-ssh%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-syntax_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-xmerl%{?_isa} = %{version}-%{release}
Obsoletes:           erlang-test_server
%description common_test
A portable framework for automatic testing.
%endif %{__with_wxwidgets}

%package compiler
Summary:             A byte code compiler for Erlang which produces highly compact code
Requires:            %{name}-crypto%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-hipe%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description compiler
A byte code compiler for Erlang which produces highly compact code.

%package crypto
Summary:             Cryptographical support
BuildRequires:       pkgconfig(openssl)
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description crypto
Cryptographical support.
%if %{__with_wxwidgets}

%package debugger
Summary:             A debugger for debugging and testing of Erlang programs
Requires:            %{name}-compiler%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-wx%{?_isa} = %{version}-%{release}
%description debugger
A debugger for debugging and testing of Erlang programs.
%endif %{__with_wxwidgets}
%if %{__with_wxwidgets}

%package dialyzer
Summary:             A DIscrepancy AnaLYZer for ERlang programs
Requires:            %{name}-compiler%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-hipe%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-syntax_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-wx%{?_isa} = %{version}-%{release} graphviz
Obsoletes:           erlang-typer
%description dialyzer
A DIscrepancy AnaLYZer for ERlang programs.
%endif %{__with_wxwidgets}

%package diameter
Summary:             Diameter (RFC 3588) library
BuildRequires:       ed
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-runtime_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-ssl%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-syntax_tools%{?_isa} = %{version}-%{release}
%description diameter
Diameter (RFC 3588) library
%if %{with doc}

%package doc
Summary:             Erlang documentation
BuildRequires:       fop libxslt
BuildArch:           noarch
%description doc
Documentation for Erlang.
%endif

%package edoc
Summary:             A utility used to generate documentation out of tags in source files
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-inets%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-syntax_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-xmerl%{?_isa} = %{version}-%{release}
%description edoc
A utility used to generate documentation out of tags in source files.

%package eldap
Summary:             Erlang LDAP library
Requires:            %{name}-asn1%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-ssl%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description eldap
Erlang LDAP library.

%package erl_docgen
Summary:             A utility used to generate erlang HTML documentation
Requires:            %{name}-edoc%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-xmerl%{?_isa} = %{version}-%{release}
%description erl_docgen
A utility used to generate erlang HTML documentation.

%package erl_interface
Summary:             Low level interface to C
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
%description erl_interface
Low level interface to C.

%package erts
Summary:             Functionality necessary to run the Erlang System itself
BuildRequires:       lksctp-tools-devel m4 ncurses-devel zlib-devel
Requires(pre): shadow-utils
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release} lksctp-tools
Provides:            erlang(erl_drv_version) = 3.3
Provides:            erlang(erl_nif_version) = 2.14
Provides:            bundled(pcre) = 8.33
Obsoletes:           erlang-appmon
Obsoletes:           erlang-docbuilder
Obsoletes:           erlang-gs
Obsoletes:           erlang-inviso
Obsoletes:           erlang-ose
Obsoletes:           erlang-percept < 20.2.3
Obsoletes:           erlang-pman
Obsoletes:           erlang-toolbar
Obsoletes:           erlang-tv
Obsoletes:           erlang-webtool
%description erts
Functionality necessary to run the Erlang System itself.
%if %{__with_wxwidgets}

%package et
Summary:             An event tracer for Erlang programs
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-runtime_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-wx%{?_isa} = %{version}-%{release}
%description et
An event tracer for Erlang programs.
%endif %{__with_wxwidgets}

%package eunit
Summary:             Support for unit testing
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description eunit
Support for unit testing.
%if %{__with_examples}

%package examples
Summary:             Examples for some Erlang modules
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-public_key%{?_isa} = %{version}-%{release}
Requires:            %{name}-sasl%{?_isa} = %{version}-%{release}
Requires:            %{name}-ssl%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description examples
Examples for some Erlang modules.
%endif %{__with_examples}

%package ftp
Summary:             FTP client
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description ftp
FTP client.

%package hipe
Summary:             High Performance Erlang
Requires:            %{name}-compiler%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-syntax_tools%{?_isa} = %{version}-%{release}
%description hipe
High Performance Erlang.

%package inets
Summary:             A set of services such as a Web server and a HTTP client etc
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-mnesia%{?_isa} = %{version}-%{release}
Requires:            %{name}-runtime_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-ssl%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description inets
A set of services such as a Web server and a HTTP client etc.
%if %{__with_java}

%package jinterface
Summary:             A library for accessing Java from Erlang
BuildRequires:       java-devel
Requires:            javapackages-tools %{name}-erts%{?_isa} = %{version}-%{release}
%description jinterface
Low level interface to Java.
%endif %{__with_java}

%package kernel
Summary:             Main erlang library
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description kernel
Main erlang library.
%if %{__with_wxwidgets}

%package megaco
Summary:             Megaco/H.248 support library
Requires:            %{name}-asn1%{?_isa} = %{version}-%{release}
Requires:            %{name}-debugger%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-et%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-runtime_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description megaco
Megaco/H.248 is a protocol for control of elements in a physically
decomposed multimedia gateway, enabling separation of call control
from media conversion.
%endif %{__with_wxwidgets}

%package mnesia
Summary:             A heavy duty real-time distributed database
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description mnesia
A heavy duty real-time distributed database.
%if %{__with_wxwidgets}

%package observer
Summary:             A set of tools for tracing and investigation of distributed systems
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-et%{?_isa} = %{version}-%{release}
Requires:            %{name}-inets%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-runtime_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-wx%{?_isa} = %{version}-%{release}
%description observer
A set of tools for tracing and investigation of distributed systems.
%endif %{__with_wxwidgets}

%package odbc
Summary:             A library for unixODBC support in Erlang
BuildRequires:       unixODBC-devel
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description odbc
An interface to relational SQL-databases built on ODBC (Open Database
Connectivity).

%package os_mon
Summary:             A monitor which allows inspection of the underlying operating system
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-mnesia%{?_isa} = %{version}-%{release}
Requires:            %{name}-otp_mibs%{?_isa} = %{version}-%{release}
Requires:            %{name}-sasl%{?_isa} = %{version}-%{release}
Requires:            %{name}-snmp%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description os_mon
A monitor which allows inspection of the underlying operating system.

%package otp_mibs
Summary:             SNMP management information base for Erlang/OTP nodes
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-mnesia%{?_isa} = %{version}-%{release}
Requires:            %{name}-snmp%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description otp_mibs
SNMP management information base for Erlang/OTP nodes.

%package parsetools
Summary:             A set of parsing and lexical analysis tools
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description parsetools
A set of parsing and lexical analysis tools.

%package public_key
Summary:             API to public key infrastructure
Requires:            %{name}-asn1%{?_isa} = %{version}-%{release}
Requires:            %{name}-crypto%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description public_key
API to public key infrastructure.
%if %{__with_wxwidgets}

%package reltool
Summary:             A release management tool
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-sasl%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-wx%{?_isa} = %{version}-%{release}
%description reltool
Reltool is a release management tool. It analyses a given
Erlang/OTP installation and determines various dependencies
between applications. The graphical frontend depicts the
dependencies and enables interactive customization of a
target system. The backend provides a batch interface
for generation of customized target systems.
%endif %{__with_wxwidgets}

%package runtime_tools
Summary:             A set of tools to include in a production system
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-mnesia%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description runtime_tools
A set of tools to include in a production system.

%package sasl
Summary:             The System Architecture Support Libraries
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
Requires:            %{name}-tools%{?_isa} = %{version}-%{release}
%description sasl
The System Architecture Support Libraries is a set of tools for
release upgrades and alarm handling etc.

%package snmp
Summary:             Simple Network Management Protocol (SNMP) support
Requires:            %{name}-crypto%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-mnesia%{?_isa} = %{version}-%{release}
Requires:            %{name}-runtime_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description snmp
Simple Network Management Protocol (SNMP) support including a
MIB compiler and tools for creating SNMP agents.

%package ssh
Summary:             Secure Shell application with sftp and ssh support
Requires:            %{name}-crypto%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-public_key%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description ssh
Secure Shell application with sftp and ssh support.

%package ssl
Summary:             Secure Socket Layer support
Requires:            %{name}-crypto%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-inets%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-public_key%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description ssl
Secure Socket Layer support.

%package stdlib
Summary:             The Erlang standard libraries
Requires:            %{name}-compiler%{?_isa} = %{version}-%{release}
Requires:            %{name}-crypto%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
%description stdlib
The Erlang standard libraries.

%package syntax_tools
Summary:             A set of tools for dealing with erlang sources
Requires:            %{name}-compiler%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description syntax_tools
A utility used to handle abstract Erlang syntax trees,
reading source files differently, pretty-printing syntax trees.

%package tftp
Summary:             TFTP client
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description tftp
TFTP client.

%package tools
Summary:             A set of programming tools including a coverage analyzer etc
%if %{__with_emacs}
BuildRequires:       emacs emacs-el
%endif %{__with_emacs}
%if %{__with_xemacs}
BuildRequires:       xemacs xemacs-packages-extra-el
%endif %{__with_xemacs}
Requires:            %{name}-compiler%{?_isa} = %{version}-%{release}
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-inets%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-runtime_tools%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%if %{__with_emacs}
Requires:            emacs-filesystem
Obsoletes:           emacs-erlang
Obsoletes:           emacs-erlang-el
%endif %{__with_emacs}
%if %{__with_xemacs}
Requires:            xemacs-filesystem
Obsoletes:           xemacs-erlang
Obsoletes:           xemacs-erlang-el
%endif %{__with_xemacs}
%description tools
A set of programming tools including a coverage analyzer etc.
%if %{__with_wxwidgets}

%package wx
Summary:             A library for wxWidgets support in Erlang
BuildRequires:       wxGTK3-devel
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release} mesa-libGL mesa-libGLU
%description wx
A Graphics System used to write platform independent user interfaces.
%endif %{__with_wxwidgets}

%package xmerl
Summary:             Provides support for XML 1.0
Requires:            %{name}-erts%{?_isa} = %{version}-%{release}
Requires:            %{name}-kernel%{?_isa} = %{version}-%{release}
Requires:            %{name}-stdlib%{?_isa} = %{version}-%{release}
%description xmerl
Provides support for XML 1.0.

%prep
%autosetup -p1 -n otp-OTP-%{version}
./otp_build autoconf

%build
%ifarch sparcv9 sparc64
ERL_FLAGS="${RPM_OPT_FLAGS} -mcpu=ultrasparc -fno-strict-aliasing"
%else
ERL_FLAGS="${RPM_OPT_FLAGS} -fno-strict-aliasing"
%endif
CFLAGS="${ERL_FLAGS}" CXXFLAGS="${ERL_FLAGS}" %configure --enable-shared-zlib --enable-sctp --enable-systemd --disable-silent-rules \
    %{?__with_hipe:--enable-hipe} \
%if %{__with_java}
    \
%else
    --without-jinterface \
%endif %{__with_java}
%if %{__with_wxwidgets}
    --with-wx-config=/usr/bin/wx-config-3.0
%else
    --without-common_test \
    --without-debugger \
    --without-dialyzer \
    --without-et \
    --without-megaco \
    --without-observer \
    --without-reltool \
    --without-wx
%endif %{__with_wxwidgets}
make clean
%if %{__with_emacs}
erlang_tools_vsn="$(sed -n 's/TOOLS_VSN = //p' lib/tools/vsn.mk)"
cat > emacs-erlang-init.el << EOF
(setq load-path (cons "%{_emacs_sitelispdir}/erlang" load-path))
(setq erlang-root-dir "%{_libdir}/erlang")
(setq exec-path (cons "%{_libdir}/erlang/bin" exec-path))
(require 'erlang-start)
EOF
mkdir emacs-erlang
cp lib/tools/emacs/*.el emacs-erlang/
pushd emacs-erlang
%{_emacs_bytecompile} *.el
popd
%endif %{__with_emacs}
%if %{__with_xemacs}
cat > xemacs-erlang-init.el << EOF
(setq load-path (cons "%{_xemacs_sitelispdir}/erlang" load-path))
(setq erlang-root-dir "%{_libdir}/erlang")
(setq exec-path (cons "%{_libdir}/erlang/bin" exec-path))
(require 'erlang-start)
EOF
mkdir xemacs-erlang
cp lib/tools/emacs/*.el xemacs-erlang/
rm -f xemacs-erlang/erlang-flymake.el xemacs-erlang/erlang-test.el xemacs-erlang/erldoc.el xemacs-erlang/erlang-edoc.el
pushd xemacs-erlang
%{_xemacs_bytecompile} *.el
popd
%endif %{__with_xemacs}
make %{?_smp_mflags}
%if %{with doc}
%ifnarch ppc %{power64}
export BASE_OPTIONS=-Xmx1024m
%else
export BASE_OPTIONS=-Xmx1536m
%endif
make %{?_smp_mflags} docs
%endif

%install
%if %{__with_emacs}
erlang_tools_vsn="$(sed -n 's/TOOLS_VSN = //p' lib/tools/vsn.mk)"
install -m 0755 -d "$RPM_BUILD_ROOT%{_emacs_sitestartdir}"
install -m 0755 -d "$RPM_BUILD_ROOT%{_emacs_sitelispdir}/erlang"
install -m 0644 emacs-erlang-init.el "$RPM_BUILD_ROOT%{_emacs_sitestartdir}/erlang-init.el"
for f in lib/tools/emacs/{README,*.el}; do
    b="$(basename "$f")";
    ln -s "%{_libdir}/erlang/lib/tools-${erlang_tools_vsn}/emacs/$b" \
        "$RPM_BUILD_ROOT%{_emacs_sitelispdir}/erlang/"
done
install -m 0644 emacs-erlang/*.elc "$RPM_BUILD_ROOT%{_emacs_sitelispdir}/erlang/"
%endif %{__with_emacs}
%if %{__with_xemacs}
install -m 0755 -d "$RPM_BUILD_ROOT%{_xemacs_sitestartdir}"
install -m 0755 -d "$RPM_BUILD_ROOT%{_xemacs_sitelispdir}/erlang"
install -m 0644 xemacs-erlang-init.el "$RPM_BUILD_ROOT%{_xemacs_sitestartdir}/erlang-init.el"
for f in lib/tools/emacs/{README,*.el}; do
    b="$(basename "$f")";
    ln -s "%{_libdir}/erlang/lib/tools-${erlang_tools_vsn}/emacs/$b" \
        "$RPM_BUILD_ROOT%{_xemacs_sitelispdir}/erlang/"
done
rm -f "$RPM_BUILD_ROOT%{_xemacs_sitelispdir}/erlang/erlang-flymake.el"
install -m 0644 xemacs-erlang/*.elc "$RPM_BUILD_ROOT%{_xemacs_sitelispdir}/erlang/"
%endif %{__with_xemacs}
make DESTDIR=$RPM_BUILD_ROOT install
%if %{with doc}
env ERL_LIBS="$RPM_BUILD_ROOT%{_libdir}/erlang/lib" make DESTDIR=$RPM_BUILD_ROOT install-docs
%endif
find $RPM_BUILD_ROOT%{_libdir}/erlang -type f -name info -exec rm -f {} \;
%if %{__with_examples}
find $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ssl-*/examples/ -type d -perm 0775 -print -exec chmod 755 {} \;
find $RPM_BUILD_ROOT%{_libdir}/erlang/lib/kernel-*/examples/uds_dist -type d -perm 0775 -print -exec chmod 755 {} \;
%else
find $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ -mindepth 1 -maxdepth 2 -type d -name examples -exec rm -rf {} \;
%endif %{__with_examples}
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/erlang/bin
%if %{with doc}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/lib
pushd .
cd $RPM_BUILD_ROOT%{_libdir}/erlang
mv -v doc $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
for i in erts-* ; do mv -v $i/doc $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$i ; done
cd $RPM_BUILD_ROOT%{_libdir}/erlang/lib
for i in * ; do mv -v $i/doc $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/lib/$i || true ; done
popd
cp -av AUTHORS LICENSE.txt README.md $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
mv -v $RPM_BUILD_ROOT%{_libdir}/erlang/PR.template $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
mv -v $RPM_BUILD_ROOT%{_libdir}/erlang/COPYRIGHT $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/README.md
%endif
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/man/man1/erlsrv.*
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/man/man1/werl.*
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/man/man3/win32reg.*
rm -r $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/man
%if %{with doc}
for manpage in $RPM_BUILD_ROOT%{_libdir}/erlang/man/man3/*
do
    mv ${manpage} ${manpage}erl
done
mkdir -p $RPM_BUILD_ROOT%{_mandir}/
mv $RPM_BUILD_ROOT%{_libdir}/erlang/man/* $RPM_BUILD_ROOT%{_mandir}/
%endif
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/Install
for exe in $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/bin/*
do
    base="$(basename "$exe")"
    next="$RPM_BUILD_ROOT%{_libdir}/erlang/bin/${base}"
    rel="$(echo "$exe" | sed "s,^$RPM_BUILD_ROOT%{_libdir}/erlang/,../,")"
    if cmp "$exe" "$next"; then
        ln -sf "$rel" "$next"
    fi
done
for exe in $RPM_BUILD_ROOT%{_libdir}/erlang/bin/*
do
    base="$(basename "$exe")"
    next="$RPM_BUILD_ROOT%{_bindir}/${base}"
    rel="$(echo "$exe" | sed "s,^$RPM_BUILD_ROOT,,")"
    if cmp "$exe" "$next"; then
        ln -sf "$rel" "$next"
    fi
done
%if %{__with_java}
install -m 0755 -d "$RPM_BUILD_ROOT%{_javadir}/%{name}"
jinterface_lib_dir="$(ls -d1 $RPM_BUILD_ROOT%{_libdir}/erlang/lib/jinterface-*/ | sed "s,^$RPM_BUILD_ROOT,,")"
test -d "$RPM_BUILD_ROOT$jinterface_lib_dir"
ln -s "${jinterface_lib_dir}priv/OtpErlang.jar" "$RPM_BUILD_ROOT%{_javadir}/%{name}/"
%endif %{__with_java}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/epmd.service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/epmd.socket
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/epmd@.service
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/epmd@.socket
%if %{__with_wxwidgets}
echo "No need to fix additional scripts"
%else
echo "Removing scripts which won't work w/o wxWidgets anyway"
for exe in ct_run dialyzer typer
do
    rm -f $RPM_BUILD_ROOT/%{_bindir}/${exe}
    rm -f $RPM_BUILD_ROOT/%{_libdir}/erlang/bin/${exe}
    rm -f $RPM_BUILD_ROOT/%{_libdir}/erlang/erts-*/bin/${exe}
done
%endif %{__with_wxwidgets}
install -d -p -m 0755 %{buildroot}%{_datadir}/erlang/
install -d -p -m 0755 %{buildroot}%{_datadir}/erlang/lib

%check
TARGET="$(make target_configured)"
ERL_TOP="$(pwd)"
ERL_TOP=${ERL_TOP} make TARGET=${TARGET} release_tests

%pre erts
getent group epmd >/dev/null || groupadd -r epmd
getent passwd epmd >/dev/null || \
useradd -r -g epmd -d /dev/null -s /sbin/nologin \
-c "Erlang Port Mapper Daemon" epmd 2>/dev/null || :

%files
%if %{with doc}
%dir %{_docdir}/%{name}-%{version}/
%doc %{_docdir}/%{name}-%{version}/AUTHORS
%doc %{_docdir}/%{name}-%{version}/COPYRIGHT
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%doc %{_docdir}/%{name}-%{version}/PR.template
%doc %{_docdir}/%{name}-%{version}/README.md
%endif

%files asn1
%dir %{_libdir}/erlang/lib/asn1-*/
%{_libdir}/erlang/lib/asn1-*/ebin
%{_libdir}/erlang/lib/asn1-*/priv
%{_libdir}/erlang/lib/asn1-*/src
%if %{with doc}
%{_mandir}/man3/asn1ct.*
%endif
%if %{__with_wxwidgets}

%files common_test
%{_bindir}/ct_run
%{_libdir}/erlang/bin/ct_run
%{_libdir}/erlang/erts-*/bin/ct_run
%{_libdir}/erlang/lib/common_test-*/
%if %{with doc}
%{_mandir}/man1/ct_run.*
%{_mandir}/man3/ct.*
%{_mandir}/man3/ct_cover.*
%{_mandir}/man3/ct_ftp.*
%{_mandir}/man3/ct_hooks.*
%{_mandir}/man3/ct_master.*
%{_mandir}/man3/ct_netconfc.*
%{_mandir}/man3/ct_property_test.*
%{_mandir}/man3/ct_rpc.*
%{_mandir}/man3/ct_slave.*
%{_mandir}/man3/ct_snmp.*
%{_mandir}/man3/ct_ssh.*
%{_mandir}/man3/ct_telnet.*
%{_mandir}/man3/ct_testspec.*
%{_mandir}/man3/unix_telnet.*
%{_mandir}/man6/common_test.*
%endif
%endif %{__with_wxwidgets}

%files compiler
%{_libdir}/erlang/lib/compiler-*/
%if %{with doc}
%{_mandir}/man3/compile.*
%endif

%files crypto
%{_libdir}/erlang/lib/crypto-*/
%if %{with doc}
%{_mandir}/man3/crypto.*
%{_mandir}/man6/crypto.*
%endif
%if %{__with_wxwidgets}

%files debugger
%{_libdir}/erlang/lib/debugger-*/
%if %{with doc}
%{_mandir}/man3/debugger.*
%{_mandir}/man3/i.*
%{_mandir}/man3/int.*
%endif
%endif %{__with_wxwidgets}
%if %{__with_wxwidgets}

%files dialyzer
%{_bindir}/dialyzer
%{_bindir}/typer
%{_libdir}/erlang/bin/dialyzer
%{_libdir}/erlang/bin/typer
%{_libdir}/erlang/erts-*/bin/dialyzer
%{_libdir}/erlang/erts-*/bin/typer
%{_libdir}/erlang/lib/dialyzer-*/
%if %{with doc}
%{_mandir}/man3/dialyzer.*
%{_mandir}/man3/typer.*
%endif
%endif %{__with_wxwidgets}

%files diameter
%dir %{_libdir}/erlang/lib/diameter-*/
%{_libdir}/erlang/lib/diameter-*/bin
%{_libdir}/erlang/lib/diameter-*/ebin
%{_libdir}/erlang/lib/diameter-*/include
%{_libdir}/erlang/lib/diameter-*/src
%if %{with doc}
%{_mandir}/man1/diameterc.*
%{_mandir}/man3/diameter.*
%{_mandir}/man3/diameter_app.*
%{_mandir}/man3/diameter_codec.*
%{_mandir}/man3/diameter_make.*
%{_mandir}/man3/diameter_sctp.*
%{_mandir}/man3/diameter_tcp.*
%{_mandir}/man3/diameter_transport.*
%{_mandir}/man4/diameter_dict.*
%endif
%if %{with doc}

%files doc
%doc %{_docdir}/%{name}-%{version}/doc
%doc %{_docdir}/%{name}-%{version}/erts-*/
%doc %{_docdir}/%{name}-%{version}/lib/
%endif

%files edoc
%{_libdir}/erlang/lib/edoc-*/
%if %{with doc}
%{_mandir}/man3/edoc.*
%{_mandir}/man3/edoc_doclet.*
%{_mandir}/man3/edoc_extract.*
%{_mandir}/man3/edoc_layout.*
%{_mandir}/man3/edoc_lib.*
%{_mandir}/man3/edoc_run.*
%endif

%files eldap
%{_libdir}/erlang/lib/eldap-*/
%if %{with doc}
%{_mandir}/man3/eldap.*
%endif

%files erl_docgen
%{_libdir}/erlang/lib/erl_docgen-*/
%if %{with doc}
%{_mandir}/man6/erl_docgen.*
%endif

%files erl_interface
%{_libdir}/erlang/lib/erl_interface-*/
%if %{with doc}
%{_mandir}/man1/erl_call.*
%{_mandir}/man3/ei.*
%{_mandir}/man3/ei_connect.*
%{_mandir}/man3/erl_connect.*
%{_mandir}/man3/erl_error.*
%{_mandir}/man3/erl_eterm.*
%{_mandir}/man3/erl_format.*
%{_mandir}/man3/erl_global.*
%{_mandir}/man3/erl_malloc.*
%{_mandir}/man3/erl_marshal.*
%{_mandir}/man3/registry.*
%endif

%files erts
%dir %{_datadir}/erlang/
%dir %{_datadir}/erlang/lib/
%dir %{_libdir}/erlang/
%dir %{_libdir}/erlang/bin/
%dir %{_libdir}/erlang/lib/
%dir %{_libdir}/erlang/releases/
%{_bindir}/epmd
%{_bindir}/erl
%{_bindir}/erlc
%{_bindir}/escript
%{_bindir}/run_erl
%{_bindir}/to_erl
%{_libdir}/erlang/bin/epmd
%{_libdir}/erlang/bin/erl
%{_libdir}/erlang/bin/erlc
%{_libdir}/erlang/bin/escript
%{_libdir}/erlang/bin/no_dot_erlang.boot
%{_libdir}/erlang/bin/run_erl
%{_libdir}/erlang/bin/start
%{_libdir}/erlang/bin/start.boot
%{_libdir}/erlang/bin/start.script
%{_libdir}/erlang/bin/start_clean.boot
%{_libdir}/erlang/bin/start_erl
%{_libdir}/erlang/bin/start_sasl.boot
%{_libdir}/erlang/bin/to_erl
%dir %{_libdir}/erlang/erts-*/
%dir %{_libdir}/erlang/erts-*/bin/
%{_libdir}/erlang/erts-*/bin/beam.smp
%{_libdir}/erlang/erts-*/bin/dyn_erl
%{_libdir}/erlang/erts-*/bin/epmd
%{_libdir}/erlang/erts-*/bin/erl
%{_libdir}/erlang/erts-*/bin/erl.src
%{_libdir}/erlang/erts-*/bin/erl_child_setup
%{_libdir}/erlang/erts-*/bin/erlc
%{_libdir}/erlang/erts-*/bin/erlexec
%{_libdir}/erlang/erts-*/bin/escript
%{_libdir}/erlang/erts-*/bin/heart
%{_libdir}/erlang/erts-*/bin/inet_gethost
%{_libdir}/erlang/erts-*/bin/run_erl
%{_libdir}/erlang/erts-*/bin/start
%{_libdir}/erlang/erts-*/bin/start.src
%{_libdir}/erlang/erts-*/bin/start_erl.src
%{_libdir}/erlang/erts-*/bin/to_erl
%{_libdir}/erlang/erts-*/include
%{_libdir}/erlang/erts-*/lib/
%{_libdir}/erlang/erts-*/src/
%{_libdir}/erlang/lib/erts-*/
%if %{with doc}
%{_mandir}/man1/epmd.*
%{_mandir}/man1/erl.*
%{_mandir}/man1/erlc.*
%{_mandir}/man1/escript.*
%{_mandir}/man1/run_erl.*
%{_mandir}/man1/start.*
%{_mandir}/man1/start_erl.*
%{_mandir}/man3/atomics.*
%{_mandir}/man3/counters.*
%{_mandir}/man3/driver_entry.*
%{_mandir}/man3/erl_driver.*
%{_mandir}/man3/erl_nif.*
%{_mandir}/man3/erl_prim_loader.*
%{_mandir}/man3/erl_tracer.*
%{_mandir}/man3/erlang.*
%{_mandir}/man3/erts_alloc.*
%{_mandir}/man3/init.*
%{_mandir}/man3/persistent_term.*
%{_mandir}/man3/scheduler.*
%{_mandir}/man3/zlib.*
%endif
%{_libdir}/erlang/releases/*
%{_libdir}/erlang/usr/
%{_unitdir}/epmd.service
%{_unitdir}/epmd.socket
%{_unitdir}/epmd@.service
%{_unitdir}/epmd@.socket
%if %{__with_wxwidgets}

%files et
%dir %{_libdir}/erlang/lib/et-*/
%{_libdir}/erlang/lib/et-*/ebin
%{_libdir}/erlang/lib/et-*/include
%{_libdir}/erlang/lib/et-*/src
%if %{with doc}
%{_mandir}/man3/et.*
%{_mandir}/man3/et_collector.*
%{_mandir}/man3/et_selector.*
%{_mandir}/man3/et_viewer.*
%endif
%endif %{__with_wxwidgets}

%files eunit
%dir %{_libdir}/erlang/lib/eunit-*/
%{_libdir}/erlang/lib/eunit-*/ebin
%{_libdir}/erlang/lib/eunit-*/include
%{_libdir}/erlang/lib/eunit-*/src
%if %{with doc}
%{_mandir}/man3/eunit.*
%{_mandir}/man3/eunit_surefire.*
%endif
%if %{__with_examples}

%files examples
%{_libdir}/erlang/lib/asn1-*/examples/
%{_libdir}/erlang/lib/diameter-*/examples/
%if %{__with_wxwidgets}
%{_libdir}/erlang/lib/et-*/examples/
%endif %{__with_wxwidgets}
%{_libdir}/erlang/lib/eunit-*/examples/
%{_libdir}/erlang/lib/inets-*/examples/
%{_libdir}/erlang/lib/kernel-*/examples/
%{_libdir}/erlang/lib/megaco-*/examples/
%{_libdir}/erlang/lib/mnesia-*/examples/
%if %{__with_wxwidgets}
%{_libdir}/erlang/lib/observer-*/examples/
%endif %{__with_wxwidgets}
%if %{__with_wxwidgets}
%{_libdir}/erlang/lib/reltool-*/examples/
%endif %{__with_wxwidgets}
%{_libdir}/erlang/lib/runtime_tools-*/examples/
%{_libdir}/erlang/lib/sasl-*/examples/
%{_libdir}/erlang/lib/snmp-*/examples/
%{_libdir}/erlang/lib/ssl-*/examples/
%{_libdir}/erlang/lib/stdlib-*/examples/
%{_libdir}/erlang/lib/syntax_tools-*/examples/
%{_libdir}/erlang/lib/tools-*/examples/
%if %{__with_wxwidgets}
%{_libdir}/erlang/lib/wx-*/examples/
%endif %{__with_wxwidgets}
%endif %{__with_examples}

%files ftp
%dir %{_libdir}/erlang/lib/ftp-*/
%{_libdir}/erlang/lib/ftp-*/ebin
%{_libdir}/erlang/lib/ftp-*/src
%if %{with doc}
%{_mandir}/man3/ftp.*
%endif

%files hipe
%{_libdir}/erlang/lib/hipe-*/

%files inets
%dir %{_libdir}/erlang/lib/inets-*/
%{_libdir}/erlang/lib/inets-*/ebin
%{_libdir}/erlang/lib/inets-*/include
%{_libdir}/erlang/lib/inets-*/priv
%{_libdir}/erlang/lib/inets-*/src
%if %{with doc}
%{_mandir}/man3/ftp.*
%{_mandir}/man3/http_uri.*
%{_mandir}/man3/httpc.*
%{_mandir}/man3/httpd.*
%{_mandir}/man3/httpd_custom_api.*
%{_mandir}/man3/httpd_socket.*
%{_mandir}/man3/httpd_util.*
%{_mandir}/man3/inets.*
%{_mandir}/man3/mod_alias.*
%{_mandir}/man3/mod_auth.*
%{_mandir}/man3/mod_esi.*
%{_mandir}/man3/mod_security.*
%{_mandir}/man3/tftp.*
%endif
%if %{__with_java}

%files jinterface
%dir %{_javadir}/%{name}/
%{_javadir}/%{name}/OtpErlang.jar
%{_libdir}/erlang/lib/jinterface-*/
%endif %{__with_java}

%files kernel
%dir %{_libdir}/erlang/lib/kernel-*/
%{_libdir}/erlang/lib/kernel-*/ebin
%{_libdir}/erlang/lib/kernel-*/include
%{_libdir}/erlang/lib/kernel-*/src
%if %{with doc}
%{_mandir}/man3/application.*
%{_mandir}/man3/auth.*
%{_mandir}/man3/code.*
%{_mandir}/man3/disk_log.*
%{_mandir}/man3/erl_boot_server.*
%{_mandir}/man3/erl_ddll.*
%{_mandir}/man3/erl_epmd.*
%{_mandir}/man3/erl_prim_loader_stub.*
%{_mandir}/man3/erlang_stub.*
%{_mandir}/man3/error_handler.*
%{_mandir}/man3/error_logger.*
%{_mandir}/man3/file.*
%{_mandir}/man3/gen_sctp.*
%{_mandir}/man3/gen_tcp.*
%{_mandir}/man3/gen_udp.*
%{_mandir}/man3/global.*
%{_mandir}/man3/global_group.*
%{_mandir}/man3/heart.*
%{_mandir}/man3/inet.*
%{_mandir}/man3/inet_res.*
%{_mandir}/man3/init_stub.*
%{_mandir}/man3/logger.*
%{_mandir}/man3/logger_disk_log_h.*
%{_mandir}/man3/logger_filters.*
%{_mandir}/man3/logger_formatter.*
%{_mandir}/man3/logger_std_h.*
%{_mandir}/man3/net_adm.*
%{_mandir}/man3/net_kernel.*
%{_mandir}/man3/os.*
%{_mandir}/man3/pg2.*
%{_mandir}/man3/rpc.*
%{_mandir}/man3/seq_trace.*
%{_mandir}/man3/user.*
%{_mandir}/man3/wrap_log_reader.*
%{_mandir}/man3/zlib_stub.*
%{_mandir}/man4/app.*
%{_mandir}/man4/config.*
%{_mandir}/man6/kernel.*
%endif
%if %{__with_wxwidgets}

%files megaco
%dir %{_libdir}/erlang/lib/megaco-*/
%{_libdir}/erlang/lib/megaco-*/ebin
%{_libdir}/erlang/lib/megaco-*/include
%{_libdir}/erlang/lib/megaco-*/priv
%{_libdir}/erlang/lib/megaco-*/src
%if %{with doc}
%{_mandir}/man3/megaco.*
%{_mandir}/man3/megaco_codec_meas.*
%{_mandir}/man3/megaco_codec_mstone1.*
%{_mandir}/man3/megaco_codec_mstone2.*
%{_mandir}/man3/megaco_codec_transform.*
%{_mandir}/man3/megaco_edist_compress.*
%{_mandir}/man3/megaco_encoder.*
%{_mandir}/man3/megaco_flex_scanner.*
%{_mandir}/man3/megaco_tcp.*
%{_mandir}/man3/megaco_transport.*
%{_mandir}/man3/megaco_udp.*
%{_mandir}/man3/megaco_user.*
%endif
%endif %{__with_wxwidgets}

%files mnesia
%dir %{_libdir}/erlang/lib/mnesia-*/
%{_libdir}/erlang/lib/mnesia-*/ebin
%{_libdir}/erlang/lib/mnesia-*/src
%if %{with doc}
%{_mandir}/man3/mnesia.*
%{_mandir}/man3/mnesia_frag_hash.*
%{_mandir}/man3/mnesia_registry.*
%endif
%if %{__with_wxwidgets}

%files observer
%dir %{_libdir}/erlang/lib/observer-*/
%{_libdir}/erlang/lib/observer-*/ebin/
%{_libdir}/erlang/lib/observer-*/include/
%{_libdir}/erlang/lib/observer-*/priv/
%{_libdir}/erlang/lib/observer-*/src/
%if %{with doc}
%{_mandir}/man1/cdv.*
%{_mandir}/man3/crashdump.*
%{_mandir}/man3/etop.*
%{_mandir}/man3/observer.*
%{_mandir}/man3/ttb.*
%{_mandir}/man6/observer.*
%endif
%endif %{__with_wxwidgets}

%files odbc
%{_libdir}/erlang/lib/odbc-*/
%if %{with doc}
%{_mandir}/man3/odbc.*
%endif

%files os_mon
%{_libdir}/erlang/lib/os_mon-*/
%if %{with doc}
%{_mandir}/man3/cpu_sup.*
%{_mandir}/man3/disksup.*
%{_mandir}/man3/memsup.*
%{_mandir}/man3/os_mon_mib.*
%{_mandir}/man3/os_sup.*
%{_mandir}/man6/os_mon.*
%endif

%files otp_mibs
%{_libdir}/erlang/lib/otp_mibs-*/
%if %{with doc}
%{_mandir}/man3/otp_mib.*
%endif

%files parsetools
%{_libdir}/erlang/lib/parsetools-*/
%if %{with doc}
%{_mandir}/man3/leex.*
%{_mandir}/man3/yecc.*
%endif

%files public_key
%{_libdir}/erlang/lib/public_key-*/
%if %{with doc}
%{_mandir}/man3/public_key.*
%{_mandir}/man6/public_key.*
%endif
%if %{__with_wxwidgets}

%files reltool
%dir %{_libdir}/erlang/lib/reltool-*/
%{_libdir}/erlang/lib/reltool-*/ebin
%{_libdir}/erlang/lib/reltool-*/src
%if %{with doc}
%{_mandir}/man3/reltool.*
%endif
%endif %{__with_wxwidgets}

%files runtime_tools
%dir %{_libdir}/erlang/lib/runtime_tools-*/
%{_libdir}/erlang/lib/runtime_tools-*/ebin/
%{_libdir}/erlang/lib/runtime_tools-*/include/
%{_libdir}/erlang/lib/runtime_tools-*/priv/
%if %{with doc}
%{_mandir}/man3/dbg.*
%{_mandir}/man3/dyntrace.*
%{_mandir}/man3/erts_alloc_config.*
%{_mandir}/man3/msacc.*
%{_mandir}/man3/system_information.*
%{_mandir}/man6/runtime_tools.*
%endif

%files sasl
%dir %{_libdir}/erlang/lib/sasl-*/
%{_libdir}/erlang/lib/sasl-*/ebin
%{_libdir}/erlang/lib/sasl-*/src
%if %{with doc}
%{_mandir}/man3/alarm_handler.*
%{_mandir}/man3/rb.*
%{_mandir}/man3/release_handler.*
%{_mandir}/man3/systools.*
%{_mandir}/man4/appup.*
%{_mandir}/man4/rel.*
%{_mandir}/man4/relup.*
%{_mandir}/man4/script.*
%{_mandir}/man6/sasl.*
%endif

%files snmp
%dir %{_libdir}/erlang/lib/snmp-*/
%{_libdir}/erlang/lib/snmp-*/bin
%{_libdir}/erlang/lib/snmp-*/ebin
%{_libdir}/erlang/lib/snmp-*/include
%{_libdir}/erlang/lib/snmp-*/mibs
%{_libdir}/erlang/lib/snmp-*/priv
%{_libdir}/erlang/lib/snmp-*/src
%if %{with doc}
%{_mandir}/man1/snmpc.*
%{_mandir}/man3/snmp.*
%{_mandir}/man3/snmpa.*
%{_mandir}/man3/snmpa_conf.*
%{_mandir}/man3/snmpa_discovery_handler.*
%{_mandir}/man3/snmpa_error.*
%{_mandir}/man3/snmpa_error_io.*
%{_mandir}/man3/snmpa_error_logger.*
%{_mandir}/man3/snmpa_error_report.*
%{_mandir}/man3/snmpa_local_db.*
%{_mandir}/man3/snmpa_mib_data.*
%{_mandir}/man3/snmpa_mib_storage.*
%{_mandir}/man3/snmpa_mpd.*
%{_mandir}/man3/snmpa_network_interface.*
%{_mandir}/man3/snmpa_network_interface_filter.*
%{_mandir}/man3/snmpa_notification_delivery_info_receiver.*
%{_mandir}/man3/snmpa_notification_filter.*
%{_mandir}/man3/snmpa_supervisor.*
%{_mandir}/man3/snmpc.*
%{_mandir}/man3/snmp_community_mib.*
%{_mandir}/man3/snmp_framework_mib.*
%{_mandir}/man3/snmp_generic.*
%{_mandir}/man3/snmp_index.*
%{_mandir}/man3/snmpm.*
%{_mandir}/man3/snmpm_conf.*
%{_mandir}/man3/snmpm_mpd.*
%{_mandir}/man3/snmpm_network_interface.*
%{_mandir}/man3/snmpm_network_interface_filter.*
%{_mandir}/man3/snmpm_user.*
%{_mandir}/man3/snmp_notification_mib.*
%{_mandir}/man3/snmp_pdus.*
%{_mandir}/man3/snmp_standard_mib.*
%{_mandir}/man3/snmp_target_mib.*
%{_mandir}/man3/snmp_user_based_sm_mib.*
%{_mandir}/man3/snmp_view_based_acm_mib.*
%{_mandir}/man6/snmp.*
%{_mandir}/man7/INET-ADDRESS-MIB.*
%{_mandir}/man7/OTP-SNMPEA-MIB.*
%{_mandir}/man7/RFC1213-MIB.*
%{_mandir}/man7/SNMP-COMMUNITY-MIB.*
%{_mandir}/man7/SNMP-FRAMEWORK-MIB.*
%{_mandir}/man7/SNMP-MPD-MIB.*
%{_mandir}/man7/SNMP-NOTIFICATION-MIB.*
%{_mandir}/man7/SNMP-TARGET-MIB.*
%{_mandir}/man7/SNMP-USER-BASED-SM-MIB.*
%{_mandir}/man7/SNMP-USM-AES-MIB.*
%{_mandir}/man7/SNMPv2-MIB.*
%{_mandir}/man7/SNMPv2-TM.*
%{_mandir}/man7/SNMP-VIEW-BASED-ACM-MIB.*
%{_mandir}/man7/STANDARD-MIB.*
%{_mandir}/man7/TRANSPORT-ADDRESS-MIB.*
%endif

%files ssh
%dir %{_libdir}/erlang/lib/ssh-*/
%{_libdir}/erlang/lib/ssh-*/ebin
%{_libdir}/erlang/lib/ssh-*/include
%{_libdir}/erlang/lib/ssh-*/src
%if %{with doc}
%{_mandir}/man3/ssh.*
%{_mandir}/man3/ssh_client_channel.*
%{_mandir}/man3/ssh_client_key_api.*
%{_mandir}/man3/ssh_connection.*
%{_mandir}/man3/ssh_file.*
%{_mandir}/man3/ssh_server_channel.*
%{_mandir}/man3/ssh_server_key_api.*
%{_mandir}/man3/ssh_sftp.*
%{_mandir}/man3/ssh_sftpd.*
%{_mandir}/man6/ssh.*
%endif

%files ssl
%dir %{_libdir}/erlang/lib/ssl-*/
%{_libdir}/erlang/lib/ssl-*/ebin
%{_libdir}/erlang/lib/ssl-*/src
%if %{with doc}
%{_mandir}/man3/ssl.*
%{_mandir}/man3/ssl_crl_cache.*
%{_mandir}/man3/ssl_crl_cache_api.*
%{_mandir}/man3/ssl_session_cache_api.*
%{_mandir}/man6/ssl.*
%endif

%files stdlib
%dir %{_libdir}/erlang/lib/stdlib-*/
%{_libdir}/erlang/lib/stdlib-*/ebin
%{_libdir}/erlang/lib/stdlib-*/include
%{_libdir}/erlang/lib/stdlib-*/src
%if %{with doc}
%{_mandir}/man3/array.*
%{_mandir}/man3/base64.*
%{_mandir}/man3/beam_lib.*
%{_mandir}/man3/binary.*
%{_mandir}/man3/c.*
%{_mandir}/man3/calendar.*
%{_mandir}/man3/dets.*
%{_mandir}/man3/dict.*
%{_mandir}/man3/digraph.*
%{_mandir}/man3/digraph_utils.*
%{_mandir}/man3/epp.*
%{_mandir}/man3/erl_anno.*
%{_mandir}/man3/erl_eval.*
%{_mandir}/man3/erl_expand_records.*
%{_mandir}/man3/erl_id_trans.*
%{_mandir}/man3/erl_internal.*
%{_mandir}/man3/erl_lint.*
%{_mandir}/man3/erl_parse.*
%{_mandir}/man3/erl_pp.*
%{_mandir}/man3/erl_scan.*
%{_mandir}/man3/erl_tar.*
%{_mandir}/man3/ets.*
%{_mandir}/man3/file_sorter.*
%{_mandir}/man3/filelib.*
%{_mandir}/man3/filename.*
%{_mandir}/man3/gb_sets.*
%{_mandir}/man3/gb_trees.*
%{_mandir}/man3/gen_event.*
%{_mandir}/man3/gen_fsm.*
%{_mandir}/man3/gen_server.*
%{_mandir}/man3/gen_statem.*
%{_mandir}/man3/io.*
%{_mandir}/man3/io_lib.*
%{_mandir}/man3/lists.*
%{_mandir}/man3/log_mf_h.*
%{_mandir}/man3/maps.*
%{_mandir}/man3/math.*
%{_mandir}/man3/ms_transform.*
%{_mandir}/man3/orddict.*
%{_mandir}/man3/ordsets.*
%{_mandir}/man3/pool.*
%{_mandir}/man3/proc_lib.*
%{_mandir}/man3/proplists.*
%{_mandir}/man3/qlc.*
%{_mandir}/man3/queue.*
%{_mandir}/man3/rand.*
%{_mandir}/man3/random.*
%{_mandir}/man3/re.*
%{_mandir}/man3/sets.*
%{_mandir}/man3/shell.*
%{_mandir}/man3/shell_default.*
%{_mandir}/man3/slave.*
%{_mandir}/man3/sofs.*
%{_mandir}/man3/string.*
%{_mandir}/man3/supervisor.*
%{_mandir}/man3/supervisor_bridge.*
%{_mandir}/man3/sys.*
%{_mandir}/man3/timer.*
%{_mandir}/man3/unicode.*
%{_mandir}/man3/uri_string.*
%{_mandir}/man3/zip.*
%{_mandir}/man6/stdlib.*
%endif

%files syntax_tools
%dir %{_libdir}/erlang/lib/syntax_tools-*/
%{_libdir}/erlang/lib/syntax_tools-*/ebin
%{_libdir}/erlang/lib/syntax_tools-*/include
%if %{with doc}
%{_mandir}/man3/epp_dodger.*
%{_mandir}/man3/erl_comment_scan.*
%{_mandir}/man3/erl_prettypr.*
%{_mandir}/man3/erl_recomment.*
%{_mandir}/man3/erl_syntax.*
%{_mandir}/man3/erl_syntax_lib.*
%{_mandir}/man3/erl_tidy.*
%{_mandir}/man3/igor.*
%{_mandir}/man3/merl.*
%{_mandir}/man3/merl_transform.*
%{_mandir}/man3/prettypr.*
%endif

%files tftp
%dir %{_libdir}/erlang/lib/tftp-*/
%{_libdir}/erlang/lib/tftp-*/ebin
%{_libdir}/erlang/lib/tftp-*/src
%if %{with doc}
%{_mandir}/man3/tftp.*
%endif

%files tools
%dir %{_libdir}/erlang/lib/tools-*/
%{_libdir}/erlang/lib/tools-*/bin
%{_libdir}/erlang/lib/tools-*/ebin
%{_libdir}/erlang/lib/tools-*/emacs
%{_libdir}/erlang/lib/tools-*/src
%{_libdir}/erlang/lib/tools-*/priv
%if %{with doc}
%{_mandir}/man3/cover.*
%{_mandir}/man3/cprof.*
%{_mandir}/man3/eprof.*
%{_mandir}/man3/erlang_mode.*
%{_mandir}/man3/fprof.*
%{_mandir}/man3/instrument.*
%{_mandir}/man3/lcnt.*
%{_mandir}/man3/make.*
%{_mandir}/man3/tags.*
%{_mandir}/man3/xref.*
%endif
%if %{__with_emacs}
%dir %{_emacs_sitelispdir}/erlang
%doc %{_emacs_sitelispdir}/erlang/README
%{_emacs_sitelispdir}/erlang/*.el
%{_emacs_sitelispdir}/erlang/*.elc
%{_emacs_sitestartdir}/erlang-init.el
%endif %{__with_emacs}
%if %{__with_xemacs}
%dir %{_xemacs_sitelispdir}/erlang
%doc %{_xemacs_sitelispdir}/erlang/README
%{_xemacs_sitelispdir}/erlang/*.el
%{_xemacs_sitelispdir}/erlang/*.elc
%{_xemacs_sitestartdir}/erlang-init.el
%endif %{__with_xemacs}
%if %{__with_wxwidgets}

%files wx
%dir %{_libdir}/erlang/lib/wx-*/
%{_libdir}/erlang/lib/wx-*/ebin
%{_libdir}/erlang/lib/wx-*/include
%{_libdir}/erlang/lib/wx-*/priv
%{_libdir}/erlang/lib/wx-*/src
%if %{with doc}
%{_mandir}/man3/gl.*
%{_mandir}/man3/glu.*
%{_mandir}/man3/wx.*
%{_mandir}/man3/wxAcceleratorEntry.*
%{_mandir}/man3/wxAcceleratorTable.*
%{_mandir}/man3/wxActivateEvent.*
%{_mandir}/man3/wxArtProvider.*
%{_mandir}/man3/wxAuiDockArt.*
%{_mandir}/man3/wxAuiManager.*
%{_mandir}/man3/wxAuiManagerEvent.*
%{_mandir}/man3/wxAuiNotebook.*
%{_mandir}/man3/wxAuiNotebookEvent.*
%{_mandir}/man3/wxAuiPaneInfo.*
%{_mandir}/man3/wxAuiSimpleTabArt.*
%{_mandir}/man3/wxAuiTabArt.*
%{_mandir}/man3/wxBitmap.*
%{_mandir}/man3/wxBitmapButton.*
%{_mandir}/man3/wxBitmapDataObject.*
%{_mandir}/man3/wxBoxSizer.*
%{_mandir}/man3/wxBrush.*
%{_mandir}/man3/wxBufferedDC.*
%{_mandir}/man3/wxBufferedPaintDC.*
%{_mandir}/man3/wxButton.*
%{_mandir}/man3/wxCalendarCtrl.*
%{_mandir}/man3/wxCalendarDateAttr.*
%{_mandir}/man3/wxCalendarEvent.*
%{_mandir}/man3/wxCaret.*
%{_mandir}/man3/wxCheckBox.*
%{_mandir}/man3/wxCheckListBox.*
%{_mandir}/man3/wxChildFocusEvent.*
%{_mandir}/man3/wxChoice.*
%{_mandir}/man3/wxChoicebook.*
%{_mandir}/man3/wxClientDC.*
%{_mandir}/man3/wxClipboard.*
%{_mandir}/man3/wxClipboardTextEvent.*
%{_mandir}/man3/wxCloseEvent.*
%{_mandir}/man3/wxColourData.*
%{_mandir}/man3/wxColourDialog.*
%{_mandir}/man3/wxColourPickerCtrl.*
%{_mandir}/man3/wxColourPickerEvent.*
%{_mandir}/man3/wxComboBox.*
%{_mandir}/man3/wxCommandEvent.*
%{_mandir}/man3/wxContextMenuEvent.*
%{_mandir}/man3/wxControl.*
%{_mandir}/man3/wxControlWithItems.*
%{_mandir}/man3/wxCursor.*
%{_mandir}/man3/wxDC.*
%{_mandir}/man3/wxDCOverlay.*
%{_mandir}/man3/wxDataObject.*
%{_mandir}/man3/wxDateEvent.*
%{_mandir}/man3/wxDatePickerCtrl.*
%{_mandir}/man3/wxDialog.*
%{_mandir}/man3/wxDirDialog.*
%{_mandir}/man3/wxDirPickerCtrl.*
%{_mandir}/man3/wxDisplay.*
%{_mandir}/man3/wxDisplayChangedEvent.*
%{_mandir}/man3/wxDropFilesEvent.*
%{_mandir}/man3/wxEraseEvent.*
%{_mandir}/man3/wxEvent.*
%{_mandir}/man3/wxEvtHandler.*
%{_mandir}/man3/wxFileDataObject.*
%{_mandir}/man3/wxFileDialog.*
%{_mandir}/man3/wxFileDirPickerEvent.*
%{_mandir}/man3/wxFilePickerCtrl.*
%{_mandir}/man3/wxFindReplaceData.*
%{_mandir}/man3/wxFindReplaceDialog.*
%{_mandir}/man3/wxFlexGridSizer.*
%{_mandir}/man3/wxFocusEvent.*
%{_mandir}/man3/wxFont.*
%{_mandir}/man3/wxFontData.*
%{_mandir}/man3/wxFontDialog.*
%{_mandir}/man3/wxFontPickerCtrl.*
%{_mandir}/man3/wxFontPickerEvent.*
%{_mandir}/man3/wxFrame.*
%{_mandir}/man3/wxGBSizerItem.*
%{_mandir}/man3/wxGCDC.*
%{_mandir}/man3/wxGLCanvas.*
%{_mandir}/man3/wxGauge.*
%{_mandir}/man3/wxGenericDirCtrl.*
%{_mandir}/man3/wxGraphicsBrush.*
%{_mandir}/man3/wxGraphicsContext.*
%{_mandir}/man3/wxGraphicsFont.*
%{_mandir}/man3/wxGraphicsMatrix.*
%{_mandir}/man3/wxGraphicsObject.*
%{_mandir}/man3/wxGraphicsPath.*
%{_mandir}/man3/wxGraphicsPen.*
%{_mandir}/man3/wxGraphicsRenderer.*
%{_mandir}/man3/wxGrid.*
%{_mandir}/man3/wxGridBagSizer.*
%{_mandir}/man3/wxGridCellAttr.*
%{_mandir}/man3/wxGridCellBoolEditor.*
%{_mandir}/man3/wxGridCellBoolRenderer.*
%{_mandir}/man3/wxGridCellChoiceEditor.*
%{_mandir}/man3/wxGridCellEditor.*
%{_mandir}/man3/wxGridCellFloatEditor.*
%{_mandir}/man3/wxGridCellFloatRenderer.*
%{_mandir}/man3/wxGridCellNumberEditor.*
%{_mandir}/man3/wxGridCellNumberRenderer.*
%{_mandir}/man3/wxGridCellRenderer.*
%{_mandir}/man3/wxGridCellStringRenderer.*
%{_mandir}/man3/wxGridCellTextEditor.*
%{_mandir}/man3/wxGridEvent.*
%{_mandir}/man3/wxGridSizer.*
%{_mandir}/man3/wxHelpEvent.*
%{_mandir}/man3/wxHtmlEasyPrinting.*
%{_mandir}/man3/wxHtmlLinkEvent.*
%{_mandir}/man3/wxHtmlWindow.*
%{_mandir}/man3/wxIcon.*
%{_mandir}/man3/wxIconBundle.*
%{_mandir}/man3/wxIconizeEvent.*
%{_mandir}/man3/wxIdleEvent.*
%{_mandir}/man3/wxImage.*
%{_mandir}/man3/wxImageList.*
%{_mandir}/man3/wxInitDialogEvent.*
%{_mandir}/man3/wxJoystickEvent.*
%{_mandir}/man3/wxKeyEvent.*
%{_mandir}/man3/wxLayoutAlgorithm.*
%{_mandir}/man3/wxListBox.*
%{_mandir}/man3/wxListCtrl.*
%{_mandir}/man3/wxListEvent.*
%{_mandir}/man3/wxListItem.*
%{_mandir}/man3/wxListItemAttr.*
%{_mandir}/man3/wxListView.*
%{_mandir}/man3/wxListbook.*
%{_mandir}/man3/wxLocale.*
%{_mandir}/man3/wxLogNull.*
%{_mandir}/man3/wxMDIChildFrame.*
%{_mandir}/man3/wxMDIClientWindow.*
%{_mandir}/man3/wxMDIParentFrame.*
%{_mandir}/man3/wxMask.*
%{_mandir}/man3/wxMaximizeEvent.*
%{_mandir}/man3/wxMemoryDC.*
%{_mandir}/man3/wxMenu.*
%{_mandir}/man3/wxMenuBar.*
%{_mandir}/man3/wxMenuEvent.*
%{_mandir}/man3/wxMenuItem.*
%{_mandir}/man3/wxMessageDialog.*
%{_mandir}/man3/wxMiniFrame.*
%{_mandir}/man3/wxMirrorDC.*
%{_mandir}/man3/wxMouseCaptureChangedEvent.*
%{_mandir}/man3/wxMouseCaptureLostEvent.*
%{_mandir}/man3/wxMouseEvent.*
%{_mandir}/man3/wxMoveEvent.*
%{_mandir}/man3/wxMultiChoiceDialog.*
%{_mandir}/man3/wxNavigationKeyEvent.*
%{_mandir}/man3/wxNotebook.*
%{_mandir}/man3/wxNotebookEvent.*
%{_mandir}/man3/wxNotifyEvent.*
%{_mandir}/man3/wxOverlay.*
%{_mandir}/man3/wxPageSetupDialog.*
%{_mandir}/man3/wxPageSetupDialogData.*
%{_mandir}/man3/wxPaintDC.*
%{_mandir}/man3/wxPaintEvent.*
%{_mandir}/man3/wxPalette.*
%{_mandir}/man3/wxPaletteChangedEvent.*
%{_mandir}/man3/wxPanel.*
%{_mandir}/man3/wxPasswordEntryDialog.*
%{_mandir}/man3/wxPen.*
%{_mandir}/man3/wxPickerBase.*
%{_mandir}/man3/wxPopupTransientWindow.*
%{_mandir}/man3/wxPopupWindow.*
%{_mandir}/man3/wxPostScriptDC.*
%{_mandir}/man3/wxPreviewCanvas.*
%{_mandir}/man3/wxPreviewControlBar.*
%{_mandir}/man3/wxPreviewFrame.*
%{_mandir}/man3/wxPrintData.*
%{_mandir}/man3/wxPrintDialog.*
%{_mandir}/man3/wxPrintDialogData.*
%{_mandir}/man3/wxPrintPreview.*
%{_mandir}/man3/wxPrinter.*
%{_mandir}/man3/wxPrintout.*
%{_mandir}/man3/wxProgressDialog.*
%{_mandir}/man3/wxQueryNewPaletteEvent.*
%{_mandir}/man3/wxRadioBox.*
%{_mandir}/man3/wxRadioButton.*
%{_mandir}/man3/wxRegion.*
%{_mandir}/man3/wxSashEvent.*
%{_mandir}/man3/wxSashLayoutWindow.*
%{_mandir}/man3/wxSashWindow.*
%{_mandir}/man3/wxScreenDC.*
%{_mandir}/man3/wxScrollBar.*
%{_mandir}/man3/wxScrollEvent.*
%{_mandir}/man3/wxScrollWinEvent.*
%{_mandir}/man3/wxScrolledWindow.*
%{_mandir}/man3/wxSetCursorEvent.*
%{_mandir}/man3/wxShowEvent.*
%{_mandir}/man3/wxSingleChoiceDialog.*
%{_mandir}/man3/wxSizeEvent.*
%{_mandir}/man3/wxSizer.*
%{_mandir}/man3/wxSizerFlags.*
%{_mandir}/man3/wxSizerItem.*
%{_mandir}/man3/wxSlider.*
%{_mandir}/man3/wxSpinButton.*
%{_mandir}/man3/wxSpinCtrl.*
%{_mandir}/man3/wxSpinEvent.*
%{_mandir}/man3/wxSplashScreen.*
%{_mandir}/man3/wxSplitterEvent.*
%{_mandir}/man3/wxSplitterWindow.*
%{_mandir}/man3/wxStaticBitmap.*
%{_mandir}/man3/wxStaticBox.*
%{_mandir}/man3/wxStaticBoxSizer.*
%{_mandir}/man3/wxStaticLine.*
%{_mandir}/man3/wxStaticText.*
%{_mandir}/man3/wxStatusBar.*
%{_mandir}/man3/wxStdDialogButtonSizer.*
%{_mandir}/man3/wxStyledTextCtrl.*
%{_mandir}/man3/wxStyledTextEvent.*
%{_mandir}/man3/wxSysColourChangedEvent.*
%{_mandir}/man3/wxSystemOptions.*
%{_mandir}/man3/wxSystemSettings.*
%{_mandir}/man3/wxTaskBarIcon.*
%{_mandir}/man3/wxTaskBarIconEvent.*
%{_mandir}/man3/wxTextAttr.*
%{_mandir}/man3/wxTextCtrl.*
%{_mandir}/man3/wxTextDataObject.*
%{_mandir}/man3/wxTextEntryDialog.*
%{_mandir}/man3/wxToggleButton.*
%{_mandir}/man3/wxToolBar.*
%{_mandir}/man3/wxToolTip.*
%{_mandir}/man3/wxToolbook.*
%{_mandir}/man3/wxTopLevelWindow.*
%{_mandir}/man3/wxTreeCtrl.*
%{_mandir}/man3/wxTreeEvent.*
%{_mandir}/man3/wxTreebook.*
%{_mandir}/man3/wxUpdateUIEvent.*
%{_mandir}/man3/wxWindow.*
%{_mandir}/man3/wxWindowCreateEvent.*
%{_mandir}/man3/wxWindowDC.*
%{_mandir}/man3/wxWindowDestroyEvent.*
%{_mandir}/man3/wxXmlResource.*
%{_mandir}/man3/wx_misc.*
%{_mandir}/man3/wx_object.*
%endif
%endif %{__with_wxwidgets}

%files xmerl
%{_libdir}/erlang/lib/xmerl-*/
%if %{with doc}
%{_mandir}/man3/xmerl.*
%{_mandir}/man3/xmerl_eventp.*
%{_mandir}/man3/xmerl_sax_parser.*
%{_mandir}/man3/xmerl_scan.*
%{_mandir}/man3/xmerl_xpath.*
%{_mandir}/man3/xmerl_xs.*
%{_mandir}/man3/xmerl_xsd.*
%endif

%changelog
* Fri Jul 30 2021 liping <liping136@huawei.com> - 21.3.3-3
- Support parallel compilation

* Sat Mar 27 2021 weishengjing <weishengjing1@huawei.com> - 21.3.3-2
- Support parallel compilation

* Mon Aug 24 2020 chengzihan <chengzihan2@huawei.com> - 21.3.3-1
- Package init
