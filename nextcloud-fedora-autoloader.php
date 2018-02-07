<?php
require_once '##PHPDIR##/Fedora/Autoloader/autoload.php';

// For PEAR components
\Fedora\Autoloader\Autoload::addIncludePath();

// Dependencies from 3rdparty composer.json
// https://github.com/nextcloud/3rdparty/blob/v12.0.5/composer.json
\Fedora\Autoloader\Dependencies::required(array(
        // "aws/aws-sdk-php"
        '##PHPDIR##/Aws3/autoload.php',
        // "bantu/ini-get-wrapper"
        '##PHPDIR##/bantu/IniGetWrapper/IniGetWrapper.php',
        // "deepdiver1975/TarStreamer"
        '##PHPDIR##/ownCloud/TarStreamer/autoload.php',
        // "doctrine/dbal"
        '##PHPDIR##/Doctrine/DBAL/autoload.php',
        // "guzzlehttp/guzzle"
        '##PHPDIR##/GuzzleHttp/autoload.php',
        // "icewind/searchdav"
        '##PHPDIR##/Icewind/SearchDAV/autoload.php',
        // "icewind/Streams"
        '##PHPDIR##/Icewind/Streams/autoload.php',
        // "interfasys/lognormalizer"
        '##PHPDIR##/InterfaSys/LogNormalizer/autoload.php',
        // "jeremeamia/superclosure"
        '##PHPDIR##/SuperClosure/autoload.php',
        // "leafo/scssphp"
        '##PHPDIR##/Leafo/ScssPhp/autoload.php',
        // "league/flysystem"
        '##PHPDIR##/League/Flysystem/autoload.php',
        // "lukasreschke/id3parser": "^0.0.1"
        '##PHPDIR##/ID3Parser/autoload.php',
        // mcnetic/zipstreamer"
        '##PHPDIR##/ZipStreamer/autoload.php',
        // "natxet/CssMin"
        '##PHPDIR##/natxet/CssMin/autoload.php',
        // "nikic/php-parser"
        '##PHPDIR##/PhpParser/autoload.php',
        // "patchwork/jsqueeze"
        '##PHPDIR##/Patchwork/JSqueeze.php',
        // "patchwork/utf8"
        '##PHPDIR##/Patchwork/autoload.php',
        // Do not autoload PEAR components
        // "phpeclib/phpseclib"
        '##PHPDIR##/phpseclib/autoload.php',
        // "pimple/pimple"
        '##PHPDIR##/Pimple/autoload.php',
        // "punic/punic"
        '##PHPDIR##/Punic/autoload.php',
        // "rackspace/php-opencloud"
        '##PHPDIR##/OpenCloud/autoload.php',
        // Note react/promise is not in composer.json
        // "react/promise"
        '##PHPDIR##/React/Promise/autoload.php',
        // "sabre/dav"
        '##PHPDIR##/Sabre/DAV/autoload.php',
        // "stecman/symfony-console-completion"
        '##PHPDIR##/Stecman/Component/Symfony/Console/BashCompletion/autoload.php',
        // "swiftmailer/swiftmailer
        '##PHPDIR##/Swift/swift_required.php',
        // "symfony/console"
        '##PHPDIR##/Symfony3/Component/Console/autoload.php',
        // "symfony/event-dispatcher"
        '##PHPDIR##/Symfony3/Component/EventDispatcher/autoload.php',
        // "symfony/polyfill-php70"
        '##PHPDIR##/Symfony/Polyfill/autoload.php',
        // "symfony/process"
        '##PHPDIR##/Symfony3/Component/Process/autoload.php',
        // "symfony/routing"
        '##PHPDIR##/Symfony3/Component/Routing/autoload.php',
        // "symfony/translation"
        '##PHPDIR##/Symfony3/Component/Translation/autoload.php',
));
