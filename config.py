# Autogenerated config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Load a restored tab as soon as it takes focus.
# Type: Bool
c.session.lazy_restore = True

# Always restore open sites when qutebrowser is reopened. Without this
# option set, `:wq` (`:quit --save`) needs to be used to save open tabs
# (and restore them), while quitting qutebrowser in any other way will
# not save/restore the session. By default, this will save to the
# session which was last loaded. This behavior can be customized via the
# `session.default_name` setting.
# Type: Bool
c.auto_save.session = True

# Automatically start playing `<video>` elements.
# Type: Bool
c.content.autoplay = False

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
colors = {
    "white": "#c2c2c7",
    "black": "#111115",
    "blue": "#0A84FF",
    "red": "#FF375F"
}

config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.blocking.enabled', False)
config.set('colors.tabs.bar.bg',  colors["white"])
config.set('colors.tabs.even.bg',  colors["white"])
config.set('colors.tabs.odd.bg',  colors["white"])
config.set('colors.tabs.even.fg',  colors["black"])
config.set('colors.tabs.odd.fg',  colors["black"])
config.set('colors.tabs.selected.even.bg',  colors["black"])
config.set('colors.tabs.selected.odd.bg',  colors["black"])
config.set('colors.tabs.selected.even.fg',  colors["white"])
config.set('colors.tabs.selected.odd.fg',  colors["white"])

config.set('colors.completion.category.bg',  colors["black"])
config.set('colors.completion.category.fg',  colors["white"])
config.set('colors.completion.fg',  colors["black"])
config.set('colors.completion.even.bg',  colors["white"])
config.set('colors.completion.odd.bg',  colors["white"])
config.set('colors.completion.item.selected.bg',  colors["blue"])
config.set('colors.completion.item.selected.fg',  colors["black"])
config.set('colors.statusbar.normal.bg',  colors["black"])
config.set('colors.statusbar.normal.fg',  colors["white"])
config.set('colors.completion.scrollbar.bg',  colors["black"])
config.set('colors.completion.scrollbar.fg',  colors["white"])
config.set('colors.downloads.bar.bg',  colors["black"])
config.set('colors.downloads.error.bg',  colors["red"])
config.set('colors.downloads.error.bg',  colors["white"])
# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
# config.set('content.notifications', False, 'https://www.reddit.com')

config.set('content.notifications.presenter', "libnotify")
# Allow websites to register protocol handlers via
# `navigator.registerProtocolHandler`.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.register_protocol_handler', True, 'https://mail.google.com?extsrc=mailto&url=%25s')

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'prev'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'multiple'

# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`). * `{0}` means the same as `{}`, but can be used
# multiple times.  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
# Type: Dict
c.url.searchengines = {'aur': 'https://aur.archlinux.org/packages/?O=0&K={}','g': 'https://www.google.com/search?q={}', 'DEFAULT': 'https://www.google.com/search?q={}', 'br': 'https://search.brave.com/search?q={}', 'anime': 'https://9anime.city/search/?keyword={}', 't': 'https://twitter.com/search?q={}&src=typed_query', 'a': 'https://www.amazon.in/s?k={}', 'arx': 'https://arxiv.org/search/?query={}&searchtype=all', 'sch': 'https://scholar.google.com/scholar?hl=en&q={}', 'gh': 'https://github.com/search?q={}', 'pdf': 'https://www.pdfdrive.com/search?q={}', 'pt': 'https://pytorch.org/docs/stable/search.html?q={}&check_keywords=yes&area=default', 'pip': 'https://pypi.org/search/?q={}', 'tf': 'https://www.tensorflow.org/s/results?q={}', 'y': 'https://www.youtube.com/search?q={}', 'd': 'https://duckduckgo.com/?q={}', 'appimage': 'https://www.appimagehub.com/find?search={}', "b": "https://www.goodreads.com/search?q={}", "np": "https://numpy.org/doc/stable/search.html?q={}", "github-pv": "https://profile-summary-for-github.com/user/{}", "k": "https://www.kaggle.com/search?q={}", "sk": "https://scikit-learn.org/stable/search.html?q={}","pd": "https://pandas.pydata.org/docs/search.html?q={}", "m": "https://www.google.com/maps/search/{}", "maven": "https://search.maven.org/search?q={}", "npm": "https://www.npmjs.com/search?q={}"}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'https://inshorts.com/en/read'

# Default zoom level.
# Type: Perc
c.zoom.default = '100%'

# Default font families to use. Whenever "default_family" is used in a
# font setting, it's replaced with the fonts listed here. If set to an
# empty value, a system-specific monospace default is used.
# Type: List of Font, or Font
c.fonts.default_family = 'Noto Sans'

# Default font size to use. Whenever "default_size" is used in a font
# setting, it's replaced with the size listed here. Valid values are
# either a float value with a "pt" suffix, or an integer value with a
# "px" suffix.
# Type: String
c.fonts.default_size = '15pt'

# Font family for standard fonts.
# Type: FontFamily
c.fonts.web.family.standard = 'Noto Sans'

# Font family for fixed fonts.
# Type: FontFamily
c.fonts.web.family.fixed = 'Noto Sans Mono'

# Font family for serif fonts.
# Type: FontFamily
c.fonts.web.family.serif = 'Noto Sans'

# Font family for sans-serif fonts.
# Type: FontFamily
c.fonts.web.family.sans_serif = 'Noto Sans'

# Default font size (in pixels) for regular text.
# Type: Int
c.fonts.web.size.default = 20

# Default font size (in pixels) for fixed-pitch text.
# Type: Int
c.fonts.web.size.default_fixed = 16

# Bindings for normal mode
config.bind(';P', "open javascript:location.href='org-protocol://capture?template=L&url=' + encodeURIComponent(location.href) + '&title=' + encodeURIComponent(document.title)")
config.bind('\\p', 'spawn --userscript mpv')
# config.bind('\\s', 'spawn --userscript speak')
config.bind('\\s', 'config-source')
config.bind('cid', 'spawn --userscript org-protocol capture Pid')
config.bind('cis', 'spawn --userscript org-protocol capture Pis')
config.bind('cit', 'spawn --userscript org-protocol capture Pit')
config.bind('ciw', 'spawn --userscript org-protocol capture Piw')
config.bind('cl', 'spawn --userscript org-protocol store-link')
config.bind('cud', 'spawn --userscript org-protocol capture Pud')
config.bind('cus', 'spawn --userscript org-protocol capture Pus')
config.bind('cut', 'spawn --userscript org-protocol capture Put')
config.bind('cuw', 'spawn --userscript org-protocol capture Puw')
config.bind('zd', 'spawn --userscript query_engine dict')
config.bind('zg', 'spawn --userscript query_engine github')
config.bind('zp', 'spawn --userscript pass pass')
config.bind('zP', 'spawn --userscript pass pin')
config.bind('zt', 'spawn --userscript translate')
config.bind('zl', 'spawn --userscript localhost list')
config.bind('zr', 'open https://outline.com/{url}')
config.bind('zs', 'spawn --userscript query_engine google')
config.bind('zu', 'spawn --userscript pass user')
config.bind('zy', 'spawn --userscript query_engine youtube')
config.bind('zzd', 'spawn --userscript query_engine dict 1')
config.bind('zzg', 'spawn --userscript query_engine github 1')
config.bind('zzs', 'spawn --userscript query_engine google 1')
config.bind('zzy', 'spawn --userscript query_engine youtube 1')
config.bind('se', 'spawn --userscript share.sh')
config.bind('~', 'tab-focus last')


# Theme
import dracula.draw


dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})
