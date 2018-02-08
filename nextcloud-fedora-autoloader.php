<?php
require_once '##DATADIR##/php/Fedora/Autoloader/autoload.php';

// For PEAR components
\Fedora\Autoloader\Autoload::addIncludePath();

// Dependencies from 3rdparty composer.json
// https://github.com/nextcloud/3rdparty/blob/v12.0.5/composer.json
// TODO: Update to NC13 and sort alphabetically
\Fedora\Autoloader\Dependencies::required(array(
        // "aws/aws-sdk-php"
        '##DATADIR##/php/Aws3/autoload.php',
        // "bantu/ini-get-wrapper"
        '##DATADIR##/php/bantu/IniGetWrapper/IniGetWrapper.php',
        // "deepdiver1975/TarStreamer"
        '##DATADIR##/php/ownCloud/TarStreamer/autoload.php',
        // "doctrine/dbal"
        '##DATADIR##/php/Doctrine/DBAL/autoload.php',
        // "guzzlehttp/guzzle"
        '##DATADIR##/php/GuzzleHttp/autoload.php',
        // "icewind/searchdav"
        '##DATADIR##/php/Icewind/SearchDAV/autoload.php',
        // "icewind/Streams"
        '##DATADIR##/php/Icewind/Streams/autoload.php',
        // "interfasys/lognormalizer"
        '##DATADIR##/php/InterfaSys/LogNormalizer/autoload.php',
        // "jeremeamia/superclosure"
        '##DATADIR##/php/SuperClosure/autoload.php',
        // "leafo/scssphp"
        '##DATADIR##/php/Leafo/ScssPhp/autoload.php',
        // "league/flysystem"
        '##DATADIR##/php/League/Flysystem/autoload.php',
        // "lukasreschke/id3parser": "^0.0.1"
        '##DATADIR##/php/ID3Parser/autoload.php',
        // mcnetic/zipstreamer"
        '##DATADIR##/php/ZipStreamer/autoload.php',
        // "natxet/CssMin"
        '##DATADIR##/php/natxet/CssMin/autoload.php',
        // "nikic/php-parser"
        '##DATADIR##/php/PhpParser/autoload.php',
        // "patchwork/jsqueeze"
        '##DATADIR##/php/Patchwork/JSqueeze.php',
        // "patchwork/utf8"
        '##DATADIR##/php/Patchwork/autoload.php',
        // Do not autoload PEAR components
        // "phpeclib/phpseclib"
        '##DATADIR##/php/phpseclib/autoload.php',
        // "pimple/pimple"
        '##DATADIR##/php/Pimple/autoload.php',
        // "punic/punic"
        '##DATADIR##/php/Punic/autoload.php',
        // "rackspace/php-opencloud"
        '##DATADIR##/php/OpenCloud/autoload.php',
        // Note react/promise is not in composer.json
        // "react/promise"
        '##DATADIR##/php/React/Promise/autoload.php',
        // "sabre/dav"
        '##DATADIR##/php/Sabre/DAV/autoload.php',
        // "stecman/symfony-console-completion"
        '##DATADIR##/php/Stecman/Component/Symfony/Console/BashCompletion/autoload.php',
        // "swiftmailer/swiftmailer
        '##DATADIR##/php/Swift/swift_required.php',
        // "symfony/console"
        '##DATADIR##/php/Symfony3/Component/Console/autoload.php',
        // "symfony/event-dispatcher"
        '##DATADIR##/php/Symfony3/Component/EventDispatcher/autoload.php',
        // "symfony/polyfill-php70"
        '##DATADIR##/php/Symfony/Polyfill/autoload.php',
        // "symfony/process"
        '##DATADIR##/php/Symfony3/Component/Process/autoload.php',
        // "symfony/routing"
        '##DATADIR##/php/Symfony3/Component/Routing/autoload.php',
        // TODO: NC 13 add symfony/translation
));
