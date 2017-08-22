<?php
$vendor = '##DATADIR##/php';

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once $vendor . '/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}

// For PEAR components
$fedoraClassLoader->setUseIncludePath(true);

// Dependencies from 3rdparty composer.json
// https://github.com/nextcloud/3rdparty/blob/v12.0.2/composer.json
// "doctrine/dbal"
require_once $vendor . '/Doctrine/DBAL/autoload.php';
// mcnetic/zipstreamer"
require_once $vendor . '/ZipStreamer/autoload.php';
// "phpeclib/phpseclib"
require_once $vendor . '/phpseclib/autoload.php';
// "rackspace/php-opencloud"
require_once $vendor . '/OpenCloud/autoload.php';
// "jeremeamia/superclosure"
require_once $vendor . '/SuperClosure/autoload.php';
// "bantu/ini-get-wrapper"
require_once $vendor . '/bantu/IniGetWrapper/IniGetWrapper.php';
// "natxet/CssMin"
require_once $vendor . '/natxet/CssMin/autoload.php';
// "punic/punic"
require_once $vendor . '/Punic/autoload.php';
// "patchwork/utf8"
require_once $vendor . '/Patchwork/autoload.php';
// "symfony/console"
require_once $vendor . '/Symfony/Component/Console/autoload.php';
// "symfony/event-dispatcher"
require_once $vendor . '/Symfony/Component/EventDispatcher/autoload.php';
// "symfony/routing"
require_once $vendor . '/Symfony/Component/Routing/autoload.php';
// "symfony/process"
require_once $vendor . '/Symfony/Component/Process/autoload.php';
// "pimple/pimple"
require_once $vendor . '/Pimple/autoload.php';
// "nikic/php-parser"
require_once $vendor . '/PhpParser/autoload.php';
// "icewind/Streams"
require_once $vendor . '/Icewind/Streams/autoload.php';
// "swiftmailer/swiftmailer
require_once $vendor . '/Swift/swift_required.php';
// "guzzlehttp/guzzle"
require_once $vendor . '/GuzzleHttp/autoload.php';
// "league/flysystem"
require_once $vendor . '/League/Flysystem/autoload.php';
// "interfasys/lognormalizer"
require_once $vendor . '/InterfaSys/LogNormalizer/autoload.php';
// "deepdiver1975/TarStreamer"
require_once $vendor . '/ownCloud/TarStreamer/autoload.php';
// "patchwork/jsqueeze"
require_once $vendor . '/Patchwork/JSqueeze.php';
// "sabre/dav"
require_once $vendor . '/Sabre/DAV/autoload.php';
// "symfony/polyfill-php70"
require_once $vendor . '/Symfony/Polyfill/autoload.php';
// "lukasreschke/id3parser": "^0.0.1"
require_once $vendor . '/ID3Parser/autoload.php';
// "stecman/symfony-console-completion"
require_once $vendor . '/Stecman/Component/Symfony/Console/BashCompletion/autoload.php';
// "leafo/scssphp"
require_once $vendor . '/Leafo/ScssPhp/autoload.php';
// "icewind/searchdav"
require_once $vendor . '/Icewind/SearchDAV/autoload.php';
