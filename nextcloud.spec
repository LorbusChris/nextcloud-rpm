Name:           nextcloud
Version:        13.0.0
Release:        1%{?dist}
Summary:        Private file sync and share server

# TODO: NC13: Re-check Licenses
License:        AGPLv3+ and MIT and BSD and ASL 2.0 and WTFPL and CC-BY-SA and GPLv3+ and Adobe
URL:            http://nextcloud.com

Source0:        https://download.nextcloud.com/server/releases/%{name}-%{version}.zip

# Packaging notes and doc
Source1:        %{name}-README.fedora
Source2:        %{name}-MIGRATION.fedora
Source3:        %{name}-mysql.txt
Source4:        %{name}-postgresql.txt
# config.php containing just settings we want to specify, nextcloud's
# initial setup will fill out other settings appropriately
Source5:        %{name}-config.php
# Our autoloader for core
Source6:        %{name}-fedora-autoloader.php
# Systemd timer for background jobs
Source10:       %{name}-systemd-timer.service
Source11:       %{name}-systemd-timer.timer
# Httpd config snippets
Source100:      %{name}-httpd.conf
Source101:      %{name}-access-httpd.conf.avail
Source102:      %{name}-auth-any.inc
Source103:      %{name}-auth-local.inc
Source104:      %{name}-auth-none.inc
Source105:      %{name}-defaults.inc
# Nginx config snippets
Source200:      %{name}-default-nginx.conf
Source201:      %{name}-conf-nginx.conf
Source202:      %{name}-php-fpm.conf
Source203:      %{name}-el7-php-fpm.conf

BuildArch:      noarch

# have %{phpdir} for convenience
%{!?phpdir:  %global phpdir  %{_datadir}/php}

# For the systemd macros
%{?systemd_requires}
BuildRequires:  systemd

# expand pear macros on install
BuildRequires:  php-pear

# Use Fedora autoloader
BuildRequires:  php-composer(fedora/autoloader) >= 1.0.0
Requires:       php-composer(fedora/autoloader) >= 1.0.0

# External PHP libs required by core. Required in build for sanity %%check
# https://github.com/nextcloud/3rdparty/blob/v13.0.0/composer.json
# "aws/aws-sdk-php": "^3.35"
BuildRequires: (php-composer(aws/aws-sdk-php) >= 3.35 with php-composer(aws/aws-sdk-php) < 4.0.0)
Requires:      (php-composer(aws/aws-sdk-php) >= 3.35 with php-composer(aws/aws-sdk-php) < 4.0.0)
# "bantu/ini-get-wrapper": "v1.0.1"
BuildRequires: (php-composer(bantu/ini-get-wrapper) >= 1.0.1 with php-composer(bantu/ini-get-wrapper) < 2.0)
Requires:      (php-composer(bantu/ini-get-wrapper) >= 1.0.1 with php-composer(bantu/ini-get-wrapper) < 2.0)
# "deepdiver1975/TarStreamer": "v0.1.0"
# Despite the different namespace this lives in the name is correct
BuildRequires: (php-composer(owncloud/tarstreamer) >= 0.1 with php-composer(owncloud/tarstreamer) < 1.0)
Requires:      (php-composer(owncloud/tarstreamer) >= 0.1 with php-composer(owncloud/tarstreamer) < 1.0)
# "doctrine/dbal": "dev-2.5.-pg10"
# TODO: NC13: Get dep updated to 2.6 upstream, package 2.6, update
# NOTE: NC13: Depends on patched dev-2.5.-pg10, fixes are in >2.6
BuildRequires: (php-composer(doctrine/dbal) >= 2.5.12 with php-composer(doctrine/dbal) < 3)
Requires:      (php-composer(doctrine/dbal) >= 2.5.12 with php-composer(doctrine/dbal) < 3)
# "guzzlehttp/guzzle": "~5.3"
BuildRequires: (php-composer(guzzlehttp/guzzle) >= 5.3.0 with php-composer(guzzlehttp/guzzle) < 6.0)
Requires:      (php-composer(guzzlehttp/guzzle) >= 5.3.0 with php-composer(guzzlehttp/guzzle) < 6.0)
# "icewind/searchdav": "0.3.1"
# NOTE: NC14: Package 1.0.x, update
BuildRequires: (php-composer(icewind/searchdav) >= 0.3.1 with php-composer(icewind/searchdav) < 0.4.0)
Requires:      (php-composer(icewind/searchdav) >= 0.3.1 with php-composer(icewind/searchdav) < 0.4.0)
# "icewind/Streams": "0.5.2"
BuildRequires: (php-composer(icewind/streams) >= 0.5.2 with php-composer(icewind/streams) < 0.6.0)
Requires:      (php-composer(icewind/streams) >= 0.5.2 with php-composer(icewind/streams) < 0.6.0)
# "interfasys/lognormalizer": "^v1.0"
BuildRequires: (php-composer(interfasys/lognormalizer) >= 1.0 with php-composer(interfasys/lognormalizer) < 2.0)
Requires:      (php-composer(interfasys/lognormalizer) >= 1.0 with php-composer(interfasys/lognormalizer) < 2.0)
# "jeremeamia/superclosure": "2.1.0"
BuildRequires: (php-composer(jeremeamia/superclosure) >= 2.1.0 with php-composer(jeremeamia/superclosure) < 3.0)
Requires:      (php-composer(jeremeamia/superclosure) >= 2.1.0 with php-composer(jeremeamia/superclosure) < 3.0)
# "leafo/scssphp": "^0.7.2"
# TODO: NC13: Package 0.7.2, update
BuildRequires: (php-composer(leafo/scssphp) >= 0.6.7 with php-composer(leafo/scssphp) < 0.8.0)
Requires:      (php-composer(leafo/scssphp) >= 0.6.7 with php-composer(leafo/scssphp) < 0.8.0)
# "league/flysystem": "^1.0"
BuildRequires: (php-composer(league/flysystem) >= 1.0.20 with php-composer(league/flysystem) < 2.0)
Requires:      (php-composer(league/flysystem) >= 1.0.20 with php-composer(league/flysystem) < 2.0)
# "lukasreschke/id3parser": "^0.0.1"
BuildRequires: (php-composer(lukasreschke/id3parser) >= 0.0.1 with php-composer(lukasreschke/id3parser) < 0.1.0)
Requires:      (php-composer(lukasreschke/id3parser) >= 0.0.1 with php-composer(lukasreschke/id3parser) < 0.1.0)
# "mcnetic/zipstreamer": "^1.0"
BuildRequires: (php-composer(mcnetic/zipstreamer) >= 1.0 with php-composer(mcnetic/zipstreamer) < 2.0)
Requires:      (php-composer(mcnetic/zipstreamer) >= 1.0 with php-composer(mcnetic/zipstreamer) < 2.0)
# "natxet/CssMin": "dev-master"
BuildRequires: (php-composer(natxet/CssMin) >= 3.0.4 with php-composer(natxet/CssMin) < 4.0)
Requires:      (php-composer(natxet/CssMin) >= 3.0.4 with php-composer(natxet/CssMin) < 4.0)
# "nikic/php-parser": "1.4.1"
BuildRequires: (php-composer(nikic/php-parser) >= 1.4.1 with php-composer(nikic/php-parser) < 2.0)
Requires:      (php-composer(nikic/php-parser) >= 1.4.1 with php-composer(nikic/php-parser) < 2.0)
# "patchwork/jsqueeze": "^2.0"
BuildRequires: (php-composer(patchwork/jsqueeze) >= 2.0 with php-composer(patchwork/jsqueeze) < 3.0)
Requires:      (php-composer(patchwork/jsqueeze) >= 2.0 with php-composer(patchwork/jsqueeze) < 3.0)
# "patchwork/utf8": "1.2.6"
BuildRequires: (php-composer(patchwork/utf8) >= 1.2.6 with php-composer(patchwork/utf8) < 2.0)
Requires:      (php-composer(patchwork/utf8) >= 1.2.6 with php-composer(patchwork/utf8) < 2.0)
# "pear/archive_tar": "1.4.3"
# archive_tar is in base el7 and doesn't have the fedora php-composer provides
%if 0%{?el7}
BuildRequires: (php-pear(Archive_Tar) >= 1.4.3 with php-pear(Archive_Tar) < 2.0)
Requires:      (php-pear(Archive_Tar) >= 1.4.3 with php-pear(Archive_Tar) < 2.0)
%else
BuildRequires: (php-composer(pear/archive_tar) >= 1.4.1 with php-composer(pear/archive_tar) < 2.0)
Requires:      (php-composer(pear/archive_tar) >= 1.4.1 with php-composer(pear/archive_tar) < 2.0)
%endif
# "pear/pear-core-minimal": "v1.10"
%if 0%{?el7}
BuildRequires: (php-pear(Console_Getopt) > 1.3 with php-pear(Console_Getopt) < 2.0)
Requires:      (php-pear(Console_Getopt) > 1.3 with php-pear(Console_Getopt) < 2.0)
BuildRequires:  php-pear(PEAR) > 1.9
Requires:       php-pear(PEAR) > 1.9
%else
BuildRequires:  php-composer(pear/pear-core-minimal) >= 1.10.1
Requires:       php-composer(pear/pear-core-minimal) >= 1.10.1
%endif
# "phpseclib/phpseclib": "2.0.4"
BuildRequires: (php-composer(phpseclib/phpseclib) >= 2.0.4 with php-composer(phpseclib/phpseclib) < 3.0)
Requires:      (php-composer(phpseclib/phpseclib) >= 2.0.4 with php-composer(phpseclib/phpseclib) < 3.0)
# "pimple/pimple": "3.2.3"
BuildRequires: (php-composer(pimple/pimple) >= 3.2.3 with php-composer(pimple/pimple) < 4.0)
Requires:      (php-composer(pimple/pimple) >= 3.2.3 with php-composer(pimple/pimple) < 4.0)
# "punic/punic": "^1.6"
BuildRequires: (php-composer(punic/punic) >= 1.6.3 with php-composer(punic/punic) < 2.0)
Requires:      (php-composer(punic/punic) >= 1.6.3 with php-composer(punic/punic) < 2.0)
# "rackspace/php-opencloud": "v1.16.0"
BuildRequires: (php-composer(rackspace/php-opencloud) >= 1.16.0 with php-composer(rackspace/php-opencloud) < 2.0)
Requires:      (php-composer(rackspace/php-opencloud) >= 1.16.0 with php-composer(rackspace/php-opencloud) < 2.0)
# "sabre/dav" : "^3.2.0"
BuildRequires: (php-composer(sabre/dav)  >= 3.2.0 with php-composer(sabre/dav) < 4.0)
Requires:      (php-composer(sabre/dav)  >= 3.2.0 with php-composer(sabre/dav) < 4.0)
# "stecman/symfony-console-completion": "^0.7.0"
BuildRequires: (php-composer(stecman/symfony-console-completion) >= 0.7.0 with php-composer(stecman/symfony-console-completion) < 0.8.0)
Requires:      (php-composer(stecman/symfony-console-completion) >= 0.7.0 with php-composer(stecman/symfony-console-completion) < 0.8.0)
# "swiftmailer/swiftmailer": "^5.4"
BuildRequires: (php-composer(swiftmailer/swiftmailer) >= 5.4.8 with php-composer(swiftmailer/swiftmailer) < 6)
Requires:      (php-composer(swiftmailer/swiftmailer) >= 5.4.8 with php-composer(swiftmailer/swiftmailer) < 6)
# "symfony/console": "^3.3.0"
BuildRequires: (php-composer(symfony/console) >= 3.3.0 with php-composer(symfony/console) < 4)
Requires:      (php-composer(symfony/console) >= 3.3.0 with php-composer(symfony/console) < 4)
# "symfony/event-dispatcher": "^3.3.0"
BuildRequires: (php-composer(symfony/event-dispatcher) >= 3.3.0 with php-composer(symfony/event-dispatcher) < 4)
Requires:      (php-composer(symfony/event-dispatcher) >= 3.3.0 with php-composer(symfony/event-dispatcher) < 4)
# "symfony/polyfill": "^1.0"
# NOTE: NC14: Removed in Master
BuildRequires: (php-composer(symfony/polyfill) >= 1.5 with php-composer(symfony/polyfill) < 2)
Requires:      (php-composer(symfony/polyfill) >= 1.5 with php-composer(symfony/polyfill) < 2)
# "symfony/process": "^3.3.0"
BuildRequires: (php-composer(symfony/process) >= 3.3.0 with php-composer(symfony/process) < 4)
Requires:      (php-composer(symfony/process) >= 3.3.0 with php-composer(symfony/process) < 4)
# "symfony/routing": "^3.3.0"
BuildRequires: (php-composer(symfony/routing) >= 3.3.0 with php-composer(symfony/routing) < 4)
Requires:      (php-composer(symfony/routing) >= 3.3.0 with php-composer(symfony/routing) < 4)
# "symfony/translation": "^3.3.0"
BuildRequires: (php-composer(symfony/translation) >= 3.3 with php-composer(symfony/translation) < 4)
Requires:      (php-composer(symfony/translation) >= 3.3 with php-composer(symfony/translation) < 4)

# External PHP libs required by files_external app
# https://github.com/nextcloud/server/blob/v13.0.0/apps/files_external/3rdparty/composer.json
# NOTE: icewind/streams is a dep but is already required by core
# "icewind/smb": "2.0.4"
BuildRequires: (php-composer(icewind/smb) >= 2.0.4 with php-composer(icewind/smb) < 3.0)
Requires:      (php-composer(icewind/smb) >= 2.0.4 with php-composer(icewind/smb) < 3.0)
# This makes smb external storage usable in performance
# and doesn't break things like encryption due to timeouts
BuildRequires:  php-pecl(smbclient)
Requires:       php-pecl(smbclient)
# Requiring so that the shipped external smb storage works
# The net command is needed and enabling smb tests for smbclient command
Requires:       samba-common-tools
Requires:       samba-client

# External PHP libs required by gallery app
# https://github.com/nextcloud/gallery/blob/v13.0.0/composer.json
# "symfony/yaml": "~3.2"
BuildRequires: (php-composer(symfony/yaml) >= 3.2.0 with php-composer(symfony/yaml) < 4)
Requires:      (php-composer(symfony/yaml) >= 3.2.0 with php-composer(symfony/yaml) < 4)

# Core PHP libs/extensions required by core
Requires:       php-bz2
Requires:       php-ctype
Requires:       php-curl
Requires:       php-dom
Requires:       php-exif
Requires:       php-fileinfo
Requires:       php-filter
Requires:       php-gd
Requires:       php-iconv
Requires:       php-imagick
Requires:       php-imap
Requires:       php-json
Requires:       php-libxml
Requires:       php-ldap
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-pdo
Requires:       php-posix
Requires:       php-session
Requires:       php-simplexml
Requires:       php-xmlreader
Requires:       php-xmlwriter
Requires:       php-spl
Requires:       php-zip
Requires:       php-zlib

Requires:       %{name}-webserver = %{version}-%{release}
Requires:       %{name}-database = %{version}-%{release}

# TODO: POLICY: Need to label the httpd rw stuff correctly until base selinux policy updated
Requires(post):   %{_sbindir}/semanage
Requires(postun): %{_sbindir}/semanage

# TODO: NC13: Revisit all bundled js libs, add link to bower.json
# bundled js libs in core
Provides: bundled(js-blueimp-md5) = 2.7.0
Provides: bundled(js-handlebars) = 4.0.5
Provides: bundled(js-jcrop) = 0.9.12
Provides: bundled(js-jquery) = 2.2.0
Provides: bundled(js-jquery-migrate) = 1.4.0
Provides: bundled(js-jquery-ui) = 1.10
Provides: bundled(js-jsTimezoneDetect) = 1.0.6
Provides: bundled(js-marked) = 0.3.6
Provides: bundled(js-moment) = 2.10.3
Provides: bundled(js-select2) = 3.4.8
Provides: bundled(js-snapjs) = 2.0.0
Provides: bundled(js-strengthify) = 0.5.1
Provides: bundled(js-zxcvbn) = gitf2a8cda13d
Provides: bundled(js-underscore) = 1.8.3

# js libs bundled in files_pdf_viewer app
Provides: bundled(js-blue) = 2.7.0

# js libs bundled in files_texteditor app
Provides: bundled(js-ace) = 1.2.5

# js libs bundled in gallery app
Provides: bundled(js-commonmark) = 0.27.0
Provides: bundled(js-dompurify) = 0.8.0
Provides: bundled(js-eventsource-polyfill) = 0.9.7
Provides: bundled(js-github-markdown-css) = 0.1

# js libs bundled in theming app
Provides: bundled(js-jscolor) = 2.0.4

# js libs bundled in user_ldap app
Provides: bundled(js-jquery-multiselect) = 1.13

%description
NextCloud gives you universal access to your files through a web interface or
WebDAV. It also provides a platform to easily view & sync your contacts,
calendars and bookmarks across all your devices and enables basic editing right
on the web. NextCloud is extendable via a simple but powerful API for
applications and plugins.

%package httpd
Summary:    Httpd integration for NextCloud

Provides:   %{name}-webserver = %{version}-%{release}
Requires:   %{name} = %{version}-%{release}

# PHP dependencies
Requires:   php

%description httpd
%{summary}.

%package nginx
Summary:    Nginx integration for NextCloud

Provides:   %{name}-webserver = %{version}-%{release}
Requires:   %{name} = %{version}-%{release}

# PHP dependencies
Requires:   php-fpm nginx

%description nginx
%{summary}.

%package mysql
Summary:    MySQL database support for NextCloud

Provides:   %{name}-database = %{version}-%{release}
Requires:   %{name} = %{version}-%{release}

# From getSupportedDatabases, mysql => pdo, mysql
Requires:   php-pdo_mysql

%description mysql
This package ensures the necessary dependencies are in place for NextCloud to
work with MySQL / MariaDB databases. It does not require a MySQL / MariaDB
server to be installed, as you may well wish to use a remote database
server.

If you want the database to be on the same system as NextCloud itself, you must
also install and enable a MySQL / MariaDB server package. See README.mysql for
more details.

%package postgresql
Summary:    PostgreSQL database support for NextCloud

Provides:   %{name}-database = %{version}-%{release}
Requires:   %{name} = %{version}-%{release}

# From getSupportedDatabases, pgsql => function, pg_connect
Requires:   php-pgsql

%description postgresql
This package ensures the necessary dependencies are in place for NextCloud to
work with a PostgreSQL database. It does not require the PostgreSQL server
package to be installed, as you may well wish to use a remote database
server.

If you want the database to be on the same system as NextCloud itself, you must
also install and enable the PostgreSQL server package. See README.postgresql
for more details.

%package sqlite
Summary:    SQLite 3 database support for NextCloud

Provides:   %{name}-database = %{version}-%{release}
Requires:   %{name} = %{version}-%{release}
# From getSupportedDatabases, pgsql => class, SQLite3
Requires:   php-sqlite3 php-pcre

%description sqlite
This package ensures the necessary dependencies are in place for NextCloud to
work with an SQLite 3 database stored on the local system.

%prep
%autosetup -n %{name} -p1

# patch backup files and .git stuff
find . -name \*.orig    -type f        -exec rm    {} \; -print
find . -name .gitignore -type f        -exec rm    {} \; -print
find . -name .github    -type d -prune -exec rm -r {} \; -print

# prepare package doc
cp %{SOURCE1} README.fedora
cp %{SOURCE2} MIGRATION.fedora
cp %{SOURCE3} README.mysql
cp %{SOURCE4} README.postgresql

# 3rdparty: move composer.json files
mv 3rdparty/composer.json 3rdparty_composer.json

pushd 3rdparty

# 3rdparty: add our Fedora autoloader
cp %{SOURCE6} ./autoload.php

# Set the vendor directory to macro based datadir in our autoloader
sed -i "s,##PHPDIR##,%{phpdir}," autoload.php

# 3rdparty: explicitly remove bundled php libraries
# https://github.com/nextcloud/3rdparty/tree/v13.0.0
rm -r aws/aws-sdk-php
rm -r bantu/ini-get-wrapper
rm -r deepdiver1975/tarstreamer
rm -r doctrine/{annotations,cache,collections,common,dbal,inflector,lexer}
rm -r guzzle/guzzle
rm -r guzzlehttp/{guzzle,psr7,promises,ringphp,streams}
rm -r icewind/{streams,searchdav}
rm -r interfasys/lognormalizer
rm -r jeremeamia/SuperClosure
rm -r leafo/scssphp
rm -r league/flysystem
rm -r lukasreschke/id3parser
rm -r mcnetic/zipstreamer
rm -r mikemccabe/json-patch-php
rm -r mtdowling/jmespath.php
rm -r natxet/CssMin
rm -r nikic/php-parser
rm -r paragonie/random_compat
rm -r patchwork/{jsqueeze,utf8}
rm -r pear/{archive_tar,console_getopt,pear-core-minimal,pear_exception}
rm -r phpseclib/phpseclib
rm -r pimple/pimple
rm -r psr/{log,http-message}
rm -r punic/punic
rm -r rackspace/php-opencloud
rm -r react/promise
rm -r sabre/{dav,event,http,uri,vobject,xml}
rm -r stecman/symfony-console-completion
rm -r swiftmailer/swiftmailer
rm -r symfony/{console,debug,event-dispatcher,polyfill-mbstring,polyfill-php70,process,routing,translation}

# 3rdparty: clean up composer, extraneous files and any empty directories
rm -r composer*
rm "LICENSE INFO" patches.txt README.md
find -type d -empty  -delete

popd

# files_external app: move composer.json
mv apps/files_external/3rdparty/composer.json files_external_composer.json

# files_external app: create autoloader
# from https://github.com/nextcloud/server/blob/v13.0.0/apps/files_external/3rdparty/composer.json
# also include additional deps that are not mentioned in this file
cat << 'EOF' | tee apps/files_external/3rdparty/autoload.php
<?php
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Icewind/Streams/autoload.php',
    '%{phpdir}/Icewind/SMB2/autoload.php',
));
EOF

# files_external app: remove bundled php libraries
rm -r apps/files_external/3rdparty/{composer*,icewind}

# gallery app: move composer.json
mv apps/gallery/composer.json gallery_composer.json

# gallery app: create autoloader
# https://github.com/nextcloud/gallery/blob/v13.0.0/composer.json
cat << 'EOF' | tee apps/gallery/vendor/autoload.php
<?php
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required(array(
  '%{phpdir}/Symfony3/Component/Yaml/autoload.php',
));
EOF

# gallery app: remove bundled php libraries and cleanup
rm -r apps/gallery/vendor/{composer*,symfony}
rm    apps/gallery/composer.lock
rm    apps/gallery/build/after_failure.sh
rm    apps/gallery/build/documentation/docpublisher.sh
rm    apps/gallery/build/xdebug_install.sh

for f in {l10n.pl,image-optimization.sh}; do
    find . -name "$f" -delete
done
rm ./l10n/rm-old.sh
find -name '.tx' -print0 | xargs -0 rm -rf
find -name '.bower.json' -print0 | xargs -0 rm -rf
find . -size 0 -type f -delete

# let's not ship upstream's 'updatenotification' app
rm -dr apps/updatenotification

# also remove the actual updater
rm -r updater

# Locate license files and put them sensibly in place
# NOTE: NC14: Uncomment once COPYING is included in the deliverable again. Already in master.
#mv COPYING nextcloud-LICENSE
mv apps/admin_audit/composer/composer/LICENSE admin_audit-app-LICENSE
mv apps/comments/composer/composer/LICENSE comments-app-LICENCE
mv apps/dav/composer/composer/LICENSE dav-app-LICENCE
mv apps/encryption/composer/composer/LICENSE encryption-app-LICENCE
mv apps/federatedfilesharing/composer/composer/LICENSE federatedfilesharing-app-LICENCE
mv apps/federation/composer/composer/LICENSE federation-app-LICENSE
mv apps/files/composer/composer/LICENSE files-app-LICENSE
mv apps/files_pdfviewer/vendor/pdfjs/LICENSE js-pdfjs-LICENSE
mv apps/files_pdfviewer/vendor/pdfjs/web/cmaps/LICENSE js-pdfjs-cmaps-LICENSE
mv apps/files_sharing/composer/composer/LICENSE files_sharing-app-LICENSE
mv apps/files_texteditor/css/DroidSansMono/Google\ Android\ License.txt DroidSansMono-LICENSE
mv apps/files_texteditor/js/core/vendor/ace-builds/LICENSE js-ace-builds-LICENSE
mv apps/files_trashbin/composer/composer/LICENSE files_trashbin-app-LICENCE
mv apps/files_versions/composer/composer/LICENSE files_versions-app-LICENCE
mv apps/gallery/COPYING gallery-app-LICENSE
mv apps/gallery/js/vendor/bigshot/LICENSE.txt js-bigshot-LICENSE
mv apps/gallery/js/vendor/commonmark/LICENSE js-commonmark-LICENSE
mv apps/gallery/js/vendor/dompurify/LICENSE js-dompurify-LICENSE
mv apps/gallery/js/vendor/eventsource-polyfill/LICENSE js-evensource-modify-LICENSE
mv apps/lookup_server_connector/composer/composer/LICENSE lookup_server_connector-app-LICENCE
mv apps/oauth2/composer/composer/LICENSE oauth2-app-LICENCE
mv apps/nextcloud_announcements/COPYING nextcloud_announcements-app-LICENSE
mv apps/notifications/COPYING notifications-app-LICENSE
mv apps/serverinfo/COPYING serverinfo-app-LICENSE
mv apps/survey_client/COPYING survey_client-app-LICENSE
mv apps/password_policy/LICENSE password_policy-app-LICENSE
mv apps/provisioning_api/composer/composer/LICENSE provisioning_api-app-LICENCE
mv apps/sharebymail/composer/composer/LICENSE sharebymail-app-LICENSE
mv apps/systemtags/composer/composer/LICENSE systemtags-app-LICENCE
mv apps/theming/js/3rdparty/jscolor/LICENSE.txt js-jscolor-LICENSE
mv apps/twofactor_backupcodes/composer/composer/LICENSE twofactor_backupcodes-app-LICENCE
mv apps/user_ldap/composer/composer/LICENSE user_ldap-app-LICENSE
mv apps/user_ldap/vendor/ui-multiselect/MIT-LICENSE js-ui-multiselect-LICENSE
mv core/fonts/LICENSE.txt fonts-LICENSE
mv core/vendor/autosize/LICENSE.md js-autosize-LICENSE
mv core/vendor/backbone/LICENSE js-backbone-LICENSE
mv core/vendor/base64/LICENSE js-base64-LICENSE
mv core/vendor/davclient.js/LICENSE js-davclient-LICENSE
mv core/vendor/DOMPurify/LICENSE js-DOMPurify-LICENSE
mv core/vendor/es6-promise/LICENSE js-es6-promise-LICENSE
mv core/vendor/jcrop/MIT-LICENSE.txt js-jcrop-LICENSE
mv core/vendor/jquery/MIT-LICENSE.txt js-jquery-LICENSE
mv core/vendor/jquery-ui/MIT-LICENSE.txt js-jquery-ui-LICENSE
mv core/vendor/jsTimezoneDetect/LICENCE.txt js-jsTimezoneDetect-LICENSE
mv core/vendor/marked/LICENSE js-marked-LICENSE
mv core/vendor/moment/LICENSE js-moment-LICENSE
mv core/vendor/select2/LICENSE js-select2-LICENSE
mv core/vendor/strengthify/LICENSE js-strengthify-LICENSE
mv core/vendor/underscore/LICENSE js-underscore-LICENSE
mv core/vendor/zxcvbn/LICENSE.txt js-zxcvbn-LICENSE
mv lib/composer/composer/LICENSE composer-LICENSE

%build
# Nothing to build

%install
install -dm 755 %{buildroot}%{_datadir}/%{name}

# create nextcloud datadir
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/data

# create writable app dir for appstore
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/apps

# create nextcloud sysconfdir
mkdir -p %{buildroot}%{_sysconfdir}/%{name}

# install content
for d in $(find . -mindepth 1 -maxdepth 1 -type d | grep -v config); do
    cp -a "$d" %{buildroot}%{_datadir}/%{name}
done

for f in {*.php,*.html,occ,robots.txt}; do
    install -pm 644 "$f" %{buildroot}%{_datadir}/%{name}
done

# symlink config dir
ln -sf %{_sysconfdir}/%{name} %{buildroot}%{_datadir}/%{name}/config

# nextcloud looks for ca-bundle.crt in config dir
ln -sf %{_sysconfdir}/pki/tls/certs/ca-bundle.crt %{buildroot}%{_sysconfdir}/%{name}/ca-bundle.crt

# set default config
install -pm 644 %{SOURCE5}    %{buildroot}%{_sysconfdir}/%{name}/config.php

# httpd config
install -Dpm 644 %{SOURCE100} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -Dpm 644 %{SOURCE101} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}-access.conf.avail
install -Dpm 644 %{SOURCE102} %{SOURCE103} %{SOURCE104} %{SOURCE105} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/

# nginx config
install -Dpm 644 %{SOURCE200} \
    %{buildroot}%{_sysconfdir}/nginx/default.d/%{name}.conf
install -Dpm 644 %{SOURCE201} \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/%{name}.conf

# php-fpm config
%if 0%{?el7}
install -Dpm 644 %{SOURCE203} \
    %{buildroot}%{_sysconfdir}/php-fpm.d/%{name}.conf
%else
install -Dpm 644 %{SOURCE202} \
    %{buildroot}%{_sysconfdir}/php-fpm.d/%{name}.conf
%endif

# Install the systemd timer
install -Dpm 644 %{SOURCE10} %{buildroot}%{_unitdir}/nextcloud-cron.service
install -Dpm 644 %{SOURCE11} %{buildroot}%{_unitdir}/nextcloud-cron.timer

%check
# Make sure there are no license files left over
# For debugging the next line can be uncommented
find . -mindepth 2 \( -name '*LICENSE*' -o -name '*LICENCE*' -o  -name '*COPYING*' \)
nb=$(find . -mindepth 2 \( -name '*LICENSE*' -o -name '*LICENCE*' -o  -name '*COPYING*' \) | wc -l )
if [ $nb -gt 0 ]
  then
  false found unexpected licenses to verify
fi

# List of apps with no dependencies: There should be 17 composer.json files
# admin_audit
# comments
# dav
# encryption
# federatedfilesharing
# federation
# files
# files_versions
# files_trashbin
# files_sharing
# lookup_server_connector
# oauth2
# provisioning_api
# sharebymail
# systemtags
# twofactor_backupcodes
# user_ldap
# There should not be more composer.json files than we know of
# For debugging the next line can be uncommented
find -name 'composer.*'
nb=$(find -name 'composer.*' | wc -l)

if [ $nb -gt 17 ]
  then
  false found unexpected composer.json files
fi

# 3rdparty checks
# For debugging the next line can be uncommented
ls %{buildroot}%{_datadir}/%{name}/3rdparty
nb=$(ls %{buildroot}%{_datadir}/%{name}/3rdparty | wc -l)
if [ $nb -gt 1  ]; then
  false core 3rdparty must only have autoload.php
fi
php %{buildroot}%{_datadir}/%{name}/3rdparty/autoload.php

# files_external checks
# For debugging the next line can be uncommented
ls %{buildroot}%{_datadir}/%{name}/apps/files_external/3rdparty
nb=$(ls %{buildroot}%{_datadir}/%{name}/apps/files_external/3rdparty | wc -l)
if [ $nb -gt 1  ]; then
  false apps/files_external/3rdparty must only have autoload.php
fi
if grep -r 3rdparty %{buildroot}%{_datadir}/%{name}/apps/files_external \
   | grep -v 3rdparty/autoload.php | grep -v signature.json; then
   false App files_external needs to be adapted
fi
php %{buildroot}%{_datadir}/%{name}/apps/files_external/3rdparty/autoload.php

# gallery checks
# For debugging the next line can be uncommented
ls %{buildroot}%{_datadir}/%{name}/apps/gallery/vendor
nb=$(ls %{buildroot}%{_datadir}/%{name}/apps/gallery/vendor | wc -l)
if [ $nb -gt 1  ]; then
  false apps/gallery/vendor must only have autoload.php
fi
php %{buildroot}%{_datadir}/%{name}/apps/gallery/vendor/autoload.php

%post httpd
/usr/bin/systemctl reload httpd.service > /dev/null 2>&1 || :

%postun httpd
if [ $1 -eq 0 ]; then
  /usr/bin/systemctl reload httpd.service > /dev/null 2>&1 || :
fi

%post nginx
%if 0%{?el7}
  # Work around missing php session directory for php-fpm in el7 bz#1338444
  if [ ! -d /var/lib/php/session ]
    then
    mkdir /var/lib/php/session
  fi
  /usr/bin/chown apache /var/lib/php/session
%endif
  /usr/bin/systemctl reload nginx.service > /dev/null 2>&1 || :
  /usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :

%postun nginx
if [ $1 -eq 0 ]; then
  /usr/bin/systemctl reload nginx.service > /dev/null 2>&1 || :
  /usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :
fi

# TODO: POLICY: upstream fedora selinux policy
%post
semanage fcontext -a -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}/config.php' 2>/dev/null || :
semanage fcontext -a -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}' 2>/dev/null || :
semanage fcontext -a -t httpd_sys_rw_content_t '%{_localstatedir}/lib/%{name}(/.*)?' 2>/dev/null || :
restorecon -R %{_sysconfdir}/%{name} || :
restorecon -R %{_localstatedir}/lib/%{name} || :

%postun
if [ $1 -eq 0  ] ; then
semanage fcontext -d -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}/config.php' 2>/dev/null || :
semanage fcontext -d -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}' 2>/dev/null || :
semanage fcontext -d -t httpd_sys_rw_content_t '%{_localstatedir}/lib/%{name}(/.*)?' 2>/dev/null || :
fi

%files
%doc AUTHORS README.fedora MIGRATION.fedora config/config.sample.php
%doc *_composer.json

%license *-LICENSE

%dir %attr(-,apache,apache) %{_sysconfdir}/%{name}
# contains sensitive data (dbpassword, passwordsalt)
%config(noreplace) %attr(0600,apache,apache) %{_sysconfdir}/%{name}/config.php
# need the symlink in confdir but it's not config
%{_sysconfdir}/%{name}/ca-bundle.crt

%{_datadir}/%{name}
%dir %attr(0755,apache,apache) %{_localstatedir}/lib/%{name}
# user data must not be world readable
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/data
%attr(-,apache,apache) %{_localstatedir}/lib/%{name}/apps

%{_unitdir}/nextcloud-cron.service
%{_unitdir}/nextcloud-cron.timer

%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_sysconfdir}/httpd/conf.d/%{name}-access.conf.avail
%{_sysconfdir}/httpd/conf.d/*.inc

%files nginx
%config(noreplace) %{_sysconfdir}/nginx/default.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/php-fpm.d/%{name}.conf

%files mysql
%doc README.mysql

%files postgresql
%doc README.postgresql

%files sqlite

%changelog
* Wed Feb 7 2018 Christian Glombek <christian.glombekg@rwth-aachen.de> - 13.0.0-1
- Update to 13.0.0
- Updated dependencies
- Added Fedora php autoloader
- Removed old patch files

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 10.0.4-2
- Add max versions to dependencies to limit each to 1 major version
- Update some dependencies to use php-composer(*) instead of package names
- Prepare for php-composer(google/apiclient) version 2 and new version 1 package

* Tue Feb 28 2017 James Hogarth <james.hogarth@gmail.com> - 10.0.4-1
- update to 10.0.4
- Add migration from owncloud documentation
- Add systemd timer for background jobs

* Wed Feb 08 2017 James Hogarth <james.hogarth@gmail.com> - 10.0.3-1
- update to 10.0.3

* Thu Oct 06 2016 James Hogarth <james.hogarth@gmail.com> - 10.0.1-1
- update to 10.0.1

* Mon Aug 01 2016 James Hogarth <james.hogarth@gmail.com> - 9.0.53-5
- Use lua to have a common srpm between epel7 and fedora

* Fri Jul 29 2016 James Hogarth <james.hogarth@gmail.com> - 9.0.53-4
- Don't unbundle javascript on EPEL7 due to versioning issues

* Fri Jul 29 2016 James Hogarth <james.hogarth@gmail.com> - 9.0.53-3
- Unbundle javascript libraries from core where possible

* Tue Jul 26 2016 James Hogarth <james.hogarth@gmail.com> - 9.0.53-2
- Update the autoloader to use the path from the approved package

* Tue Jul 19 2016 James Hogarth <james.hogarth@gmail.com> - 9.0.53-1
- New release 9.0.53

* Thu Jul 14 2016 James Hogarth <james.hogarth@gmail.com> - 9.0.52-1
- Initial nextcloud build
