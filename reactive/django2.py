from charms.reactive import (
    set_state,
    when,
    when_not,
)
from charmhelpers.core import (
    hookenv,
    host,
)


@when_not('django2.installed')
def install_django2():
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    set_state('django2.installed')


@when('website.available')
def configure_website(website):
    website.configure(port=hookenv.config('port')
