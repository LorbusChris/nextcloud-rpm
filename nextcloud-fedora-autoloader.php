<?php
require_once '##DATADIR##/php/Fedora/Autoloader/autoload.php';

// For PEAR components
\Fedora\Autoloader\Autoload::addIncludePath();

// Dependencies from 3rdparty composer.json
// https://github.com/nextcloud/3rdparty/blob/v12.0.5/composer.json
// TODO: Update to NC13 and sort alphabetically
\Fedora\Autoloader\Dependencies::required(array(
        // "doctrine/dbal"
        '##DATADIR##/php/Doctrine/DBAL/autoload.php',
        // mcnetic/zipstreamer"
        '##DATADIR##/php/ZipStreamer/autoload.php',
        // "phpeclib/phpseclib"
        '##DATADIR##/php/phpseclib/autoload.php',
        // "rackspace/php-opencloud"
        '##DATADIR##/php/OpenCloud/autoload.php',
        // "jeremeamia/superclosure"
        '##DATADIR##/php/SuperClosure/autoload.php',
        // "bantu/ini-get-wrapper"
        '##DATADIR##/php/bantu/IniGetWrapper/IniGetWrapper.php',
        // "natxet/CssMin"
        '##DATADIR##/php/natxet/CssMin/autoload.php',
        // "punic/punic"
        '##DATADIR##/php/Punic/autoload.php',
        // "patchwork/utf8"
        '##DATADIR##/php/Patchwork/autoload.php',
        // "symfony/console"
        '##DATADIR##/php/Symfony/Component/Console/autoload.php',
        // "symfony/event-dispatcher"
        '##DATADIR##/php/Symfony/Component/EventDispatcher/autoload.php',
        // "symfony/routing"
        '##DATADIR##/php/Symfony/Component/Routing/autoload.php',
        // "symfony/process"
        '##DATADIR##/php/Symfony/Component/Process/autoload.php',
        // "pimple/pimple"
        '##DATADIR##/php/Pimple/autoload.php',
        // "nikic/php-parser"
        '##DATADIR##/php/PhpParser/autoload.php',
        // "icewind/Streams"
        '##DATADIR##/php/Icewind/Streams/autoload.php',
        // "swiftmailer/swiftmailer
        '##DATADIR##/php/Swift/swift_required.php',
        // "guzzlehttp/guzzle"
        '##DATADIR##/php/GuzzleHttp/autoload.php',
        // "league/flysystem"
        '##DATADIR##/php/League/Flysystem/autoload.php',
        // "interfasys/lognormalizer"
        '##DATADIR##/php/InterfaSys/LogNormalizer/autoload.php',
        // "deepdiver1975/TarStreamer"
        '##DATADIR##/php/ownCloud/TarStreamer/autoload.php',
        // "patchwork/jsqueeze"
        '##DATADIR##/php/Patchwork/JSqueeze.php',
        // "sabre/dav"
        '##DATADIR##/php/Sabre/DAV/autoload.php',
        // "symfony/polyfill-php70"
        '##DATADIR##/php/Symfony/Polyfill/autoload.php',
        // "lukasreschke/id3parser": "^0.0.1"
        '##DATADIR##/php/ID3Parser/autoload.php',
        // "stecman/symfony-console-completion"
        '##DATADIR##/php/Stecman/Component/Symfony/Console/BashCompletion/autoload.php',
        // "leafo/scssphp"
        '##DATADIR##/php/Leafo/ScssPhp/autoload.php',
        // "icewind/searchdav"
        '##DATADIR##/php/Icewind/SearchDAV/autoload.php',
        // "aws/aws-sdk-php"
        '##DATADIR##/php/Aws/autoload.php',
        // "react/promise"
        '##DATADIR##/php/React/Promise/autoload.php',
));
